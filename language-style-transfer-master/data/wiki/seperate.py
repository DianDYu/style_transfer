import random

txt0 = open("wiki.simple", "r")
txt1 = open("wiki.unsimplified", "r")
lines0 = txt0.readlines()
lines1 = txt1.readlines()
num = len(lines0)
train0 = open("wiki.train.0", "w")
train1 = open("wiki.train.1", "w")
dev0 = open("wiki.dev.0", "w")
dev1 = open("wiki.dev.1", "w")
test0 = open("wiki.test.0", "w")
test1 = open("wiki.test.1", "w")
idxTrain0 = random.sample(range(0,num), 100000)
idxTrain1 = random.sample(range(0,num), 100000)
allIdx = set(range(0, num))
idxLeft0 = list(allIdx - set(idxTrain0))
idxLeft1 = list(allIdx - set(idxTrain1))
leftNum = len(idxLeft0)
idxDev0 = idxLeft0[:leftNum/2]
idxTest0 = idxLeft0[leftNum/2:]
idxDev1 = idxLeft1[:leftNum/2]
idxTest1 = idxLeft1[leftNum/2:]
for i in idxTrain0:
    train0.write(lines0[i])
for i in idxTrain1:
    train1.write(lines1[i])
for i in idxDev0:
    dev0.write(lines0[i])
for i in idxDev1:
    dev1.write(lines1[i])
for i in idxTest0:
    test0.write(lines0[i])
for i in idxTest1:
    test1.write(lines1[i])
train0.close()
train1.close()
dev0.close()
dev1.close()
test0.close()
test1.close()

