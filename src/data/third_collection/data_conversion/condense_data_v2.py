from heapq import merge
from my_libraries.data_instance import Dataset
import numpy as np

tags = ['s1_s2_r1_p1_s1_',
        #'s1_s2_r1_p1_s2_',
        's1_s2_r1_p2_s1_',
        #'s1_s2_r1_p2_s2_',
        's1_s2_r2_p1_s1_',
        #'s1_s2_r2_p1_s2_',
        's1_s2_r2_p2_s1_',
        #'s1_s2_r2_p2_s2_',
        's1_s3_r1_p1_s1_',
        #'s1_s3_r1_p1_s2_',
        's1_s3_r1_p2_s1_',
        #'s1_s3_r1_p2_s2_',
        's1_s3_r2_p1_s1_',
        #'s1_s3_r2_p1_s2_',
        's1_s3_r2_p2_s1_',
        #'s1_s3_r2_p2_s2_',
        's3_s2_r1_p1_s1_',
        #'s3_s2_r1_p1_s2_',
        's3_s2_r1_p2_s1_',
        #'s3_s2_r1_p2_s2_',
        's3_s2_r2_p1_s1_',
        #'s3_s2_r2_p1_s2_',
        's3_s2_r2_p2_s1_',
        #'s3_s2_r2_p2_s2_'
        ]


total_dataset = Dataset([],[],[],[],[],[])

for i in tags:

    if i =='s1_s3_r1_p2_s2_' or i =='s1_s3_r2_p2_s1_' or i=='s1_s2_r2_p1_s2_':
        continue

    print('Combining ', i)
    a = Dataset([],[],[],[],[],[])
    a.load('src/data/third_collection/pickle/datapoints/confidence/' + i + '.pickle') 
    
    total_dataset.unite(a)
                #print(total_dataset.dataset[2][-1])

total_dataset.save('src/data/third_collection/LOSO2.pickle')
