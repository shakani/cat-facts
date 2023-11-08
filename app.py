import streamlit as st 

def fetch_fact():
    return 'Cat fact placeholder'

def app():
    st.title('Cat Facts')
    st.markdown("Here's a random cat fact to brighten your day!")
    st.markdown(fetch_fact())

if __name__ == "__main__":
    app()