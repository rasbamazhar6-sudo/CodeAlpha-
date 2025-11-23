"""
===========================================================
                    STOCK PORTFOLIO TRACKER
===========================================================
DESCRIPTION:
    A professional-style portfolio tracker that lets users:
    
      • Add stocks and quantities
      • View real-time-like summary
      • See profit/loss status
      • Save portfolio as TXT or CSV

    Features:
      • Menu-driven system
      • Color-coded output
      • Clean, realistic formatting
===========================================================
"""

import csv

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

stock_data = {
    "AAPL": {"name": "Apple Inc.",       "price": 180, "cost": 170},
    "TSLA": {"name": "Tesla Motors",     "price": 250, "cost": 260},
    "GOOGL": {"name": "Alphabet Inc.",   "price": 140, "cost": 120},
    "AMZN": {"name": "Amazon",           "price": 130, "cost": 140},
    "MSFT": {"name": "Microsoft Corp.",  "price": 400, "cost": 390},
    "META": {"name": "Meta Platforms",   "price": 330, "cost": 310},
    "NVDA": {"name": "NVIDIA Corp.",     "price": 450, "cost": 420}
}

portfolio = {}

def show_available_stocks():
    print("\nAvailable Stocks:")
    print("-" * 55)
    print("{:<10} {:<20} {:<15}".format("SYMBOL", "COMPANY", "PRICE ($)"))
    print("-" * 55)

    for symbol, info in stock_data.items():
        print("{:<10} {:<20} {:<15}".format(symbol, info["name"], info["price"]))

    print("-" * 55)

def add_stock():
    while True:
        stock = input("\nEnter stock symbol (or type 'done'): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_data:
            print(f"{RED}[ERROR]{RESET} Invalid stock symbol!")
            continue

        try:
            qty = int(input("Enter quantity: "))
        except:
            print(f"{RED}[ERROR]{RESET} Quantity must be a number!")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"{GREEN}[SUCCESS]{RESET} Added {qty} shares of {stock}.")

def show_summary():
    if not portfolio:
        print(f"{YELLOW}\nYour portfolio is empty!{RESET}")
        return

    print("\n==========================================================")
    print("                        PORTFOLIO SUMMARY                  ")
    print("==========================================================")

    print("{:<10} {:<15} {:<10} {:<12} {:<15}".format(
        "STOCK", "COMPANY", "QTY", "PRICE($)", "P/L"
    ))
    print("-" * 65)

    grand_total = 0
    total_pl = 0

    for stock, qty in portfolio.items():
        info = stock_data[stock]
        price = info["price"]
        cost = info["cost"]

        investment = qty * price
        pl = (price - cost) * qty
        grand_total += investment
        total_pl += pl

        # Color for P/L
        pl_color = GREEN if pl >= 0 else RED

        print("{:<10} {:<15} {:<10} {:<12} {}${}{}".format(
            stock, info["name"][:14], qty, price, pl_color, pl, RESET
        ))

    print("-" * 65)
    print(f"{'TOTAL PORTFOLIO VALUE:':<25} ${grand_total}")

    if total_pl >= 0:
        print(f"{GREEN}TOTAL PROFIT: ${total_pl}{RESET}")
    else:
        print(f"{RED}TOTAL LOSS: ${total_pl}{RESET}")

    print("==========================================================\n")

def save_report():
    if not portfolio:
        print(f"{YELLOW}Portfolio is empty! Nothing to save.{RESET}")
        return

    print("\nSave Options:")
    print("1. Save as TXT")
    print("2. Save as CSV")
    print("3. Cancel")

    choice = input("Enter choice: ")

    if choice == "1":
        with open("portfolio_report.txt", "w") as file:
            file.write("STOCK | COMPANY | PRICE | QTY | P/L\n")
            file.write("-------------------------------------\n")

            for stock, qty in portfolio.items():
                data = stock_data[stock]
                pl = (data["price"] - data["cost"]) * qty

                file.write(
                    f"{stock} | {data['name']} | ${data['price']} | {qty} | ${pl}\n"
                )

        print(f"{GREEN}Saved as portfolio_report.txt{RESET}")

    elif choice == "2":
        with open("portfolio_report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Company", "Price", "Quantity", "P/L"])

            for stock, qty in portfolio.items():
                data = stock_data[stock]
                pl = (data["price"] - data["cost"]) * qty
                writer.writerow([stock, data["name"], data["price"], qty, pl])

        print(f"{GREEN}Saved as portfolio_report.csv{RESET}")

    else:
        print("Skipped saving.")

while True:
    print("\n==========================================================")
    print("                 STOCK PORTFOLIO TRACKER                  ")
    print("==========================================================")
    print("1. View Available Stocks")
    print("2. Add Stocks to Portfolio")
    print("3. View Portfolio Summary")
    print("4. Save Report")
    print("5. Exit")
    print("==========================================================")

    option = input("Select an option (1–5): ")

    if option == "1":
        show_available_stocks()

    elif option == "2":
        show_available_stocks()
        add_stock()

    elif option == "3":
        show_summary()

    elif option == "4":
        save_report()

    elif option == "5":
        print("\nThank you for using the Stock Portfolio Tracker!\n")
        break

    else:
        print(f"{RED}Invalid option! Please choose 1–5.{RESET}")
