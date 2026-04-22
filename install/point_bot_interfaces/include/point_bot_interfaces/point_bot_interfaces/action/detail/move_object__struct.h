// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from point_bot_interfaces:action/MoveObject.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "point_bot_interfaces/action/move_object.h"


#ifndef POINT_BOT_INTERFACES__ACTION__DETAIL__MOVE_OBJECT__STRUCT_H_
#define POINT_BOT_INTERFACES__ACTION__DETAIL__MOVE_OBJECT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'object'
// Member 'goal'
#include "geometry_msgs/msg/detail/pose_stamped__struct.h"

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_Goal
{
  geometry_msgs__msg__PoseStamped object;
  geometry_msgs__msg__PoseStamped goal;
} point_bot_interfaces__action__MoveObject_Goal;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_Goal.
typedef struct point_bot_interfaces__action__MoveObject_Goal__Sequence
{
  point_bot_interfaces__action__MoveObject_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_Goal__Sequence;

// Constants defined in the message

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_Result
{
  bool success;
} point_bot_interfaces__action__MoveObject_Result;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_Result.
typedef struct point_bot_interfaces__action__MoveObject_Result__Sequence
{
  point_bot_interfaces__action__MoveObject_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_Result__Sequence;

// Constants defined in the message

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_Feedback
{
  uint8_t structure_needs_at_least_one_member;
} point_bot_interfaces__action__MoveObject_Feedback;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_Feedback.
typedef struct point_bot_interfaces__action__MoveObject_Feedback__Sequence
{
  point_bot_interfaces__action__MoveObject_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_Feedback__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "point_bot_interfaces/action/detail/move_object__struct.h"

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  point_bot_interfaces__action__MoveObject_Goal goal;
} point_bot_interfaces__action__MoveObject_SendGoal_Request;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_SendGoal_Request.
typedef struct point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence
{
  point_bot_interfaces__action__MoveObject_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} point_bot_interfaces__action__MoveObject_SendGoal_Response;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_SendGoal_Response.
typedef struct point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence
{
  point_bot_interfaces__action__MoveObject_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  point_bot_interfaces__action__MoveObject_SendGoal_Event__request__MAX_SIZE = 1
};
// response
enum
{
  point_bot_interfaces__action__MoveObject_SendGoal_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_SendGoal_Event
{
  service_msgs__msg__ServiceEventInfo info;
  point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence request;
  point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence response;
} point_bot_interfaces__action__MoveObject_SendGoal_Event;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_SendGoal_Event.
typedef struct point_bot_interfaces__action__MoveObject_SendGoal_Event__Sequence
{
  point_bot_interfaces__action__MoveObject_SendGoal_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_SendGoal_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} point_bot_interfaces__action__MoveObject_GetResult_Request;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_GetResult_Request.
typedef struct point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence
{
  point_bot_interfaces__action__MoveObject_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "point_bot_interfaces/action/detail/move_object__struct.h"

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_GetResult_Response
{
  int8_t status;
  point_bot_interfaces__action__MoveObject_Result result;
} point_bot_interfaces__action__MoveObject_GetResult_Response;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_GetResult_Response.
typedef struct point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence
{
  point_bot_interfaces__action__MoveObject_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
// already included above
// #include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  point_bot_interfaces__action__MoveObject_GetResult_Event__request__MAX_SIZE = 1
};
// response
enum
{
  point_bot_interfaces__action__MoveObject_GetResult_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_GetResult_Event
{
  service_msgs__msg__ServiceEventInfo info;
  point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence request;
  point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence response;
} point_bot_interfaces__action__MoveObject_GetResult_Event;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_GetResult_Event.
typedef struct point_bot_interfaces__action__MoveObject_GetResult_Event__Sequence
{
  point_bot_interfaces__action__MoveObject_GetResult_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_GetResult_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "point_bot_interfaces/action/detail/move_object__struct.h"

/// Struct defined in action/MoveObject in the package point_bot_interfaces.
typedef struct point_bot_interfaces__action__MoveObject_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  point_bot_interfaces__action__MoveObject_Feedback feedback;
} point_bot_interfaces__action__MoveObject_FeedbackMessage;

// Struct for a sequence of point_bot_interfaces__action__MoveObject_FeedbackMessage.
typedef struct point_bot_interfaces__action__MoveObject_FeedbackMessage__Sequence
{
  point_bot_interfaces__action__MoveObject_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} point_bot_interfaces__action__MoveObject_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // POINT_BOT_INTERFACES__ACTION__DETAIL__MOVE_OBJECT__STRUCT_H_
