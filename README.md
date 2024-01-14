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
![image](https://github.com/dileep99999/LUNA/assets/108917385/dccfb6e3-4828-4aec-af85-1f9d9e94e506)
