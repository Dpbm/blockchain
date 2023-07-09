// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract JazzCoin is ERC20{
    constructor(uint256 initialSupply) ERC20("Jazz", "JZ") {
        _mint(msg.sender, initialSupply);
    }

    function _reward() internal {
        uint256 total = block.difficulty * 200;
        _mint(block.coinbase, total);
    }

    function _beforeTransaction(address to, address from, uint256 value) internal virtual override {
        if(!(from == address(0) && to == block.coinbase)){
            _reward();
        }
        
        super._beforeTransaction(to, from, value);
    }
}
