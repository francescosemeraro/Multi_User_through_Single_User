import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
        'tag', 
        default_value="tag", 
        description="Tag related to the acquisition"),
        Node(
            package='acquisition_block',
            namespace='video_bag',
            executable='bag_recorder',
            name='video_recorder',
            parameters=[
                {"tag": launch.substitutions.LaunchConfiguration('tag')}, 
                {"type_of_file": "video"}, 
                {"topic_name": "rbg/image_raw"}] 
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

