// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from interface_msgs:msg/TimeWindowOnline.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__FUNCTIONS_H_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "interface_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "interface_msgs/msg/detail/time_window_online__struct.h"

/// Initialize msg/TimeWindowOnline message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interface_msgs__msg__TimeWindowOnline
 * )) before or use
 * interface_msgs__msg__TimeWindowOnline__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
bool
interface_msgs__msg__TimeWindowOnline__init(interface_msgs__msg__TimeWindowOnline * msg);

/// Finalize msg/TimeWindowOnline message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
void
interface_msgs__msg__TimeWindowOnline__fini(interface_msgs__msg__TimeWindowOnline * msg);

/// Create msg/TimeWindowOnline message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interface_msgs__msg__TimeWindowOnline__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
interface_msgs__msg__TimeWindowOnline *
interface_msgs__msg__TimeWindowOnline__create();

/// Destroy msg/TimeWindowOnline message.
/**
 * It calls
 * interface_msgs__msg__TimeWindowOnline__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
void
interface_msgs__msg__TimeWindowOnline__destroy(interface_msgs__msg__TimeWindowOnline * msg);


/// Initialize array of msg/TimeWindowOnline messages.
/**
 * It allocates the memory for the number of elements and calls
 * interface_msgs__msg__TimeWindowOnline__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
bool
interface_msgs__msg__TimeWindowOnline__Sequence__init(interface_msgs__msg__TimeWindowOnline__Sequence * array, size_t size);

/// Finalize array of msg/TimeWindowOnline messages.
/**
 * It calls
 * interface_msgs__msg__TimeWindowOnline__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
void
interface_msgs__msg__TimeWindowOnline__Sequence__fini(interface_msgs__msg__TimeWindowOnline__Sequence * array);

/// Create array of msg/TimeWindowOnline messages.
/**
 * It allocates the memory for the array and calls
 * interface_msgs__msg__TimeWindowOnline__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
interface_msgs__msg__TimeWindowOnline__Sequence *
interface_msgs__msg__TimeWindowOnline__Sequence__create(size_t size);

/// Destroy array of msg/TimeWindowOnline messages.
/**
 * It calls
 * interface_msgs__msg__TimeWindowOnline__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interface_msgs
void
interface_msgs__msg__TimeWindowOnline__Sequence__destroy(interface_msgs__msg__TimeWindowOnline__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__FUNCTIONS_H_
