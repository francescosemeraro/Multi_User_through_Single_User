import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from my_libraries.data_instance import Dataset

reduced_skeleton = True

file_name = 's07_a03_t05_r03.pickle'

s = Dataset([],[],[],[],[],[])

s.load(file_name)

skel = s.get_data_as_array()



if reduced_skeleton:
    #Reduced skeleton

    convs = np.squeeze(s.get_data_as_array()[0,:,1,:]) #Spine naval points

    cons = [[0,1],[1,2],[2,3],[3,5],[5,6],[6,7],[7,8],[3,12],[12,13],[13,14],[14,15],[15,16],[14,17],[3,26]]

    lims = [(-0.8, 0.8),(-0.4, 0.4),(-0.6,0.6)]

    titles = ['- Y','- Z','X']

    for i in range(s.get_data_dim()[0]):

        qx = s.dataset[2][0][i][0]    
        qy = s.dataset[2][0][i][1]    
        qz = s.dataset[2][0][i][2]    
        qw = s.dataset[2][0][i][3]

        R = np.array([[1-2*(qy**2)-2*(qz**2), 2*qx*qy-2*qz*qw, 2*qx*qz+2*qy*qw],
        [2*qx*qy+2*qz*qw, 1-2*(qx**2)-2*(qz**2), 2*qy*qz-2*qx*qw],
        [2*qx*qz-2*qy*qw, 2*qy*qz+2*qx*qw, 1-2*(qx**2)-2*(qy**2)]])   


        for j in range(s.get_data_dim()[1]):
            if j==1:
                print("Conversion")
                print(convs[i])
                print(skel[0,i,j,:])
                print(np.matmul(R,np.squeeze(skel[0,i,j,:])))
                print(np.matmul(np.linalg.inv(R),np.squeeze(skel[0,i,j,:])))
            skel[0,i,j,:]=np.matmul(np.linalg.inv(R),np.squeeze(skel[0,i,j,:]))-np.array([-convs[i][1],-convs[i][2],convs[i][0]])
            print()
            
    sk_x = skel[0,:,:,0].copy()
    sk_y = skel[0,:,:,1].copy()
    sk_z = skel[0,:,:,2].copy()
    skel[0,:,:,0] = sk_z
    skel[0,:,:,1] = -sk_y
    skel[0,:,:,2] = sk_x

else: 
    #Full-body
    cons = [[0,1],[0,18],[0,22],[1,2],[2,3],[4,5],[5,6],[6,7],[7,8],[8,9],[7,10],
                [2,11],[2,4],[11,12],[12,13],[13,14],[14,15],[15,16],[14,17],[0,22],[18,19],
                [19,20],[20,21],[0,22],[22,23],[23,24],[24,25],[3,26],[26,30],[26,28],[28,30],
                [30,27],[28,27],[0,22],[30,31],[28,29]]
    
    lims = [(-1.1, 1.3),(1.25, 3.25),(-0.8,1.2)]
    titles = ['X','Z','- Y']

    sk_x = skel[0,:,:,0].copy()
    sk_y = skel[0,:,:,1].copy()
    sk_z = skel[0,:,:,2].copy()
    skel[0,:,:,0] = sk_x
    skel[0,:,:,1] = sk_z
    skel[0,:,:,2] = -sk_y


def update_lines(num, sk, lines):
    
    if num >= sk.shape[1]:
        num = sk.shape[1]
    #print("New data to plot \n")
    
    for line, con in zip(lines, cons):
        l = np.empty((sk.shape[3],2))
        l[:,0] = np.transpose(sk[0,num,con[0],:])
        l[:,1] = np.transpose(sk[0,num,con[1],:])
        #print("New point ", l)
        line.set_data(l[0:2,:])
        line.set_3d_properties(np.transpose(l[2,:]))
    
    s_n = np.squeeze(sk[0,num,1,:])
    
    lines[-1].set_position((s_n[0],s_n[1]))
    lines[-1].set_3d_properties(s_n[2])
    lines[-1].set_horizontalalignment('center')
    lines[-1].set_rotation_mode('anchor')

    #lines[-1].set_3d_properties((0.06),('z'))
    #lines = [ax.plot(dat[0,:], dat[1,:], dat[2,:]) for dat in data]
    return lines


# Attaching 3D axis to the figure
fig = plt.figure()
#plt.style.use("ggplot")
ax = fig.add_subplot(projection="3d")
    
# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot([], [], [])[0] for dat in range(len(cons))]

bbox = {'fc': '0.8', 'pad': 0}
lines.append(ax.text(0.06,0,0, s='Spine naval', horizontalalignment='center' ))

# Setting the axes properties
ax.set(xlim3d=lims[0],xlabel=titles[0])

ax.set(ylim3d=lims[1],ylabel=titles[1])

ax.set(zlim3d=lims[2],zlabel=titles[2])

ax.set_title('Processed skeleton')

#ax.scatter(0.06,0,0, color='blue')

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, skel.shape[1], fargs=(skel,lines), interval=50)

plt.show()
