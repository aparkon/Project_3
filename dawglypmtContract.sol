/ SPDX-License-Identifier: MIT

// SPDX-License-Identifier: Something Else


pragma solidity ^0.5.7;

contract paymentContract {
    address owner;
    uint pmtAmount;
    bool successfullWlk;

    constructor() payable public {
        owner = msg.sender; // msg sender represents address being called
        pmtAmount = msg.value; //msg value tells us how much ether is being sent 
        successfullWlk = false; 
    }

    // create modifier so the only person who can call the contract is the owner
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    // only allocate once the service has been succesfull.

    modifier walkSuccessfullpmt {
        require(successfullWlk == true);
        _;
    }    

    // list of Dog walker wallers
    address payable[] walkerWallets;

    // map through inheritance
    mapping(address => uint) pmtamountHold;

    //set payment for each Dog walker address

    function setPayment(address payable wallet, uint amount) public {
        walkerWallets.push(wallet);
        pmtamountHold[wallet] = amount;
    }    

    // set the payout for each address 
    function payout() private walkSuccessfullpmt {
        for(uint i=0; i<walkerWallets.length; i++) {
            walkerWallets[i].transfer(pmtamountHold[walkerWallets[i]]);
            // transferring funds from contract address to reciever address
        }
    }

    // oracle switch simulation
    function walkSuccessfull() payable public onlyOwner {
        successfullWlk = true;
        payout();
    }
}


