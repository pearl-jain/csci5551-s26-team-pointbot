#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to btcpp_ros2_interfaces__srv__GetTrees_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetTrees_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetTrees_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetTrees_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GetTrees_Request {
  type RmwMsg = super::srv::rmw::GetTrees_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
    }
  }
}


// Corresponds to btcpp_ros2_interfaces__srv__GetTrees_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetTrees_Response {
    /// Ids of the available trees
    pub tree_ids: Vec<std::string::String>,

}



impl Default for GetTrees_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetTrees_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GetTrees_Response {
  type RmwMsg = super::srv::rmw::GetTrees_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        tree_ids: msg.tree_ids
          .into_iter()
          .map(|elem| elem.as_str().into())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        tree_ids: msg.tree_ids
          .iter()
          .map(|elem| elem.as_str().into())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      tree_ids: msg.tree_ids
          .into_iter()
          .map(|elem| elem.to_string())
          .collect(),
    }
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


