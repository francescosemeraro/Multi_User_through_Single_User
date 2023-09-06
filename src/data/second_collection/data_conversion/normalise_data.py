from my_libraries.data_instance import Dataset
import numpy as np

#subjects = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11']
subjects = ['s02','s05']
'''
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
'''
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

for i in full_tags:

    if i =='s10_a01_t04_r01':
        continue

    a = Dataset([],[],[],[],[],[])

    try:
        a.load('../pickle_with_prep/'+i+'.pickle')

        d=a.get_data_as_array()
        #print(a.get_data_dim())

        if d.shape[1]<130:
            print("Not enough to make a window out of ", i)
            continue
        else:
            num_of_windows = int(d.shape[1]/overlap) -5 + 1

            #print(i + ' will have ' + str(num_of_windows) + ' windows')

            data = []
            
            labels = []

            prep = []

            J0 = d[0,:,1,:].copy()

            diffs = np.array([d[0,:,3,:]-d[0,:,1,:]],dtype=float)
            
            norms = np.linalg.norm(diffs[0],axis=1)

            indices = [0,2,3,5,6,7,12,13,14,26]

            points = d[0,:,indices,:].copy()
            points = np.transpose(points,[1,0,2])
            #print(points.shape)

            for j in range(d.shape[1]):

                for k in range(points.shape[1]):
                    
                    points[j,k,:]=(points[j,k,:]-J0[j,:])/norms[j]

            for j in range(num_of_windows):
                
                labels.append(int(i[6]))
                #print(len(labels))

                data.append(points[0+j*overlap:window_width+j*overlap,:,:])
                #print(len(data))

                prep.append([J0[0+j*overlap:window_width+j*overlap,:],norms[0+j*overlap:window_width+j*overlap]])
                #print(len(prep))
            
            b = Dataset(data_points=data,labels=labels,prep_data=prep,test_set=[],test_labels=[],test_prep=[])
            #print(b.get_size())
            b.save('../windows/'+i+'_windows.pickle')
    except:
        print(i,' missing')
