import streamlit as st
import random

l = random.sample([12,433,424,2342,5234,1,2,4,1,2,43], 5)
st.write(l)
st.bar_chart(l)