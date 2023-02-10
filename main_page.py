import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from thefuzz import fuzz, process 
import streamlit as st
import itertools
import re
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.set_page_config(
    page_title = "Fuzzy Sanctions",
    layout="wide"
    )

def draw_all(key,plot=False):
    st.write("""
    # Integrationsseminar Projekt Frontend
    

    """)

with st.sidebar:
    draw_all("sidebar")

# Add a title and intro text
st.title('European Union Consolidated Financial Sanctions List')
#st.sidebar.markdown("# Main page ")


userInputName = st.text_input('Enter possible name of partner', 'Search')
st.write('Entered name', userInputName)

col1, col2, col3, col4 = st.columns(4)
#col4, col5 = st.columns(2)


# Preprocessing 
## Einlesen der Daten
df = pd.read_csv("data/EuropeanSanctions.csv")

## Erstellen der Datengrundlage
identityInformation = []
for index, row in df.iterrows():
    identityInformation.append(df['Identity information'][index])
#flatlists = list(itertools.chain.from_iterable(identityInformation))
identityInformation2 = [string.split() for string in identityInformation]
flatlists2 = list(itertools.chain.from_iterable(identityInformation2))
flatlists3 = [string for string in flatlists2 if not string.startswith('(')]


# Jaro Winkler Implementation
def jaro_winkler(str1: str, str2: str) -> float:
    resultlist = []
    
    for element in str2:

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
                    + match_count / len(element)
                    + (match_count - transpositions) / match_count
                ))

        # common prefix up to 4 characters
        prefix_len = 0
        for c1, c2 in zip(str1[:4], element[:4]):
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


# Fuzzy Similarity Implementation
def findBusinessPartner(input, name):
  
    resultlist= process.extract(input, name)
    resultlist.sort()
    resultlist = resultlist[:5]
    st.write("Top 5 Results:")
    resultlist
    # st.write("Return:")
    # print('Fuzzy', resultlist)
    # for element in resultlist:
    #     st.write(element)


# Levenstein Implementation
import numpy as np

def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()

def levenshteinDistanceDP(token1, token2):
    
    # safe results
    resultlist = []
    
    def calculations_levenstein(token1, token2):
        distances = np.zeros((len(token1) + 1, len(token2) + 1))

        for t1 in range(len(token1) + 1):
            distances[t1][0] = t1

        for t2 in range(len(token2) + 1):
            distances[0][t2] = t2
            
        a = 0
        b = 0
        c = 0
        
        for t1 in range(1, len(token1) + 1):
            for t2 in range(1, len(token2) + 1):
                if (token1[t1-1] == token2[t2-1]):
                    distances[t1][t2] = distances[t1 - 1][t2 - 1]
                else:
                    a = distances[t1][t2 - 1]
                    b = distances[t1 - 1][t2]
                    c = distances[t1 - 1][t2 - 1]
                    
                    if (a <= b and a <= c):
                        distances[t1][t2] = a + 1
                    elif (b <= a and b <= c):
                        distances[t1][t2] = b + 1
                    else:
                        distances[t1][t2] = c + 1

        # print matrix
        # printDistances(distances, len(token1), len(token2))
        return distances[len(token1)][len(token2)]

    for element in token2:
        resultlist.append([calculations_levenstein(token1, element), element])
    resultlist.sort()
    resultlist = resultlist[:5]
    print(resultlist)
    
    st.write("Top 5 results:")
    for ele in resultlist:
        st.write(ele)


# Longest Common Substring

def lcs(S,T):
    
    resultlist = []
    
    def lcs_calc(S,T):
        m = len(S)
        n = len(T)
        counter = [[0]*(n+1) for x in range(m+1)]
        longest = 0
        lcs_set = set()
        for i in range(m):
            for j in range(n):
                if S[i] == T[j]:
                    c = counter[i][j] + 1
                    counter[i+1][j+1] = c
                    if c > longest:
                        lcs_set = set()
                        longest = c
                        lcs_set.add(S[i-c+1:i+1])
                    elif c == longest:
                        lcs_set.add(S[i-c+1:i+1])

        return lcs_set

    for element in T:
        resultlist.append([lcs_calc(S, element), element])
    resultlist.sort(reverse=True)
    resultlist = resultlist[:5]
    
    print(resultlist)
    
    st.write("Top 5 results:")
    for ele in resultlist:
        st.write(ele)


# Display Similarities 
with col1:
    st.header('Fuzzy Score')
    findBusinessPartner(userInputName, flatlists3)

with col2:
    st.header('Jaro Winkler Similarity')
    jaro_winkler(userInputName, flatlists3)

with col3:
    st.header('Levenshtein Distance')
    levenshteinDistanceDP(userInputName, flatlists3)
    
with col4:
    st.header('Longest Common Substring ')
    lcs(userInputName, flatlists3)
            
      
st.markdown('***')  
st.title("Auto Filter European Union Consolidated Financial Sanctions List")

# st.write(
#     """This app accomodates the blog [here](https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/)
#     and walks you through one example of how the Streamlit
#     Data Science Team builds add-on functions to Streamlit.
#     """
# )


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns
    Args:
        df (pd.DataFrame): Original dataframe
    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].str.contains(user_text_input, na=False)]

    return df

st.dataframe(filter_dataframe(df))

st.write('Input Data')
st.write(flatlists3)
