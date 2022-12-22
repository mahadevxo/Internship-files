import os
import streamlit as st

st.header("Support Vector Machines (SVM) Testing")
st.sidebar.header("This page is for testing the models")

def predictor(file, model):
    import svm
    if file != None:
            x = st.empty()
            x.write("Predicting...")
            cm, accuracy = svm.svm_testing(file, model)
            st.write("Confusion Matrix: ", cm)
            st.write("Accuracy: ", accuracy)
            x.write("Done!")
            return None

files = os.listdir()
models = []
for file in files:
    if file.endswith(".sav"):
        models.append(file)

model = st.selectbox("Select a model", models)
print(model)
file = st.file_uploader("Upload a CSV file for prediction", type=["csv", "data"])
ret = st.button("Predict", on_click=(predictor(file, model)))
