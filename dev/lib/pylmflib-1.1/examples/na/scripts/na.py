#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import pylmflib
import imp
import subprocess
import multiprocessing
import datetime


def spawn_full_process(*args, **kwargs):
    pylmflib.write_tex(*args, **kwargs)
    for round in range(2):
        subprocess.call(["xelatex", "-output-directory=%s" % result_directory, "%s" % args[1], "--halt-on-error=N"])


if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
    start = datetime.datetime.now()

    print("*-*-* avancement maximal : 3")

    working_directory = sys.argv[1]
    os.chdir(working_directory)
    print(os.getcwd())

    eol_script = os.path.join(pylmflib.utils.__path__[0], 'eol', 'eol.py')
    uid_script = os.path.join(pylmflib.utils.__path__[0], 'uid', 'uid.py')
    table_script = os.path.join(pylmflib.utils.__path__[0], 'tables', 'tables.py')

    # Entrées.
    result_directory = os.path.join(working_directory, "result")
    lexicon_file = os.path.join(working_directory, "Dictionary.txt")
    configuration_file = os.path.join(working_directory, "config.xml")
    setting_file = os.path.join(working_directory, "setting.py")
    sort_order_file = os.path.join(working_directory, "sort_order.xml")
    latex_preamble = os.path.join(working_directory, "preamble.tex")
    latex_french_introduction = os.path.join(working_directory, "introduction_fra.tex")
    latex_english_introduction = os.path.join(working_directory, "introduction_eng.tex")
    latex_chinese_introduction = os.path.join(working_directory, "introduction_cmn.tex")
    french_title = u"Dictionnaire na-chinois-français"
    english_title = u"Na-English-Chinese-French Dictionary"
    chinese_title = u"\zh{摩梭-汉-英-法词典}"

    # Sorties.
    eol_lexicon_file = os.path.join(result_directory, "dictionary-eol.txt")
    uid_lexicon_file = os.path.join(result_directory, "dictionary-uid.txt")
    xml_lexicon_file = os.path.join(result_directory, "dictionary.xml")
    french_table_file = os.path.join(result_directory, 'table_fra.tex')
    english_table_file = os.path.join(result_directory, 'table_eng.tex')
    chinese_table_file = os.path.join(result_directory, 'table_cmn.tex')
    french_dictionary_file = os.path.join(result_directory, 'dictionary_fra.tex')
    english_dictionary_file = os.path.join(result_directory, 'dictionary_eng.tex')
    chinese_dictionary_file = os.path.join(result_directory, 'dictionary_cmn.tex')

    print("*-*-* avancement : 1")

    # Fonctions et variables personnelles surdéfinissantes.
    personal_settings = imp.load_source("", setting_file)

    if not os.path.exists(result_directory):
        os.mkdir(result_directory)

    pylmflib.read_config(configuration_file)

    os.system("python2 %s -i %s -o %s"% (eol_script, lexicon_file, eol_lexicon_file))
    os.system("python2 %s -i %s -o %s"% (eol_script, eol_lexicon_file, uid_lexicon_file))

    lexical_resource = pylmflib.read_mdf(id="na")

    (xml_order, xml_type) = pylmflib.read_sort_order(sort_order_file)
    personal_settings.classify_lexicon(lexical_resource.get_lexicon("na"), xml_order, xml_type)

    os.system("python2 %s -i %s -f %s -e %s -c %s" % (table_script, lexicon_file, french_table_file, english_table_file, chinese_table_file))

    pylmflib.write_xml_lmf(lexical_resource, xml_lexicon_file)

    print("*-*-* avancement : 2")

    # Partie avec parallélisme.
    dictionary_languages = {"french": {'target': spawn_full_process, 'args': [lexical_resource, french_dictionary_file], 'kwargs': {'preamble': latex_preamble, 'introduction': latex_french_introduction, 'lmf2tex': personal_settings.tex_fra, 'items': personal_settings.items, 'sort_order': xml_order, 'tables': [french_table_file], 'title': french_title, 'tex_language': "french", 'tex_other_languages': ["chinese"]}},
                             "english": {'target': spawn_full_process, 'args': [lexical_resource, english_dictionary_file], 'kwargs': {'preamble': latex_preamble, 'introduction': latex_english_introduction, 'lmf2tex': personal_settings.tex_eng, 'items': personal_settings.items, 'sort_order': xml_order, 'tables': [english_table_file], 'title': english_title, 'tex_language': "english", 'tex_other_languages': ["chinese"]}},
                             "chinese": {'target': spawn_full_process, 'args': [lexical_resource, chinese_dictionary_file], 'kwargs': {'preamble': latex_preamble, 'introduction': latex_chinese_introduction, 'lmf2tex': personal_settings.tex_cmn, 'items': personal_settings.items, 'sort_order': xml_order, 'tables': [chinese_table_file], 'title': chinese_title, 'tex_language': "chinese", 'tex_other_languages': ["english", "french"]}}
                            }
    process_list = []
    for language, parameters in dictionary_languages.items():
        print(u"Langue : %s" % language)
        process = multiprocessing.Process(target=parameters['target'], args=parameters['args'], kwargs=parameters['kwargs'])
        process_list.append(process)
        process.start()
    for process in process_list:
        process.join()

    end =  datetime.datetime.now()
    print(u"%s secondes !" % (end-start).total_seconds())
else:
    print(u"Aucun répertoire valide en entrée...")
