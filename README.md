# fuzzy_sanctions

Einsatz von Word Embedding-Algorithmen in Business Anwendungen
Aufgabe: Unter Verwendung existierender Python-Bibliotheken (Gensim, etc) Erstellung eines Screening-Algorithmus: Nutzen europäischer Sanktionslisten als Corpus, um einen gegebenen Business Partner (d.h. Namen- und Adress-Information) "fuzzy" zu identifizieren oder zu "entlasten". Entwicklung von Qualitätskennzahlen und gegebenenfalls eines UIs

Bereich: Natural Language Processing

## was wollen wir erreichen?
1. Eingabe von Namen eines Businesspartners
2. Ergebnis, ob dieser Name in sanktionsliste vorhanden oder nicht
3. Ergebnis mit relevanten Kennzahlen ( Wortähnlichkeit,....

## linkliste, erster research
- https://towardsdatascience.com/fuzzy-string-matching-in-python-68f240d910fe
- https://www.activestate.com/blog/how-to-implement-fuzzy-matching-in-python/
- https://pypi.org/project/fuzzysearch/
- https://www.datacamp.com/tutorial/fuzzy-string-python

- https://medium.com/warwick-artificial-intelligence/fuzzy-matching-word-vectors-and-google-ml-kit-lessons-learned-d2376d87ef8a
- https://www.rosette.com/blog/word-embeddings-for-fuzzy-matching-of-organization-names/

  A Fuzzy Approach to Approximate String Matching for Text Retrieval in NLP:
  - https://www.researchgate.net/publication/333339583_A_Fuzzy_Approach_to_Approximate_String_Matching_for_Text_Retrieval_in_NLP
  
## wo sind daten?
- https://www.finanz-sanktionsliste.de/fisalis/
- https://www.bex.ag/sanktionslisten/

## Tutorials
- http://echrislynch.com/2018/07/13/turning-a-pdf-into-a-pandas-dataframe/

## welche packages kann man nutzen?
- PyPDF2
- spacy
- gensim

## welche zwischenschritte haben wir?

##additional ideas
- Categories of Sanctions
- Country separation
- Male / Female 

