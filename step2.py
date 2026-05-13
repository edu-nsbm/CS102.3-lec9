# Develop the program, when a customer wants to exchange LKR (Buying foreign currency)
# Calculate how much LKR he needs to pay


def buy_foreign_currency(rates: tuple[list[str], list[float]]) -> float:

    currency, currency_rates = rates

    # for coin, count in zip(currency, currency_rates):
    #     print(f"1 {coin} = {count} LKR")

    print("--- Buy Foreign Currency ---")

    while True:
        chosen_currency: str = input("\nWhich currency do you want to buy?: ").upper()

        if chosen_currency not in currency:
            print("Error: Invalid currency selected. Retry...")
        else:
            break

    currency_index = currency.index(chosen_currency)
    rate = currency_rates[currency_index]

    amount: float = float(input(f"Enter the {chosen_currency} amount: "))

    return amount * rate


def input_rates() -> tuple[list[str], list[float]]:
    currency: list[str] = ["USD", "GBP", "EUR", "THB", "INR"]
    rates: list[float] = []

    for coin in currency:
        curr_rate: float = float(input(f"Enter rate in LKR for {coin}: "))
        rates.append(curr_rate)

    return (currency, rates)


def main() -> None:
    currency, rates = input_rates()

    print()

    print("-" * 23)
    print(f"{'Currency':<10} | {'Rate (LKR)':>10}")
    print("-" * 23)

    for coin, rate in zip(currency, rates):
        print(f"{coin:<10} | {rate:>10.2f}")

    print()

    payment: float = buy_foreign_currency((currency, rates))

    print()

    print(f"Payment: {payment}")


if __name__ == "__main__":
    main()
