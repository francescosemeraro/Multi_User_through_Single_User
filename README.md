# Towards Multi-User Activity Recognition through Facilitated Training Data and Deep Learning for Human-Robot Collaboration Applications 
### Francesco Semeraro*, Jon Carberry and Angelo Cangelosi <br />
##### <sup>*</sup> Corresponding author

Read full paper <a href="https://ieeexplore.ieee.org/document/10191782">here</a>, Presented at [IJCNN 2023](https://2023.ijcnn.org/)

In this paper, we propose a new way of generating training data regarding multi-user activity starting from data related to single-user activity. We combine them in post-processing to generate a datapoint relatable to an actual multi-user activity scenario. We assessed the validity of such approach, we trained a LSTM and a variational autoencoder composed of STGCNNs with such artificially generated training data to recognise the joint activity of users who were actually present in the same scenario at the same time. All this was performed through a distributed learning strategy by means of Tensorflow 2 GPU and Keras libraries. The results showed that it is possible to achieve the same performance you would get by using real data as training set.

This repository contains the code you can use to replicate such results.

### How to cite our paper
You can cite our paper using: 
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
