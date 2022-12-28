import streamlit as st, time
import svm

class main:
    def __init__(self):
        st.header("Support Vector Machines (SVM) Training")
        st.sidebar.header("This page is for training the models")
        file = st.file_uploader("Upload a CSV file for prediction", type=["csv", "data"])
        contains_id = st.checkbox("Does the dataset contain an ID column?")
        ret = st.button("Predict", on_click=None)
        if(ret):
            self.train(file, contains_id) 

    def train(self, file, contains_id):
        import svm
        if file != None:
            x = st.empty()
            x.write("Predicting...")
            clf = svm.training(file, contains_id)
            x.write("Done!")
            save = st.button("Save Model", on_click=svm.save(clf, file))
if __name__ == "__main__":
    main()