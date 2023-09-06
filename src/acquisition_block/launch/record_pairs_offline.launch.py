import launch
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    azure_kinect_launch_prefix = get_package_share_directory('azure_kinect_ros_driver')

    included_launch = launch.actions.IncludeLaunchDescription(PythonLaunchDescriptionSource([azure_kinect_launch_prefix, '/launch/driver.launch.py']),
     launch_arguments={'color_resolution':'720P', 'fps':'30', 'body_tracking_enabled':'true', 'depth_mode':'NFOV_UNBINNED'}.items())

    return LaunchDescription([
        DeclareLaunchArgument(
        'tag', 
        default_value="tag", 
        description="Tag related to the acquisition"),
        Node(
            package='acquisition_block',
            namespace='labels',
            executable='dynamic_labeller',
            name='dynamic_labeller',
        ),
        Node(
            package='acquisition_block',
            namespace='label_bag',
            executable='bag_recorder',
            name='label_recorder',
            parameters=[
                {"tag": launch.substitutions.LaunchConfiguration('tag')}, 
                {"type_of_file": "label"}, 
                {"topic_name": "label"}] 
        ),
        included_launch,
        Node(
            package='acquisition_block',
            namespace='video_bag',
            executable='bag_recorder',
            name='video_recorder',
            parameters=[
                {"tag": launch.substitutions.LaunchConfiguration('tag')}, 
                {"type_of_file": "video"}, 
                {"topic_name": "rgb/image_raw"}] 
        ),
        Node(
            package='acquisition_block',
            namespace='depth_bag',
            executable='bag_recorder',
            name='depth_recorder',
            parameters=[
                {"tag": launch.substitutions.LaunchConfiguration('tag')}, 
                {"type_of_file": "depth"}, 
                {"topic_name": "depth/image_raw"}] 
        ),
        Node(
            package='acquisition_block',
            namespace='skel_bag',
            executable='bag_recorder',
            name='skel_recorder',
            parameters=[
                {"tag": launch.substitutions.LaunchConfiguration('tag')}, 
                {"type_of_file": "skeleton"}, 
                {"topic_name": "body_tracking_data"}] 
        )
    ])

