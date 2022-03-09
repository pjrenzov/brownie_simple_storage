from brownie import SimpleStorage, accounts

def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    stored = simple_storage.retrieve()
    expected = 0
    assert stored == expected