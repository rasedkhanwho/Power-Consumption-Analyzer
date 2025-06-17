# analyzer.py

def calculate_energy(power_watts, hours_per_day, days_per_month=30):
    return (power_watts * hours_per_day * days_per_month) / 1000  # kWh

def main():
    print("\U0001F50C Power Consumption Analyzer \U0001F50B")
    appliance_data = []

    while True:
        name = input("\nEnter appliance name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            power = float(input(f"Enter power of {name} in watts: "))
            hours = float(input(f"Enter hours per day you use {name}: "))
        except ValueError:
            print("Please enter numeric values.")
            continue

        energy = calculate_energy(power, hours)
        appliance_data.append((name, power, hours, round(energy, 2)))

    total_energy = sum([item[3] for item in appliance_data])
    rate_per_kwh = 7.0  # You can adjust this as per your local electricity rate
    estimated_bill = total_energy * rate_per_kwh

    print("\n\U0001F4CA Appliance Report:")
    for item in appliance_data:
        print(f"{item[0]}: {item[3]} kWh/month")

    print(f"\nTotal Energy: {total_energy:.2f} kWh/month")
    print(f"Estimated Monthly Bill: {estimated_bill:.2f} BDT")

if __name__ == "__main__":
    main()
