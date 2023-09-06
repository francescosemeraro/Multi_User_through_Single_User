from interface_msgs import msg
import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType
from rcl_interfaces.msg import ParameterDescriptor
from std_msgs.msg import Bool
from interface_msgs.msg import TimeWindowForTwo
import numpy as np
import sys
sys.path.insert(0, '/home/francesco/phd_ws/src/reasoning_block/reasoning_block')
from data_instance import Dataset
import pickle

#Node designed to produce datasets of sequences of motion frames to train the learning framework
#This node can be called through produce_dataset.launch and can receive two parameters from it as input: file_name and label

class DatasetGenerator(Node):

    def __init__(self):
        super().__init__('dataset_generator_for_two')
        
        #Absolute path where to store the dataset
        self.folder_path = '/home/francesco/phd_ws/src/reasoning_block/reasoning_block/'
        
        #Parameter representing the name of the file
        my_parameter_descriptor1 = ParameterDescriptor(description='Absolute path of the .pickle file to store the dataset in')
        self.declare_parameter('file_name','example_dataset.pickle',my_parameter_descriptor1)

        #Parameter representing the label to assign to the current data points being produced
        my_parameter_descriptor2 = ParameterDescriptor(description='Label to give to the data to save')
        self.declare_parameter('label','None',my_parameter_descriptor2)

        #Subscription to the node where to get the data points from
        self.subscription1 = self.create_subscription(
            TimeWindowForTwo,
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
        
        #List to store the produced dataset instances
        self.dataset = Dataset()

        #Label to assign to all the data points currently produced
        self.label = self.get_parameter('label').get_parameter_value().integer_value

        self.count = 0
        self.publisher_ = self.create_publisher(Bool, '/save_dataset', 10)
        
    def listener_callback(self, msg):
        #Construction of the DataInstance object to populate the later Dataset object
        self.count=self.count+1
        self.get_logger().info('Entered callback "%i"' % self.count)
        motion_data_dim = len(msg.time_window_one[0].poses)
        timesteps = len(msg.time_window_one)*2

        motion_frame = np.zeros((timesteps, motion_data_dim, 3), dtype = float)

        #data_instance = DataInstance()

        #Filling of a motion frame
        for i in range(timesteps):
            for j in range(motion_data_dim):
                skeleton_point_1 = msg.time_window_one[i].poses[j].position
                skeleton_point_2 = msg.time_window_two[i].poses[j].position
                motion_frame[i,j,:] = [skeleton_point_1.x, skeleton_point_1.y, skeleton_point_1.z,skeleton_point_2.x, skeleton_point_2.y, skeleton_point_2.z]

        self.dataset.append_data(motion_frame,self.label)
        

        if self.count==100:
            msg=Bool()
            msg.data = True
            self.publisher_.publish(msg)


    def save_dataset(self, msg):
        #Saving of a Dataset object produced (must be called through terminal)
        if msg.data == True:
            self.get_logger().info('Saving dataset')

            file_name = self.get_parameter('file_name').get_parameter_value().string_value
            
            
            self.dataset.save(self.folder_path+file_name)
            

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
