import random

def addElem(list):
    for i in range(0, 9999999):
        list.insert(i, i * 1000 * random.random())

list = []
addElem(list)
