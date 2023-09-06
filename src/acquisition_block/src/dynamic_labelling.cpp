// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <memory>

#include "rclcpp/rclcpp.hpp"
//#include "/opt/ros/foxy/include/rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int64.hpp"
#include "visualization_msgs/msg/marker_array.hpp"
#include "geometry_msgs/msg/pose_array.hpp"
using std::placeholders::_1;
using namespace std::chrono_literals;
using namespace std;

//Node that performs skeleton normalisation and generates sequences of motion frames to send to the reasoning block
//Through preprocessing.launch.py, it is possible to specify the parameters called separator, sequence_length and not_overlapped

class DynamicLabel : public rclcpp::Node
{
public: 
  
  DynamicLabel()
  : Node("Dynamic_labeller")
  {
    //Subscription to front-end node between Azure Kinect and robotic system

    std::function<void(const std_msgs::msg::Int64::SharedPtr)> callback_function = std::bind(&DynamicLabel::ChangeLabel, this, _1);
    subscription_to_new_label = this->create_subscription<std_msgs::msg::Int64>(
      "/new_label", 10, callback_function);

    std::function<void(const visualization_msgs::msg::MarkerArray::SharedPtr)> callback_function_2 = std::bind(&DynamicLabel::LabelSkeleton, this, _1);
    subscription_to_body_tracking = this->create_subscription<visualization_msgs::msg::MarkerArray>(
      "/body_tracking_data", 10, callback_function_2);
    
//Publisher to node that peforms recognition based on machine learning
    publisher_to_label = this->create_publisher<std_msgs::msg::Int64>("/label", 10);
    //timer_ = this->create_wall_timer(10ms, std::bind(&MinimalPublisher::timer_callback, this));
    //RCLCPP_INFO(this->get_logger(), "Entered constructor");

  }

private:

  std_msgs::msg::Int64 initialise_label()
  {
    std_msgs::msg::Int64 dummy;

    int64_t number = 9;
    dummy.data = number;
    RCLCPP_INFO(this->get_logger(), "Label initialised");

    return dummy;
  }

  void ChangeLabel(const std_msgs::msg::Int64::SharedPtr msg) 
  {
    if (msg->data!=0)
    {
      RCLCPP_INFO(this->get_logger(), "New label assigned");

      label.data = msg->data;
    }
  }

  void LabelSkeleton(const visualization_msgs::msg::MarkerArray::SharedPtr msg) 
  {
    //label.data = ;
    publisher_to_label->publish(label);
  }

  //uint64_t new_label;
  std_msgs::msg::Int64 label = initialise_label();
  //std_msgs::msg::Int64 label;

  //Definition of publisher and subscriber
  rclcpp::Subscription<std_msgs::msg::Int64>::SharedPtr subscription_to_new_label;
  rclcpp::Subscription<visualization_msgs::msg::MarkerArray>::SharedPtr subscription_to_body_tracking;
  rclcpp::Publisher<std_msgs::msg::Int64>::SharedPtr publisher_to_label;
   
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  //std::cout<<"ENtered here";
  //std::cout<<"ENtered here";
  rclcpp::spin(std::make_shared<DynamicLabel>());
  //auto node = std::make_shared<DynamicLabel>();
  //auto logger = node->get_logger();
  //RCLCPP_INFO(logger,"Entered here");
  //rclcpp::spin(node);
  //std::cout<<"ENtered here";
  rclcpp::shutdown();
  return 0;
}