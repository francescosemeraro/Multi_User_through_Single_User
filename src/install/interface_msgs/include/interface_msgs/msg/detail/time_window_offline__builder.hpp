// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interface_msgs:msg/TimeWindowOffline.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__BUILDER_HPP_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__BUILDER_HPP_

#include "interface_msgs/msg/detail/time_window_offline__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interface_msgs
{

namespace msg
{

namespace builder
{

class Init_TimeWindowOffline_norm
{
public:
  explicit Init_TimeWindowOffline_norm(::interface_msgs::msg::TimeWindowOffline & msg)
  : msg_(msg)
  {}
  ::interface_msgs::msg::TimeWindowOffline norm(::interface_msgs::msg::TimeWindowOffline::_norm_type arg)
  {
    msg_.norm = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface_msgs::msg::TimeWindowOffline msg_;
};

class Init_TimeWindowOffline_q_spine
{
public:
  explicit Init_TimeWindowOffline_q_spine(::interface_msgs::msg::TimeWindowOffline & msg)
  : msg_(msg)
  {}
  Init_TimeWindowOffline_norm q_spine(::interface_msgs::msg::TimeWindowOffline::_q_spine_type arg)
  {
    msg_.q_spine = std::move(arg);
    return Init_TimeWindowOffline_norm(msg_);
  }

private:
  ::interface_msgs::msg::TimeWindowOffline msg_;
};

class Init_TimeWindowOffline_j0
{
public:
  explicit Init_TimeWindowOffline_j0(::interface_msgs::msg::TimeWindowOffline & msg)
  : msg_(msg)
  {}
  Init_TimeWindowOffline_q_spine j0(::interface_msgs::msg::TimeWindowOffline::_j0_type arg)
  {
    msg_.j0 = std::move(arg);
    return Init_TimeWindowOffline_q_spine(msg_);
  }

private:
  ::interface_msgs::msg::TimeWindowOffline msg_;
};

class Init_TimeWindowOffline_time_window
{
public:
  Init_TimeWindowOffline_time_window()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TimeWindowOffline_j0 time_window(::interface_msgs::msg::TimeWindowOffline::_time_window_type arg)
  {
    msg_.time_window = std::move(arg);
    return Init_TimeWindowOffline_j0(msg_);
  }

private:
  ::interface_msgs::msg::TimeWindowOffline msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface_msgs::msg::TimeWindowOffline>()
{
  return interface_msgs::msg::builder::Init_TimeWindowOffline_time_window();
}

}  // namespace interface_msgs

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__BUILDER_HPP_
