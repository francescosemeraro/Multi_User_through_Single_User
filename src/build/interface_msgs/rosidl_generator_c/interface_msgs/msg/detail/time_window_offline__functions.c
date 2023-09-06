// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interface_msgs:msg/TimeWindowOffline.idl
// generated code does not contain a copyright notice
#include "interface_msgs/msg/detail/time_window_offline__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `time_window`
#include "geometry_msgs/msg/detail/pose_array__functions.h"
// Member `j0`
#include "geometry_msgs/msg/detail/point__functions.h"
// Member `q_spine`
#include "geometry_msgs/msg/detail/quaternion__functions.h"
// Member `norm`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
interface_msgs__msg__TimeWindowOffline__init(interface_msgs__msg__TimeWindowOffline * msg)
{
  if (!msg) {
    return false;
  }
  // time_window
  if (!geometry_msgs__msg__PoseArray__Sequence__init(&msg->time_window, 0)) {
    interface_msgs__msg__TimeWindowOffline__fini(msg);
    return false;
  }
  // j0
  if (!geometry_msgs__msg__Point__Sequence__init(&msg->j0, 0)) {
    interface_msgs__msg__TimeWindowOffline__fini(msg);
    return false;
  }
  // q_spine
  if (!geometry_msgs__msg__Quaternion__Sequence__init(&msg->q_spine, 0)) {
    interface_msgs__msg__TimeWindowOffline__fini(msg);
    return false;
  }
  // norm
  if (!rosidl_runtime_c__double__Sequence__init(&msg->norm, 0)) {
    interface_msgs__msg__TimeWindowOffline__fini(msg);
    return false;
  }
  return true;
}

void
interface_msgs__msg__TimeWindowOffline__fini(interface_msgs__msg__TimeWindowOffline * msg)
{
  if (!msg) {
    return;
  }
  // time_window
  geometry_msgs__msg__PoseArray__Sequence__fini(&msg->time_window);
  // j0
  geometry_msgs__msg__Point__Sequence__fini(&msg->j0);
  // q_spine
  geometry_msgs__msg__Quaternion__Sequence__fini(&msg->q_spine);
  // norm
  rosidl_runtime_c__double__Sequence__fini(&msg->norm);
}

interface_msgs__msg__TimeWindowOffline *
interface_msgs__msg__TimeWindowOffline__create()
{
  interface_msgs__msg__TimeWindowOffline * msg = (interface_msgs__msg__TimeWindowOffline *)malloc(sizeof(interface_msgs__msg__TimeWindowOffline));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interface_msgs__msg__TimeWindowOffline));
  bool success = interface_msgs__msg__TimeWindowOffline__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interface_msgs__msg__TimeWindowOffline__destroy(interface_msgs__msg__TimeWindowOffline * msg)
{
  if (msg) {
    interface_msgs__msg__TimeWindowOffline__fini(msg);
  }
  free(msg);
}


bool
interface_msgs__msg__TimeWindowOffline__Sequence__init(interface_msgs__msg__TimeWindowOffline__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interface_msgs__msg__TimeWindowOffline * data = NULL;
  if (size) {
    data = (interface_msgs__msg__TimeWindowOffline *)calloc(size, sizeof(interface_msgs__msg__TimeWindowOffline));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interface_msgs__msg__TimeWindowOffline__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interface_msgs__msg__TimeWindowOffline__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interface_msgs__msg__TimeWindowOffline__Sequence__fini(interface_msgs__msg__TimeWindowOffline__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interface_msgs__msg__TimeWindowOffline__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interface_msgs__msg__TimeWindowOffline__Sequence *
interface_msgs__msg__TimeWindowOffline__Sequence__create(size_t size)
{
  interface_msgs__msg__TimeWindowOffline__Sequence * array = (interface_msgs__msg__TimeWindowOffline__Sequence *)malloc(sizeof(interface_msgs__msg__TimeWindowOffline__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interface_msgs__msg__TimeWindowOffline__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interface_msgs__msg__TimeWindowOffline__Sequence__destroy(interface_msgs__msg__TimeWindowOffline__Sequence * array)
{
  if (array) {
    interface_msgs__msg__TimeWindowOffline__Sequence__fini(array);
  }
  free(array);
}
