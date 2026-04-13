#include <memory>
#include <ament_index_cpp/get_package_share_directory.hpp>
#include "rclcpp/rclcpp.hpp"

#include "behaviortree_cpp/bt_factory.h"
#include "control/log_node.hpp"

class ControlTreeNode : public rclcpp::Node {
public:
    ControlTreeNode(const std::string & node_name) : Node(node_name) {
        BT::BehaviorTreeFactory factory;
        factory.registerNodeType<LogString>("LogString");

        // Load behavior tree from Groot2
        std::string package_share_directory = ament_index_cpp::get_package_share_directory("control");
        std::string behavior_tree_path = package_share_directory + "/point_bot_tree.btproj";
        tree = factory.createTreeFromFile(behavior_tree_path);

        tree.tickWhileRunning();
    }

private:
    BT::Tree tree;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<ControlTreeNode>("Control_Tree_Node"));
    rclcpp::shutdown();

    return 0;
}