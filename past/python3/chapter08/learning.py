import sys, json, re, numpy, math, knock71_function
from stemming.porter2 import stem

def create_features(sentence, ids, stopwordList):
    f_vec = numpy.zeros(len(ids))
    for word in sentence.split(' '):
        if not(word.strip() in stopwordList):
            tempword = stem(re.sub('[\.\,\;\:\!\?\(\)\"\']', '', word).strip())
            if tempword in ids:
                f_vec[ids[tempword]] += 1
    return(f_vec)
                
def hypothesis(w, phi):
    temp = numpy.dot(w, phi)
    if temp <= -709:
        temp = -709
    return((1 / (1 + math.e ** (- temp))))

def sign (x, threshold):
    if x >= threshold:
        return(1)
    else:
        return(-1)

def update_weights(w, phi, y, alpha):
    temp = numpy.dot(w, phi)
    if temp <= -709:
        temp = -709
    w += alpha * y * phi * ((math.e ** temp) / ((1 + (math.e ** temp)) ** 2))

def learning(w, ids, model, alpha, stopwordList):
    X = model[3:]
    y = float(model[:2])
    phi = create_features(X, ids, stopwordList)
    update_weights(w, phi, y, alpha)
