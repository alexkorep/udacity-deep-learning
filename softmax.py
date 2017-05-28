import numpy as np


def softmax1d(input):
    if not isinstance(input, list):
        input = input.tolist()

    total_exp = sum(np.exp(i) for i in input)
    if not total_exp:
        # zero array
        return input

    result = []
    for val in input:
        result.append(np.exp(val) / total_exp)

    return np.array(result)


def softmax2d(input):
    intermed = np.transpose(input)
    result = []
    for val in intermed:
        row = softmax1d(val)
        result.append(row)

    result = np.transpose(result)
    return result


def softmax(input):
    if not len(input):
        return input

    if not isinstance(input[0], (int, long, float, complex)):
        return softmax2d(input)

    return softmax1d(input)

scores = [1.0, 2.0, 3.0]
print softmax(scores)

scores = np.array([[1, 2, 3, 6],
                   [2, 4, 5, 6],
                   [3, 8, 7, 6]])

print softmax(scores)