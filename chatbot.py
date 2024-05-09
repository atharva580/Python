def chat_bot_system():
    name = input("Enter Your Name: ")
    print(f"Hello {name}, Welcome to MET-Restaurant\n")
    print(f"What would you like to order, {name}?\n")

    menu_options = ["Rice-Plate", "Samosa", "Vada-Pava", "Chole-Bhature", "Pohe"]
    order_count = [0] * len(menu_options)

    while True:
        for i, option in enumerate(menu_options, start=1):
            print(f"Option {i}: {option}")

        opt = int(input("\nI would like to have option: "))
        if opt > len(menu_options):
            print("Display relevant query")
            continue

        print(f"\nYou Confirm order: {menu_options[opt - 1]}")
        order_count[opt - 1] += 1

        if order_count[opt - 1] >= 5:
            break

        order = input("Do you want anything else (yes/no): ").upper()
        print()

        if order == "YES":
            continue
        else:
            break

    your_order(menu_options, order_count)
    print(f"\nYour total bill is {total_bill(order_count)}")
    print("\nThanks for your order!")

def total_bill(order_count):
    total = 0
    prices = [50, 25, 25, 55, 25]

    for count, price in zip(order_count, prices):
        total += count * price

    return total

def your_order(menu_options, order_count):
    print("Your Order is:")
    for option, count in zip(menu_options, order_count):
        if count > 0:
            print(f"{option} {count}")

if __name__ == "__main__":
    chat_bot_system()
