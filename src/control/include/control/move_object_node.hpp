#include "behaviortree_ros2/plugins.hpp"
#include "behaviortree_ros2/bt_action_node.hpp"

#include "rclcpp/rclcpp.hpp"
#include "point_bot_interfaces/action/move_object.hpp"
#include "geometry_msgs/msg/pose_stamped.hpp"


class MoveObjectAction : public BT::RosActionNode<point_bot_interfaces::action::MoveObject> {
public:
    MoveObjectAction(const std::string& name, const BT::NodeConfiguration& config, const BT::RosNodeParams& params) 
    : BT::RosActionNode<point_bot_interfaces::action::MoveObject>(name, config, params) {}

    static BT::PortsList providedPorts() {
        return {
            BT::InputPort<geometry_msgs::msg::PoseStamped>("object_pose"),
            BT::InputPort<geometry_msgs::msg::PoseStamped>("goal_pose")
        };
    }
    
    bool setGoal(Goal& goal) override {
        getInput("object_pose", goal.object);
        getInput("goal_pose", goal.goal);

        return true;
    }

    BT::NodeStatus onResultReceived(const WrappedResult& res) override {
        return res.result->success ? BT::NodeStatus::SUCCESS : BT::NodeStatus::FAILURE;
    }
private:
    rclcpp::Node::SharedPtr node;
};