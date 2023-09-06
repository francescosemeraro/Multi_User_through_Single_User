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

for j in tags:

    if j =='s1_s3_r1_p2_s2_' or j =='s1_s3_r2_p2_s1_' or j=='s1_s2_r2_p1_s2_': #I missed one labelling in the last one
        continue

    a = Dataset([],[],[],[],[],[])

    a.load('src/data/third_collection/pickle/datapoints/processed/' + j + '.pickle')

    a.rename_classes()

    labels=a.get_labels()
    print(len(labels))
    to_remove = []
    print(a.dataset[2][0])
    old_label = None
    for i in range(len(labels)):
        if labels[i] != old_label and old_label is not None:
            to_remove.append(i-2)
            to_remove.append(i-1)
            to_remove.append(i)
            to_remove.append(i+1)
        old_label = labels[i]
    print(to_remove)
    a.pop('train',to_remove)
    
    a.save('src/data/third_collection/pickle/datapoints/confidence/' + j + '.pickle')
