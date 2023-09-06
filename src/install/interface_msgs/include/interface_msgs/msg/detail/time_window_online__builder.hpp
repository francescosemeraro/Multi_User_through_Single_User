// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interface_msgs:msg/TimeWindowOnline.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__BUILDER_HPP_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__BUILDER_HPP_

#include "interface_msgs/msg/detail/time_window_online__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interface_msgs
{

namespace msg
{

namespace builder
{

class Init_TimeWindowOnline_time_window_2
{
public:
  explicit Init_TimeWindowOnline_time_window_2(::interface_msgs::msg::TimeWindowOnline & msg)
  : msg_(msg)
  {}
  ::interface_msgs::msg::TimeWindowOnline time_window_2(::interface_msgs::msg::TimeWindowOnline::_time_window_2_type arg)
  {
    msg_.time_window_2 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface_msgs::msg::TimeWindowOnline msg_;
};

class Init_TimeWindowOnline_time_window_1
{
public:
  Init_TimeWindowOnline_time_window_1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TimeWindowOnline_time_window_2 time_window_1(::interface_msgs::msg::TimeWindowOnline::_time_window_1_type arg)
  {
    msg_.time_window_1 = std::move(arg);
    return Init_TimeWindowOnline_time_window_2(msg_);
  }

private:
  ::interface_msgs::msg::TimeWindowOnline msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface_msgs::msg::TimeWindowOnline>()
{
  return interface_msgs::msg::builder::Init_TimeWindowOnline_time_window_1();
}

}  // namespace interface_msgs

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__BUILDER_HPP_
