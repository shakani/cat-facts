import streamlit as st 
import catfact as cf 
import catpic as cp

USE_API = False

def fetch_fact(USE_API=False):
    if not USE_API:
        return 'Cat fact'
    else:
        return cf.fetch_fact()

def fetch_pic(USE_API=False):
    if not USE_API:
        return 'https://cdn2.thecatapi.com/images/MTYwNzYxNg.jpg'
    else:
        return cp.fetch_pic()


def app():
    st.title('Cat Facts')
    st.markdown("Here's a random cat fact to brighten your day!")
    fact = fetch_fact(USE_API)
    st.markdown(fact)
    img = fetch_pic(USE_API)
    st.image(img)

if __name__ == "__main__":
    app()