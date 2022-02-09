async def update_bank(user,change = 0,mode = "Wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", 'w') as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["Wallet"],users[str(user.id)]["Bank"]]
    return bal
