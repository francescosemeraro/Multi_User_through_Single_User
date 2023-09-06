// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interface_msgs:msg/TimeWindow.idl
// generated code does not contain a copyright notice
#include "interface_msgs/msg/detail/time_window__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `time_window`
#include "geometry_msgs/msg/detail/pose_array__functions.h"

bool
interface_msgs__msg__TimeWindow__init(interface_msgs__msg__TimeWindow * msg)
{
  if (!msg) {
    return false;
  }
  // time_window
  if (!geometry_msgs__msg__PoseArray__Sequence__init(&msg->time_window, 0)) {
    interface_msgs__msg__TimeWindow__fini(msg);
    return false;
  }
  return true;
}

void
interface_msgs__msg__TimeWindow__fini(interface_msgs__msg__TimeWindow * msg)
{
  if (!msg) {
    return;
  }
  // time_window
  geometry_msgs__msg__PoseArray__Sequence__fini(&msg->time_window);
}

interface_msgs__msg__TimeWindow *
interface_msgs__msg__TimeWindow__create()
{
  interface_msgs__msg__TimeWindow * msg = (interface_msgs__msg__TimeWindow *)malloc(sizeof(interface_msgs__msg__TimeWindow));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interface_msgs__msg__TimeWindow));
  bool success = interface_msgs__msg__TimeWindow__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interface_msgs__msg__TimeWindow__destroy(interface_msgs__msg__TimeWindow * msg)
{
  if (msg) {
    interface_msgs__msg__TimeWindow__fini(msg);
  }
  free(msg);
}


bool
interface_msgs__msg__TimeWindow__Sequence__init(interface_msgs__msg__TimeWindow__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interface_msgs__msg__TimeWindow * data = NULL;
  if (size) {
    data = (interface_msgs__msg__TimeWindow *)calloc(size, sizeof(interface_msgs__msg__TimeWindow));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interface_msgs__msg__TimeWindow__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interface_msgs__msg__TimeWindow__fini(&data[i - 1]);
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
interface_msgs__msg__TimeWindow__Sequence__fini(interface_msgs__msg__TimeWindow__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interface_msgs__msg__TimeWindow__fini(&array->data[i]);
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

interface_msgs__msg__TimeWindow__Sequence *
interface_msgs__msg__TimeWindow__Sequence__create(size_t size)
{
  interface_msgs__msg__TimeWindow__Sequence * array = (interface_msgs__msg__TimeWindow__Sequence *)malloc(sizeof(interface_msgs__msg__TimeWindow__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interface_msgs__msg__TimeWindow__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interface_msgs__msg__TimeWindow__Sequence__destroy(interface_msgs__msg__TimeWindow__Sequence * array)
{
  if (array) {
    interface_msgs__msg__TimeWindow__Sequence__fini(array);
  }
  free(array);
}
