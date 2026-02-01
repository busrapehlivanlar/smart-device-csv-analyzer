import csv
import random

def generate_device_data(filename, num_records=50):
    device_ranges = {
        "TV": (30, 60),
        "Washing Machine": (20, 90),
        "Refrigerator": (2, 8),
        "Air Conditioner": (16, 30)
    }

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["device", "temperature", "energy_consumption"])

        for _ in range(num_records):
            device = random.choice(list(device_ranges.keys()))
            min_temp, max_temp = device_ranges[device]
            temperature = round(random.uniform(min_temp, max_temp), 2)
            energy = round(random.uniform(0.5, 5.0), 2)

            writer.writerow([device, temperature, energy])

if __name__ == "__main__":
    generate_device_data("data/device_data.csv")
