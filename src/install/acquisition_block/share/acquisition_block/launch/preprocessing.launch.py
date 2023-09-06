from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
import launch.substitution

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='acquisition_block',
            namespace='sk1',
            executable='sk_generator',
            name='skeleton_generator',
            
        ),
        Node(
            package='acquisition_block',
            namespace='sg1',
            executable='sq_generator',
            name='sequence_generator',
            output='screen',
            parameters=[
                {"separator": 120.000}, {"sequence_length": 26}, {"not_overlapped": 20} 
            ]
        )
    ])

