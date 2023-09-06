// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interface_msgs:msg/TimeWindowOnline.idl
// generated code does not contain a copyright notice
#include "interface_msgs/msg/detail/time_window_online__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `time_window_1`
// Member `time_window_2`
#include "geometry_msgs/msg/detail/pose_array__functions.h"

bool
interface_msgs__msg__TimeWindowOnline__init(interface_msgs__msg__TimeWindowOnline * msg)
{
  if (!msg) {
    return false;
  }
  // time_window_1
  if (!geometry_msgs__msg__PoseArray__Sequence__init(&msg->time_window_1, 0)) {
    interface_msgs__msg__TimeWindowOnline__fini(msg);
    return false;
  }
  // time_window_2
  if (!geometry_msgs__msg__PoseArray__Sequence__init(&msg->time_window_2, 0)) {
    interface_msgs__msg__TimeWindowOnline__fini(msg);
    return false;
  }
  return true;
}

void
interface_msgs__msg__TimeWindowOnline__fini(interface_msgs__msg__TimeWindowOnline * msg)
{
  if (!msg) {
    return;
  }
  // time_window_1
  geometry_msgs__msg__PoseArray__Sequence__fini(&msg->time_window_1);
  // time_window_2
  geometry_msgs__msg__PoseArray__Sequence__fini(&msg->time_window_2);
}

interface_msgs__msg__TimeWindowOnline *
interface_msgs__msg__TimeWindowOnline__create()
{
  interface_msgs__msg__TimeWindowOnline * msg = (interface_msgs__msg__TimeWindowOnline *)malloc(sizeof(interface_msgs__msg__TimeWindowOnline));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interface_msgs__msg__TimeWindowOnline));
  bool success = interface_msgs__msg__TimeWindowOnline__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interface_msgs__msg__TimeWindowOnline__destroy(interface_msgs__msg__TimeWindowOnline * msg)
{
  if (msg) {
    interface_msgs__msg__TimeWindowOnline__fini(msg);
  }
  free(msg);
}


bool
interface_msgs__msg__TimeWindowOnline__Sequence__init(interface_msgs__msg__TimeWindowOnline__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interface_msgs__msg__TimeWindowOnline * data = NULL;
  if (size) {
    data = (interface_msgs__msg__TimeWindowOnline *)calloc(size, sizeof(interface_msgs__msg__TimeWindowOnline));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interface_msgs__msg__TimeWindowOnline__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interface_msgs__msg__TimeWindowOnline__fini(&data[i - 1]);
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
interface_msgs__msg__TimeWindowOnline__Sequence__fini(interface_msgs__msg__TimeWindowOnline__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interface_msgs__msg__TimeWindowOnline__fini(&array->data[i]);
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

interface_msgs__msg__TimeWindowOnline__Sequence *
interface_msgs__msg__TimeWindowOnline__Sequence__create(size_t size)
{
  interface_msgs__msg__TimeWindowOnline__Sequence * array = (interface_msgs__msg__TimeWindowOnline__Sequence *)malloc(sizeof(interface_msgs__msg__TimeWindowOnline__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interface_msgs__msg__TimeWindowOnline__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interface_msgs__msg__TimeWindowOnline__Sequence__destroy(interface_msgs__msg__TimeWindowOnline__Sequence * array)
{
  if (array) {
    interface_msgs__msg__TimeWindowOnline__Sequence__fini(array);
  }
  free(array);
}
