import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from numpy.lib.function_base import diff
from my_libraies.data_instance import Dataset

reduced_skeleton = True

file_name = 'src/data/second_collection/pickle_with_prep/s07_a03_t04_r05.pickle'

s = Dataset([],[],[],[],[],[])

s.load(file_name)

skel = s.get_data_as_array()



if reduced_skeleton:
    #Reduced skeleton
    J0 = skel[0,:,1,:].copy()

    diffs = np.array([skel[0,:,3,:]-skel[0,:,1,:]],dtype=float)
    
    norms = np.linalg.norm(diffs[0],axis=1)
    
    cons = [[0,1],[1,2],[2,3],[3,5],[5,6],[6,7],[3,12],[12,13],[13,14],[3,26]]

    lims = [(-1, 1),(-1,1),(-0.75,1.5)]

    #titles = ['- Y','- Z','X']
    
    title = 'Normalised skeleton'

    for i in range(s.get_data_dim()[0]):

        for j in range(s.get_data_dim()[1]):
            
            skel[0,i,j,:]=(skel[0,i,j,:]-J0[i,:])/norms[i]

else: 
    #Full-body
    cons = [[0,1],[0,18],[0,22],[1,2],[2,3],[4,5],[5,6],[6,7],[7,8],[8,9],[7,10],
                [2,11],[2,4],[11,12],[12,13],[13,14],[14,15],[15,16],[14,17],[0,22],[18,19],
                [19,20],[20,21],[0,22],[22,23],[23,24],[24,25],[3,26],[26,30],[26,28],[28,30],
                [30,27],[28,27],[0,22],[30,31],[28,29]]
    
    lims = [(-1.1, 1.3),(1.25, 3.25),(-0.8,1.2)]
    
    
    title = 'Normalised skeleton'

sk_x = skel[0,:,:,0].copy()
sk_y = skel[0,:,:,1].copy()
sk_z = skel[0,:,:,2].copy()

skel[0,:,:,0] = sk_x
skel[0,:,:,1] = sk_z
skel[0,:,:,2] = -sk_y

titles = ['X','Z','- Y']


def update_lines(num, sk, lines):
    
    if num >= sk.shape[1]:
        num = sk.shape[1]
    
    for line, con in zip(lines, cons):
        l = np.empty((sk.shape[3],2))
        l[:,0] = np.transpose(sk[0,num,con[0],:])
        l[:,1] = np.transpose(sk[0,num,con[1],:])
        line.set_data(l[0:2,:])
        line.set_3d_properties(np.transpose(l[2,:]))
    
    s_n = np.squeeze(sk[0,num,1,:])
    
    lines[-1].set_position((s_n[0],s_n[1]))
    lines[-1].set_3d_properties(s_n[2])
    lines[-1].set_horizontalalignment('center')
    lines[-1].set_rotation_mode('anchor')

    return lines


# Attaching 3D axis to the figure
fig = plt.figure()

ax = fig.add_subplot(projection="3d")
    
lines = [ax.plot([], [], [])[0] for _ in range(len(cons))]

bbox = {'fc': '0.8', 'pad': 0}
lines.append(ax.text(0,0,0, s='Spine naval', horizontalalignment='center' ))

# Setting the axes properties
ax.set(xlim3d=lims[0],xlabel=titles[0])

ax.set(ylim3d=lims[1],ylabel=titles[1])

ax.set(zlim3d=lims[2],zlabel=titles[2])

ax.set_title('Normalised skeleton')

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, skel.shape[1], fargs=(skel,lines), interval=50)

plt.show()
