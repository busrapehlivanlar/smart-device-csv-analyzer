import csv 
import random

def generate_device_data(filename, num_records=50):
    devices = ["TV", "Washing Machine", "Refrigerator", "Air Conditioner"]
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["device", "temperature", "energy_consumption"])
      
        for _ in range(num_records):
            device = random.choice(devices)
            temperature = round(random.uniform(20, 80), 2)
            energy = round(random.uniform(0.5, 5.0), 2)

            writer.writerow([device, temperature, energy])
if __name__ == "__main__":
    generate_device_data("veri/device_data.csv")




