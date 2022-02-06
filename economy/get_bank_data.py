async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users
