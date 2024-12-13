"""app.py"""

import streamlit as st

# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)

st.title("Bean counter :paw_prints:")

addend = st.number_input("Beans to add", 0, 10)
if st.button("Add"):
    st.session_state.beans += addend
st.markdown(f"Beans counted: {st.session_state.beans}")

first = st.container()
second = st.container()

second.button("A")
first.button("B")

st.button("Next", key="submit")
st.button("Back", key="cancel")

st.selectbox("A", [1, 2, 3], None, help="Pick a number", placeholder="Pick me")
