# Fuzzy_sanctions

Einsatz von Word Embedding-Algorithmen in Business Anwendungen
Aufgabe: Unter Verwendung existierender Python-Bibliotheken (Gensim, etc) Erstellung eines Screening-Algorithmus: Nutzen europäischer Sanktionslisten als Corpus, um einen gegebenen Business Partner (d.h. Namen- und Adress-Information) "fuzzy" zu identifizieren oder zu "entlasten". Entwicklung von Qualitätskennzahlen und gegebenenfalls eines UIs
---

## Fuzzy Sanctions Frontent (UI)

Hosting des UI mittels Streamlit. Das Frontend ist verfügbar unter folgender URL beziehungsweise QR-Code.

- https://fuzzy-sanctions.streamlit.app/


![Alt text](img/bad4f017-a6b8-42fe-b51b-8cde08de2fbf.jpg)

## Bereich: Natural Language Processing


## Zieldefinition
- Eingabe von Namen (Personene, Entitäten oder Gruppen)
  -> Unscharfe beziehungsweise fehlertolerate Suchmaschine (Fuzzy)
- Ergebnisausgabe: Namen mit der höchsten Ähnlichkeit und zugehöriger Score 
- FrontEnd (UI) für die Eingabe und Darstellung der Ergebnisse
- Darstellung der relevanten Kennzahlen bzw. Güte
   1. extrinsisch
      - wie gut funktioniert ein anderes modell?
      - wie gut funktioniert die klassifikiation
   2. intrinsisch
      - wort vektoren anschauen, wie gut sind die? 
      - mit menschlichen dictionaries vergleichen ob der vektor genau die gleiche ähnlichkeit ausssagt!

## Ergebnis 
- "Fuzzy" Suchmaschine für finanzsankionierte Personen, Entitäten und Gruppen
- Bereinigung der Daten mittels NER
- Word Embedding (Word2vec) und Vektorbasierte Vergleichsmethoden aufgrund der fehlenden Daten (Volltext) ausgeschlossen
- Ausgabe mittels verschiedener Vergleichsmethoden
- Ausgabe Personen-, Entitäten- bzw. Gruppenbezogenen Informationen

## erster Research (tieferes Literaturverzeichnis in schriftlicher Ausarbeitung)
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
- theFuzz
- spacy
- gensim

## word embeddings
- https://towardsdatascience.com/word-embeddings-exploration-explanation-and-exploitation-with-code-in-python-5dac99d5d795
Gensim_Word2Vec_Tutorial
- https://www.kaggle.com/code/pierremegret/gensim-word2vec-tutorial

##additional ideas
- Categories of Sanctions
- Country separation
- Male / Female 

