from fcntl import F_SEAL_SEAL
import numpy as np
import csv
from my_libraries.data_instance import Dataset
from matplotlib import pyplot as plt


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


mins = []

num_of_frames = 32

frames_per_subject = 0

purpose = None

for_vis = False


if for_vis:
    frames_of_interest = [i for i in range(num_of_frames)]
    frames_per_subject = num_of_frames
    purpose = 'visualisation'
else:
    frames_of_interest = [0,1,2,3,5,6,7,12,13,14,26]
    frames_per_subject = 11 
    purpose = 'datapoints'


frames_in_window = 130

overlapping = 26

full_tags = []

for j in tags:

    if j =='s1_s3_r1_p2_s2_' or j =='s1_s3_r2_p2_s1_' or j=='s1_s2_r2_p1_s2_':
        continue
    
    #d = Dataset([],[],[],[],[],[])


    with open('src/data/third_collection/csv/'+ j + 'datastream.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l_samples = sum(1 for row in csv_reader)

    with open('src/data/third_collection/csv/'+ j + 'datastream.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        num_of_skels = int(l_samples/num_of_frames)
        pair=np.full((frames_per_subject*2,3),None)
        window=np.full((frames_in_window,frames_per_subject*2,3),None)

        label = None
        first_tag = None
        second_tag = None
    
        rows = np.array([row for idx, row in enumerate(csv_reader)])
        counter_shift = 0
        window_filler = 0
        first_saved = False
        final_entries = [[],[],[]]
        
        for i in range(num_of_skels):

            indexing = list(np.array(frames_of_interest)+num_of_frames*i)

            if first_tag == None and second_tag == None:
                if float(rows[indexing[0],0]) > 0:
                    pair[frames_per_subject:,:] = np.array(rows[indexing,:3]).astype(np.float)
                    second_tag = rows[i*num_of_frames,-2]
                else:
                    pair[:frames_per_subject,:] = np.array(rows[indexing,:3]).astype(np.float)
                    first_tag = rows[i*num_of_frames,-2]
            elif first_tag == None and second_tag is not None and float(rows[indexing[0],0]) < 0:
                pair[:frames_per_subject,:] = np.array(rows[indexing,:3]).astype(np.float)
                first_tag = rows[i*num_of_frames,-2]
            elif first_tag is not None and second_tag == None and float(rows[indexing[0],0]) > 0:
                pair[frames_per_subject:,:] = np.array(rows[indexing,:3]).astype(np.float)
                second_tag = rows[i*num_of_frames,-2]
            elif rows[i*num_of_frames,-2] == first_tag:
                pair[:frames_per_subject,:] = np.array(rows[indexing,:3]).astype(np.float)
            elif rows[i*num_of_frames,-2] == second_tag:
                pair[frames_per_subject:,:] = np.array(rows[indexing,:3]).astype(np.float)
            else:
                print("Warning! Third tag!")
            #if first_tag == None:
            #    pair[:frames_per_subject,:] = np.array(rows[indexing,:3]).astype(np.float)
            #    first_tag = rows[i*num_of_frames,-2]
            #elif rows[i*num_of_frames,-2] == first_tag:
            #    pair[:frames_per_subject,:] = np.array(rows[indexing,:3]).astype(np.float)
            #elif second_tag == None:
            #    pair[frames_per_subject:,:] = np.array(rows[indexing,:3]).astype(np.float)
            #    second_tag = rows[i*num_of_frames,-2]
            #elif rows[i*num_of_frames,-2] == second_tag:
            #    pair[frames_per_subject:,:] = np.array(rows[indexing,:3]).astype(np.float)
            #else:
            #    print("Warning! Tag unknown!")
            
            if first_tag and second_tag:
                if window_filler < frames_in_window:
                    window[window_filler,:,:] = pair
                    window_filler = window_filler + 1
                else:
                    if not first_saved:
                        label = int(rows[i*num_of_frames,-1])
                        final_entries[0].append(window.copy())
                        final_entries[1].append(label)
                        final_entries[2].append(j)
                        first_saved = True

                    window[:-1] = window[1:]
                    window[-1] = pair
                    counter_shift = counter_shift + 1

                    if counter_shift >= overlapping:
                        label = int(rows[i*num_of_frames,-1])
                        final_entries[0].append(window.copy())
                        final_entries[1].append(label)
                        final_entries[2].append(j)
                        counter_shift = 0

    d = Dataset([],[],[],[],[],[])
    d.append_data(final_entries)
    d.save('src/data/third_collection/pickle/' + purpose + '/' + j + '.pickle')
    d.clear_dataset()
