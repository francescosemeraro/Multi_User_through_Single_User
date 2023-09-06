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

    if j =='s1_s3_r1_p2_s2_' or j =='s1_s3_r2_p2_s1_' or j=='s1_s2_r2_p1_s2_':
        continue

    a = Dataset([],[],[],[],[],[])

    a.load('src/data/third_collection/pickle/datapoints/' + j + '.pickle')

    skel=a.get_data_as_array()
    #print(a.get_data_dim())

    num_of_frames = int(a.get_data_dim()[1]/2)



    for z in range(a.get_size()):

        J01 = skel[z,:,1,:].copy()
        J02 = skel[z,:,1+num_of_frames,:].copy()

        diffs1 = np.array([skel[z,:,3,:]-skel[z,:,1,:]],dtype=float)
        diffs2 = np.array([skel[z,:,3+num_of_frames,:]-skel[z,:,1+num_of_frames,:]],dtype=float)
        
        norms1 = np.linalg.norm(diffs1[0],axis=1)
        norms2 = np.linalg.norm(diffs2[0],axis=1)

        for i in range(a.get_data_dim()[0]):

            for y in range(num_of_frames):
                
                skel[z,i,y,:]=(skel[z,i,y,:]-J01[i,:])/norms1[i]
                skel[z,i,y+num_of_frames,:]=(skel[z,i,y+num_of_frames,:]-J02[i,:])/norms2[i]
    #for i in range(s.get_data_dim()[0]):

#        for j in range(num_of_frames):
            
    #skel[:,:,:num_of_frames,:]=(skel[:,:,:num_of_frames,:]-J01)/norms1
    #skel[:,:,num_of_frames:,:]=(skel[:,:,num_of_frames:,:]-J02)/norms2

    skel = np.delete(skel,[1,1+num_of_frames],2)
    data = []
    for i in range(skel.shape[0]):
        data.append(skel[i,:,:,:])
    prep_data = [j,j]
    b = Dataset(data_points=data,labels=a.get_labels(),prep_data=[[j,j]]*a.get_size(),test_set=[],test_labels=[],test_prep=[])
    #print(b.get_size())
    b.save('src/data/third_collection/pickle/datapoints/processed/' + j + '.pickle')
