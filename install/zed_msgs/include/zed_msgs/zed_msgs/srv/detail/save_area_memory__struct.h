// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from zed_msgs:srv/SaveAreaMemory.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "zed_msgs/srv/save_area_memory.h"


#ifndef ZED_MSGS__SRV__DETAIL__SAVE_AREA_MEMORY__STRUCT_H_
#define ZED_MSGS__SRV__DETAIL__SAVE_AREA_MEMORY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'area_file_path'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SaveAreaMemory in the package zed_msgs.
typedef struct zed_msgs__srv__SaveAreaMemory_Request
{
  /// Path of an area localization file that describes the surroundings. Use ".area" extension.
  rosidl_runtime_c__String area_file_path;
} zed_msgs__srv__SaveAreaMemory_Request;

// Struct for a sequence of zed_msgs__srv__SaveAreaMemory_Request.
typedef struct zed_msgs__srv__SaveAreaMemory_Request__Sequence
{
  zed_msgs__srv__SaveAreaMemory_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} zed_msgs__srv__SaveAreaMemory_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SaveAreaMemory in the package zed_msgs.
typedef struct zed_msgs__srv__SaveAreaMemory_Response
{
  /// indicate successful run of service
  bool success;
  /// informational, e.g. for error messages
  rosidl_runtime_c__String message;
} zed_msgs__srv__SaveAreaMemory_Response;

// Struct for a sequence of zed_msgs__srv__SaveAreaMemory_Response.
typedef struct zed_msgs__srv__SaveAreaMemory_Response__Sequence
{
  zed_msgs__srv__SaveAreaMemory_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} zed_msgs__srv__SaveAreaMemory_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  zed_msgs__srv__SaveAreaMemory_Event__request__MAX_SIZE = 1
};
// response
enum
{
  zed_msgs__srv__SaveAreaMemory_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/SaveAreaMemory in the package zed_msgs.
typedef struct zed_msgs__srv__SaveAreaMemory_Event
{
  service_msgs__msg__ServiceEventInfo info;
  zed_msgs__srv__SaveAreaMemory_Request__Sequence request;
  zed_msgs__srv__SaveAreaMemory_Response__Sequence response;
} zed_msgs__srv__SaveAreaMemory_Event;

// Struct for a sequence of zed_msgs__srv__SaveAreaMemory_Event.
typedef struct zed_msgs__srv__SaveAreaMemory_Event__Sequence
{
  zed_msgs__srv__SaveAreaMemory_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} zed_msgs__srv__SaveAreaMemory_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ZED_MSGS__SRV__DETAIL__SAVE_AREA_MEMORY__STRUCT_H_
