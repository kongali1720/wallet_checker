import requests
from eth_account import Account

ETHERSCAN_API_KEY = "masukkan_api_key_anda_di_sini"

def generate_wallet():
    acct = Account.create()
    return acct.key.hex(), acct.address

def get_eth_balance(address):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": ETHERSCAN_API_KEY
    }
    response = requests.get(url, params=params)
    result = response.json()
    if result["status"] == "1":
        balance_eth = int(result["result"]) / (10 ** 18)
        return balance_eth
    else:
        return None

if __name__ == "__main__":
    print("🔐 Generating Wallet + Checking Balance...")
    private_key, address = generate_wallet()
    print(f"🧾 Private Key : {private_key}")
    print(f"📮 Address     : {address}")
    
    if ETHERSCAN_API_KEY == "masukkan_api_key_anda_di_sini":
        print("⚠️  Masukkan API key kamu dulu di script ini!")
    else:
        balance = get_eth_balance(address)
        if balance is not None:
            print(f"💰 Balance     : {balance:.18f} ETH")
        else:
            print("❌ Gagal cek saldo (cek koneksi/API key)")
