// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interface_msgs:msg/TimeWindowOnline.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interface_msgs/msg/detail/time_window_online__rosidl_typesupport_introspection_c.h"
#include "interface_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interface_msgs/msg/detail/time_window_online__functions.h"
#include "interface_msgs/msg/detail/time_window_online__struct.h"


// Include directives for member types
// Member `time_window_1`
// Member `time_window_2`
#include "geometry_msgs/msg/pose_array.h"
// Member `time_window_1`
// Member `time_window_2`
#include "geometry_msgs/msg/detail/pose_array__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interface_msgs__msg__TimeWindowOnline__init(message_memory);
}

void TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_fini_function(void * message_memory)
{
  interface_msgs__msg__TimeWindowOnline__fini(message_memory);
}

size_t TimeWindowOnline__rosidl_typesupport_introspection_c__size_function__PoseArray__time_window_1(
  const void * untyped_member)
{
  const geometry_msgs__msg__PoseArray__Sequence * member =
    (const geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return member->size;
}

const void * TimeWindowOnline__rosidl_typesupport_introspection_c__get_const_function__PoseArray__time_window_1(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__PoseArray__Sequence * member =
    (const geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return &member->data[index];
}

void * TimeWindowOnline__rosidl_typesupport_introspection_c__get_function__PoseArray__time_window_1(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__PoseArray__Sequence * member =
    (geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return &member->data[index];
}

bool TimeWindowOnline__rosidl_typesupport_introspection_c__resize_function__PoseArray__time_window_1(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__PoseArray__Sequence * member =
    (geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  geometry_msgs__msg__PoseArray__Sequence__fini(member);
  return geometry_msgs__msg__PoseArray__Sequence__init(member, size);
}

size_t TimeWindowOnline__rosidl_typesupport_introspection_c__size_function__PoseArray__time_window_2(
  const void * untyped_member)
{
  const geometry_msgs__msg__PoseArray__Sequence * member =
    (const geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return member->size;
}

const void * TimeWindowOnline__rosidl_typesupport_introspection_c__get_const_function__PoseArray__time_window_2(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__PoseArray__Sequence * member =
    (const geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return &member->data[index];
}

void * TimeWindowOnline__rosidl_typesupport_introspection_c__get_function__PoseArray__time_window_2(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__PoseArray__Sequence * member =
    (geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  return &member->data[index];
}

bool TimeWindowOnline__rosidl_typesupport_introspection_c__resize_function__PoseArray__time_window_2(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__PoseArray__Sequence * member =
    (geometry_msgs__msg__PoseArray__Sequence *)(untyped_member);
  geometry_msgs__msg__PoseArray__Sequence__fini(member);
  return geometry_msgs__msg__PoseArray__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_member_array[2] = {
  {
    "time_window_1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_msgs__msg__TimeWindowOnline, time_window_1),  // bytes offset in struct
    NULL,  // default value
    TimeWindowOnline__rosidl_typesupport_introspection_c__size_function__PoseArray__time_window_1,  // size() function pointer
    TimeWindowOnline__rosidl_typesupport_introspection_c__get_const_function__PoseArray__time_window_1,  // get_const(index) function pointer
    TimeWindowOnline__rosidl_typesupport_introspection_c__get_function__PoseArray__time_window_1,  // get(index) function pointer
    TimeWindowOnline__rosidl_typesupport_introspection_c__resize_function__PoseArray__time_window_1  // resize(index) function pointer
  },
  {
    "time_window_2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_msgs__msg__TimeWindowOnline, time_window_2),  // bytes offset in struct
    NULL,  // default value
    TimeWindowOnline__rosidl_typesupport_introspection_c__size_function__PoseArray__time_window_2,  // size() function pointer
    TimeWindowOnline__rosidl_typesupport_introspection_c__get_const_function__PoseArray__time_window_2,  // get_const(index) function pointer
    TimeWindowOnline__rosidl_typesupport_introspection_c__get_function__PoseArray__time_window_2,  // get(index) function pointer
    TimeWindowOnline__rosidl_typesupport_introspection_c__resize_function__PoseArray__time_window_2  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_members = {
  "interface_msgs__msg",  // message namespace
  "TimeWindowOnline",  // message name
  2,  // number of fields
  sizeof(interface_msgs__msg__TimeWindowOnline),
  TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_member_array,  // message members
  TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_init_function,  // function to initialize message memory (memory has to be allocated)
  TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_type_support_handle = {
  0,
  &TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interface_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_msgs, msg, TimeWindowOnline)() {
  TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, PoseArray)();
  TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, PoseArray)();
  if (!TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_type_support_handle.typesupport_identifier) {
    TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TimeWindowOnline__rosidl_typesupport_introspection_c__TimeWindowOnline_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
