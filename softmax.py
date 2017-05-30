import numpy as np


def softmax(input):
    sum = np.sum(np.exp(input), 0)
    if not sum.any():
        return input

    return np.exp(input)/sum

scores = [1.0, 2.0, 3.0]
print softmax(scores)
scores = [100.0, 101.0, 102.0]
print softmax(scores)

"""
scores = np.array([[1, 2, 3, 6],
                   [2, 4, 5, 6],
                   [3, 8, 7, 6]])

print softmax(scores)
"""