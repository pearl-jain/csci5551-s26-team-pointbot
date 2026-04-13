#include "behaviortree_cpp/action_node.h"
#include "rclcpp/rclcpp.hpp"

#include "geometry_msgs/msg/pose_stamped.hpp"

class DetectGoal : public BT::SyncActionNode {
public:
    DetectGoal(const std::string& name, const BT::NodeConfiguration& config, rclcpp::Logger node_logger)
    : BT::SyncActionNode(name, config), logger(node_logger) {
        std::srand(std::time(0));
    }

    static BT::PortsList providedPorts() {
        return {BT::OutputPort<geometry_msgs::msg::PoseStamped>("goal_pose")};
    }

    BT::NodeStatus tick() override {
        RCLCPP_INFO(logger, "Detect Goal: Running");
        std::this_thread::sleep_for(std::chrono::seconds(1));
        
        int result = std::rand() % 100 + 1;
        if (result > 50) {
            auto pose_goal = geometry_msgs::msg::PoseStamped();
            pose_goal.header.frame_id = "panda_link0";
            pose_goal.pose.orientation.w = 1.0;
            pose_goal.pose.position.x = 0.28;
            pose_goal.pose.position.y = -0.2;
            pose_goal.pose.position.z = 0.5;

            setOutput("goal_pose", pose_goal);
            
            return BT::NodeStatus::SUCCESS;
        }

        return BT::NodeStatus::FAILURE;
    }
private:
    rclcpp::Logger logger;
};