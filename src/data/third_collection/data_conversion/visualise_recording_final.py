import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from numpy.lib.function_base import diff
from my_libraries.data_instance import Dataset



def update_lines(num, sk, lines):
    
    if num >= sk.shape[1]:
        num = sk.shape[1]
    
    for line, con in zip(lines, cons):
        l = np.empty((sk.shape[3],2))
        l[:,0] = np.transpose(sk[desired_window,-1,con[0],:])
        l[:,1] = np.transpose(sk[desired_window,-1,con[1],:])
        line.set_data(l[0:2,:])
        line.set_3d_properties(np.transpose(l[2,:]))
    
    s_n = np.squeeze(sk[desired_window,num,1,:])
    
    #lines[-1].set_position((s_n[0],s_n[1]))
    #lines[-1].set_3d_properties(s_n[2])
    #lines[-1].set_horizontalalignment('center')
    #lines[-1].set_rotation_mode('anchor')

    return lines


# Attaching 3D axis to the figure
fig = plt.figure()

ax = fig.add_subplot(projection="3d")

bbox = {'fc': '0.8', 'pad': 0}

labels = ['Working-Working','Working-Requesting','Working-Preparing','Requesting-Working',
            'Requesting-Requesting','Requesting-Preparing','Preparing-Working','Preparing-Requesting',
            'Preparing-Preparing']

reduced_skeleton = False

file_name = 'src/data/third_collection/pickle/visualisation/s1_s2_r2_p1_s1_.pickle'

s = Dataset([],[],[],[],[],[])

s.load(file_name)

skel = s.get_data_as_array()
print(s.get_labels())

desired_window = 63
num_of_frames = int(s.get_data_dim()[1]/2)

if reduced_skeleton:
    J01 = skel[desired_window,:,1,:].copy()
    J02 = skel[desired_window,:,1+num_of_frames,:].copy()

    diffs1 = np.array([skel[desired_window,:,3,:]-skel[desired_window,:,1,:]],dtype=float)
    diffs2 = np.array([skel[desired_window,:,3+num_of_frames,:]-skel[desired_window,:,1+num_of_frames,:]],dtype=float)
    
    norms1 = np.linalg.norm(diffs1[0],axis=1)
    norms2 = np.linalg.norm(diffs2[0],axis=1)
    
    cons = [[0,1],[1,2],[2,3],[3,5],[5,6],[6,7],[3,12],[12,13],[13,14],[3,26]]

    leng = len(cons)

    cons = 2*cons

    conv = np.array(cons)
    conv[leng:,:] = conv[leng:,:]+num_of_frames
    cons = conv.tolist()
    
    lims = [(-1, 1),(-1,1),(-1,1.5)]
    
    for i in range(s.get_data_dim()[0]):

        for j in range(num_of_frames):
            
            skel[desired_window,i,j,:]=(skel[desired_window,i,j,:]-J01[i,:])/norms1[i]
            skel[desired_window,i,j+num_of_frames,:]=(skel[desired_window,i,j+num_of_frames,:]-J02[i,:])/norms2[i]

else: 


    #Full-body
    cons = [[0,1],[0,18],[0,22],[1,2],[2,3],[4,5],[5,6],[6,7],[7,8],[8,9],[7,10],
                [2,11],[2,4],[11,12],[12,13],[13,14],[14,15],[15,16],[14,17],[0,22],[18,19],
                [19,20],[20,21],[0,22],[22,23],[23,24],[24,25],[3,26],[26,30],[26,28],[28,30],
                [30,27],[28,27],[0,22],[30,31],[28,29]]

    leng = len(cons)

    cons = 2*cons

    conv = np.array(cons)
    conv[leng:,:] = conv[leng:,:]+num_of_frames
    cons = conv.tolist()
    
    lims = [(-1,1),(2, 3.5),(-0.8,0.75)]
    
    
    title = 'Normalised skeleton'

sk_x = skel[desired_window,:,:,0].copy()
sk_y = skel[desired_window,:,:,1].copy()
sk_z = skel[desired_window,:,:,2].copy()

#print(sk_y)

skel[desired_window,:,:,0] = sk_x
skel[desired_window,:,:,1] = sk_z
skel[desired_window,:,:,2] = -sk_y

titles = ['X','Z','- Y']

lines = [ax.plot([], [], [])[0] for _ in range(len(cons))]

#if reduced_skeleton:
#    lines.append(ax.text(0,0,0, s='Spine naval 1=2', horizontalalignment='center' ))

# Setting the axes properties
ax.set(xlim3d=lims[0],xlabel=titles[0])

ax.set(ylim3d=lims[1],ylabel=titles[1])

ax.set(zlim3d=lims[2],zlabel=titles[2])

#ax.set_title(labels[s.get_labels()[desired_window]-1])

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, skel.shape[1], fargs=(skel,lines), interval=50)

plt.show()
