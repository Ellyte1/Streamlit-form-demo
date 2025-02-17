import streamlit as st
import Display



st.title('GATE')
st.text_input('Enter your name')
col1,col2 = st.columns(2)
with col1:
    st.text_input("Education1")
    st.radio('Gender', ['male','female'])
    st.selectbox('Subjects', ['Physics','Chemistry','Math'])
with col2:
    st.text_input("Education2")
    st.text('Education3')
    st.checkbox('pg')
    st.checkbox('Phd')


st.text_input('Enter value')
st.button('submit')
if st.button('submit'):
    st.session_state.page = 'Display'
