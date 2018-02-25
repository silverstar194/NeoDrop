"""
Importing:

neo> import contract sc/3-domain.avm 0710 05 True False
neo> contract search ...

a7374f701bac9c905157bfa368eb674bc218e0a9
neo> testinvoke a7374f701bac9c905157bfa368eb674bc218e0a9 storeblock ["testblockhere", "IDOFBLOCK"]
neo> testinvoke a7374f701bac9c905157bfa368eb674bc218e0a9 retrieveblock ["IDOFBLOCK""]
neo> testinvoke a7374f701bac9c905157bfa368eb674bc218e0a9 storeaddresslist ["test_list", "org_name"]
neo> testinvoke a7374f701bac9c905157bfa368eb674bc218e0a9 storetracking ["tracking", "tracking_block_id"]
neo> testinvoke a7374f701bac9c905157bfa368eb674bc218e0a9 retrievetracking ["tracking_block_id"]
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify
from boa.blockchain.vm.Neo.Runtime import CheckWitness
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.code.builtins import concat



def Main(operation, args):
    owner = b'02b01c489f71b4470e480f53f507ca76aa132d6b1000c20f01141e766f6e186801'
    nargs = len(args)
    if nargs == 0:
        print("No Arguments Supplied.. Opps")
        return 0

    if operation == 'storeblock':
        block = args[0]
        block_id = args[1]
        return StorageBlock(block, block_id, owner)

    if operation == 'retrieveblock':
        block_id = args[0]
        return RetrieveBlock(block_id)

    if operation == 'storeaddresslist':
        addr_list = args[0]
        organization_name = args[1]
        return StoreAddressList(addr_list, organization_name, owner)

    if operation == 'retrieveaddresslist':
        organization_name = args[0]
        return RetrieveAddressList(organization_name)


    if operation == 'storetracking':
        tracking = args[0]
        block_id_tracking= args[1]
        return StoreTracking(block_id_tracking, tracking, owner)

    if operation == 'retrievetracking':
        block_id_tracking = args[0]
        return RetrieveTracking(block_id_tracking)




def StorageBlock(block, block_id, owner):
    msg = concat("Block Storage: ", block_id)
    Notify(msg)

    if not CheckWitness(owner):
        Notify("Only Owner is able to store a block")
        return False

    context = GetContext()
    exists = Get(context, block_id)
    if exists:
        Notify("Block Already Stored")
        return False

    Put(context, block_id, block)
    return True


def RetrieveBlock(block_id):
    msg = concat("Retrieving Block: ", block_id)
    Notify(msg)

    context = GetContext()
    block = Get(context, block_id)
    if not block:
        Notify("No Block with given ID")
        return False

    Notify(block)
    return block



def StoreAddressList(addr_list, organization_name, owner):
    msg = "Storing Address List: "
    Notify(msg)

    if not CheckWitness(owner):
        Notify("Only Owner is able to store and update address")
        return False

    context = GetContext()
    exists = Get(context, organization_name)
    if exists:
        Notify("Organization has same name. Please add version number")
        return False

    Put(context, organization_name, addr_list)
    return True

def RetrieveAddressList(organization_name):
    msg = concat("Retrieving Address List: ", organization_name)
    Notify(msg)

    context = GetContext()
    list_addr = Get(context, organization_name)
    if not list_addr:
        Notify("No Addresses Stored")
        return False

    Notify(list_addr)
    return list_addr

def StoreTracking(block_id_tracking, tracking, owner):
    msg = "Storing Tracking Number: "
    Notify(msg)

    if not CheckWitness(owner):
        Notify("Only Owner is able to store and update tracking")
        return False

    context = GetContext()
    exists = Get(context, block_id_tracking)
    if exists:
        Notify("Organization has already added tracking for this block.")
        return False

    Put(context, block_id_tracking, tracking)
    return True

def RetrieveTracking(block_id_tracking):
    msg = concat("Retrieving Tracking Number for Block: ", block_id_tracking)
    Notify(msg)

    context = GetContext()
    tracking = Get(context, block_id_tracking)
    if not tracking:
        Notify("No Tracking Stored for Block")
        return False

    Notify(tracking)
    return tracking




