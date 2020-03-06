import sklearn.datasets

digits = sklearn.datasets.load_digits()

print('data count=', len(digits.images))
print('image data=', digits.images[0])
print('what number', digits.target[0])