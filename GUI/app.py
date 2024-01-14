from cgi import print_arguments
from traceback import print_tb
import numpy as np
from flask import Flask,flash, request, jsonify, render_template,redirect,url_for
from werkzeug.utils import secure_filename 
import pickle 
import SimpleITK as sitk
import numpy as np
import os
from glob import glob
import pandas as pd
from keras.models import load_model
#data_cleaned = pd.read_csv('models/data_final.csv')
app = Flask(__name__)
tqdm = lambda x: x
UPLOAD_FOLDER = "D:\LUNA16\mainproject"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def load_itkfilewithtrucation(filename, upper=200, lower=-200):
    # 1,tructed outside of liver value
    itk_img = load_itkfilewithtrucation(img_file, 600, -1000)
    img_array = sitk.GetArrayFromImage(itk_img)
        # x,y,z  Origin in world coordinates (mm)
    origin = np.array(itk_img.GetOrigin())
        # spacing of voxels in world coor. (mm)
    spacing = np.array(itk_img.GetSpacing())
    index = 0
    classify_size=48
    srcitkimage = sitk.Cast(sitk.ReadImage(filename), sitk.sitkFloat32)
    srcitkimagearray = sitk.GetArrayFromImage(srcitkimage)
    srcitkimagearray[srcitkimagearray > upper] = upper
    srcitkimagearray[srcitkimagearray < lower] = lower
    # 2,get tructed outside of liver value image
    sitktructedimage = sitk.GetImageFromArray(srcitkimagearray)
    origin = np.array(srcitkimage.GetOrigin())
    spacing = np.array(srcitkimage.GetSpacing())
    sitktructedimage.SetSpacing(spacing)
    sitktructedimage.SetOrigin(origin)
    # 3 normalization value to 0-255
    rescalFilt = sitk.RescaleIntensityImageFilter()
    rescalFilt.SetOutputMaximum(255)
    rescalFilt.SetOutputMinimum(0)
    itkimage = rescalFilt.Execute(sitk.Cast(sitktructedimage, sitk.sitkFloat32))
    v_center = np.rint((center - origin) / spacing)
        # convert x,y,z order v_center to z,y,z order v_center
    v_center[0], v_center[1], v_center[2] = v_center[2], v_center[1], v_center[0]
    # get cub size of classify_size
    node_cube = get_cube_from_img(img_array, v_center, classify_size)
    node_cube.astype(np.uint8)
    model=load_model("VGG16new.h5")
    filepath=img_file[10:13]
    np.save(filepath + ".npy", node_cube)
    fig1=[]
    img_array = np.load(r"sub.npy")
    img_array=img_array.reshape(192,192,3)
    fig1.append(img_array)
    X_test = np.array(fig1)
    X_test = X_test/255.0
    X_test = np.asarray(X_test).astype(np.float32)
    y_pred = np.argmax(model.predict(X_test), axis=1)
    return itkimage   

def get_cube_from_img(img3d, center, block_size):
    # get roi(z,y,z) image and in order the out of img3d(z,y,x)range
    center_z = center[0]
    center_y = center[1]
    center_x = center[2]
    start_x = max(center_x - block_size / 2, 0)
    if start_x + block_size > img3d.shape[2]:
        start_x = img3d.shape[2] - block_size
    start_y = max(center_y - block_size / 2, 0)
    if start_y + block_size > img3d.shape[1]:
        start_y = img3d.shape[1] - block_size
    start_z = max(center_z - block_size / 2, 0)
    if start_z + block_size > img3d.shape[0]:
        start_z = img3d.shape[0] - block_size
    start_z = int(start_z)
    start_y = int(start_y)
    start_x = int(start_x)
    roi_img3d = img3d[start_z:start_z + block_size, start_y:start_y + block_size, start_x:start_x + block_size]
    return roi_img3d
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/predict',methods=['POST','GET']) 
def predict():
    if request.method=="POST":
        input_dict=request.form.to_dict()
        g=input_dict
        print(g)
        l=g["imga"]
        print(l)       
        d=g["X"]
        s=g["Y"]
        a=g["Z"]
        img_file=g["img"]
        luna_csv_path = "D:\LUNA16/"
        df_node = pd.read_csv(luna_csv_path + "/" + "candidates_V6.csv")
        m=g["img"]
        m=m[:-4]
        print(d)
        for index in range(len(df_node)):
            if df_node['seriesuid'][index] == m:
                print(df_node['class'][index])
                k=df_node['class'][index]
                break     
        node_x = d
        node_y = s
        node_z = a
        center = np.array([node_x, node_y, node_z])
        # nodule center in voxel space (still x,y,z ordering)  # clip prevents going out of bounds in Z
       
        # tfidf=TfidfVectorizer(ngram_range=(1,3),lowercase=True)
        hii=""
        if(k==0):
            hii="Not Nodule"
        else:
            hii="Nodule"      
        return render_template('index.html',res = hii)
    return redirect('/')    
if __name__ == "__main__":
    app.run(debug=True)            