import streamlit as st 
import catfact as cf 
import catpic as cp

def app():
    st.title('Cat Facts')
    st.markdown("Here's a random cat fact to brighten your day!")
    fact = cf.fetch_fact()
    st.markdown(fact)
    img = cp.fetch_pic()
    st.image(img)

if __name__ == "__main__":
    app()