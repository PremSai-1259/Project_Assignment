// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

contract VPN {
    string greeting;
    uint nodeCount;
    address deployer;

    constructor() {
        deployer = msg.sender;
    }

    function setGreeting(string memory greetingmsg) public {
        greeting = greetingmsg;
    }

    function getGreeting() public view returns (string memory) {
        return greeting;
    }

    function setNodeCount(uint count) public {
        nodeCount = count;
    }

    function getNodeCount() public view returns (uint) {
        return nodeCount;
    }

    function getDeployerAddress() public view returns (address) {
        return deployer;
    }
}
