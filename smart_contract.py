from boa.blockchain.vm.Neo.Runtime import Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification

from boa.blockchain.vm.Neo.TransactionType import InvocationTransaction
from boa.blockchain.vm.Neo.Transaction import *

from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete



##  scp -i NEO.pem /Users/Admin/Documents/NEO/smart_contract.py ubuntu@ec2-18-144-41-130.us-west-1.compute.amazonaws.com:/home/ubuntu/neo-python/contrac

## docker cp smart_contract.py neo-privatenet:/neo-python/contracts/smart_contract.py

def Main(operation, batch_key, batch_value):
    OWNER =b'031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf4a'
    
    
    context = GetContext()

    #Verify that the invoker in owner and able to store
    if CheckWitness(OWNER):

        if operation == 'store_batch':
            ##Check that item is not already stored
            item_value = Get(context, batch_key)
    
            #Item is already stored
            if len(item_value) == 0:
                return 0

            Put(context, batch_key, batch_value)
            return batch_key


        if operation == 'add_vaild_address':
            key_store = 'address_index'
            address_index = Get(context, key_store)

            ##Store new valid address and update address_index
            Put(context, address_index, batch_value)
            key_store = 'address_index'
            Put(context, key_store, address_index+1)
            return batch_value


## NON_OWNER ACCESS
            
    ##This can be used by other start contracts for retrieval and usage of data    
    if operation == 'retrieve_batch':
        batch_value = Get(context, batch_key)

        if len(batch_value) == 0:
            return 0

        return batch_value


    ##This is a expensive operation try to minimize usage
    if operation == 'verify_address':
        key_store = 'address_index'
        address_index = Get(context, key_store)

        for i in range(address_index):
            address = Get(context, i)
            if address == batch_key:
                return True

        return False






                    

        