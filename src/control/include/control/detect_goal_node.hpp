#include "behaviortree_ros2/plugins.hpp"
#include "behaviortree_ros2/bt_action_node.hpp"

#include "rclcpp/rclcpp.hpp"
#include "point_bot_interfaces/action/perception.hpp"
#include "geometry_msgs/msg/pose_stamped.hpp"

class DetectGoalAction : public BT::RosActionNode<point_bot_interfaces::action::Perception> {
public:
    DetectGoalAction(const std::string& name, const BT::NodeConfiguration& config, const BT::RosNodeParams& params) 
    : BT::RosActionNode<point_bot_interfaces::action::Perception>(name, config, params) {}

    static BT::PortsList providedPorts() {
        return providedBasicPorts({
            BT::OutputPort<geometry_msgs::msg::PoseStamped>("goal_pose"),
        });
    }
    
    bool setGoal(Goal& goal) override {
        goal.task = "detect_goal";
        return true;
    }

    BT::NodeStatus onResultReceived(const WrappedResult& res) override {
        auto node_ptr = node_.lock();
        if (node_ptr) {
            if (res.code != rclcpp_action::ResultCode::SUCCEEDED || !res.result->success) {
                RCLCPP_WARN(node_ptr->get_logger(), "[%s]: Goal perception failed.", name().c_str());
                return BT::NodeStatus::FAILURE;
            }

            setOutput("goal_pose", res.result->pose);
            
            RCLCPP_INFO(node_ptr->get_logger(), "[%s]: Goal detected successfully.", name().c_str());
        }

        return BT::NodeStatus::SUCCESS;
    }
};