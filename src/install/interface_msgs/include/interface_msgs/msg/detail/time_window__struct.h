// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interface_msgs:msg/TimeWindow.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__STRUCT_H_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__STRUCT_H_

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

// Struct defined in msg/TimeWindow in the package interface_msgs.
typedef struct interface_msgs__msg__TimeWindow
{
  geometry_msgs__msg__PoseArray__Sequence time_window;
} interface_msgs__msg__TimeWindow;

// Struct for a sequence of interface_msgs__msg__TimeWindow.
typedef struct interface_msgs__msg__TimeWindow__Sequence
{
  interface_msgs__msg__TimeWindow * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface_msgs__msg__TimeWindow__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__STRUCT_H_
