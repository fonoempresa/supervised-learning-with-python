"""
Features:
● Petal length
● Petal width
● Sepal length
● Sepal width
Target variable: Species
● Versicolor
● Virginica
● Setosa
"""
#import datasets from sklearn
from sklearn import datasets

#import pandas
import pandas as pd

#import matplotlib
import matplotlib.pyplot as plt

#choose a plotting style
plt.style.use('ggplot')

#load iris dataset
iris = datasets.load_iris()

#prints the type/type object of iris
print(type(iris))

#prints the dictionary keys of iris data
print(iris.keys())

#prints the type/type object of given attributes
print(type(iris.data), type(iris.target))

#prints the no of rows and columns in the dataset
print(iris.data.shape)

#prints the target set of the data
print(iris.target_names)

#load iris dataset
X = iris.data

#load iris target set
Y = iris.target

#convert datasets' type into dataframe 
df = pd.DataFrame(X, columns=iris.feature_names)

#print the head elements of dataframe
print(df.head())
