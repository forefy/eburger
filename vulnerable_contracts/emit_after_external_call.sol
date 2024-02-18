// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

contract MistakenContract {
    UnexpectedInteractorContract public unexpectedInteractorContract; // Reference to an external contract
    uint256 public amountToTransfer;    // Amount intended for transfer; vulnerable to manipulation
    event Transfer(uint256 amount);     // Event to log the amount intended for transfer

    // Function to set the address of the external contract
    function addOtherContract(address _unexpectedInteractorContract) public {
        unexpectedInteractorContract = UnexpectedInteractorContract(_unexpectedInteractorContract);
    }

    // Function to update the amount intended for transfer
    // Vulnerable as any external caller can manipulate this value
    function updateAmountToTransfer(uint256 newAmount) public {
        amountToTransfer = newAmount;
    }

    // The emitted event can mislead to think 'amountToTransfer' was transferred, not 'msg.value'
    function transferMoneyFromBridge() public payable {
        amountToTransfer = msg.value; // or does it??

        /*
            Commented line below demonstrates a mitigated situation, where the state variable is copied to a
            local memory variable, preventing manipulation from external calls prior to the emit.
            amountToTransfer still remains untrusted, but we can use emit amountToTransferLocal instead.
        */         
        // uint256 amountToTransferLocal = amountToTransfer;
        
        unexpectedInteractorContract.doChores();


        /*
            Now when amountToTransfer is emitted with the state variable, it creates a risky area within the
            codebase that can lead developers to think/rely upon the fact that amountToTransfer represents msg.value.
            This might be true, but due to the external call to UnexpectedInteractorContract we can no longer
            trust that amountToTransfer wasn't manipulated.
        */
        emit Transfer(amountToTransfer);

    }
}

// External contract that can manipulate the state of MistakenContract
contract UnexpectedInteractorContract {
    MistakenContract public mistakenContract;

    constructor(address _mistakenContract) {
        mistakenContract = MistakenContract(_mistakenContract);
    }

    function doChores() public payable {
        // ..

        // Manipulate the amountToTransfer on the MistakenContract
        mistakenContract.updateAmountToTransfer(type(uint256).max);

        // ..
    }
}
