# Fuzzy_sanctions
---
Einsatz von Word Embedding-Algorithmen in Business Anwendungen
Aufgabe: Unter Verwendung existierender Python-Bibliotheken (Gensim, etc) Erstellung eines Screening-Algorithmus: Nutzen europäischer Sanktionslisten als Corpus, um einen gegebenen Business Partner (d.h. Namen- und Adress-Information) "fuzzy" zu identifizieren oder zu "entlasten". Entwicklung von Qualitätskennzahlen und gegebenenfalls eines UIs

Bereich: Natural Language Processing
---
## Was wollen wir erreichen?
1. Eingabe von Namen eines Businesspartners
   1. Sofern der Name Falsch geschrieben wurde soll eine Word-Embedding Methode den richtigen Namen Fuzzy erkennen können
2. Ergebnis, ob dieser Name in sanktionsliste vorhanden oder nicht
3. WebApp für die Eingabe und das Ausgeben der Ergebnisse
4. Ergebnis mit relevanten Kennzahlen ( Wortähnlichkeit,....

## Linkliste, erster research
- https://towardsdatascience.com/fuzzy-string-matching-in-python-68f240d910fe
- https://www.activestate.com/blog/how-to-implement-fuzzy-matching-in-python/
- https://pypi.org/project/fuzzysearch/
- https://www.datacamp.com/tutorial/fuzzy-string-python

- https://medium.com/warwick-artificial-intelligence/fuzzy-matching-word-vectors-and-google-ml-kit-lessons-learned-d2376d87ef8a
- https://www.rosette.com/blog/word-embeddings-for-fuzzy-matching-of-organization-names/

A Fuzzy Approach to Approximate String Matching for Text Retrieval in NLP:
- https://www.researchgate.net/publication/333339583_A_Fuzzy_Approach_to_Approximate_String_Matching_for_Text_Retrieval_in_NLP
  
Fuzzy matching entities in a custom entity dictionary
- https://medium.com/tailo-ai/fuzzy-matching-entities-in-a-custom-entity-dictionary-310158d2b60e
## Datenzugriff
- https://www.finanz-sanktionsliste.de/fisalis/
- https://www.bex.ag/sanktionslisten/

## Tutorials
- http://echrislynch.com/2018/07/13/turning-a-pdf-into-a-pandas-dataframe/

## Packages
- PyPDF2
- spacy
- gensim

## word embeddings
- https://towardsdatascience.com/word-embeddings-exploration-explanation-and-exploitation-with-code-in-python-5dac99d5d795
Gensim_Word2Vec_Tutorial
- https://www.kaggle.com/code/pierremegret/gensim-word2vec-tutorial

## Welche zwischenschritte haben wir?

##additional ideas
- Categories of Sanctions
- Country separation
- Male / Female 

