import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from flask import Flask, request
from keras.models import load_model
from keras import backend as K
from keras.preprocessing.image import img_to_array
import pickle
import pandas as pd
import numpy as np
import cv2
import tensorflow as tf
graph = tf.get_default_graph()

""" Loading the saved-model """
new_model = load_model('grape_leaf_24.h5')

app = Flask(__name__)

port = int(os.environ.get('PORT', 3000))

@app.route('/disease',methods = ['POST', 'GET'])
def disease_classifier():
	if request.method=='POST':
		
		# Reading the saved class labels
		pickle_in = open("label.pkl","rb")
		lb = pickle.load(pickle_in)

		

		if request.files['file'].filename == '':
			return 'No selected file'
		else:

			# Reading test-file object from request
			filestr = request.files['file'].read()

			#converting file-object to image format
			npimg = np.fromstring(filestr,np.uint8)
			img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)

			sample_list = []
			sample = convert_image_to_array(img)

			sample_list.append(sample)
			np_sample_list = np.array(sample_list,dtype=np.float16)/255.0

			global graph
			with graph.as_default():
				sample_result = new_model.predict(np_sample_list)

			res_index = np.argmax(sample_result)

			return lb.classes_[res_index]



	else:
		return "Grape-leaf disease identifier"

def convert_image_to_array(image):
    #im = cv2.imread(image)
    im = cv2.resize(image,(256,256))
    return img_to_array(im)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)