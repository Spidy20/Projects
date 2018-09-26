from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import  train_test_split

iris=load_iris()

x=iris.data
y=iris.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

MLP=MLPClassifier(activation="relu",solver="adam")
MLP.fit(x_train,y_train)
print(MLP.score(x_test,y_test))

