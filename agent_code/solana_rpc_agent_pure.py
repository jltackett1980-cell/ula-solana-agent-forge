# Pure-Python Solana RPC Agent Demo - No native dependencies
# Autonomous agent queries Solana devnet via JSON-RPC using urllib only

import json
import urllib.request
import time

RPC_URL = "https://api.devnet.solana.com"

def rpc_call(method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or []
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(RPC_URL, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        return {"error": str(e)}

def run_solana_agent():
    print("ULA Solana Agent Forge - Pure Python RPC Agent Starting")
    print("Querying Solana Devnet via public RPC...")

    # Get latest blockhash
    bh_resp = rpc_call("getLatestBlockhash")
    if "error" in bh_resp:
        print(f"Error fetching blockhash: {bh_resp['error']}")
        return
    blockhash = bh_resp['result']['value']['blockhash']
    print(f"Latest Blockhash: {blockhash}")

    # Get recent performance samples
    perf_resp = rpc_call("getRecentPerformanceSamples", [5])
    if "error" in perf_resp:
        print(f"Error fetching performance: {perf_resp['error']}")
        return
    samples = perf_resp['result']
    print("Recent Performance Samples:")
    for s in samples:
        print(f"  Slot {s['slot']}: {s['numTransactions']} txs")

    # Simple autonomous decision
    if samples and samples[0]['numTransactions'] > 100:
        print("Network healthy - agent decides: READY TO DEPLOY")
    else:
        print("Network load low - agent waits")

    print("Agent cycle complete. Sleeping 10s for next loop...")
    time.sleep(10)

if __name__ == "__main__":
    run_solana_agent()
