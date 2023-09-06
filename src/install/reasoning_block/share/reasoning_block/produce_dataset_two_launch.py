import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
        'file_name', 
        default_value="example_dataset.pickle", 
        description="Name of the file where to store the Dataset object (specify .pickle format"),
        DeclareLaunchArgument(
        'label', 
        default_value="None", 
        description="Label to assign to every DataInstance object that will populate the Dataset object"),
        Node(
            package='reasoning_block',
            executable='dataset_generator_for_two',
            name='dataset_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {"file_name": launch.substitutions.LaunchConfiguration('file_name')},
                {"label": launch.substitutions.LaunchConfiguration('label')}
            ]
        )
    ])