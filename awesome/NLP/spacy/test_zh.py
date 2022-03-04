""" Basic fuctionalities provided by SpaCy

https://spacy.io/usage/linguistic-features/#named-entities

"""
import spacy
# from spacy.lang.zh.examples import sentences 

# nlp = spacy.load("zh_core_web_sm")
nlp = spacy.load("zh_core_web_trf")
# doc = nlp(sentences[0])
doc = nlp("我有一隻小毛驢我從來也不騎 有一天我心血來潮騎著去趕集")
print(doc.text)

for token in doc:
    print(token.text, token.pos_, token.dep_, token.ent_type)

print("\nEntities:")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
