import requests
from config import RPC_ENDPOINT


def determine_slot_range(window_size=100):
    end_slot = get_current_slot()
    start_slot = max(0, end_slot - window_size)
    return start_slot, end_slot

def get_current_slot():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSlot",
        "params": []
    }
    resp = requests.post(RPC_ENDPOINT, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()["result"]

def get_block(slot):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBlock",
        "params": [slot, {"encoding": "json", "transactionDetails": "full"}]
    }
    try:
        response = requests.post(RPC_ENDPOINT, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json().get("result")
        return result
    except Exception as e:
        print(f"Error fetching block {slot}: {e}")
        return None