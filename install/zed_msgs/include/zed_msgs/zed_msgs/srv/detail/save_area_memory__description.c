// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from zed_msgs:srv/SaveAreaMemory.idl
// generated code does not contain a copyright notice

#include "zed_msgs/srv/detail/save_area_memory__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_zed_msgs
const rosidl_type_hash_t *
zed_msgs__srv__SaveAreaMemory__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x89, 0x8b, 0x6e, 0x5e, 0xc4, 0x83, 0x0b, 0x77,
      0xb5, 0x02, 0x1e, 0xde, 0x26, 0x1c, 0x13, 0xe8,
      0xd5, 0x1c, 0x41, 0xf4, 0xbb, 0xc2, 0xa7, 0x0c,
      0x8b, 0x1e, 0x17, 0x96, 0xb6, 0x12, 0x57, 0xe1,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_zed_msgs
const rosidl_type_hash_t *
zed_msgs__srv__SaveAreaMemory_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x51, 0xbd, 0x16, 0x93, 0xab, 0xc4, 0xdf, 0x21,
      0x93, 0x1d, 0xbe, 0xf2, 0xb7, 0x92, 0xc2, 0x1f,
      0x21, 0xb6, 0x7d, 0xb7, 0xc5, 0xe4, 0xe6, 0xe0,
      0xa7, 0x8a, 0x2b, 0x5f, 0x4e, 0x65, 0x1e, 0xe8,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_zed_msgs
const rosidl_type_hash_t *
zed_msgs__srv__SaveAreaMemory_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x5c, 0x88, 0x16, 0x5a, 0xf2, 0xd1, 0x86, 0xef,
      0x86, 0x43, 0x9c, 0x90, 0x34, 0x9b, 0xc2, 0xf5,
      0x4b, 0x68, 0x0c, 0xcf, 0x5b, 0xa0, 0x79, 0xd8,
      0xe1, 0xf4, 0xbe, 0xa2, 0x99, 0xb4, 0x73, 0x1f,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_zed_msgs
const rosidl_type_hash_t *
zed_msgs__srv__SaveAreaMemory_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xb6, 0x9b, 0x28, 0xa2, 0xb7, 0x38, 0x73, 0x73,
      0x0a, 0x7c, 0xc9, 0x46, 0x32, 0xaa, 0x4d, 0x7d,
      0xc0, 0x74, 0x5d, 0x29, 0xa0, 0x62, 0x9c, 0xe1,
      0x16, 0x1d, 0xbf, 0xdc, 0x5f, 0x2e, 0x96, 0xeb,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "service_msgs/msg/detail/service_event_info__functions.h"
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char zed_msgs__srv__SaveAreaMemory__TYPE_NAME[] = "zed_msgs/srv/SaveAreaMemory";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";
static char zed_msgs__srv__SaveAreaMemory_Event__TYPE_NAME[] = "zed_msgs/srv/SaveAreaMemory_Event";
static char zed_msgs__srv__SaveAreaMemory_Request__TYPE_NAME[] = "zed_msgs/srv/SaveAreaMemory_Request";
static char zed_msgs__srv__SaveAreaMemory_Response__TYPE_NAME[] = "zed_msgs/srv/SaveAreaMemory_Response";

// Define type names, field names, and default values
static char zed_msgs__srv__SaveAreaMemory__FIELD_NAME__request_message[] = "request_message";
static char zed_msgs__srv__SaveAreaMemory__FIELD_NAME__response_message[] = "response_message";
static char zed_msgs__srv__SaveAreaMemory__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field zed_msgs__srv__SaveAreaMemory__FIELDS[] = {
  {
    {zed_msgs__srv__SaveAreaMemory__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {zed_msgs__srv__SaveAreaMemory_Request__TYPE_NAME, 35, 35},
    },
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {zed_msgs__srv__SaveAreaMemory_Response__TYPE_NAME, 36, 36},
    },
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {zed_msgs__srv__SaveAreaMemory_Event__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription zed_msgs__srv__SaveAreaMemory__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory_Event__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory_Request__TYPE_NAME, 35, 35},
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory_Response__TYPE_NAME, 36, 36},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
zed_msgs__srv__SaveAreaMemory__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {zed_msgs__srv__SaveAreaMemory__TYPE_NAME, 27, 27},
      {zed_msgs__srv__SaveAreaMemory__FIELDS, 3, 3},
    },
    {zed_msgs__srv__SaveAreaMemory__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = zed_msgs__srv__SaveAreaMemory_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = zed_msgs__srv__SaveAreaMemory_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[4].fields = zed_msgs__srv__SaveAreaMemory_Response__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char zed_msgs__srv__SaveAreaMemory_Request__FIELD_NAME__area_file_path[] = "area_file_path";

static rosidl_runtime_c__type_description__Field zed_msgs__srv__SaveAreaMemory_Request__FIELDS[] = {
  {
    {zed_msgs__srv__SaveAreaMemory_Request__FIELD_NAME__area_file_path, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
zed_msgs__srv__SaveAreaMemory_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {zed_msgs__srv__SaveAreaMemory_Request__TYPE_NAME, 35, 35},
      {zed_msgs__srv__SaveAreaMemory_Request__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char zed_msgs__srv__SaveAreaMemory_Response__FIELD_NAME__success[] = "success";
static char zed_msgs__srv__SaveAreaMemory_Response__FIELD_NAME__message[] = "message";

static rosidl_runtime_c__type_description__Field zed_msgs__srv__SaveAreaMemory_Response__FIELDS[] = {
  {
    {zed_msgs__srv__SaveAreaMemory_Response__FIELD_NAME__success, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory_Response__FIELD_NAME__message, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
zed_msgs__srv__SaveAreaMemory_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {zed_msgs__srv__SaveAreaMemory_Response__TYPE_NAME, 36, 36},
      {zed_msgs__srv__SaveAreaMemory_Response__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char zed_msgs__srv__SaveAreaMemory_Event__FIELD_NAME__info[] = "info";
static char zed_msgs__srv__SaveAreaMemory_Event__FIELD_NAME__request[] = "request";
static char zed_msgs__srv__SaveAreaMemory_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field zed_msgs__srv__SaveAreaMemory_Event__FIELDS[] = {
  {
    {zed_msgs__srv__SaveAreaMemory_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {zed_msgs__srv__SaveAreaMemory_Request__TYPE_NAME, 35, 35},
    },
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {zed_msgs__srv__SaveAreaMemory_Response__TYPE_NAME, 36, 36},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription zed_msgs__srv__SaveAreaMemory_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory_Request__TYPE_NAME, 35, 35},
    {NULL, 0, 0},
  },
  {
    {zed_msgs__srv__SaveAreaMemory_Response__TYPE_NAME, 36, 36},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
zed_msgs__srv__SaveAreaMemory_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {zed_msgs__srv__SaveAreaMemory_Event__TYPE_NAME, 33, 33},
      {zed_msgs__srv__SaveAreaMemory_Event__FIELDS, 3, 3},
    },
    {zed_msgs__srv__SaveAreaMemory_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = zed_msgs__srv__SaveAreaMemory_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = zed_msgs__srv__SaveAreaMemory_Response__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# Save the current area memory to a file\n"
  "\n"
  "# Path of an area localization file that describes the surroundings. Use \".area\" extension.\n"
  "string area_file_path\n"
  "---\n"
  "bool success   # indicate successful run of service\n"
  "string message # informational, e.g. for error messages";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
zed_msgs__srv__SaveAreaMemory__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {zed_msgs__srv__SaveAreaMemory__TYPE_NAME, 27, 27},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 268, 268},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
zed_msgs__srv__SaveAreaMemory_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {zed_msgs__srv__SaveAreaMemory_Request__TYPE_NAME, 35, 35},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
zed_msgs__srv__SaveAreaMemory_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {zed_msgs__srv__SaveAreaMemory_Response__TYPE_NAME, 36, 36},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
zed_msgs__srv__SaveAreaMemory_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {zed_msgs__srv__SaveAreaMemory_Event__TYPE_NAME, 33, 33},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
zed_msgs__srv__SaveAreaMemory__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *zed_msgs__srv__SaveAreaMemory__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[3] = *zed_msgs__srv__SaveAreaMemory_Event__get_individual_type_description_source(NULL);
    sources[4] = *zed_msgs__srv__SaveAreaMemory_Request__get_individual_type_description_source(NULL);
    sources[5] = *zed_msgs__srv__SaveAreaMemory_Response__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
zed_msgs__srv__SaveAreaMemory_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *zed_msgs__srv__SaveAreaMemory_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
zed_msgs__srv__SaveAreaMemory_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *zed_msgs__srv__SaveAreaMemory_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
zed_msgs__srv__SaveAreaMemory_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *zed_msgs__srv__SaveAreaMemory_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[3] = *zed_msgs__srv__SaveAreaMemory_Request__get_individual_type_description_source(NULL);
    sources[4] = *zed_msgs__srv__SaveAreaMemory_Response__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
