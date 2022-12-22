import streamlit as st
import numpy as np
import pandas as pd
import time

if st.checkbox("Show Data"):
    dataframe = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(dataframe)

    option = st.selectbox('Which number?', dataframe['a'])
    'You selected: ', option

x = st.slider('x slider')
st.write(x, 'squared is', x * x)

st.text_input('text input', key = 'name')
st.session_state.name

selbox = st.selectbox('selectbox', ['a', 'b', 'c'])
slider = st.slider('slider', 0, 10, (3, 7))

left_column, right_column = st.columns(2)
right_column.button('hi')

with left_column:
    chosen = st.radio('radio', ['a', 'b', 'c'])
    st.write('You selected', chosen)

latestiter = st.empty()
bar = st.progress(0)
for i in range(100):
    latestiter.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'and now we\'re done'

with st.sidebar.form("Input"):
    queryText = st.text_area("SQL to execute:", height=3, max_chars=None)
    btnResult = st.form_submit_button('Run')

if btnResult:
    st.sidebar.text('Button pushed')

    # run query
    st.write(queryText)