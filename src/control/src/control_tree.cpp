#include <memory>
#include <ament_index_cpp/get_package_share_directory.hpp>
#include "rclcpp/rclcpp.hpp"

#include "behaviortree_cpp/bt_factory.h"
#include "behaviortree_ros2/plugins.hpp"
#include "control/log_node.hpp"
#include "control/detect_object_node.hpp"
#include "control/detect_goal_node.hpp"
#include "control/move_object_node.hpp"

class ControlTreeNode : public rclcpp::Node {
public:
    ControlTreeNode(const std::string & node_name) 
    : Node(node_name) {
        // Create Timer
        timer = this->create_wall_timer(
            std::chrono::milliseconds(100),
            std::bind(&ControlTreeNode::behavior_tree_callback, this)
        );
    }

    void setup_tree() {
        // Setup Groot2 Behavior Tree
        BT::BehaviorTreeFactory factory;

        // Lambda functions tell the behavior tree how to make the node

        // Setup Log String Tree Node
        factory.registerBuilder<LogString>(
            "LogString",
            [this](const std::string& name, const BT::NodeConfiguration& config) { 
                return std::make_unique<LogString>(name, config, this->get_logger()); 
            }
        );

        // Setup Detect Object Action
        BT::RosNodeParams detect_object_params;
        detect_object_params.nh = shared_from_this();
        detect_object_params.default_port_value = "perception";
        factory.registerBuilder<DetectObjectAction>(
            "DetectObject",
            [detect_object_params](const std::string& name, const BT::NodeConfiguration& config) {
                return std::make_unique<DetectObjectAction>(name, config, detect_object_params);
            }
        );

        // Setup Detect Goal Action
        BT::RosNodeParams detect_goal_params;
        detect_goal_params.nh = shared_from_this();
        detect_goal_params.default_port_value = "perception";
        factory.registerBuilder<DetectGoalAction>(
            "DetectGoal",
            [detect_goal_params](const std::string& name, const BT::NodeConfiguration& config) {
                return std::make_unique<DetectGoalAction>(name, config, detect_goal_params);
            }
        );

        // Setup Move Object Action
        BT::RosNodeParams move_object_params;
        move_object_params.nh = shared_from_this();
        move_object_params.default_port_value = "move_object";
        factory.registerBuilder<MoveObjectAction>(
            "MoveObject",
            [move_object_params](const std::string& name, const BT::NodeConfiguration& config) {
                return std::make_unique<MoveObjectAction>(name, config, move_object_params);
            }
        );

        // Load behavior tree from Groot2
        std::string package_share_directory = ament_index_cpp::get_package_share_directory("control");
        std::string behavior_tree_path = package_share_directory + "/point_bot_tree.xml";
        tree = factory.createTreeFromFile(behavior_tree_path);
    }

private:
    void behavior_tree_callback() {
        // Control tree node logic with ros
        BT::NodeStatus status = tree.tickOnce();

        if (status == BT::NodeStatus::SUCCESS) {
            RCLCPP_INFO(this->get_logger(), "Tree Ended: SUCCESS");
            timer->cancel();
            rclcpp::shutdown();
        } else if (status == BT::NodeStatus::FAILURE) {
            RCLCPP_ERROR(this->get_logger(), "Tree Ended: FAILURE");
            timer->cancel();
            rclcpp::shutdown();
        }
    }

    BT::Tree tree;
    rclcpp::TimerBase::SharedPtr timer;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);

    auto node = std::make_shared<ControlTreeNode>("control_tree_node");

    node->setup_tree();

    rclcpp::spin(node);    
    rclcpp::shutdown();

    return 0;
}