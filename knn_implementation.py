from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

"""
https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/classification.py
"""
"""
Algorithm - Euclidean Distance.
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

Predict Function.
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
"""
iris = datasets.load_iris()

knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(iris['data'], iris['target'])

X = [
    [5.9, 1.0, 5.1, 1.8],
    [3.4, 2.0, 1.1, 4.8],
]

print(X)

prediction = knn.predict(X)

print(prediction)
