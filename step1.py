def main() -> None:
    currency: list[str] = ["UDS", "GBP", "EUR", "THB", "INR"]
    rates: list[float] = []

    for coin in currency:
        curr_rate: float = float(input(f"Enter rate in LKR for {coin}: "))
        rates.append(curr_rate)

    print("-" * 23)
    print(f"{'Currency':<10} | {'Rate (LKR)':>10}")
    print("-" * 23)
    for count in range(0, 5):
        print(f"{currency[count]:<10} | {rates[count]:>10.2f}")


if __name__ == "__main__":
    main()
