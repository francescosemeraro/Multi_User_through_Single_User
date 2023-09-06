import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
        'separator_z', 
        default_value="-100.00", 
        description="Z coordinate, according to camera frame, of the point needed to discern an instance related to a person"),
        DeclareLaunchArgument(
        'separator_y', 
        default_value="-100.00", 
        description="Y coordinate, according to camera frame, of the point needed to discern an instance related to a person"),
        DeclareLaunchArgument(
        'sequence_length', 
        default_value="1", 
        description="Number of motion frames to include in a sequence"),
        DeclareLaunchArgument(
        'not_overlapped', 
        default_value="1", 
        description="Number of frames that do not overlap between two adjacent sequences"),
        Node(
            package='acquisition_block',
            namespace='sk1',
            executable='sk_generator',
            name='skeleton_generator',
        ),
        Node(
            package='acquisition_block',
            namespace='sg1',
            executable='sq_generator_two',
            name='sequence_generator',
            parameters=[
                {"separator_z": launch.substitutions.LaunchConfiguration('separator_z')}, 
                {"separator_y": launch.substitutions.LaunchConfiguration('separator_y')}, 
                {"sequence_length": launch.substitutions.LaunchConfiguration('sequence_length')},
                {"not_overlapped": launch.substitutions.LaunchConfiguration('not_overlapped')}                 
            ]
        )
    ])

