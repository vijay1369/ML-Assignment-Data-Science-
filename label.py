import spacy

from spacy import displacy

nlp = spacy.load('en_core_web_sm')
file_name = 'input.docx'
introduction_file_text = open(file_name,encoding="ISO-8859-1").read()
introduction_file_doc = nlp(introduction_file_text)

for token in introduction_file_doc.ents:
  print(token.label_)
displacy.serve(introduction_file_doc, style="ent")