import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add a title and intro text
st.title('European UnionConsolidated Financial Sanctions List')
st.text('Check the status of potential business partners')

st.sidebar.markdown("# Main page ")

#col1, col2 = st.columns(2  )
userInputName = st.text_input('Enter possible name of partner', 'Search')
st.write('Entered name', userInputName)

#userInputAddress = col2.st.text_input('Enter possible address of partner', 'Search')
#col2.st.write('Entered address')

# Further imports of functions
from nltk.tokenize import word_tokenize
from gensim.models.phrases import Phrases, Phraser
#import fuzzysearch
#import fuzzywuzzy
import PyPDF2

pdfFileObj = open('20221118-FULL.pdf', 'rb') #Create pdf object
pdfReader = PyPDF2.PdfReader(pdfFileObj) 

allText = ""
for i in range(792): #Iterating over n pages 
    pageObj = pdfReader.pages[i]
    page = pageObj.extract_text()
    allText += page #Store page content into string variable

# Preprocessing
allText = allText.replace(';','')

alltext_string_all = allText.replace('Legal basis',';Legal basis').replace('Identity information',';Identity information').replace('Programme', ';Programme').replace('Birth information',';Birth information').replace('Citizenship information',';Citizenship information').replace('Contact information',';Contact information')
testListSplit = alltext_string_all.split('reference number: EU')

# Create dataframe
dbn_df = pd.DataFrame([sub.split(";") for sub in testListSplit])
dbn_df.fillna("",inplace=True)
dbn_df.columns = ['EU Reference', 'Legal basis', 'Programme', 'Identity information', 'Birth information', 'Citizenship information', 'Contact information']
dataframe = dbn_df

dataframe['Legal basis'] = dataframe['Legal basis'].apply(lambda x: x.replace('Legal basis: ','').replace('\n',''))
dataframe['Programme'] = dataframe['Programme'].apply(lambda x: x.replace('Programme: ','').replace('\n',''))
dataframe['Identity information'] = dataframe['Identity information'].apply(lambda x: x.replace('Identity information:','').replace('Name/Alias:',';').replace('•','').replace('Function:','').split(';'))
dataframe.replace('^\s+', '', regex=True, inplace=True) #front
dataframe.replace('\s+$', '', regex=True, inplace=True) #end
dataframe['Birth information'] = dataframe['Birth information'].apply(lambda x: x.replace('Birth information:\n•',''))

dataframe['Identity information'] = dataframe['Identity information'].apply(lambda x: [y.strip() for y in x ])


from thefuzz import fuzz, process 

# Preprocessing
n = dbn_df['Identity information'].to_string().split()

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