// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interface_msgs:msg/TimeWindow.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__STRUCT_HPP_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'time_window'
#include "geometry_msgs/msg/detail/pose_array__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interface_msgs__msg__TimeWindow __attribute__((deprecated))
#else
# define DEPRECATED__interface_msgs__msg__TimeWindow __declspec(deprecated)
#endif

namespace interface_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TimeWindow_
{
  using Type = TimeWindow_<ContainerAllocator>;

  explicit TimeWindow_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit TimeWindow_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _time_window_type =
    std::vector<geometry_msgs::msg::PoseArray_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::PoseArray_<ContainerAllocator>>::other>;
  _time_window_type time_window;

  // setters for named parameter idiom
  Type & set__time_window(
    const std::vector<geometry_msgs::msg::PoseArray_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::PoseArray_<ContainerAllocator>>::other> & _arg)
  {
    this->time_window = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interface_msgs::msg::TimeWindow_<ContainerAllocator> *;
  using ConstRawPtr =
    const interface_msgs::msg::TimeWindow_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interface_msgs::msg::TimeWindow_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interface_msgs::msg::TimeWindow_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interface_msgs::msg::TimeWindow_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interface_msgs::msg::TimeWindow_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interface_msgs::msg::TimeWindow_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interface_msgs::msg::TimeWindow_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interface_msgs::msg::TimeWindow_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interface_msgs::msg::TimeWindow_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interface_msgs__msg__TimeWindow
    std::shared_ptr<interface_msgs::msg::TimeWindow_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interface_msgs__msg__TimeWindow
    std::shared_ptr<interface_msgs::msg::TimeWindow_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TimeWindow_ & other) const
  {
    if (this->time_window != other.time_window) {
      return false;
    }
    return true;
  }
  bool operator!=(const TimeWindow_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TimeWindow_

// alias to use template instance with default allocator
using TimeWindow =
  interface_msgs::msg::TimeWindow_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interface_msgs

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW__STRUCT_HPP_
