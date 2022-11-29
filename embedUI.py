import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add a title and intro text
st.title('WebEmbedding European UnionConsolidated Financial Sanctions List')
st.text('This is a web app to fuzzy search possible business partners')


title = st.text_input('Business Partner', 'Search')
st.write('Business Partner is', title)