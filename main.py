from rpc_client import get_block, determine_slot_range
from parser import parse_transactions
from writer import write_to_csv
import time
START_SLOT, END_SLOT = determine_slot_range()



def main():
    all_records = []
    for slot in range(START_SLOT, END_SLOT):
        block = get_block(slot)
        if block and 'transactions' in block:
            parsed = parse_transactions(slot, block['transactions'])
            all_records.extend(parsed)
        time.sleep(3)
    print(all_records)
    if all_records:
        write_to_csv(all_records, "solana_transactions.csv")

if __name__ == "__main__":
    main()