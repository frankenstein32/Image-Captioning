# Image-Captioning
Generates Textual Description of Images

# Image captioning model architecture
Combined a CNN and LSTM  :
- Using a CNN for image embedding
- In a sentence language model, an LSTM is predicting the next word in a sentence.

# Data Set
Download the data-set from the link given here <a href="https://forms.illinois.edu/sec/1713398">data-set</a>.
- Dataset is consisting of two types of data:
  1. Images stored in a Flicker8k_Dataset file.
  
   2. text data stored in a Flicker8k_txt file.<br>
      2.1 Further in txt directory the data is divided into some txt file such as:<br>
          2.1.1 Flickr_8k.trainImages.txt => Contains name of all images available with their extensions.<br>
          2.1.2 Flickr8k.token.txt => Contains name of the images with 5 captions for each image.

# About the files Uploaded 

- data_split.ipynb => This file is cleaning the training data, testing data and validation data and storing them according to their respective names.
Splitting is in such a way that in the new file column consist of the image name and second column consist of the caption available in such a format given below: 

          image_name <tab separated> <start> caption <end>.
 
- text_n_image_pre.ipynb => This file is reading the training data modified above and preprocessing the text data and image data before feeding the data to computational models.

- img_emd.ipynb => This file is storing the image embeddings viz, Creating a new dictionary train_data and storing image_name as Key and the prediction of the captions as the value and storing the data in a pickel file.
 The prediction are prepared from the RESNET50 Computational model.
 
- img_cap_model.ipynb => This file genrates the prediction of the captions for the given image using LSTM computational model.
This is the file where the testing takes place.
