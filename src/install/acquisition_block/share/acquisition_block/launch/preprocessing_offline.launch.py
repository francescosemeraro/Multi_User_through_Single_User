import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
        'separator', 
        default_value="-100.00", 
        description="Distance from camera needed to discern an instance related to a person"),
        DeclareLaunchArgument(
        'sequence_length', 
        default_value="1", 
        description="Number of motion frames to include in a sequence"),
        DeclareLaunchArgument(
        'not_overlapped', 
        default_value="1", 
        description="Number of frames that do not overlap between two adjacent sequences"),
        DeclareLaunchArgument(
        'save_prep', 
        default_value="true", 
        description="Boolean to record pre-processing data"),
        Node(
            package='acquisition_block',
            namespace='sk1',
            executable='sk_generator',
            name='skeleton_generator',
        ),
        Node(
            package='acquisition_block',
            namespace='sg1',
            executable='sq_generator_one',
            name='sequence_generator',
            parameters=[
                {"separator": launch.substitutions.LaunchConfiguration('separator')}, 
                {"sequence_length": launch.substitutions.LaunchConfiguration('sequence_length')},
                {"save_prep": launch.substitutions.LaunchConfiguration('save_prep')},
                {"not_overlapped": launch.substitutions.LaunchConfiguration('not_overlapped')}                 
            ]
        )
    ])

