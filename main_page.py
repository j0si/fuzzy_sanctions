import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from thefuzz import fuzz, process 



# Add a title and intro text
st.title('European UnionConsolidated Financial Sanctions List')
st.caption('Check the status of potential business partners')

st.sidebar.markdown("# Main page ")

#col1, col2 = st.columns(2  )
userInputName = st.text_input('Enter possible name of partner', 'Search')
st.write('Entered name', userInputName)

#userInputAddress = col2.st.text_input('Enter possible address of partner', 'Search')
#col2.st.write('Entered address')

df = pd.read_csv("data/EuropeanSanctions.csv")

col1, col2, col3 = st.columns(3)


# Preprocessing
n = df['Identity information'].to_string().split()

# Functions





def findBusinessPartner(input, name, threshold):
    namelist = name.split(" ")
    print(namelist)
    count = 0
    resultlist = []
    for name in namelist:

        for i in input:
        
            if fuzz.ratio(i, name) >= threshold:
                count += 1
                #print(fuzz.ratio(i, name), name, i)
                resultlist.append([fuzz.ratio(i,name) ,name,i])
                
    resultlist.sort(key = lambda x: x[0], reverse = True)
    if count == 0: 
        print(f'Your requested Business partner {name} with fuzzy threshold {threshold} cannot be found on the EU Sanctions List')

    st.write(resultlist)

with col1:
    st.header('Fuzzy Similarity')
    'Business Partner is', findBusinessPartner(n, userInputName, 60)
with col2:
    st.header('Jaro Winkler Similarity')
    'Jaro Winkler Similarity', jaro_winkler_sim(n, userInputName)
with col3:
    st.metric("Wind", "9 mph", "-8%")
