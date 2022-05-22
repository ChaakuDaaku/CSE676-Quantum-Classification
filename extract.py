import os
import re
import random

data_dir = './dataset/'
lst = os.listdir('./images/')
labels = []

for filename in lst:
    _, label, _ = re.split("([A-z]+_)+", filename)
    if label[:-1] not in labels:
        labels.append(label[:-1])
      
labels = random.sample(labels, k=8)
labels.sort()


def train_test_val_split(percent, data_set):
    lst = os.listdir("./images/")
    n = len(lst)
    samples = random.sample(lst, k=int(abs(n*percent)))

    for filename in samples:
        _, label, name = re.split("([A-z]+_)+", filename)
        
        if label[:-1] in labels and ".jpg" in name:            
            _dir = data_dir + data_set + "/" + label[:-1] + "/"
            if not os.path.exists(_dir):
                os.makedirs(_dir)
            os.replace("./images/" + filename, _dir + name)

train_test_val_split(0.7, "train")
train_test_val_split(0.5, "test")
train_test_val_split(1, "val")
