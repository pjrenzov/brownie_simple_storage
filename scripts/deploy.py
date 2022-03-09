from brownie import accounts, SimpleStorage

def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    storage_value = simple_storage.retrieve()
    print(storage_value)
    transaction = simple_storage.store(15)
    transaction.wait(1)
    print(simple_storage.retrieve())

def main():
    deploy_simple_storage()