#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to btcpp_ros2_interfaces__msg__NodeStatus
/// NodeStatus Enums

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::NodeStatus::default())
  }
}

impl rosidl_runtime_rs::Message for NodeStatus {
  type RmwMsg = super::msg::rmw::NodeStatus;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        status: msg.status,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      status: msg.status,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      status: msg.status,
    }
  }
}


