import numpy as np
import csv
from my_libraries.data_instance import Dataset
from matplotlib import pyplot as plt

subjects = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11']

'''tags = ['_a01_t01_r01','_a01_t01_r02','_a01_t01_r03','_a01_t01_r04','_a01_t01_r05','_a01_t01_r06',
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

num_of_frames = 32

full_tags = []

for i in subjects:

    for j in tags:

        full_tags.append(i+j)

for i in full_tags:

    if i =='s10_a01_t04_r01':
        continue
    
    #print('csv/'+ i + '.csv')

    l_samples = 0

    with open('../csv/'+ i + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l_samples = sum(1 for row in csv_reader)

    with open('../csv/'+ i + '.csv') as csv_file:

        try:
            with open('../prep/'+ i + '_prep.csv') as prep_file:    
                csv_reader = csv.reader(csv_file, delimiter=',')
                prep_reader = csv.reader(prep_file, delimiter=',')
                num_of_skels = int(l_samples/num_of_frames)
                a=np.full((num_of_skels,num_of_frames,3),None)
                p=np.full((num_of_skels,4),None)
                #a_m = np.full([num_of_frames,3],None)

                
                #if num_of_skels<130:
                #    print(i, ' has only ', num_of_skels, ' samples, so it will not be converted')
                #    continue

                d = 0
                j = 0
                
                #for row, prep_row in zip(csv_reader, prep_reader):
                for prep_row in prep_reader:
                    for row in csv_reader:
                        #print(row)
                        #print([float(row[0]),float(row[1]),float(row[2])])
                        a[d,j,:] = [float(row[0]),float(row[1]),float(row[2])]
                        if j < num_of_frames - 1:
                            j = j + 1                
                        else:
                            p[d,:] = [float(prep_row[0]),float(prep_row[1]),float(prep_row[2]),float(prep_row[3])]
                            j = 0
                            d = d + 1

                b=Dataset([],[],[],[],[],[])
                
                c = int(i[6])

                
                b.append_data([[a], [c], [p]])
                b.save('../pickle_with_prep/' + i + '.pickle')
                print(i+" successfully converted")
        except:
            print(i, " missing")

#print(np.min(np.asarray(mins)))
'''
h=np.histogram(mins, bins=np.arange(450))
print(h)

plt.hist(mins,bins='auto')
plt.xlabel('Number of samples')
plt.ylabel('Occurrency')
plt.show()



plt.plot(np.histogram(mins)[1][1:],np.cumsum(np.histogram(mins)[0]))
plt.xlabel('Number of samples')
plt.ylabel('Cumulative sum of occurrencies')
plt.show()
'''
