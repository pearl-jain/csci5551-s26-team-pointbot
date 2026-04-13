#include "behaviortree_cpp/action_node.h"
#include "rclcpp/rclcpp.hpp"

class LogString : public BT::SyncActionNode {
public:
    LogString(const std::string& name, const BT::NodeConfiguration& config):
    BT::SyncActionNode(name, config) 
    {}

    static BT::PortsList providedPorts() {
        return {};
    }

    BT::NodeStatus tick() override {
        std::cout << "LogString: " << this->name() << std::endl;

        return BT::NodeStatus::SUCCESS;
    }
};