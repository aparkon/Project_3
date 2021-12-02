// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC1155/ERC1155.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC1155/extensions/ERC1155Burnable.sol";



contract DawglyToken is ERC1155, Ownable, ERC1155Burnable {
    constructor() ERC1155("") {}

    function setURI(string memory newuri) public onlyOwner {
        _setURI(newuri);
    }

    function mint( uint256 id, uint256 amount)
        public
        onlyOwner
    {
        _mint(msg.sender, id, amount,"");
    }

    function mintBatch(uint256[] memory ids, uint256[] memory amounts)
        public
        onlyOwner
    {
        _mintBatch(msg.sender, ids, amounts,"");
    }

    function withdraw() public onlyOwner{
        require(address(this).balance > 0, "Balance is 0");
        payable(owner()).transfer(address(this).balance);
    }

    function safeTransferFrom(address from, address to, uint256 id, uint256 amount)
        payable 
        public virtual {
        _safeTransferFrom(from, to, id, amount,"");
    }

    function safeBatchTransferFrom( address from, address to, uint256[] memory ids, uint256[] memory amounts) 
        payable
        public virtual {
        _safeBatchTransferFrom(from, to, ids, amounts,"");
    }

}
