def parse_transactions(slot, transactions):
    records = []
    for tx in transactions:
        try:
            signature = tx['transaction']['signatures'][0]
            fee = tx['meta'].get('fee')
            status = tx['meta'].get('err')
            accounts = tx['transaction']['message']['accountKeys']
            records.append({
                'slot': slot,
                'tx_hash': signature,
                'fee': fee,
                'status': status,
                'accounts': ','.join(accounts)
            })
        except Exception as e:
            print(f"Parse error in slot {slot}: {e}")
    return records