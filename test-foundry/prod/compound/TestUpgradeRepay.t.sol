// SPDX-License-Identifier: GNU AGPLv3
pragma solidity ^0.8.0;

import "./TestRepay.t.sol";

contract TestUpgradeRepay is TestRepay {
    function _beforeEach() internal override {
        _upgrade();
    }
}
