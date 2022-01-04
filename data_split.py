import os

test = open(r'test.txt','r')
train = open(r'train.txt','r')
valid = open(r'valid.txt','r')

test_classes = []
for line in test:
    temp = line.split()
    if temp[1] in test_classes:
        continue
    else:
        test_classes.append(temp[1])
        
train_classes = []
for line in train:
    temp = line.split()
    if temp[1] in train_classes:
        continue
    else:
        train_classes.append(temp[1])

valid_classes = []
for line in valid:
    temp = line.split()
    if temp[1] in valid_classes:
        continue
    else:
        valid_classes.append(temp[1])

test_path = "/Users/roshanrajan/Desktop/oxford-102-flowers/test"
train_path = "/Users/roshanrajan/Desktop/oxford-102-flowers/train"
valid_path = "/Users/roshanrajan/Desktop/oxford-102-flowers/valid"
img_path = "/Users/roshanrajan/Desktop/Fellowship.ai_challenge"

#for each in test_classes:
#    path = os.path.join(test_path,each)
#    os.mkdir(path)

#for each in train_classes:
#    path = os.path.join(train_path,each)
#    os.mkdir(path)

#for each in valid_classes:
#    path = os.path.join(valid_path,each)
#    os.mkdir(path)
test3 = open(r'test.txt','r')
train3 = open(r'train.txt','r')
valid3 = open(r'valid.txt','r')

for line in test3:
    temp = line.split()
    prev = os.path.join(img_path,temp[0])
    new = os.path.join(test_path,temp[1],temp[0][4:])
    os.rename(prev,new)

for line in train3:
    temp = line.split()
    prev = os.path.join(img_path,temp[0])
    new = os.path.join(train_path,temp[1],temp[0][4:])
    os.rename(prev,new)

for line in valid3:
    temp = line.split()
    prev = os.path.join(img_path,temp[0])
    new = os.path.join(valid_path,temp[1],temp[0][4:])
    os.rename(prev,new)


    


