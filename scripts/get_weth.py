from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    get_weth()


def get_weth():
    """mints weth by depositing eth"""
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    # not using get contract as not deploying mocks and using config.
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 WETH")
    return tx
