import streamlit as st
import svm

class main:
    def __init__(self):
        st.header("Support Vector Machines (SVM) Training")
        st.sidebar.header("This page is for training the models")
        traintest = st.slider("Testing Sample", 0.0, 1.0, 0.2, 0.1)
        file = st.file_uploader("Upload a CSV file for prediction", type=["csv", "data"])
        ret = st.button("Predict", on_click=(self.predictor(file, traintest)))
        

    def predictor(self, file, traintest):
        import svm
        if file != None:
            x = st.empty()
            x.write("Predicting...")
            cm, accuracy, clf= svm.svm_training(file, traintest)
            st.write("Confusion Matrix: ", cm)
            st.write("Accuracy: ", accuracy)
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