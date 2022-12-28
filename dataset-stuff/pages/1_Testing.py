import os
import pickle
import streamlit as st

st.header("Support Vector Machines (SVM) Testing")
st.sidebar.header("This page is for testing the models")

def test(file, model):
    import svm
    if file != None:
            x = st.empty()
            x.write("Predicting...")
            classificationReport = svm.testing(file, model)
            st.write(classificationReport)
            x.write("Done!")
            return None

files = os.listdir()
models = []
for file in files:
    if file.endswith(".pkl"):
        models.append(file)

if models == []:
    st.write("No models found")
else:
    model = st.selectbox("Select a model", models)
    assert model != None, "No model selected"
    model = pickle.load(open(model, 'rb'))
    file = st.file_uploader("Upload a CSV file for prediction", type=["csv", "data"])
    ret = st.button("Predict", on_click=(test(file, model)))
