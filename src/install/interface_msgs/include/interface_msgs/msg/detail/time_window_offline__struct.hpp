// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interface_msgs:msg/TimeWindowOffline.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__STRUCT_HPP_
#define INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__STRUCT_HPP_

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
// Member 'j0'
#include "geometry_msgs/msg/detail/point__struct.hpp"
// Member 'q_spine'
#include "geometry_msgs/msg/detail/quaternion__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interface_msgs__msg__TimeWindowOffline __attribute__((deprecated))
#else
# define DEPRECATED__interface_msgs__msg__TimeWindowOffline __declspec(deprecated)
#endif

namespace interface_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TimeWindowOffline_
{
  using Type = TimeWindowOffline_<ContainerAllocator>;

  explicit TimeWindowOffline_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit TimeWindowOffline_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _time_window_type =
    std::vector<geometry_msgs::msg::PoseArray_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::PoseArray_<ContainerAllocator>>::other>;
  _time_window_type time_window;
  using _j0_type =
    std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other>;
  _j0_type j0;
  using _q_spine_type =
    std::vector<geometry_msgs::msg::Quaternion_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Quaternion_<ContainerAllocator>>::other>;
  _q_spine_type q_spine;
  using _norm_type =
    std::vector<double, typename ContainerAllocator::template rebind<double>::other>;
  _norm_type norm;

  // setters for named parameter idiom
  Type & set__time_window(
    const std::vector<geometry_msgs::msg::PoseArray_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::PoseArray_<ContainerAllocator>>::other> & _arg)
  {
    this->time_window = _arg;
    return *this;
  }
  Type & set__j0(
    const std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other> & _arg)
  {
    this->j0 = _arg;
    return *this;
  }
  Type & set__q_spine(
    const std::vector<geometry_msgs::msg::Quaternion_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Quaternion_<ContainerAllocator>>::other> & _arg)
  {
    this->q_spine = _arg;
    return *this;
  }
  Type & set__norm(
    const std::vector<double, typename ContainerAllocator::template rebind<double>::other> & _arg)
  {
    this->norm = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interface_msgs::msg::TimeWindowOffline_<ContainerAllocator> *;
  using ConstRawPtr =
    const interface_msgs::msg::TimeWindowOffline_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interface_msgs::msg::TimeWindowOffline_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interface_msgs::msg::TimeWindowOffline_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interface_msgs::msg::TimeWindowOffline_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interface_msgs::msg::TimeWindowOffline_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interface_msgs::msg::TimeWindowOffline_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interface_msgs::msg::TimeWindowOffline_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interface_msgs::msg::TimeWindowOffline_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interface_msgs::msg::TimeWindowOffline_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interface_msgs__msg__TimeWindowOffline
    std::shared_ptr<interface_msgs::msg::TimeWindowOffline_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interface_msgs__msg__TimeWindowOffline
    std::shared_ptr<interface_msgs::msg::TimeWindowOffline_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TimeWindowOffline_ & other) const
  {
    if (this->time_window != other.time_window) {
      return false;
    }
    if (this->j0 != other.j0) {
      return false;
    }
    if (this->q_spine != other.q_spine) {
      return false;
    }
    if (this->norm != other.norm) {
      return false;
    }
    return true;
  }
  bool operator!=(const TimeWindowOffline_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TimeWindowOffline_

// alias to use template instance with default allocator
using TimeWindowOffline =
  interface_msgs::msg::TimeWindowOffline_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interface_msgs

#endif  // INTERFACE_MSGS__MSG__DETAIL__TIME_WINDOW_OFFLINE__STRUCT_HPP_
