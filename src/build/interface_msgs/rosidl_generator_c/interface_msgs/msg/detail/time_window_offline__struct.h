// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interface_msgs:msg/TimeWindowOffline.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__STRUCT_H_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'time_window'
#include "geometry_msgs/msg/detail/pose_array__struct.h"
// Member 'j0'
#include "geometry_msgs/msg/detail/point__struct.h"
// Member 'q_spine'
#include "geometry_msgs/msg/detail/quaternion__struct.h"
// Member 'norm'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in msg/TimeWindowOffline in the package interface_msgs.
typedef struct interface_msgs__msg__TimeWindowOffline
{
  geometry_msgs__msg__PoseArray__Sequence time_window;
  geometry_msgs__msg__Point__Sequence j0;
  geometry_msgs__msg__Quaternion__Sequence q_spine;
  rosidl_runtime_c__double__Sequence norm;
} interface_msgs__msg__TimeWindowOffline;

// Struct for a sequence of interface_msgs__msg__TimeWindowOffline.
typedef struct interface_msgs__msg__TimeWindowOffline__Sequence
{
  interface_msgs__msg__TimeWindowOffline * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface_msgs__msg__TimeWindowOffline__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__STRUCT_H_
