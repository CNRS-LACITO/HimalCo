#! /usr/bin/env python

from config.mdf import mdf_semanticRelation, pd_grammaticalNumber, pd_person, pd_anymacy, pd_clusivity
from utils.error_handling import OutputError
from common.defs import VERNACULAR, ENGLISH, NATIONAL, REGIONAL

from docx import Document
from docx.shared import Inches

def doc_write(object, filename):
    """! @brief Write a document file.
    @param object The LMF instance to convert into document output format.
    @param filename The name of the document file to write with full path, for instance 'user/output.doc'.
    """
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
            for lexical_entry in lexicon.get_lexical_entries():
                # Heading
                document.add_heading(lexical_entry.get_lexeme(), level=1)
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
