import streamlit as st 
import catfact as cf 

def fetch_fact():
    return 'Cat fact placeholder'

def app():
    st.title('Cat Facts')
    st.markdown("Here's a random cat fact to brighten your day!")
    fact = cf.fetch_fact()
    st.markdown(fact)

if __name__ == "__main__":
    app()