// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from interface_msgs:msg/TimeWindow.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "interface_msgs/msg/detail/time_window__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace interface_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TimeWindow_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) interface_msgs::msg::TimeWindow(_init);
}

void TimeWindow_fini_function(void * message_memory)
{
  auto typed_message = static_cast<interface_msgs::msg::TimeWindow *>(message_memory);
  typed_message->~TimeWindow();
}

size_t size_function__TimeWindow__time_window(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<geometry_msgs::msg::PoseArray> *>(untyped_member);
  return member->size();
}

const void * get_const_function__TimeWindow__time_window(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<geometry_msgs::msg::PoseArray> *>(untyped_member);
  return &member[index];
}

void * get_function__TimeWindow__time_window(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<geometry_msgs::msg::PoseArray> *>(untyped_member);
  return &member[index];
}

void resize_function__TimeWindow__time_window(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<geometry_msgs::msg::PoseArray> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TimeWindow_message_member_array[1] = {
  {
    "time_window",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<geometry_msgs::msg::PoseArray>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_msgs::msg::TimeWindow, time_window),  // bytes offset in struct
    nullptr,  // default value
    size_function__TimeWindow__time_window,  // size() function pointer
    get_const_function__TimeWindow__time_window,  // get_const(index) function pointer
    get_function__TimeWindow__time_window,  // get(index) function pointer
    resize_function__TimeWindow__time_window  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TimeWindow_message_members = {
  "interface_msgs::msg",  // message namespace
  "TimeWindow",  // message name
  1,  // number of fields
  sizeof(interface_msgs::msg::TimeWindow),
  TimeWindow_message_member_array,  // message members
  TimeWindow_init_function,  // function to initialize message memory (memory has to be allocated)
  TimeWindow_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TimeWindow_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TimeWindow_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace interface_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<interface_msgs::msg::TimeWindow>()
{
  return &::interface_msgs::msg::rosidl_typesupport_introspection_cpp::TimeWindow_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, interface_msgs, msg, TimeWindow)() {
  return &::interface_msgs::msg::rosidl_typesupport_introspection_cpp::TimeWindow_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
