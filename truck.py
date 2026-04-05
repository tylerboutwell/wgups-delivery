class Truck:
    #init function so trucks can be created using these functions
    def __init__(self, capacity, speed, packages, mileage, address, depart_time):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages  # List of package IDs
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    #str function so that trucks can be printed with the variables we need to see
    def __str__(self):
        package_ids = [p.package_id for p in self.packages]
        return f"Truck Capacity: {self.capacity}, Speed: {self.speed}, Packages: {package_ids}, Mileage: {self.mileage}, Address: {self.address}, Depart: {self.depart_time}"
