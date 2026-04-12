# Student ID: [012106184]

#Import csv to read files, datetime for using time, and the python files I created for HashTable, Package, and Truck
import csv
import datetime
from hash_table import HashTable
from package import Package
from truck import Truck

# Function to Load Distances
def load_distance_data():
    with open("WGUPS_Distance_Table.csv") as csvfile:
        return list(csv.reader(csvfile))


# Function to Load Address Names (to find indices for distance table)
def load_address_data():
    with open("WGUPS_Addresses.csv") as csvfile:
        return list(csv.reader(csvfile))


# Function to Load Packages into the Hash Table
def load_package_data(filename, hash_table):
    with open(filename) as csvfile:

        #Loop through rows using csv.reader
        reader = csv.reader(csvfile)
        for row in reader:

            # Use variables for clarity (Indices match CSV structure)
            p_id = int(row[0])
            p_address = row[1]
            p_city = row[2]
            p_state = row[3]
            p_zip = row[4]
            p_deadline = row[5]
            p_weight = row[6]
            # Special notes might be empty, we handle that here
            p_note = row[7] if len(row) > 7 else ""

            # Create the Package object
            pkg = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_note)

            # Insert into Hash Table
            hash_table.insert(p_id, pkg)


# Function to get index of address for distance table
def get_address_index(address_string, address_data):
    for index, row in enumerate(address_data):
        # Check if the package address is inside the long string from the CSV
        if address_string in row[0]:
            return index
    return None

# Function to Get distance between two addresses
def distance_in_between(addr1, addr2, distance_data, address_data):
    address_index1 = get_address_index(addr1, address_data)
    address_index2 = get_address_index(addr2, address_data)
    distance = distance_data[address_index1][address_index2]
    if distance == '':
        distance = distance_data[address_index2][address_index1]
    return float(distance)

# Nearest Neighbor Algorithm
def deliver_packages(truck, hash_table, distance_data, address_data):
    # Create a list of actual Package objects from the truck's list of IDs and put them in not_delivered list
    not_delivered = []
    for p_id in truck.packages:
        pkg = hash_table.lookup(p_id)
        pkg.departure_time = truck.depart_time
        not_delivered.append(pkg)

    # Clear truck.packages
    truck.packages.clear()

    #Loop through each package to find the closest one and deliver the closest one
    while len(not_delivered) > 0:
        # Find the package with the address closest to truck.address
        next_package = None
        next_package_distance = 200000
        for package in not_delivered:

            if distance_in_between(package.address, truck.address, distance_data, address_data) < next_package_distance:
                next_package = package
                next_package_distance = distance_in_between(package.address, truck.address, distance_data, address_data)

        # Update truck.mileage
        truck.mileage += next_package_distance

        #Update the trucks current address
        truck.address = next_package.address

        # Update truck.time based on (distance / 18mph)
        truck.time += datetime.timedelta(hours=next_package_distance / 18)

        # Set package.delivery_time = truck.time
        next_package.delivery_time = truck.time

        # Add next closest package to truck list
        truck.packages.append(next_package)

        # Remove from not_delivered
        not_delivered.remove(next_package)


def main():
    # Initialize components
    my_hash_table = HashTable()
    load_package_data("WGUPS_Package_File.csv", my_hash_table)
    distance_data = load_distance_data()
    address_data = load_address_data()

    # Load Trucks
    truck1 = Truck(16, 18, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 37], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
    truck2 = Truck(16, 18, [3, 6, 18, 25, 28, 32, 33, 34, 35, 36, 38, 39, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
    truck3 = Truck(16, 18, [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

    # Run Deliveries
    deliver_packages(truck1, my_hash_table, distance_data, address_data)
    deliver_packages(truck2, my_hash_table, distance_data, address_data)

    # Only 2 drivers so truck3 departs after truck1 or truck2 is finished
    truck3.depart_time = min(truck1.time, truck2.time)
    deliver_packages(truck3, my_hash_table, distance_data, address_data)

    # User Interface
    print("Welcome to WGUPS Routing System")
    user_time = input("Please enter a time to check status (HH:MM): ")
    (h, m) = user_time.split(':')
    convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=0)

    #Update and print status of each trucks' packages with the truck's id as the header
    print("--Truck 1 packages--")
    for pkg in truck1.packages:
        pkg.update_status(convert_time)
        print(str(pkg))
    print("--Truck 2 packages--")
    for pkg in truck2.packages:
        pkg.update_status(convert_time)
        print(str(pkg))
    print("--Truck 3 packages--")
    for pkg in truck3.packages:
        pkg.update_status(convert_time)
        print(str(pkg))

    # Print each truck's mileage
    print("Truck 1 total mileage(end of day): " + str(truck1.mileage))
    print("Truck 2 total mileage(end of day): " + str(truck2.mileage))
    print("Truck 3 total mileage(end of day): " + str(truck3.mileage))

# Run program
main()