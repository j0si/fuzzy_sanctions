import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add a title and intro text
st.title('WebEmbedding European UnionConsolidated Financial Sanctions List')
st.text('This is a web app to fuzzy search possible business partners')


userInput = st.text_input('Business Partner', 'Search')
st.write('Business Partner is', userInput)


# Further imports 
import pandas as pd
import PyPDF2
from thefuzz import fuzz, process

pdfFileObj = open('20221118-FULL.pdf', 'rb') #Create pdf object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# Preprocessing
allText = ""
for i in range(100): #Iterating over n pages 
    pageObj = pdfReader.getPage(i)
    page = pageObj.extractText()
    allText += page #Store page content into string variable


allText = allText.replace(';','')

alltext_string_all = allText.replace('Legal basis',';Legal basis').replace('Identity information',';Identity information').replace('Programme', ';Programme').replace('Birth information',';Birth information').replace('Citizenship information',';Citizenship information').replace('Contact information',';Contact information').replace('Remark',';Remark')
testListSplit = alltext_string_all.split('reference number: EU')

# Create dataframe
dbn_df = pd.DataFrame([sub.split(";") for sub in testListSplit])
dbn_df.fillna("",inplace=True)
dbn_df.columns = ['EU Reference', 'Legal basis', 'Programme', 'Identity information', 'Birth information', 'Citizenship information', 'Contact information', 'Remark','','','','','','','','',]

def cleanupDataframe(dataframe):
    dataframe['Legal basis'] = dataframe['Legal basis'].apply(lambda x: x.replace('Legal basis: ','').replace('\n',''))
    dataframe['Programme'] = dataframe['Programme'].apply(lambda x: x.replace('Programme: ','').replace('\n',''))
    dataframe['Identity information'] = dataframe['Identity information'].apply(lambda x: x.replace('Identity information:','').replace('\n','').replace('Name/Alias:',';').replace('•','').replace('Function:',''))
    dataframe.replace('^\s+', '', regex=True, inplace=True) #front
    dataframe.replace('\s+$', '', regex=True, inplace=True) #end
    
    return dataframe

def stripDataframe(dataframe):
    dataframe['Identity information'] = dataframe['Identity information'].apply(lambda x: x.strip())
    
    return dataframe

cleanupDataframe(dbn_df)
stripDataframe(dbn_df)

st.dataframe(dbn_df)

n = dbn_df['Identity information'].to_string().split()

# Search function
def findBusinessPartner(input, name, threshold):

    for i in n:
        if fuzz.ratio(i, name) >= threshold:
            print(fuzz.ratio(i, name), name)



st.write('Business Partner is', findBusinessPartner(n, userInput, 95))