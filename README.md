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

# Conclusion
   This project presents an approach for False Positive Reduction of Lung Nodule Detection using Deep Learning Techniques. The Lung Nodule Analysis (LUNA 16) dataset have many nodules which are both True and False Nodules. By using the whole dataset for Lung Cancer classification purpose, it becomes more difficult for cardiologists. The false positive reduction in lung nodule analysis is challenging job often as the lung nodules are 3D and are having a wide variation in sizes and shapes. A kind of Artificial Neural Network i.e. Convolutional Neural Network is proposed in this paper to reduce false positives in lung nodule analysis. The proposed approach is an end-to-end approach which indicates there is no manual feature extraction. The samples used in this model are all given from the original CT images only. Data augmentation techniques like Rotations, ZCA whitening, Shifting, Zooming, Flipping and many more is done for replication of the data. The experiment results show that as a single CNN algorithm i.e. VGG 16 by applying 3 layers i.e. Flatten, Dense and Dropout layers using transfer learning gives the good performance which greatly simplifies the detection process of lung nodules. 

![image](https://github.com/dileep99999/LUNA/assets/108917385/fdb65cd5-8a71-4591-8dc1-5135de379acf)

