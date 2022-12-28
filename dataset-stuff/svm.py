def training(dataset, contains_id):
    import pandas as pd
    import numpy as np
    from sklearn.svm import SVC
    from sklearn.metrics import confusion_matrix, classification_report
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import GridSearchCV

    dataset = pd.read_csv(dataset)
    dataset.replace('?', np.nan, inplace=True)
    dataset.dropna(axis = 1,inplace=True)

    if contains_id:
        dataset.drop(dataset.columns[0], axis=1, inplace=True)

    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X = StandardScaler().fit_transform(X)

    params = {'kernel': ['linear', 'rbf', 'poly'], 'C': range(0, 1000, 50), 'degree': [1, 2, 3, 4, 5], 'gamma': [1, 0.1]}
    model = GridSearchCV(SVC(), params, cv = 3, refit=True, verbose=3)

    model.fit(X, y)
    return model

def save(model, dataset):
    import pickle
    dataset = dataset.name
    dataset = dataset.replace(".csv", ".pkl")
    pickle.dump(model, open(dataset, 'wb'))

def testing(dataset, model):
    import pandas as pd
    import numpy as np
    from sklearn.svm import SVC
    from sklearn.metrics import confusion_matrix, classification_report
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import GridSearchCV

    dataset = pd.read_csv(dataset)
    dataset.replace('?', np.nan, inplace=True)  
    dataset.dropna(axis = 1,inplace=True)

    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X = StandardScaler().fit_transform(X)

    ypred = model.predict(X)
    return classification_report(y, ypred, zero_division=1)