// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interface_msgs:msg/TimeWindowOnline.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__STRUCT_HPP_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'time_window_1'
// Member 'time_window_2'
#include "geometry_msgs/msg/detail/pose_array__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interface_msgs__msg__TimeWindowOnline __attribute__((deprecated))
#else
# define DEPRECATED__interface_msgs__msg__TimeWindowOnline __declspec(deprecated)
#endif

namespace interface_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TimeWindowOnline_
{
  using Type = TimeWindowOnline_<ContainerAllocator>;

  explicit TimeWindowOnline_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit TimeWindowOnline_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _time_window_1_type =
    std::vector<geometry_msgs::msg::PoseArray_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::PoseArray_<ContainerAllocator>>::other>;
  _time_window_1_type time_window_1;
  using _time_window_2_type =
    std::vector<geometry_msgs::msg::PoseArray_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::PoseArray_<ContainerAllocator>>::other>;
  _time_window_2_type time_window_2;

  // setters for named parameter idiom
  Type & set__time_window_1(
    const std::vector<geometry_msgs::msg::PoseArray_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::PoseArray_<ContainerAllocator>>::other> & _arg)
  {
    this->time_window_1 = _arg;
    return *this;
  }
  Type & set__time_window_2(
    const std::vector<geometry_msgs::msg::PoseArray_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::PoseArray_<ContainerAllocator>>::other> & _arg)
  {
    this->time_window_2 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interface_msgs::msg::TimeWindowOnline_<ContainerAllocator> *;
  using ConstRawPtr =
    const interface_msgs::msg::TimeWindowOnline_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interface_msgs::msg::TimeWindowOnline_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interface_msgs::msg::TimeWindowOnline_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interface_msgs::msg::TimeWindowOnline_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interface_msgs::msg::TimeWindowOnline_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interface_msgs::msg::TimeWindowOnline_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interface_msgs::msg::TimeWindowOnline_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interface_msgs::msg::TimeWindowOnline_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interface_msgs::msg::TimeWindowOnline_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interface_msgs__msg__TimeWindowOnline
    std::shared_ptr<interface_msgs::msg::TimeWindowOnline_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interface_msgs__msg__TimeWindowOnline
    std::shared_ptr<interface_msgs::msg::TimeWindowOnline_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TimeWindowOnline_ & other) const
  {
    if (this->time_window_1 != other.time_window_1) {
      return false;
    }
    if (this->time_window_2 != other.time_window_2) {
      return false;
    }
    return true;
  }
  bool operator!=(const TimeWindowOnline_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TimeWindowOnline_

// alias to use template instance with default allocator
using TimeWindowOnline =
  interface_msgs::msg::TimeWindowOnline_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interface_msgs

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_ONLINE__STRUCT_HPP_
