import streamlit as st

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is an example of a stremlite app. 

    **There's :rainbow[so much] you can build!**
    """
)

if st.button("Send balloons!"):
    st.balloons()
