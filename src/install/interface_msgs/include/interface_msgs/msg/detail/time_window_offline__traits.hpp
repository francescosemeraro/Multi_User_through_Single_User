// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interface_msgs:msg/TimeWindowOffline.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__TRAITS_HPP_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__TRAITS_HPP_

#include "interface_msgs/msg/detail/time_window_offline__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interface_msgs::msg::TimeWindowOffline>()
{
  return "interface_msgs::msg::TimeWindowOffline";
}

template<>
inline const char * name<interface_msgs::msg::TimeWindowOffline>()
{
  return "interface_msgs/msg/TimeWindowOffline";
}

template<>
struct has_fixed_size<interface_msgs::msg::TimeWindowOffline>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interface_msgs::msg::TimeWindowOffline>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interface_msgs::msg::TimeWindowOffline>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__TRAITS_HPP_
