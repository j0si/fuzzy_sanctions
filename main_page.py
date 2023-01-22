import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from thefuzz import fuzz, process 



# Add a title and intro text
st.title('European UnionConsolidated Financial Sanctions List')
st.caption('Check the status of potential business partners')

st.sidebar.markdown("# Main page ")

userInputName = st.text_input('Enter possible name of partner', 'Search')
st.write('Entered name', userInputName)

#userInputAddress = col2.st.text_input('Enter possible address of partner', 'Search')
#col2.st.write('Entered address')

df = pd.read_csv("data/EuropeanSanctions.csv")

col1, col2, col3 = st.columns(3)


# Preprocessing
n = df['Identity information'].to_string().split()

# Functions

def jaro_winkler(str1: str, str2: str) -> float:
    resultlist = []
    def get_matched_characters(_str1: str, _str2: str) -> str:
            matched = []
            limit = min(len(_str1), len(_str2)) // 2
            for i, l in enumerate(_str1):
                left = int(max(0, i - limit))
                right = int(min(i + limit + 1, len(_str2)))
                if l in _str2[left:right]:
                    matched.append(l)
                    _str2 = f"{_str2[0:_str2.index(l)]} {_str2[_str2.index(l) + 1:]}"
            return "".join(matched)

    for element in str2:

        # matching characters
        matching_1 = get_matched_characters(str1, element)
        matching_2 = get_matched_characters(element, str1)
        match_count = len(matching_1)

        # transposition
        transpositions = (
            len([(c1, c2) for c1, c2 in zip(matching_1, matching_2) if c1 != c2]) // 2)

        if not match_count:
            jaro = 0.0
        else:
            jaro = (
                1
                / 3
                * (
                    match_count / len(str1)
                    + match_count / len(str2)
                    + (match_count - transpositions) / match_count
                ))

        # common prefix up to 4 characters
        prefix_len = 0
        for c1, c2 in zip(str1[:4], str2[:4]):
            if c1 == c2:
                prefix_len += 1 
            else:
                break
        resultlist.append([round(jaro + 0.1 * prefix_len * (1 - jaro), 4),element])

    resultlist.sort(reverse=True)
    resultlist = resultlist[:5]
    print(resultlist)

    st.write("Top 5 Results:")
    for ele in resultlist:
        st.write(ele)
    #     # if result >= 0.5:
    #     #     st.write(result, element)



def findBusinessPartner(input, name):
  
    resultlist= process.extract(input, name)
    resultlist.sort()
    resultlist = resultlist[:5]
    st.write("Top 5 Results:")
    resultlist
    st.write("Return:")
    for element in resultlist:
        st.write(element)
  



with col1:
    st.header('Fuzzy Similarity')
    findBusinessPartner(userInputName, n)
with col2:
    st.header("Levenshtein Distance")
    #'Levenshtein Distance', levenshteinDistanceDP(userInputName, n)
with col3:
    st.header('Jaro Winkler Similarity')
    jaro_winkler(userInputName, n)