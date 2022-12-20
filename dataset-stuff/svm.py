def svm(datasetRaw, kernel, degree, traintest):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import LabelEncoder

    dataset = pd.read_csv(datasetRaw)
    dataset.replace('?', np.nan, inplace=True)
    dataset.dropna(axis = 1 ,inplace=True)

    datatype = dataset.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all())
    newdata = []
    for data in datatype:
        newdata.append(datatype[1])
    datatype = newdata
    le = LabelEncoder()
    for i in range(len(datatype)):
        if datatype[i] == False:
            dataset.iloc[:,i] = le.fit_transform(dataset.iloc[:,i])  

    xtrain, xtest , ytrain, ytest = train_test_split(dataset.iloc[:, :-1], dataset.iloc[:,dataset.shape[1]-1], test_size=traintest, random_state=0)
    sc = StandardScaler()
    xtrain = sc.fit_transform(xtrain)
    xtest = sc.transform(xtest)

    svcmodel = SVC(kernel=kernel, degree=degree, C=1.0, gamma='auto', cache_size=12000)
    svcmodel.fit(xtrain, ytrain)

    ypred = svcmodel.predict(xtest)

    cm = confusion_matrix(ytest, ypred)
    accuracy = accuracy_score(ytest, ypred)


    return cm, accuracy