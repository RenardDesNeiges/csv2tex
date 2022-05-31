from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape


def make_receipt(_infos_perso='1', _infos_banque='2', _id_receipt='3', filname="receipt",_note=None):
    doc = Document()

    doc.preamble.append(Command('title', 'Demande de remboursement N°{}'.format(_id_receipt)))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    # Add stuff to the document
    with doc.create(Section('Informations Personelles', numbering=False)):
        doc.append(_infos_perso)

    with doc.create(Section('Informations Banquaires', numbering=False)):
        doc.append(_infos_banque)
    
    if _note:
        with doc.create(Section('Note', numbering=False)):
            doc.append(_note)
    
    doc.generate_pdf(filname, clean_tex=True)

