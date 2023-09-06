// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interface_msgs:msg/TimeWindowOffline.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interface_msgs/msg/detail/time_window_offline__rosidl_typesupport_introspection_c.h"
#include "interface_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interface_msgs/msg/detail/time_window_offline__functions.h"
#include "interface_msgs/msg/detail/time_window_offline__struct.h"


// Include directives for member types
// Member `time_window`
#include "geometry_msgs/msg/pose_array.h"
// Member `time_window`
#include "geometry_msgs/msg/detail/pose_array__rosidl_typesupport_introspection_c.h"
// Member `j0`
#include "geometry_msgs/msg/point.h"
// Member `j0`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"
// Member `q_spine`
#include "geometry_msgs/msg/quaternion.h"
// Member `q_spine`
#include "geometry_msgs/msg/detail/quaternion__rosidl_typesupport_introspection_c.h"
// Member `norm`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interface_msgs__msg__TimeWindowOffline__init(message_memory);
}

void TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_fini_function(void * message_memory)
{
  interface_msgs__msg__TimeWindowOffline__fini(message_memory);
}

size_t TimeWindowOffline__rosidl_typesupport_introspection_c__size_function__PoseArray__time_window(
  const void * untyped_member)
{
  const geometry_msgs__msg__PoseArray__Sequence * member =
    (const geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return member->size;
}

const void * TimeWindowOffline__rosidl_typesupport_introspection_c__get_const_function__PoseArray__time_window(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__PoseArray__Sequence * member =
    (const geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return &member->data[index];
}

void * TimeWindowOffline__rosidl_typesupport_introspection_c__get_function__PoseArray__time_window(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__PoseArray__Sequence * member =
    (geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return &member->data[index];
}

bool TimeWindowOffline__rosidl_typesupport_introspection_c__resize_function__PoseArray__time_window(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__PoseArray__Sequence * member =
    (geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  geometry_msgs__msg__PoseArray__Sequence__fini(member);
  return geometry_msgs__msg__PoseArray__Sequence__init(member, size);
}

size_t TimeWindowOffline__rosidl_typesupport_introspection_c__size_function__Point__j0(
  const void * untyped_member)
{
  const geometry_msgs__msg__Point__Sequence * member =
    (const geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return member->size;
}

const void * TimeWindowOffline__rosidl_typesupport_introspection_c__get_const_function__Point__j0(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__Point__Sequence * member =
    (const geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return &member->data[index];
}

void * TimeWindowOffline__rosidl_typesupport_introspection_c__get_function__Point__j0(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__Point__Sequence * member =
    (geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return &member->data[index];
}

bool TimeWindowOffline__rosidl_typesupport_introspection_c__resize_function__Point__j0(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__Point__Sequence * member =
    (geometry_msgs__msg__Point__Sequence *)(untyped_member);
  geometry_msgs__msg__Point__Sequence__fini(member);
  return geometry_msgs__msg__Point__Sequence__init(member, size);
}

size_t TimeWindowOffline__rosidl_typesupport_introspection_c__size_function__Quaternion__q_spine(
  const void * untyped_member)
{
  const geometry_msgs__msg__Quaternion__Sequence * member =
    (const geometry_msgs__msg__Quaternion__Sequence *)(untyped_member);
  return member->size;
}

const void * TimeWindowOffline__rosidl_typesupport_introspection_c__get_const_function__Quaternion__q_spine(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__Quaternion__Sequence * member =
    (const geometry_msgs__msg__Quaternion__Sequence *)(untyped_member);
  return &member->data[index];
}

void * TimeWindowOffline__rosidl_typesupport_introspection_c__get_function__Quaternion__q_spine(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__Quaternion__Sequence * member =
    (geometry_msgs__msg__Quaternion__Sequence *)(untyped_member);
  return &member->data[index];
}

bool TimeWindowOffline__rosidl_typesupport_introspection_c__resize_function__Quaternion__q_spine(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__Quaternion__Sequence * member =
    (geometry_msgs__msg__Quaternion__Sequence *)(untyped_member);
  geometry_msgs__msg__Quaternion__Sequence__fini(member);
  return geometry_msgs__msg__Quaternion__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_member_array[4] = {
  {
    "time_window",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_msgs__msg__TimeWindowOffline, time_window),  // bytes offset in struct
    NULL,  // default value
    TimeWindowOffline__rosidl_typesupport_introspection_c__size_function__PoseArray__time_window,  // size() function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__get_const_function__PoseArray__time_window,  // get_const(index) function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__get_function__PoseArray__time_window,  // get(index) function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__resize_function__PoseArray__time_window  // resize(index) function pointer
  },
  {
    "j0",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_msgs__msg__TimeWindowOffline, j0),  // bytes offset in struct
    NULL,  // default value
    TimeWindowOffline__rosidl_typesupport_introspection_c__size_function__Point__j0,  // size() function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__get_const_function__Point__j0,  // get_const(index) function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__get_function__Point__j0,  // get(index) function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__resize_function__Point__j0  // resize(index) function pointer
  },
  {
    "q_spine",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_msgs__msg__TimeWindowOffline, q_spine),  // bytes offset in struct
    NULL,  // default value
    TimeWindowOffline__rosidl_typesupport_introspection_c__size_function__Quaternion__q_spine,  // size() function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__get_const_function__Quaternion__q_spine,  // get_const(index) function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__get_function__Quaternion__q_spine,  // get(index) function pointer
    TimeWindowOffline__rosidl_typesupport_introspection_c__resize_function__Quaternion__q_spine  // resize(index) function pointer
  },
  {
    "norm",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_msgs__msg__TimeWindowOffline, norm),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_members = {
  "interface_msgs__msg",  // message namespace
  "TimeWindowOffline",  // message name
  4,  // number of fields
  sizeof(interface_msgs__msg__TimeWindowOffline),
  TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_member_array,  // message members
  TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_init_function,  // function to initialize message memory (memory has to be allocated)
  TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_type_support_handle = {
  0,
  &TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interface_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_msgs, msg, TimeWindowOffline)() {
  TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, PoseArray)();
  TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Quaternion)();
  if (!TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_type_support_handle.typesupport_identifier) {
    TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TimeWindowOffline__rosidl_typesupport_introspection_c__TimeWindowOffline_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
