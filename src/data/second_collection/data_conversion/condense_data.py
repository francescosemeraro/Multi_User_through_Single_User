from my_libraries.data_instance import Dataset
import numpy as np

subjects = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11']

tags = ['_a01_t01_r01','_a01_t01_r02','_a01_t01_r03','_a01_t01_r04','_a01_t01_r05','_a01_t01_r06',
    '_a01_t02_r01','_a01_t02_r02','_a01_t02_r03','_a01_t02_r04','_a01_t02_r05','_a01_t02_r06',
    '_a01_t03_r01','_a01_t03_r02','_a01_t03_r03','_a01_t03_r04','_a01_t03_r05','_a01_t03_r06',
    '_a01_t04_r01','_a01_t04_r02','_a01_t04_r03','_a01_t04_r04','_a01_t04_r05','_a01_t04_r06',
    '_a01_t05_r01','_a01_t05_r02','_a01_t05_r03','_a01_t05_r04','_a01_t05_r05','_a01_t05_r06',
    '_a02_t01_r01','_a02_t01_r02','_a02_t01_r03','_a02_t01_r04','_a02_t01_r05','_a02_t01_r06',
    '_a02_t02_r01','_a02_t02_r02','_a02_t02_r03','_a02_t02_r04','_a02_t02_r05','_a02_t02_r06',
    '_a02_t03_r01','_a02_t03_r02','_a02_t03_r03','_a02_t03_r04','_a02_t03_r05','_a02_t03_r06',
    '_a02_t04_r01','_a02_t04_r02','_a02_t04_r03','_a02_t04_r04','_a02_t04_r05','_a02_t04_r06',
    '_a02_t05_r01','_a02_t05_r02','_a02_t05_r03','_a02_t05_r04','_a02_t05_r05','_a02_t05_r06',
    '_a03_t01_r01','_a03_t01_r02','_a03_t01_r03','_a03_t01_r04','_a03_t01_r05','_a03_t01_r06',
    '_a03_t02_r01','_a03_t02_r02','_a03_t02_r03','_a03_t02_r04','_a03_t02_r05','_a03_t02_r06',
    '_a03_t03_r01','_a03_t03_r02','_a03_t03_r03','_a03_t03_r04','_a03_t03_r05','_a03_t03_r06',
    '_a03_t04_r01','_a03_t04_r02','_a03_t04_r03','_a03_t04_r04','_a03_t04_r05','_a03_t04_r06',
    '_a03_t05_r01','_a03_t05_r02','_a03_t05_r03','_a03_t05_r04','_a03_t05_r05','_a03_t05_r06']


mins = []

overlap = 26

window_width = 130

full_tags = []

for i in subjects:

    for j in tags:

        full_tags.append(i+j)

b = Dataset([],[],[],[],[],[])

for i in full_tags:

    if i =='s10_a01_t04_r01':
        continue

    a = Dataset([],[],[],[],[],[])

    try:
        a.load('windows/' + i + '_windows.pickle') 

        data = a.get_data()
        labels = a.get_labels()
        prep = a.get_prep()

        for j in range(a.get_size()):

            b.append_data(data[j],labels[j],prep[j])
    except:
        continue

b.save('Condensed_dataset.pickle')
