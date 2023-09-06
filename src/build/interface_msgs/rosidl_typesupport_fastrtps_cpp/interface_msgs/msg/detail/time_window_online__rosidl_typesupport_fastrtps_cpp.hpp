// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from interface_msgs:msg/TimeWindowOnline.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "interface_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "interface_msgs/msg/detail/time_window_online__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace interface_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interface_msgs
cdr_serialize(
  const interface_msgs::msg::TimeWindowOnline & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interface_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  interface_msgs::msg::TimeWindowOnline & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interface_msgs
get_serialized_size(
  const interface_msgs::msg::TimeWindowOnline & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interface_msgs
max_serialized_size_TimeWindowOnline(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace interface_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interface_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, interface_msgs, msg, TimeWindowOnline)();

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
