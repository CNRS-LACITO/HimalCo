#! /usr/bin/env python

from config.mdf import mdf_semanticRelation, pd_grammaticalNumber, pd_person, pd_anymacy, pd_clusivity
from utils.error_handling import OutputError
from common.defs import VERNACULAR, ENGLISH, NATIONAL, REGIONAL
from utils.io import ENCODING

from docx import Document
from docx.shared import Inches

def doc_write(object, filename, items=lambda lexical_entry: lexical_entry.get_lexeme(), sort_order=None):
    """! @brief Write a document file.
    @param object The LMF instance to convert into document output format.
    @param filename The name of the document file to write with full path, for instance 'user/output.doc'.
    @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
    @param sort_order Python list. Default value is 'None', which means that the document output is alphabetically ordered.
    """
    if sort_order is None:
        # TODO
        return
    document = Document()
    # Parse LMF values
    if object.__class__.__name__ == "LexicalResource":
        for lexicon in object.get_lexicons():
            # Document title
            document.add_heading(lexicon.get_id(), 0)
            # Plain paragraph
            document.add_paragraph(lexicon.get_label())
            # Page break
            document.add_page_break()
            # Lexicon is already ordered
            n = -1
            level = 0
            current_item = ("", "")
            for lexical_entry in lexicon.get_lexical_entries():
                # Consider only main entries (subentries will be written as parts of the main entry)
                if lexical_entry.find_related_forms("main entry") != []:
                    continue
                # Check if item of current element is different from previous one
                while items(lexical_entry) != current_item[0].decode(ENCODING):
                    try:
                        n += 1
                        current_item = sort_order[n]
                        while current_item[0].startswith("TITLE"):
                            level = int(current_item[0][-1])
                            # Heading
                            document.add_heading(current_item[1].decode(ENCODING), level=level)
                            n += 1
                            current_item = sort_order[n]
                        # Heading
                        document.add_heading(current_item[1].decode(ENCODING), level=level+1)
                    except IndexError:
                        # Reached end of list
                        break
                # Heading
                document.add_heading(lexical_entry.get_lexeme(), level=level+2)
                # Paragraph
                p = document.add_paragraph()
                # Bold
                p.add_run(lexical_entry.get_partOfSpeech()).bold = True
                for sense in lexical_entry.get_senses():
                    # Items in unordered list
                    for gloss in sense.find_glosses(language=None):
                        document.add_paragraph(gloss, style='ListBullet')
                    # Items in ordered list
                    for context in sense.get_contexts():
                        for example in context.find_written_forms():
                            document.add_paragraph(example, style='ListNumber')
                # Intense quote
                document.add_paragraph('Paradigms', style='IntenseQuote')
                # Table
                table = document.add_table(rows=1, cols=2)
                hdr_cells = table.rows[0].cells
                hdr_cells[0].text = 'Paradigm'
                hdr_cells[1].text = 'Form'
                for item in lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["sg"]):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "sg"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["pl"]):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "pl"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['s']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1s"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['s']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "2s"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['s']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "3s"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['s']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "4s"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['d']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1d"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['d']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "2d"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['d']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "3d"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['d']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "4d"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1p"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['e']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1e"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['i']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1i"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['p']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "2p"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['p']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "3p"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['p']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "4p"
                    row_cells[1].text = item
                    # Paragraph
                    p = document.add_paragraph()
                    # Italic
                    p.add_run(lexical_entry.find_notes(type=None)).italic = True
                    # Picture
                    #document.add_picture('name.png', width=Inches(1.25))
    else:
        raise OutputError(object, "Object to write must be a Lexical Resource.")
    document.save(filename)
