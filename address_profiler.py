"""
Address Profiler — анализ активности Bitcoin-адреса.
"""

import requests
import argparse
from datetime import datetime

def fetch_address_profile(address):
    url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("❌ Ошибка при запросе к Blockchair API.")
    return r.json()["data"][address]

def profile_address(address):
    data = fetch_address_profile(address)
    meta = data["address"]
    txs = data["transactions"]

    print(f"📍 Address Profiler для: {address}")
    print(f"💰 Баланс: {meta['balance']} сатоши")
    print(f"🔄 Транзакций: {meta['transaction_count']}")
    print(f"📥 Получено всего: {meta['received']} сатоши")
    print(f"📤 Отправлено всего: {meta['spent']} сатоши")

    if txs:
        print(f"🕰️ Первая активность: блок {meta['first_seen_receiving_block']} ({txs[-1]})")
        print(f"⏱️ Последняя активность: блок {meta['last_seen_receiving_block']} ({txs[0]})")
    else:
        print("❗ Нет транзакционной активности.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Address Profiler — анализ активности адреса.")
    parser.add_argument("address", help="Bitcoin-адрес")
    args = parser.parse_args()
    profile_address(args.address)
