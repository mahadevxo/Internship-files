import streamlit as st
import svm

class main:
    def __init__(self):
        st.header("Support Vector Machines (SVM) Training")
        st.sidebar.header("This page is for training the models")
        file = st.file_uploader("Upload a CSV file for prediction", type=["csv", "data"])
        ret = st.button("Predict", on_click=(self.predictor(file)))
        

    def predictor(self, file):
        import svm
        if file != None:
            x = st.empty()
            x.write("Predicting...")
            clf= svm.svm_training(file)
            x.write("Done!")
            save = st.button("Save Model", on_click = self.save(file, clf))
            return None
    
    def save(self, file, clf):
        import pickle
        import svm
        import os
        filename = str(file).replace(".csv", ".sav")
        filename = filename.split("'")[1]
        with open(filename, 'w') as fp:
            pass
        pickle.dump(clf, open(filename, 'wb'))
        st.write("Model saved!")
        return None
if __name__ == "__main__":
    main()