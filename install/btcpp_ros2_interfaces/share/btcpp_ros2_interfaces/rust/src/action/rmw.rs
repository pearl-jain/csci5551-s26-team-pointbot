
#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_Goal() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__ExecuteTree_Goal__init(msg: *mut ExecuteTree_Goal) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Goal>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Goal>);
    fn btcpp_ros2_interfaces__action__ExecuteTree_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ExecuteTree_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Goal>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExecuteTree_Goal {
    /// Name of the tree to execute
    pub target_tree: rosidl_runtime_rs::String,

    /// Optional, implementation-dependent, payload.
    pub payload: rosidl_runtime_rs::String,

}



impl Default for ExecuteTree_Goal {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__ExecuteTree_Goal__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__ExecuteTree_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ExecuteTree_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ExecuteTree_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ExecuteTree_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/ExecuteTree_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_Goal() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_Result() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__ExecuteTree_Result__init(msg: *mut ExecuteTree_Result) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Result>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Result>);
    fn btcpp_ros2_interfaces__action__ExecuteTree_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ExecuteTree_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Result>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExecuteTree_Result {
    /// Status of the tree
    pub node_status: super::super::msg::rmw::NodeStatus,

    /// result payload or error message
    pub return_message: rosidl_runtime_rs::String,

}



impl Default for ExecuteTree_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__ExecuteTree_Result__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__ExecuteTree_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ExecuteTree_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ExecuteTree_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ExecuteTree_Result where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/ExecuteTree_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_Result() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__ExecuteTree_Feedback__init(msg: *mut ExecuteTree_Feedback) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Feedback>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Feedback>);
    fn btcpp_ros2_interfaces__action__ExecuteTree_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ExecuteTree_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_Feedback>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExecuteTree_Feedback {
    /// This can be customized by the user
    pub message: rosidl_runtime_rs::String,

}



impl Default for ExecuteTree_Feedback {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__ExecuteTree_Feedback__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__ExecuteTree_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ExecuteTree_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ExecuteTree_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ExecuteTree_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/ExecuteTree_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_Feedback() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__init(msg: *mut ExecuteTree_FeedbackMessage) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_FeedbackMessage>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_FeedbackMessage>);
    fn btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ExecuteTree_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_FeedbackMessage>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExecuteTree_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::ExecuteTree_Feedback,

}



impl Default for ExecuteTree_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ExecuteTree_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ExecuteTree_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ExecuteTree_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/ExecuteTree_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_FeedbackMessage() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_Goal() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__Sleep_Goal__init(msg: *mut Sleep_Goal) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sleep_Goal>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sleep_Goal>);
    fn btcpp_ros2_interfaces__action__Sleep_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sleep_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<Sleep_Goal>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sleep_Goal {

    // This member is not documented.
    #[allow(missing_docs)]
    pub msec_timeout: i32,

}



impl Default for Sleep_Goal {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__Sleep_Goal__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__Sleep_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sleep_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sleep_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sleep_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/Sleep_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_Goal() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_Result() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__Sleep_Result__init(msg: *mut Sleep_Result) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sleep_Result>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sleep_Result>);
    fn btcpp_ros2_interfaces__action__Sleep_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sleep_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<Sleep_Result>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sleep_Result {

    // This member is not documented.
    #[allow(missing_docs)]
    pub done: bool,

}



impl Default for Sleep_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__Sleep_Result__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__Sleep_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sleep_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sleep_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sleep_Result where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/Sleep_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_Result() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__Sleep_Feedback__init(msg: *mut Sleep_Feedback) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sleep_Feedback>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sleep_Feedback>);
    fn btcpp_ros2_interfaces__action__Sleep_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sleep_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<Sleep_Feedback>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sleep_Feedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub cycle: i32,

}



impl Default for Sleep_Feedback {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__Sleep_Feedback__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__Sleep_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sleep_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sleep_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sleep_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/Sleep_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_Feedback() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__init(msg: *mut Sleep_FeedbackMessage) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sleep_FeedbackMessage>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sleep_FeedbackMessage>);
    fn btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sleep_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<Sleep_FeedbackMessage>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sleep_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::Sleep_Feedback,

}



impl Default for Sleep_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sleep_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sleep_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sleep_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/Sleep_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_FeedbackMessage() }
  }
}




#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__init(msg: *mut ExecuteTree_SendGoal_Request) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_SendGoal_Request>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_SendGoal_Request>);
    fn btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ExecuteTree_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_SendGoal_Request>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExecuteTree_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::ExecuteTree_Goal,

}



impl Default for ExecuteTree_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ExecuteTree_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ExecuteTree_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ExecuteTree_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/ExecuteTree_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Request() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__init(msg: *mut ExecuteTree_SendGoal_Response) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_SendGoal_Response>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_SendGoal_Response>);
    fn btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ExecuteTree_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_SendGoal_Response>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExecuteTree_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for ExecuteTree_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ExecuteTree_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ExecuteTree_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ExecuteTree_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/ExecuteTree_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_SendGoal_Response() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__init(msg: *mut ExecuteTree_GetResult_Request) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_GetResult_Request>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_GetResult_Request>);
    fn btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ExecuteTree_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_GetResult_Request>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExecuteTree_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for ExecuteTree_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ExecuteTree_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ExecuteTree_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ExecuteTree_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/ExecuteTree_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Request() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__init(msg: *mut ExecuteTree_GetResult_Response) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_GetResult_Response>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_GetResult_Response>);
    fn btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ExecuteTree_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<ExecuteTree_GetResult_Response>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExecuteTree_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::ExecuteTree_Result,

}



impl Default for ExecuteTree_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ExecuteTree_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ExecuteTree_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ExecuteTree_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/ExecuteTree_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_GetResult_Response() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__init(msg: *mut Sleep_SendGoal_Request) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sleep_SendGoal_Request>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sleep_SendGoal_Request>);
    fn btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sleep_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<Sleep_SendGoal_Request>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sleep_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::Sleep_Goal,

}



impl Default for Sleep_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sleep_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sleep_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sleep_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/Sleep_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_SendGoal_Request() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__init(msg: *mut Sleep_SendGoal_Response) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sleep_SendGoal_Response>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sleep_SendGoal_Response>);
    fn btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sleep_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<Sleep_SendGoal_Response>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sleep_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for Sleep_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sleep_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sleep_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sleep_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/Sleep_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_SendGoal_Response() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__Sleep_GetResult_Request__init(msg: *mut Sleep_GetResult_Request) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sleep_GetResult_Request>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sleep_GetResult_Request>);
    fn btcpp_ros2_interfaces__action__Sleep_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sleep_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<Sleep_GetResult_Request>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sleep_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for Sleep_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__Sleep_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__Sleep_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sleep_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sleep_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sleep_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/Sleep_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_GetResult_Request() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__action__Sleep_GetResult_Response__init(msg: *mut Sleep_GetResult_Response) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sleep_GetResult_Response>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__action__Sleep_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sleep_GetResult_Response>);
    fn btcpp_ros2_interfaces__action__Sleep_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sleep_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<Sleep_GetResult_Response>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sleep_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::Sleep_Result,

}



impl Default for Sleep_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__action__Sleep_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__action__Sleep_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sleep_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__action__Sleep_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sleep_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sleep_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/action/Sleep_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__action__Sleep_GetResult_Response() }
  }
}






#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct ExecuteTree_SendGoal;

impl rosidl_runtime_rs::Service for ExecuteTree_SendGoal {
    type Request = ExecuteTree_SendGoal_Request;
    type Response = ExecuteTree_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_SendGoal() }
    }
}




#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to btcpp_ros2_interfaces__action__ExecuteTree_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct ExecuteTree_GetResult;

impl rosidl_runtime_rs::Service for ExecuteTree_GetResult {
    type Request = ExecuteTree_GetResult_Request;
    type Response = ExecuteTree_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__action__ExecuteTree_GetResult() }
    }
}




#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__action__Sleep_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct Sleep_SendGoal;

impl rosidl_runtime_rs::Service for Sleep_SendGoal {
    type Request = Sleep_SendGoal_Request;
    type Response = Sleep_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__action__Sleep_SendGoal() }
    }
}




#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__action__Sleep_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to btcpp_ros2_interfaces__action__Sleep_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct Sleep_GetResult;

impl rosidl_runtime_rs::Service for Sleep_GetResult {
    type Request = Sleep_GetResult_Request;
    type Response = Sleep_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__action__Sleep_GetResult() }
    }
}


