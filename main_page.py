import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from thefuzz import fuzz, process 

# Add a title and intro text
st.title('European UnionConsolidated Financial Sanctions List')
st.text('Check the status of potential business partners')

st.sidebar.markdown("# Main page ")

#col1, col2 = st.columns(2  )
userInputName = st.text_input('Enter possible name of partner', 'Search')
st.write('Entered name', userInputName)

#userInputAddress = col2.st.text_input('Enter possible address of partner', 'Search')
#col2.st.write('Entered address')

df = pd.read_csv("data/EuropeanSanctions.csv")


# Preprocessing
n = df['Identity information'].to_string().split()

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

    return resultlist



col3, col4, col5 = st.columns(3)
col3.metric("Temperature", "70 °F", "1.2 °F")
col4.metric("Wind", "9 mph", "-8%")
col5.metric("Humidity", "86%", "4%")




st.write('Business Partner is', findBusinessPartner(n, userInputName, 60))