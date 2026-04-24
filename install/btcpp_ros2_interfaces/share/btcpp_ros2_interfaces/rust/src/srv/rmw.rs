#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__srv__GetTrees_Request() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__srv__GetTrees_Request__init(msg: *mut GetTrees_Request) -> bool;
    fn btcpp_ros2_interfaces__srv__GetTrees_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetTrees_Request>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__srv__GetTrees_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetTrees_Request>);
    fn btcpp_ros2_interfaces__srv__GetTrees_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetTrees_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GetTrees_Request>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__srv__GetTrees_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetTrees_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetTrees_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__srv__GetTrees_Request__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__srv__GetTrees_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetTrees_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__srv__GetTrees_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__srv__GetTrees_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__srv__GetTrees_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetTrees_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetTrees_Request where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/srv/GetTrees_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__srv__GetTrees_Request() }
  }
}


#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__srv__GetTrees_Response() -> *const std::ffi::c_void;
}

#[link(name = "btcpp_ros2_interfaces__rosidl_generator_c")]
extern "C" {
    fn btcpp_ros2_interfaces__srv__GetTrees_Response__init(msg: *mut GetTrees_Response) -> bool;
    fn btcpp_ros2_interfaces__srv__GetTrees_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetTrees_Response>, size: usize) -> bool;
    fn btcpp_ros2_interfaces__srv__GetTrees_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetTrees_Response>);
    fn btcpp_ros2_interfaces__srv__GetTrees_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetTrees_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GetTrees_Response>) -> bool;
}

// Corresponds to btcpp_ros2_interfaces__srv__GetTrees_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetTrees_Response {
    /// Ids of the available trees
    pub tree_ids: rosidl_runtime_rs::Sequence<rosidl_runtime_rs::String>,

}



impl Default for GetTrees_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !btcpp_ros2_interfaces__srv__GetTrees_Response__init(&mut msg as *mut _) {
        panic!("Call to btcpp_ros2_interfaces__srv__GetTrees_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetTrees_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__srv__GetTrees_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__srv__GetTrees_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { btcpp_ros2_interfaces__srv__GetTrees_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetTrees_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetTrees_Response where Self: Sized {
  const TYPE_NAME: &'static str = "btcpp_ros2_interfaces/srv/GetTrees_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__btcpp_ros2_interfaces__srv__GetTrees_Response() }
  }
}






#[link(name = "btcpp_ros2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__srv__GetTrees() -> *const std::ffi::c_void;
}

// Corresponds to btcpp_ros2_interfaces__srv__GetTrees
#[allow(missing_docs, non_camel_case_types)]
pub struct GetTrees;

impl rosidl_runtime_rs::Service for GetTrees {
    type Request = GetTrees_Request;
    type Response = GetTrees_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__btcpp_ros2_interfaces__srv__GetTrees() }
    }
}


