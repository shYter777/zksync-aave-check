
# ZkSync Token Balance Monitor

This Python script connects to the ZkSync Era network and continuously monitors the balance of a specific token contract on the ZkSync blockchain. It checks the balance of the given contract every 60 seconds and displays only the first 9 digits of the token balance.

## Features

- Connects to ZkSync Era using an RPC provider.
- Monitors the balance of a specified token contract (e.g., the ZK token contract).
- Displays only the first 9 digits of the token balance for easy readability.
- Runs in an infinite loop and checks the balance every 60 seconds.

## Requirements

- Python 3.x
- `web3` library for interacting with the Ethereum-compatible blockchain (ZkSync Era).
  
To install the necessary dependencies, use the following command:

```bash
pip install web3
```

## How to Use

1. **Get the Contract Address**:  
   First, obtain the contract address for the ZK token or any other token you want to monitor on ZkSync. You can find this on the ZkSync Explorer.

2. **Edit the Script**:  
   In the script, replace the placeholder `"0xYourTokenContractAddressHere"` with the actual address of the token contract.

   Also, specify the contract address you want to monitor for the token balance in the `PROXY_CONTRACT_ADDRESS` variable.

   Example:

   ```python
   ZK_TOKEN_CONTRACT = "0xYourTokenContractAddressHere"  # Replace with the actual token contract address
   PROXY_CONTRACT_ADDRESS = "0xd6cD2c0fC55936498726CacC497832052A9B2D1B"  # Replace with the address of the contract you're monitoring
   ```

3. **Run the Script**:  
   After setting the correct contract addresses, run the script using Python:

   ```bash
   python monitor_balance.py
   ```

   The script will connect to the ZkSync network and start displaying the balance of the specified contract. The balance will be updated every 60 seconds and only the first 9 digits will be shown.

## Example Output

Once the script is running, the output will look like this:

```
Balance of contract 0xd6cD2c0fC55936498726CacC497832052A9B2D1B: 140066552
```

The balance is updated every minute, showing only the first 9 digits for simplicity.

## Error Handling

- If the connection to ZkSync Era fails, the script will print an error message.
- If there are issues with fetching the balance, the script will display the relevant error message.

## Contributing

If you have any suggestions or improvements, feel free to submit a pull request or create an issue.

## License

This project is open source and available under the MIT License.

---
