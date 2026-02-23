# Autonomous Solana RPC Agent - Part of ULA Solana Agent Forge
# Queries Solana devnet, gets latest blockhash, simulates a tx - 100% no human code

from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts
import time

def run_solana_agent():
    print("ULA Solana Agent Forge - Autonomous RPC Agent Starting")
    print("Connecting to Solana Devnet...")
    
    client = Client("https://api.devnet.solana.com")
    
    if not client.is_connected():
        print("Connection failed - check network")
        return
    
    print("Connected successfully!")
    
    # Get latest blockhash (real on-chain data)
    blockhash_resp = client.get_latest_blockhash()
    blockhash = blockhash_resp.value.blockhash
    print(f"Latest Blockhash: {blockhash}")
    
    # Get recent performance samples (TPS-like metric)
    perf_samples = client.get_recent_performance_samples(5)
    print("Recent Performance Samples:")
    for sample in perf_samples.value:
        print(f"  Slot {sample.slot}: {sample.num_transactions} txs")
    
    # Simulate agent decision: "Should deploy now?"
    if len(perf_samples.value) > 0 and perf_samples.value[0].num_transactions > 100:
        print("Network healthy - agent decides: READY TO DEPLOY")
    else:
        print("Network load low - agent waits")
    
    print("Agent cycle complete. Sleeping 10s for next loop...")
    time.sleep(10)
    # In real agent: loop forever

if __name__ == "__main__":
    run_solana_agent()
