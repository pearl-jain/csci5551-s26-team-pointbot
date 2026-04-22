#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__msg__NodeStatus() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__msg__NodeStatus__init(msg: *mut NodeStatus) -> bool;
    fn btcpp_ros2_interfaces__msg__NodeStatus__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NodeStatus>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__msg__NodeStatus__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NodeStatus>);
    fn btcpp_ros2_interfaces__msg__NodeStatus__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NodeStatus>, out_seq: *mut rosidl_runtime_rs::Sequence<NodeStatus>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__msg__NodeStatus
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// NodeStatus Enums

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NodeStatus {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: u8,

}

impl NodeStatus {

    // This constant is not documented.
    #[allow(missing_docs)]
    pub const IDLE: u8 = 0;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const RUNNING: u8 = 1;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const SUCCESS: u8 = 2;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const FAILURE: u8 = 3;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const SKIPPED: u8 = 4;

}


impl Default for NodeStatus {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__msg__NodeStatus__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__msg__NodeStatus__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NodeStatus {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__msg__NodeStatus__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__msg__NodeStatus__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__msg__NodeStatus__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NodeStatus {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NodeStatus where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/msg/NodeStatus";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__msg__NodeStatus() }
  }
}


