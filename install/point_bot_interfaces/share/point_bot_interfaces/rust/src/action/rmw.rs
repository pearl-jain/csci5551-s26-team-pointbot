
#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_Goal() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__Perception_Goal__init(msg: *mut Perception_Goal) -> bool;
    fn point_bot_interfaces__action__Perception_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Perception_Goal>, size: usize) -> bool;
    fn point_bot_interfaces__action__Perception_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Perception_Goal>);
    fn point_bot_interfaces__action__Perception_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Perception_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<Perception_Goal>) -> bool;
}

// Corresponds to point_bot_interfaces__action__Perception_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Perception_Goal {

    // This member is not documented.
    #[allow(missing_docs)]
    pub task: rosidl_runtime_rs::String,

}



impl Default for Perception_Goal {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__Perception_Goal__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__Perception_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Perception_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Perception_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Perception_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/Perception_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_Goal() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_Result() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__Perception_Result__init(msg: *mut Perception_Result) -> bool;
    fn point_bot_interfaces__action__Perception_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Perception_Result>, size: usize) -> bool;
    fn point_bot_interfaces__action__Perception_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Perception_Result>);
    fn point_bot_interfaces__action__Perception_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Perception_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<Perception_Result>) -> bool;
}

// Corresponds to point_bot_interfaces__action__Perception_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Perception_Result {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub image: sensor_msgs::msg::rmw::Image,


    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: geometry_msgs::msg::rmw::PoseStamped,

}



impl Default for Perception_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__Perception_Result__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__Perception_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Perception_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Perception_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Perception_Result where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/Perception_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_Result() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__Perception_Feedback__init(msg: *mut Perception_Feedback) -> bool;
    fn point_bot_interfaces__action__Perception_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Perception_Feedback>, size: usize) -> bool;
    fn point_bot_interfaces__action__Perception_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Perception_Feedback>);
    fn point_bot_interfaces__action__Perception_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Perception_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<Perception_Feedback>) -> bool;
}

// Corresponds to point_bot_interfaces__action__Perception_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Perception_Feedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for Perception_Feedback {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__Perception_Feedback__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__Perception_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Perception_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Perception_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Perception_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/Perception_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_Feedback() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__Perception_FeedbackMessage__init(msg: *mut Perception_FeedbackMessage) -> bool;
    fn point_bot_interfaces__action__Perception_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Perception_FeedbackMessage>, size: usize) -> bool;
    fn point_bot_interfaces__action__Perception_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Perception_FeedbackMessage>);
    fn point_bot_interfaces__action__Perception_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Perception_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<Perception_FeedbackMessage>) -> bool;
}

// Corresponds to point_bot_interfaces__action__Perception_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Perception_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::Perception_Feedback,

}



impl Default for Perception_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__Perception_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__Perception_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Perception_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Perception_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Perception_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/Perception_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_FeedbackMessage() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_Goal() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__MoveObject_Goal__init(msg: *mut MoveObject_Goal) -> bool;
    fn point_bot_interfaces__action__MoveObject_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Goal>, size: usize) -> bool;
    fn point_bot_interfaces__action__MoveObject_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Goal>);
    fn point_bot_interfaces__action__MoveObject_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveObject_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Goal>) -> bool;
}

// Corresponds to point_bot_interfaces__action__MoveObject_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveObject_Goal {

    // This member is not documented.
    #[allow(missing_docs)]
    pub object: geometry_msgs::msg::rmw::PoseStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: geometry_msgs::msg::rmw::PoseStamped,

}



impl Default for MoveObject_Goal {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__MoveObject_Goal__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__MoveObject_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveObject_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveObject_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveObject_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/MoveObject_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_Goal() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_Result() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__MoveObject_Result__init(msg: *mut MoveObject_Result) -> bool;
    fn point_bot_interfaces__action__MoveObject_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Result>, size: usize) -> bool;
    fn point_bot_interfaces__action__MoveObject_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Result>);
    fn point_bot_interfaces__action__MoveObject_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveObject_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Result>) -> bool;
}

// Corresponds to point_bot_interfaces__action__MoveObject_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveObject_Result {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for MoveObject_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__MoveObject_Result__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__MoveObject_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveObject_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveObject_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveObject_Result where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/MoveObject_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_Result() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__MoveObject_Feedback__init(msg: *mut MoveObject_Feedback) -> bool;
    fn point_bot_interfaces__action__MoveObject_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Feedback>, size: usize) -> bool;
    fn point_bot_interfaces__action__MoveObject_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Feedback>);
    fn point_bot_interfaces__action__MoveObject_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveObject_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveObject_Feedback>) -> bool;
}

// Corresponds to point_bot_interfaces__action__MoveObject_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveObject_Feedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for MoveObject_Feedback {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__MoveObject_Feedback__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__MoveObject_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveObject_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveObject_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveObject_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/MoveObject_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_Feedback() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__MoveObject_FeedbackMessage__init(msg: *mut MoveObject_FeedbackMessage) -> bool;
    fn point_bot_interfaces__action__MoveObject_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_FeedbackMessage>, size: usize) -> bool;
    fn point_bot_interfaces__action__MoveObject_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_FeedbackMessage>);
    fn point_bot_interfaces__action__MoveObject_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveObject_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveObject_FeedbackMessage>) -> bool;
}

// Corresponds to point_bot_interfaces__action__MoveObject_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveObject_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::MoveObject_Feedback,

}



impl Default for MoveObject_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__MoveObject_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__MoveObject_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveObject_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveObject_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveObject_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/MoveObject_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_FeedbackMessage() }
  }
}




#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__Perception_SendGoal_Request__init(msg: *mut Perception_SendGoal_Request) -> bool;
    fn point_bot_interfaces__action__Perception_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Perception_SendGoal_Request>, size: usize) -> bool;
    fn point_bot_interfaces__action__Perception_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Perception_SendGoal_Request>);
    fn point_bot_interfaces__action__Perception_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Perception_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<Perception_SendGoal_Request>) -> bool;
}

// Corresponds to point_bot_interfaces__action__Perception_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Perception_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::Perception_Goal,

}



impl Default for Perception_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__Perception_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__Perception_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Perception_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Perception_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Perception_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/Perception_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_SendGoal_Request() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__Perception_SendGoal_Response__init(msg: *mut Perception_SendGoal_Response) -> bool;
    fn point_bot_interfaces__action__Perception_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Perception_SendGoal_Response>, size: usize) -> bool;
    fn point_bot_interfaces__action__Perception_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Perception_SendGoal_Response>);
    fn point_bot_interfaces__action__Perception_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Perception_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<Perception_SendGoal_Response>) -> bool;
}

// Corresponds to point_bot_interfaces__action__Perception_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Perception_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for Perception_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__Perception_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__Perception_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Perception_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Perception_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Perception_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/Perception_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_SendGoal_Response() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__Perception_GetResult_Request__init(msg: *mut Perception_GetResult_Request) -> bool;
    fn point_bot_interfaces__action__Perception_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Perception_GetResult_Request>, size: usize) -> bool;
    fn point_bot_interfaces__action__Perception_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Perception_GetResult_Request>);
    fn point_bot_interfaces__action__Perception_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Perception_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<Perception_GetResult_Request>) -> bool;
}

// Corresponds to point_bot_interfaces__action__Perception_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Perception_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for Perception_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__Perception_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__Perception_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Perception_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Perception_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Perception_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/Perception_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_GetResult_Request() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__Perception_GetResult_Response__init(msg: *mut Perception_GetResult_Response) -> bool;
    fn point_bot_interfaces__action__Perception_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Perception_GetResult_Response>, size: usize) -> bool;
    fn point_bot_interfaces__action__Perception_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Perception_GetResult_Response>);
    fn point_bot_interfaces__action__Perception_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Perception_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<Perception_GetResult_Response>) -> bool;
}

// Corresponds to point_bot_interfaces__action__Perception_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Perception_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::Perception_Result,

}



impl Default for Perception_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__Perception_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__Perception_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Perception_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__Perception_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Perception_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Perception_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/Perception_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__Perception_GetResult_Response() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__MoveObject_SendGoal_Request__init(msg: *mut MoveObject_SendGoal_Request) -> bool;
    fn point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_SendGoal_Request>, size: usize) -> bool;
    fn point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_SendGoal_Request>);
    fn point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveObject_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveObject_SendGoal_Request>) -> bool;
}

// Corresponds to point_bot_interfaces__action__MoveObject_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveObject_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::MoveObject_Goal,

}



impl Default for MoveObject_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__MoveObject_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__MoveObject_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveObject_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveObject_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveObject_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/MoveObject_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_SendGoal_Request() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__MoveObject_SendGoal_Response__init(msg: *mut MoveObject_SendGoal_Response) -> bool;
    fn point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_SendGoal_Response>, size: usize) -> bool;
    fn point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_SendGoal_Response>);
    fn point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveObject_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveObject_SendGoal_Response>) -> bool;
}

// Corresponds to point_bot_interfaces__action__MoveObject_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveObject_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for MoveObject_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__MoveObject_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__MoveObject_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveObject_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveObject_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveObject_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/MoveObject_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_SendGoal_Response() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__MoveObject_GetResult_Request__init(msg: *mut MoveObject_GetResult_Request) -> bool;
    fn point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_GetResult_Request>, size: usize) -> bool;
    fn point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_GetResult_Request>);
    fn point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveObject_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveObject_GetResult_Request>) -> bool;
}

// Corresponds to point_bot_interfaces__action__MoveObject_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveObject_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for MoveObject_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__MoveObject_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__MoveObject_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveObject_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveObject_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveObject_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/MoveObject_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_GetResult_Request() }
  }
}


#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "point_bot_interfaces__rosidl_generator_c")]
extern "C" {
    fn point_bot_interfaces__action__MoveObject_GetResult_Response__init(msg: *mut MoveObject_GetResult_Response) -> bool;
    fn point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_GetResult_Response>, size: usize) -> bool;
    fn point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveObject_GetResult_Response>);
    fn point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveObject_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveObject_GetResult_Response>) -> bool;
}

// Corresponds to point_bot_interfaces__action__MoveObject_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveObject_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::MoveObject_Result,

}



impl Default for MoveObject_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !point_bot_interfaces__action__MoveObject_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to point_bot_interfaces__action__MoveObject_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveObject_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { point_bot_interfaces__action__MoveObject_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveObject_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveObject_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "point_bot_interfaces/action/MoveObject_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__point_bot_interfaces__action__MoveObject_GetResult_Response() }
  }
}






#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__point_bot_interfaces__action__Perception_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to point_bot_interfaces__action__Perception_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct Perception_SendGoal;

impl rosidl_runtime_rs::Service for Perception_SendGoal {
    type Request = Perception_SendGoal_Request;
    type Response = Perception_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__point_bot_interfaces__action__Perception_SendGoal() }
    }
}




#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__point_bot_interfaces__action__Perception_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to point_bot_interfaces__action__Perception_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct Perception_GetResult;

impl rosidl_runtime_rs::Service for Perception_GetResult {
    type Request = Perception_GetResult_Request;
    type Response = Perception_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__point_bot_interfaces__action__Perception_GetResult() }
    }
}




#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__point_bot_interfaces__action__MoveObject_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to point_bot_interfaces__action__MoveObject_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct MoveObject_SendGoal;

impl rosidl_runtime_rs::Service for MoveObject_SendGoal {
    type Request = MoveObject_SendGoal_Request;
    type Response = MoveObject_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__point_bot_interfaces__action__MoveObject_SendGoal() }
    }
}




#[link(name = "point_bot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__point_bot_interfaces__action__MoveObject_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to point_bot_interfaces__action__MoveObject_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct MoveObject_GetResult;

impl rosidl_runtime_rs::Service for MoveObject_GetResult {
    type Request = MoveObject_GetResult_Request;
    type Response = MoveObject_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__point_bot_interfaces__action__MoveObject_GetResult() }
    }
}


