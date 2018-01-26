# ml_classification

Researchers believe the best way to attack AI is to have strong base in algorithms that mimic what the human brain learns.

### What is machine learning?

### Unsupervised learning

The data taken here neither has proper coordinates nor proper parameters. There is no proper specification of different types of output.

Unsupervised learning is where you only have input data (X) and no corresponding output variables.

The goal for unsupervised learning is to model the underlying structure or distribution in the data in order to learn more about the data.

These are called unsupervised learning because unlike supervised learning above there is no correct answers and there is no teacher. Algorithms are left to their own devises to discover and present the interesting structure in the data.

Unsupervised learning problems can be further grouped into clustering and association problems.

#### Clustering: 
A clustering problem is where you want to discover the inherent groupings in the data, such as grouping customers by purchasing behavior.

#### Association:  
An association rule learning problem is where you want to discover rules that describe large portions of your data, such as people that buy X also tend to buy Y.
Some popular examples of unsupervised learning algorithms are:

k-means for clustering problems.
Apriori algorithm for association rule learning problems.

### Reinforcement learning

### Supervised learning

Applied in pursuit of right answer.

The majority of practical machine learning uses supervised learning.

Supervised learning is where you have input variables (x) and an output variable (Y) and you use an algorithm to learn the mapping function from the input to the output.

Y = f(X)

The goal is to approximate the mapping function so well that when you have new input data (x) that you can predict the output variables (Y) for that data.

It is called supervised learning because the process of an algorithm learning from the training dataset can be thought of as a teacher supervising the learning process. We know the correct answers, the algorithm iteratively makes predictions on the training data and is corrected by the teacher. Learning stops when the algorithm achieves an acceptable level of performance.

Supervised learning problems can be further grouped into regression and classification problems.

#### Classification:
A classification problem is when the output variable is a category, such as “red” or “blue” or “disease” and “no disease”.

#### Regression:
A regression problem is when the output variable is a real value, such as “dollars” or “weight”.
Some common types of problems built on top of classification and regression include recommendation and time series prediction respectively.

Some popular examples of supervised machine learning algorithms are:

Linear regression for regression problems.
Random forest for classification and regression problems.
Support vector machines for classification problems.


### Exploratory data analysis (EDA) - The Iris Dataset.

**Features:**

● Petal length

● Petal width

● Sepal length

● Sepal width

Target variable: Species

● Versicolor

● Virginica

● Setosa

### **Using KNN for classification.**

The KNN(K- Nearest Neighbors ) algorithm can be summarized as:

A positive integer k is specified, along with a new sample.

We select the k entries in our database which are closest to the new sample.

We find the most common classification of these entries.

This is the classification we give to the new sample.
