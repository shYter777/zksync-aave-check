from web3 import Web3
import time

# RPC-узел ZkSync Era
ZKSYNC_RPC = "https://mainnet.era.zksync.io"

# Адрес контракта токенов ZK (замените на актуальный адрес контракта)
ZK_TOKEN_CONTRACT = "0x5A7d6b2F92C77FAD6CCaBd7EE0624E64907Eaf3E"  # Замените на актуальный адрес

# ABI для стандарта ERC-20 (баланс токенов)
TOKEN_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

# Инициализация Web3
web3 = Web3(Web3.HTTPProvider(ZKSYNC_RPC))

# Проверка подключения
if web3.is_connected():
    print("Подключение установлено!")
else:
    print("Подключение не удалось.")

# Подключение к токен-контракту
zk_token_contract = web3.eth.contract(
    address=Web3.to_checksum_address(ZK_TOKEN_CONTRACT),
    abi=TOKEN_ABI
)

# Укажите адрес вашего контракта для проверки баланса
PROXY_CONTRACT_ADDRESS = "0xd6cD2c0fC55936498726CacC497832052A9B2D1B"  # Замените на адрес вашего контракта

# Функция для отображения первых 9 цифр баланса
def display_balance(balance):
    # Преобразуем баланс в строку, обрезаем на первые 9 цифр
    balance_str = str(balance)
    return balance_str[:9]

# Бесконечный цикл для проверки баланса каждую минуту
while True:
    try:
        # Получаем баланс контракта
        contract_balance = zk_token_contract.functions.balanceOf(
            Web3.to_checksum_address(PROXY_CONTRACT_ADDRESS)
        ).call()
        
        # Показываем только первые 9 цифр
        print(f"Balance of contract {PROXY_CONTRACT_ADDRESS}: {display_balance(contract_balance)}")
        
    except Exception as e:
        print(f"Ошибка вызова balanceOf: {e}")
    
    # Задержка 60 секунд перед следующей проверкой
    time.sleep(60)
