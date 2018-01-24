from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()

print(digits.keys())

print(digits.images.shape)
print(digits.data.shape)

plt.imshow(digits.images[12], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
