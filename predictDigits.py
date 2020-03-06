import sklearn.datasets
import sklearn.svm
from PIL import Image
import numpy

# Image change to Number list
def imageToData(fileName):
    grayImage = Image.open(fileName).convert("L")
    grayImage = grayImage.resize((8,8), Image.ANTIALIAS)
    
    numImage = numpy.asarray(grayImage, dtype = float)
    numImage = numpy.floor(16 -16 * (numImage / 256))
    numImage = numImage.flatten()

    return numImage

# gess Number
def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    print("I gess", n)

data = imageToData("3.png")
predictDigits(data)
