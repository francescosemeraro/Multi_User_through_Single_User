# Towards Multi-User Activity Recognition through Facilitated Training Data and Deep Learning for Human-Robot Collaboration Applications 
### Francesco Semeraro*, Jon Carberry and Angelo Cangelosi <br />
##### <sup>*</sup> Corresponding author

Read full paper <a href="https://ieeexplore.ieee.org/document/10191782">here</a>, Presented at [IJCNN 2023](https://2023.ijcnn.org/)

In this paper, we propose a new way of generating training data regarding multi-user activity starting from data related to single-user activity. We combine them in post-processing to generate a datapoint relatable to an actual multi-user activity scenario. We assessed the validity of such approach, we trained a LSTM and a variational autoencoder composed of STGCNNs with such artificially generated training data to recognise the joint activity of users who were actually present in the same scenario at the same time. All this was performed through a distributed learning strategy by means of Tensorflow 2 GPU and Keras libraries. The results showed that it is possible to achieve the same performance you would get by using real data as training set.

This repository contains the code you can use to replicate such results.

### How to cite our paper
If any of the content of this repository was helpful to you, please cite our paper using:
```
@INPROCEEDINGS{10191782,
  author={Semeraro, Francesco and Carberry, Jon and Cangelosi, Angelo},
  booktitle={2023 International Joint Conference on Neural Networks (IJCNN)}, 
  title={Towards Multi-User Activity Recognition through Facilitated Training Data and Deep Learning for Human-Robot Collaboration Applications}, 
  year={2023},
  volume={},
  number={},
  pages={01-09},
  doi={10.1109/IJCNN54540.2023.10191782}}
```

### Requirements
To be able to run all the scripts, you will need to install the following:
<br />
1- Python 3.10 <br />
2- Tensorflow 2.8.0 <br />
3- tensorflow_probability  <br />
4- ROS 2 Foxy Fitzeroy  <br />
5- np_utils  <br />
6- wandb <br />
7- sqlite3. <br />
<br />

### The data
Please find the .csv files related to this project at the following links:

First part: <a href="https://figshare.com/articles/dataset/Multi-user_activity_recognition_database_with_single_user_training_data/22593298">here</a> 
Second part: <a href="https://figshare.com/articles/dataset/Multi-user_activity_recognition_database_Second_part_/24421438">here</a>  



### The repository
The main elements of the repository are the following:
<br />
1- "acquisition_block", ROS 2 Foxy package to store data through an Azure Kinect camera in compressed bag files <br />
2- "data", which contains all the pre-processing scripts of the data acquired in the experiments  <br />
3- "Azure_Kinect_ROS_Driver", official ROS 2 Foxy Microsoft package to communicate with the Azure Kinect  <br />
4- "networks", which contains the code used for the instantiation and trainings of the deep learning models under a distributed training strategy  <br />
5- "libraries", folder used to install some custom libraries used in the "data" and "networks" folders.  <br />
<br />

