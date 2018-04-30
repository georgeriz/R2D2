from foo import foo
import spacy

nlp = spacy.load('en')

doc = nlp(unicode(foo()))

for token in doc:
    print token.pos_