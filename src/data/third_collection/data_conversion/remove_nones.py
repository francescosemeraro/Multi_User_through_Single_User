import numpy as np
import csv
from my_libraries.data_instance import Dataset
from matplotlib import pyplot as plt
from os import listdir

full_tags = listdir()

for i in full_tags:
    print(i)
    
    if i =='s10_a01_t04_r01.pickle' or i =='remove_nones.py':
        continue

    nones_to_replace = 0

    a = Dataset([],[],[],[],[],[])
    a.load(i)
    dat = a.get_data_as_array()
    total_nones = 0
    for j in range(dat.shape[1]):        
        if dat[0,j,0,0]==None:
            nones_to_replace = nones_to_replace + 1
        elif nones_to_replace > 0: #replace None with the next skeleton available
            dat[0,j-nones_to_replace:j,:,:] = np.tile(dat[0,j,:,:],nones_to_replace)
            total_nones = total_nones + nones_to_replace
            nones_to_replace = 0

    print(i+' had '+str(total_nones)+' Nones')
    a.save('../pickle_no_nones/'+i)
