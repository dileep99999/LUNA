# LUNA
False Positive Reduction of Lung Nodule Detection using Deep Learning Techniques
# DATASET 
The LIDC/IDRI data set is publicly available including the annotations of nodules by four radiologists.It contain 888 CT scans. The LIDC/IDRI database contains annotations which were collected during a two-phase annotation process using 4 experienced radiologists. Each radiologist marked lesions they identified as non-nodule, nodule < 3 mm, and nodules >= 3 mm.
The data is structured as follows:
subset0.zip to subset9.zip: 10 zip files which contain all CT scans 
annotations.csv: csv file that contains the annotations used as reference standard for the 'nodule detection' track
sampleSubmission.csv: an example of a submission file in the correct format
candidates.csv: the original set of candidates used for the LUNA16 workshop. This file is kept for completeness.
candidates_V2.csv: csv file that contains an extended set of candidate locations for the ‘false positive reduction’ track. 
evaluation script: the evaluation script that is used in the LUNA16 framework
lung segmentation: a directory that contains the lung segmentation for CT images computed using automatic algorithms
additional_annotations.csv: csv file that contain additional nodule annotations from our observer study. The file will be available soon
# Data Augmentation
Augment the nodule image data by using different techniques like
                     	1. Rotations
                    	2. ZCA Whitening
			3. Shifting (Width, Height, Depth)
			4. Zooming (zoom in & zoom out) 
			5. Flipping (Horizontal, vertifcal and depth)
Feature Standardization - standardize pixel values across the entire dataset.
Random Rotations - sample data may have varying and different rotations in the scene.
Random Shifts - images may not be centered in the frame. They may be off-center in a variety of different ways.
Random Flips - improve performance on large and complex problems is to create random flips of images in your training data.
![image](https://github.com/dileep99999/LUNA/assets/108917385/5d81499d-c3e0-4fca-b7ef-745dd61f529a)

