""" Importing important Libraries """
import numpy as np
import os
import matplotlib.pyplot as plt
from IPython.display import Image, display

""" Loding the data and saving path in images_dir """
images_dir = os.listdir("./Flicker8k_Dataset/")

""" loading paths of the data """
images_path = './Flicker8k_Dataset/'
captions_path = './Flickr8k_text/Flickr8k.token.txt'
train_path = './Flickr8k_text/Flickr_8k.trainImages.txt'
val_path = './Flickr8k_text/Flickr_8k.devImages.txt'
test_path = './Flickr8k_text/Flickr_8k.testImages.txt'

""" Reading the images, caption and token data """
captions = open(captions_path, 'r').read().split("\n")
x_train = open(train_path, 'r').read().split("\n")
x_val = open(val_path, 'r').read().split("\n")
x_test = x_val = open(test_path, 'r').read().split("\n")

""" Creating a dictionary, where key => Image name
	and value => captions stored in a list """
tokens = {}

for ix in range(len(captions)):
    temp = captions[ix].split("#")
    if temp[0] in tokens:
        tokens[temp[0]].append(temp[1][2:])
    else:
        tokens[temp[0]] = [temp[1][2:]]
        
temp = captions[32].split("#")
z = Image(filename=images_path+temp[0])
""" Uncomment to display the image 
	display(z) """

""" Uncomment to print the 5 captions of 0th token 
for ix in range(len(tokens[temp[0]])):
    print(tokens[temp[0]][ix]) """

""" Creating the training, testing and validation file to store their data """
train_dataset = open('./flickr_8k_train_dataset.txt','w')
train_dataset.write("image_id\tcaptions\n")

val_dataset = open('./flickr_8k_val_dataset.txt','w')
val_dataset.write("image_id\tcaptions\n")

test_dataset = open('./flickr_8k_test_dataset.txt','w')
test_dataset.write("image_id\tcaptions\n")

""" Preparing the training data """
for img in x_train:
    if img == '':
        pass
    else:
        for capt in tokens[img]:
            caption = "<start> "+capt+" <end>"
            train_dataset.write(img+"\t"+caption+"\n")
train_dataset.close()

""" Preparing the testing data """
for img in x_test:
    if img == '':
        pass
    else:
        for capt in tokens[img]:
            caption = "<start> "+capt+" <end>"
            test_dataset.write(img+"\t"+caption+"\n")
test_dataset.close()

""" Preparing the Validation data """
for img in x_val:
    if img == '':
        pass
    else:
        for capt in tokens[img]:
            caption = "<start> "+capt+" <end>"
            val_dataset.write(img+"\t"+caption+"\n")
val_dataset.close()