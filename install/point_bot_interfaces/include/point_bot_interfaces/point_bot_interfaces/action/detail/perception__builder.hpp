// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from point_bot_interfaces:action/Perception.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "point_bot_interfaces/action/perception.hpp"


#ifndef POINT_BOT_INTERFACES__ACTION__DETAIL__PERCEPTION__BUILDER_HPP_
#define POINT_BOT_INTERFACES__ACTION__DETAIL__PERCEPTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "point_bot_interfaces/action/detail/perception__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_Goal_task
{
public:
  Init_Perception_Goal_task()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::point_bot_interfaces::action::Perception_Goal task(::point_bot_interfaces::action::Perception_Goal::_task_type arg)
  {
    msg_.task = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_Goal>()
{
  return point_bot_interfaces::action::builder::Init_Perception_Goal_task();
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_Result_pose
{
public:
  explicit Init_Perception_Result_pose(::point_bot_interfaces::action::Perception_Result & msg)
  : msg_(msg)
  {}
  ::point_bot_interfaces::action::Perception_Result pose(::point_bot_interfaces::action::Perception_Result::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_Result msg_;
};

class Init_Perception_Result_image
{
public:
  explicit Init_Perception_Result_image(::point_bot_interfaces::action::Perception_Result & msg)
  : msg_(msg)
  {}
  Init_Perception_Result_pose image(::point_bot_interfaces::action::Perception_Result::_image_type arg)
  {
    msg_.image = std::move(arg);
    return Init_Perception_Result_pose(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_Result msg_;
};

class Init_Perception_Result_success
{
public:
  Init_Perception_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Perception_Result_image success(::point_bot_interfaces::action::Perception_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_Perception_Result_image(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_Result>()
{
  return point_bot_interfaces::action::builder::Init_Perception_Result_success();
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{


}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_Feedback>()
{
  return ::point_bot_interfaces::action::Perception_Feedback(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_SendGoal_Request_goal
{
public:
  explicit Init_Perception_SendGoal_Request_goal(::point_bot_interfaces::action::Perception_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::point_bot_interfaces::action::Perception_SendGoal_Request goal(::point_bot_interfaces::action::Perception_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_SendGoal_Request msg_;
};

class Init_Perception_SendGoal_Request_goal_id
{
public:
  Init_Perception_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Perception_SendGoal_Request_goal goal_id(::point_bot_interfaces::action::Perception_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Perception_SendGoal_Request_goal(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_SendGoal_Request>()
{
  return point_bot_interfaces::action::builder::Init_Perception_SendGoal_Request_goal_id();
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_SendGoal_Response_stamp
{
public:
  explicit Init_Perception_SendGoal_Response_stamp(::point_bot_interfaces::action::Perception_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::point_bot_interfaces::action::Perception_SendGoal_Response stamp(::point_bot_interfaces::action::Perception_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_SendGoal_Response msg_;
};

class Init_Perception_SendGoal_Response_accepted
{
public:
  Init_Perception_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Perception_SendGoal_Response_stamp accepted(::point_bot_interfaces::action::Perception_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Perception_SendGoal_Response_stamp(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_SendGoal_Response>()
{
  return point_bot_interfaces::action::builder::Init_Perception_SendGoal_Response_accepted();
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_SendGoal_Event_response
{
public:
  explicit Init_Perception_SendGoal_Event_response(::point_bot_interfaces::action::Perception_SendGoal_Event & msg)
  : msg_(msg)
  {}
  ::point_bot_interfaces::action::Perception_SendGoal_Event response(::point_bot_interfaces::action::Perception_SendGoal_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_SendGoal_Event msg_;
};

class Init_Perception_SendGoal_Event_request
{
public:
  explicit Init_Perception_SendGoal_Event_request(::point_bot_interfaces::action::Perception_SendGoal_Event & msg)
  : msg_(msg)
  {}
  Init_Perception_SendGoal_Event_response request(::point_bot_interfaces::action::Perception_SendGoal_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_Perception_SendGoal_Event_response(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_SendGoal_Event msg_;
};

class Init_Perception_SendGoal_Event_info
{
public:
  Init_Perception_SendGoal_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Perception_SendGoal_Event_request info(::point_bot_interfaces::action::Perception_SendGoal_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_Perception_SendGoal_Event_request(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_SendGoal_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_SendGoal_Event>()
{
  return point_bot_interfaces::action::builder::Init_Perception_SendGoal_Event_info();
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_GetResult_Request_goal_id
{
public:
  Init_Perception_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::point_bot_interfaces::action::Perception_GetResult_Request goal_id(::point_bot_interfaces::action::Perception_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_GetResult_Request>()
{
  return point_bot_interfaces::action::builder::Init_Perception_GetResult_Request_goal_id();
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_GetResult_Response_result
{
public:
  explicit Init_Perception_GetResult_Response_result(::point_bot_interfaces::action::Perception_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::point_bot_interfaces::action::Perception_GetResult_Response result(::point_bot_interfaces::action::Perception_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_GetResult_Response msg_;
};

class Init_Perception_GetResult_Response_status
{
public:
  Init_Perception_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Perception_GetResult_Response_result status(::point_bot_interfaces::action::Perception_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Perception_GetResult_Response_result(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_GetResult_Response>()
{
  return point_bot_interfaces::action::builder::Init_Perception_GetResult_Response_status();
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_GetResult_Event_response
{
public:
  explicit Init_Perception_GetResult_Event_response(::point_bot_interfaces::action::Perception_GetResult_Event & msg)
  : msg_(msg)
  {}
  ::point_bot_interfaces::action::Perception_GetResult_Event response(::point_bot_interfaces::action::Perception_GetResult_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_GetResult_Event msg_;
};

class Init_Perception_GetResult_Event_request
{
public:
  explicit Init_Perception_GetResult_Event_request(::point_bot_interfaces::action::Perception_GetResult_Event & msg)
  : msg_(msg)
  {}
  Init_Perception_GetResult_Event_response request(::point_bot_interfaces::action::Perception_GetResult_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_Perception_GetResult_Event_response(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_GetResult_Event msg_;
};

class Init_Perception_GetResult_Event_info
{
public:
  Init_Perception_GetResult_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Perception_GetResult_Event_request info(::point_bot_interfaces::action::Perception_GetResult_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_Perception_GetResult_Event_request(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_GetResult_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_GetResult_Event>()
{
  return point_bot_interfaces::action::builder::Init_Perception_GetResult_Event_info();
}

}  // namespace point_bot_interfaces


namespace point_bot_interfaces
{

namespace action
{

namespace builder
{

class Init_Perception_FeedbackMessage_feedback
{
public:
  explicit Init_Perception_FeedbackMessage_feedback(::point_bot_interfaces::action::Perception_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::point_bot_interfaces::action::Perception_FeedbackMessage feedback(::point_bot_interfaces::action::Perception_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_FeedbackMessage msg_;
};

class Init_Perception_FeedbackMessage_goal_id
{
public:
  Init_Perception_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Perception_FeedbackMessage_feedback goal_id(::point_bot_interfaces::action::Perception_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Perception_FeedbackMessage_feedback(msg_);
  }

private:
  ::point_bot_interfaces::action::Perception_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::point_bot_interfaces::action::Perception_FeedbackMessage>()
{
  return point_bot_interfaces::action::builder::Init_Perception_FeedbackMessage_goal_id();
}

}  // namespace point_bot_interfaces

#endif  // POINT_BOT_INTERFACES__ACTION__DETAIL__PERCEPTION__BUILDER_HPP_
