import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


data=pd.read_csv('train.csv')
dataTest=pd.read_csv('test.csv')
dataTest=dataTest.iloc[:,-14:-2]

species = data.iloc[:,-2:-1].values
x_train, x_test,y_train, y_test  = train_test_split(data.iloc[:,-14:-2],species,test_size=0.33,random_state=0)

knn = KNeighborsClassifier(n_neighbors=10,metric='minkowski')
knn.fit(x_train,y_train.ravel())
result = knn.predict(x_test)

predicted = knn.predict(dataTest)
expected = y_test
print(predicted) 