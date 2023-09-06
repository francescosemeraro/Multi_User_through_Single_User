// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interface_msgs:msg/TimeWindow.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__BUILDER_HPP_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__BUILDER_HPP_

#include "interface_msgs/msg/detail/time_window__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interface_msgs
{

namespace msg
{

namespace builder
{

class Init_TimeWindow_time_window
{
public:
  Init_TimeWindow_time_window()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interface_msgs::msg::TimeWindow time_window(::interface_msgs::msg::TimeWindow::_time_window_type arg)
  {
    msg_.time_window = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface_msgs::msg::TimeWindow msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface_msgs::msg::TimeWindow>()
{
  return interface_msgs::msg::builder::Init_TimeWindow_time_window();
}

}  // namespace interface_msgs

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__BUILDER_HPP_
