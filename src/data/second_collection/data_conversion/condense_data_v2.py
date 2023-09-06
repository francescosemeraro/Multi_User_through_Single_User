from heapq import merge
from my_libraries.data_instance import Dataset
import numpy as np

subjects = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11']

#tags = ['_a01_t01_r01','_a01_t01_r02','_a01_t01_r03','_a01_t01_r04','_a01_t01_r05','_a01_t01_r06',
    #'_a01_t02_r01','_a01_t02_r02','_a01_t02_r03','_a01_t02_r04','_a01_t02_r05','_a01_t02_r06',
    #'_a01_t03_r01','_a01_t03_r02','_a01_t03_r03','_a01_t03_r04','_a01_t03_r05','_a01_t03_r06',
    #'_a01_t04_r01','_a01_t04_r02','_a01_t04_r03','_a01_t04_r04','_a01_t04_r05','_a01_t04_r06',
    #'_a01_t05_r01','_a01_t05_r02','_a01_t05_r03','_a01_t05_r04','_a01_t05_r05','_a01_t05_r06',
#    '_a02_t01_r01','_a02_t01_r02','_a02_t01_r03','_a02_t01_r04','_a02_t01_r05','_a02_t01_r06',
    #'_a02_t02_r01','_a02_t02_r02','_a02_t02_r03','_a02_t02_r04','_a02_t02_r05','_a02_t02_r06',
    #'_a02_t03_r01','_a02_t03_r02','_a02_t03_r03','_a02_t03_r04','_a02_t03_r05','_a02_t03_r06',
    #'_a02_t04_r01','_a02_t04_r02','_a02_t04_r03','_a02_t04_r04','_a02_t04_r05','_a02_t04_r06',
    #'_a02_t05_r01','_a02_t05_r02','_a02_t05_r03','_a02_t05_r04','_a02_t05_r05','_a02_t05_r06',
#    '_a03_t01_r01','_a03_t01_r02','_a03_t01_r03','_a03_t01_r04','_a03_t01_r05','_a03_t01_r06']
    #'_a03_t02_r01','_a03_t02_r02','_a03_t02_r03','_a03_t02_r04','_a03_t02_r05','_a03_t02_r06',
    #'_a03_t03_r01','_a03_t03_r02','_a03_t03_r03','_a03_t03_r04','_a03_t03_r05','_a03_t03_r06',
    #'_a03_t04_r01','_a03_t04_r02','_a03_t04_r03','_a03_t04_r04','_a03_t04_r05','_a03_t04_r06',
    #'_a03_t05_r01','_a03_t05_r02','_a03_t05_r03','_a03_t05_r04','_a03_t05_r05','_a03_t05_r06']

tags = ['_a01_t01_r01','_a01_t01_r06',
    '_a01_t02_r01','_a01_t02_r06',
    '_a01_t03_r01','_a01_t03_r06',
    '_a01_t04_r01','_a01_t04_r06',
    '_a01_t05_r01','_a01_t05_r06',
    '_a02_t01_r01','_a02_t01_r06',
    '_a02_t02_r01','_a02_t02_r06',
    '_a02_t03_r01','_a02_t03_r06',
    '_a02_t04_r01','_a02_t04_r06',
    '_a02_t05_r01','_a02_t05_r06',
    '_a03_t01_r01','_a03_t01_r06',
    '_a03_t02_r01','_a03_t02_r06',
    '_a03_t03_r01','_a03_t03_r06',
    '_a03_t04_r01','_a03_t04_r06',
    '_a03_t05_r01','_a03_t05_r06']


mins = []

overlap = 26

window_width = 130

full_tags = []

for i in subjects:

    for j in tags:

        full_tags.append(i+j)

print(len(full_tags))

total_dataset = Dataset([],[],[],[],[],[])

tags_per_iter = 18

#iterator = 3

for iterator in range(11):

    for i in range(iterator*tags_per_iter,(iterator+1)*tags_per_iter):

        if full_tags[i] =='s10_a01_t04_r01':
            continue

        if iterator != 0:
            
            for j in full_tags[0:iterator*tags_per_iter]:
                
                try:
                    #print('Combining ', full_tags[i],' and ',j)
                    a = Dataset([],[],[],[],[],[])
                    a.load('../windows/' + full_tags[i] + '_windows.pickle') 

                    if j =='s10_a01_t04_r01':
                        continue
                    
                    b = Dataset([],[],[],[],[],[])
                    b.load('../windows/' + j + '_windows.pickle') 
                    
                    #merged_dataset = Dataset([],[],[],[],[],[])
                    merged_dataset = a.merge(b,full_tags[i],j)
                    
                    total_dataset.unite(merged_dataset)
                    #print(total_dataset.get_size())

                #print(total_dataset.dataset[2][-1])
                except:
                    print(i,' missing')

        if iterator != 10:
            
            for j in full_tags[(iterator+1)*tags_per_iter:]:
                
                try:
                    print('Combining ', full_tags[i],' and ',j)
                    a = Dataset([],[],[],[],[],[])
                    a.load('../windows/' + full_tags[i] + '_windows.pickle') 

                    if j =='s10_a01_t04_r01':
                        continue

                    b = Dataset([],[],[],[],[],[])
                    b.load('../windows/' + j + '_windows.pickle') 
                    
                    #merged_dataset = Dataset([],[],[],[],[],[])
                    merged_dataset = a.merge(b,full_tags[i],j)

                    total_dataset.unite(merged_dataset)
                    #print(total_dataset.get_size())
                except:
                    print(i,' missing')

total_dataset.save('Total_dataset.pickle')
