
def nltk_tb_settings(options):
    settings = tb.ToolboxSettings()
    settings.open(options.struct)
    tree = settings.parse(unwrap=False, encoding='cp1252')
    settings_tree = tb.ElementTree(tree)
    settings_str = tb.to_settings_string(settings_tree).encode(CODEC)
    if options.verbose:
        print settings_str
        for element in settings_tree.getroot():
            print element.tag
    return settings_tree

def nltk_tb_sf(options):
    return tb.StandardFormat(filename=options.input, encoding=CODEC)

def nltk_tb_sfm(first_element, options):
    sfm = tb.to_sfm_string(first_element, encoding=CODEC, errors='strict', unicode_fields=None)
    if options.verbose:
        print sfm
    return sfm

# Working with Toolbox Data
def nltk_tb_db(options):
    db = tb.ToolboxData()
    # From Lexique Pro database
    db.open(options.database)
    lexicon = db.parse(options.grammar, encoding=CODEC)
    #tb.data.indent(lexicon)
    tree = tb.ElementTree(lexicon)
    output = open_file(options.output, "w")
    tree.write(output, encoding=CODEC)
    output.close()
    # Using ElementTree for Accessing Toolbox Data
    [lexeme.text.lower() for lexeme in tree.findall('record/lx')]
    simple_tree = tb.ElementTree(tree.getroot()[1])
    if options.verbose:
        simple_tree.write(sys.stdout)
    # Formatting Entries
    data = tb.ToolboxData(filename=option.input)
    first_element = data.parse(grammar=options.grammar, encoding=CODEC)
    tree = tb.ElementTree(element=first_element)
    tb.remove_blanks(tree.getroot())
    return (first_element, tree)
# Adding a Field to Each Entry

# Validating a Toolbox Lexicon
def validate(lexicon, options):
    fd = nltk.FreqDist(':'.join(field.tag for field in entry) for entry in lexicon.getroot())
    if options.verbose:
        print fd.items()
    ignored_tags = ['arg', 'dcsv', 'pt', 'vx']
#from code_toolbox_validation import *
#validate_lexicon(options.grammar, lexicon.getroot(), ignored_tags)
