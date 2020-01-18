from keras.preprocessing import image as im
import cv2
import numpy as np
import PIL
from PIL import Image
from pyimagesearch.cancernet import CancerNet
from keras.optimizers import Adagrad
import image_slicer
import boto3
from botocore.client import Config
import datetime
import urllib.request

# Use the array data from the first image in this dataset:
NUM_EPOCHS = 40
INIT_LR = 1e-2
opt = Adagrad(lr=INIT_LR, decay=INIT_LR / NUM_EPOCHS)
dim = (48,48)

# load model
model = CancerNet.build(width=48, height=48, depth=3, classes=2)
model.load_weights('/home/ubuntu/cloud/upload/model/weights00000040.h5')

# image slicer
red = Image.new('RGBA', (50,50), color='red')
red.putalpha(1)

def process_image(url, patientName):
    
    temp_img_dir = '/home/ubuntu/temp/'
    name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print("downloading image...")
    urllib.request.urlretrieve(url,temp_img_dir+name+'.jpg')
    print("finished Download")
    size  = cv2.imread(temp_img_dir+name+'.jpg')
    size = int((size.shape[0]/50)*(size.shape[0]/50))

    tiles = image_slicer.slice(temp_img_dir+name+'.jpg', size, save=False)
    tile_index = 0

    for tile in tiles:

        tile = np.array(tile.image)
        #tile = tile[:,:,:-1]   #for png we need this if not we don't reducing alpha
        tile = cv2.resize(tile,dim)
        tile  = im.img_to_array(tile)
        tile  = tile/255
        tile = np.expand_dims(tile, axis=0)
        if(model.predict_classes(tile)[0] == 1):
            alpha = tiles[tile_index].image.copy()
            tiles[tile_index].image = alpha.putalpha(1)
            tiles[tile_index].image = Image.alpha_composite(red,alpha)
        tile_index += 1

    tiles = image_slicer.join(tiles)
    tiles.save(temp_img_dir+name+'_finished.jpg')

    #upload the image here 'tiles' is the processed image'
    outputName = "/patient/" + patientName + "/result/result.jpg"
    s3 = boto3.resource(
        's3',
        aws_access_key_id='AKIASKKR5242U53BQZ5C',
        aws_secret_access_key='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',
        config=Config(signature_version='s3v4')
    )
    print("uploading image...")
    s3.Bucket('4160-project').upload_file(temp_img_dir+name+'_finished.jpg', Key=outputName)
    print("finished uploading...")
    result_path = 'https://4160-project.s3.us-east-2.amazonaws.com/'+ outputName
    return(result_path) # return the url
