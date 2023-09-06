// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from interface_msgs:msg/TimeWindow.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__FUNCTIONS_H_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "interface_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "interface_msgs/msg/detail/time_window__struct.h"

/// Initialize msg/TimeWindow message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interface_msgs__msg__TimeWindow
 * )) before or use
 * interface_msgs__msg__TimeWindow__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
bool
interface_msgs__msg__TimeWindow__init(interface_msgs__msg__TimeWindow * msg);

/// Finalize msg/TimeWindow message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
void
interface_msgs__msg__TimeWindow__fini(interface_msgs__msg__TimeWindow * msg);

/// Create msg/TimeWindow message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interface_msgs__msg__TimeWindow__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
interface_msgs__msg__TimeWindow *
interface_msgs__msg__TimeWindow__create();

/// Destroy msg/TimeWindow message.
/**
 * It calls
 * interface_msgs__msg__TimeWindow__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
void
interface_msgs__msg__TimeWindow__destroy(interface_msgs__msg__TimeWindow * msg);


/// Initialize array of msg/TimeWindow messages.
/**
 * It allocates the memory for the number of elements and calls
 * interface_msgs__msg__TimeWindow__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
bool
interface_msgs__msg__TimeWindow__Sequence__init(interface_msgs__msg__TimeWindow__Sequence * array, size_t size);

/// Finalize array of msg/TimeWindow messages.
/**
 * It calls
 * interface_msgs__msg__TimeWindow__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
void
interface_msgs__msg__TimeWindow__Sequence__fini(interface_msgs__msg__TimeWindow__Sequence * array);

/// Create array of msg/TimeWindow messages.
/**
 * It allocates the memory for the array and calls
 * interface_msgs__msg__TimeWindow__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
interface_msgs__msg__TimeWindow__Sequence *
interface_msgs__msg__TimeWindow__Sequence__create(size_t size);

/// Destroy array of msg/TimeWindow messages.
/**
 * It calls
 * interface_msgs__msg__TimeWindow__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
void
interface_msgs__msg__TimeWindow__Sequence__destroy(interface_msgs__msg__TimeWindow__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__FUNCTIONS_H_
