// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from zed_msgs:srv/SaveAreaMemory.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "zed_msgs/srv/save_area_memory.hpp"


#ifndef ZED_MSGS__SRV__DETAIL__SAVE_AREA_MEMORY__BUILDER_HPP_
#define ZED_MSGS__SRV__DETAIL__SAVE_AREA_MEMORY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "zed_msgs/srv/detail/save_area_memory__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace zed_msgs
{

namespace srv
{

namespace builder
{

class Init_SaveAreaMemory_Request_area_file_path
{
public:
  Init_SaveAreaMemory_Request_area_file_path()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::zed_msgs::srv::SaveAreaMemory_Request area_file_path(::zed_msgs::srv::SaveAreaMemory_Request::_area_file_path_type arg)
  {
    msg_.area_file_path = std::move(arg);
    return std::move(msg_);
  }

private:
  ::zed_msgs::srv::SaveAreaMemory_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::zed_msgs::srv::SaveAreaMemory_Request>()
{
  return zed_msgs::srv::builder::Init_SaveAreaMemory_Request_area_file_path();
}

}  // namespace zed_msgs


namespace zed_msgs
{

namespace srv
{

namespace builder
{

class Init_SaveAreaMemory_Response_message
{
public:
  explicit Init_SaveAreaMemory_Response_message(::zed_msgs::srv::SaveAreaMemory_Response & msg)
  : msg_(msg)
  {}
  ::zed_msgs::srv::SaveAreaMemory_Response message(::zed_msgs::srv::SaveAreaMemory_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::zed_msgs::srv::SaveAreaMemory_Response msg_;
};

class Init_SaveAreaMemory_Response_success
{
public:
  Init_SaveAreaMemory_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SaveAreaMemory_Response_message success(::zed_msgs::srv::SaveAreaMemory_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_SaveAreaMemory_Response_message(msg_);
  }

private:
  ::zed_msgs::srv::SaveAreaMemory_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::zed_msgs::srv::SaveAreaMemory_Response>()
{
  return zed_msgs::srv::builder::Init_SaveAreaMemory_Response_success();
}

}  // namespace zed_msgs


namespace zed_msgs
{

namespace srv
{

namespace builder
{

class Init_SaveAreaMemory_Event_response
{
public:
  explicit Init_SaveAreaMemory_Event_response(::zed_msgs::srv::SaveAreaMemory_Event & msg)
  : msg_(msg)
  {}
  ::zed_msgs::srv::SaveAreaMemory_Event response(::zed_msgs::srv::SaveAreaMemory_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::zed_msgs::srv::SaveAreaMemory_Event msg_;
};

class Init_SaveAreaMemory_Event_request
{
public:
  explicit Init_SaveAreaMemory_Event_request(::zed_msgs::srv::SaveAreaMemory_Event & msg)
  : msg_(msg)
  {}
  Init_SaveAreaMemory_Event_response request(::zed_msgs::srv::SaveAreaMemory_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_SaveAreaMemory_Event_response(msg_);
  }

private:
  ::zed_msgs::srv::SaveAreaMemory_Event msg_;
};

class Init_SaveAreaMemory_Event_info
{
public:
  Init_SaveAreaMemory_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SaveAreaMemory_Event_request info(::zed_msgs::srv::SaveAreaMemory_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_SaveAreaMemory_Event_request(msg_);
  }

private:
  ::zed_msgs::srv::SaveAreaMemory_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::zed_msgs::srv::SaveAreaMemory_Event>()
{
  return zed_msgs::srv::builder::Init_SaveAreaMemory_Event_info();
}

}  // namespace zed_msgs

#endif  // ZED_MSGS__SRV__DETAIL__SAVE_AREA_MEMORY__BUILDER_HPP_
