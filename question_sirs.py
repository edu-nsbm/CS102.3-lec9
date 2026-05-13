def main() -> None:
    currency: list[str] = ["USD", "GBP", "EUR", "THB", "INR"]
    rates: list[float] = []

    for coin in currency:
        curr_rate: float = float(input(f"Enter rate in LKR for {coin}: "))
        rates.append(curr_rate)

    print()

    print("-" * 23)
    print(f"{'Currency':<10} | {'Rate (LKR)':>10}")
    print("-" * 23)

    for coin, rate in zip(currency, rates):
        print(f"{coin:<10} | {rate:>10.2f}")

    print()

    choice: int = int(input("Enter 0-USD, 1-GBP, 2-EUR, 3-THB, 4-INR, 5-Exit: "))

    total: float = 0

    while choice != 5:
        amount: float = float(input("Enter how much: "))
        total += rates[choice] * amount

        choice = int(input("Enter 0-USD, 1-GBP, 2-EUR, 3-THB, 4-INR, 5-Exit: "))

    print("Bill is = ", total)


if __name__ == "__main__":
    main()
