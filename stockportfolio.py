# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3400,
    "MSFT": 300
}

def calculate_investment():
    total_investment = 0
    investments = {}

    while True:
        stock_name = input("Enter stock name (or type 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break
        if stock_name not in stock_prices:
            print("Stock not found. Please enter a valid stock name.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            investment_value = stock_prices[stock_name] * quantity
            total_investment += investment_value
            investments[stock_name] = investment_value
        except ValueError:
            print("Please enter a valid quantity.")

    print("\nInvestment Summary:")
    for stock, value in investments.items():
        print(f"{stock}: ${value}")

    print(f"\nTotal Investment Value: ${total_investment}")

    # Optionally save the result to a file
    save_to_file = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save_to_file == 'yes':
        file_type = input("Enter file type (txt/csv): ").lower()
        filename = f"investment_summary.{file_type}"
        with open(filename, 'w') as file:
            file.write("Investment Summary:\n")
            for stock, value in investments.items():
                file.write(f"{stock}: ${value}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(f"Results saved to {filename}")

if __name__ == "__main__":
    calculate_investment()
