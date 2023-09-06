from interface_msgs import msg
import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType
from rcl_interfaces.msg import ParameterDescriptor
from std_msgs.msg import Bool
from interface_msgs.msg import TimeWindowOffline
import numpy as np
import sys
sys.path.insert(0, '/home/francesco/phd_ws/src/reasoning_block/reasoning_block')
from data_instance import Dataset
import pickle

#Node designed to produce datasets of sequences of motion frames to train the learning framework
#This node can be called through produce_dataset.launch and can receive two parameters from it as input: file_name and label

class DatasetGenerator(Node):

    def __init__(self):
        super().__init__('dataset_generator')
        
        #Absolute path where to store the dataset
        self.folder_path = '/home/francesco/phd_ws/src/reasoning_block/reasoning_block/'
        
        #Parameter representing the name of the file
        my_parameter_descriptor1 = ParameterDescriptor(description='Absolute path of the .pickle file to store the dataset in')
        self.declare_parameter('file_name','example_dataset.pickle',my_parameter_descriptor1)

        #Parameter representing the label to assign to the current data points being produced
        my_parameter_descriptor2 = ParameterDescriptor(description='Label to give to the data to save')
        self.declare_parameter('label','None',my_parameter_descriptor2)

        #Parameter representing the label to assign to the current data points being produced
        my_parameter_descriptor3 = ParameterDescriptor(description='Boolean to tell whether to save pre-processing data')
        self.declare_parameter('save_prep','False',my_parameter_descriptor3)

        #Parameter representing the label to assign to the current data points being produced
        my_parameter_descriptor4 = ParameterDescriptor(description='Integer representing the number of samples to save before stopping; if 0, you will need to send a ROS2 message to store the data up to that point')
        self.declare_parameter('samples', 'None', my_parameter_descriptor4)

        #List to store the produced dataset instances
        self.dataset = Dataset([],[],[],[],[],[])

        #Label to assign to all the data points currently produced
        self.label = self.get_parameter('label').get_parameter_value().integer_value
        
        #Parameter to use to store pre-processing data
        self.save_prep = self.get_parameter('save_prep').get_parameter_value().bool_value
        
        #Parameter to use to store pre-processing data
        self.samples = self.get_parameter('samples').get_parameter_value().integer_value
        self.get_logger().info('samples set to "%i"' % self.samples)
        self.get_logger().info('label set to "%i"' % self.label)

        self.count = 0
        self.publisher_ = self.create_publisher(Bool, '/save_dataset', 10)

        #Subscription to the node where to get the data points from
        self.subscription1 = self.create_subscription(
            TimeWindowOffline,
            '/to_ml',
            self.listener_callback,
            10)
        self.subscription1 # prevent unused variable warning

        #Subscription to the node from which to receive the command to save the stockpiled data
        self.subscription2 = self.create_subscription(
            Bool,
            '/save_dataset',
            self.save_dataset,
            10)
        self.subscription2 # prevent unused variable warning
        
        
    def listener_callback(self, msg):
        #Construction of the DataInstance object to populate the later Dataset object
        self.count=self.count+1
        #self.get_logger().info('Entered callback "%i"' % self.count)
        motion_data_dim = len(msg.time_window[0].poses)
        timesteps = len(msg.time_window)

        motion_frame = np.zeros((timesteps, motion_data_dim, 3), dtype = float)

        prep_data = np.zeros((timesteps, 8),dtype = float)
        #data_instance = DataInstance()

        #Filling of a motion frame
        for i in range(timesteps):
            for j in range(motion_data_dim):
                skeleton_point = msg.time_window[i].poses[j].position
                motion_frame[i,j,:] = [skeleton_point.x, skeleton_point.y, skeleton_point.z]
            if self.save_prep:
                #print(msg.j0[i])
                #prep_data.append([msg.j0[i],msg.norm[i]])
                #print("Saving pre-processing data")
                prep_data[i,:] = [msg.j0[i].x,msg.j0[i].y,msg.j0[i].z,msg.norm[i],msg.q_spine[i].x,msg.q_spine[i].y,msg.q_spine[i].z,msg.q_spine[i].w]
                #print(prep_data[i,:]) 
        #print(prep_data)
        if self.save_prep:
            print(prep_data)
            self.dataset.append_data(motion_frame,self.label,prep_data)
            #print(self.dataset.dataset[2][-1])
            #print('Entered here')
            self.get_logger().info('Entered callback "%i"' % self.count)
        else:
            self.dataset.append_data(motion_frame,self.label)
        
        if self.samples != 'None':
            if self.count==self.samples:
                msg=Bool()
                msg.data = True
                self.publisher_.publish(msg)
                print('A dataset with "%i" samples was saved' % self.samples )


    def save_dataset(self, msg):
        #Saving of a Dataset object produced (must be called through terminal)
        if msg.data == True:
            self.get_logger().info('Saving dataset')

            file_name = self.get_parameter('file_name').get_parameter_value().string_value
            
            print(len(self.dataset.dataset[2]))
            self.dataset.save(self.folder_path+file_name)
            d=Dataset([],[],[],[],[],[])
            print(len(d.dataset[2]))
            print(d.dataset[2])

            d.load(self.folder_path+file_name)
            print(len(d.dataset[2]))
            print(len(d.dataset[1]))
#            print(d.dataset[2])
            

def main(args=None):
    rclpy.init(args=args)

    dataset_generator = DatasetGenerator()

    rclpy.spin(dataset_generator)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    #dataset_generator.save_dataset()
    dataset_generator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
