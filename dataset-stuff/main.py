import streamlit as st
import svm

class main:
    def __init__(self):
        st.header("Support Vector Machines (SVM)")
        degree = st.slider("Degree", min_value=0, max_value=100, value=5, step=1)
        kernel = st.selectbox("Kernel", ["linear", "poly", "rbf", "sigmoid"])
        traintest = st.number_input("Train/Test Split", min_value=0.0, max_value=1.0, value=0.2)
        file = st.file_uploader("Upload a CSV file for prediction", type=["csv"])
        st.button("Predict", on_click=(self.predictor(file, kernel, degree, traintest)))
        

    def predictor(self, file, kernel, degree, traintest):
        if not(file == None):
            x = st.empty()
            x.write("Predicting...")
            cm, accuracy = svm.svm(file, kernel, degree, traintest)
            st.write("Confusion Matrix: ", cm)
            st.write("Accuracy: ", accuracy)
            x.write("Done!")
if __name__ == "__main__":
    main()