def svm_training(datasetRaw, traintest):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import GridSearchCV

    dataset = pd.read_csv(datasetRaw)
    dataset.replace('?', np.nan, inplace=True)
    dataset.dropna(axis = 1,inplace=True)

    datatype = dataset.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all())
    newdata = []
    for data in datatype:
        newdata.append(datatype[1])
    datatype = newdata
    le = LabelEncoder()
    for i in range(len(datatype)):
        if datatype[i] == False:
            dataset.iloc[:,i] = le.fit_transform(dataset.iloc[:,i])  

    sc = StandardScaler()
    param = {'kernel': ('linear', 'rbf', 'poly'), 'C': [1, 10], 'degree': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'gamma': ('auto', 'scale')}
    clf = GridSearchCV(SVC(probability=True), param, cv=5, refit=True)

    cm, accuracy = None, None

    if(traintest == 0.0):
        x = dataset.iloc[:, :-1]
        y = dataset.iloc[:,dataset.shape[1]-1]
        x = sc.fit_transform(x)        
        ypred = clf.fit(x, y).predict(x)
        cm = confusion_matrix(y, ypred)
        accuracy = accuracy_score(y, ypred)

    else:
        xtrain, xtest , ytrain, ytest = train_test_split(dataset.iloc[:, :-1], dataset.iloc[:,dataset.shape[1]-1], test_size=traintest, random_state=0)
        xtrain = sc.fit_transform(xtrain)
        xtest = sc.transform(xtest)
        clf.fit(xtrain, ytrain)
        ypred = clf.predict(xtest)
        cm = confusion_matrix(ytest, ypred)
        accuracy = accuracy_score(ytest, ypred)
 
    return cm, (str(accuracy*100)+"%"), clf

def svm_testing(datasetRaw, model):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import GridSearchCV
    import pickle

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

    x = dataset.iloc[:, :-1]
    y = dataset.iloc[:,dataset.shape[1]-1]

    sc = StandardScaler()
    x = sc.fit_transform(x)
    x = sc.transform(x)

    clf = pickle.load(open(model, 'rb'))

    ypred = clf.predict(x)
    accuracy = (accuracy_score(y, ypred))*100

    cm = confusion_matrix(y, ypred)
    accuracy = accuracy_score(y, ypred)
    print()

    return cm, (str(accuracy*100)+"%")