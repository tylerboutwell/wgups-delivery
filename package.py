import datetime


class Package:
    #init function so packages can be created using these variables
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, special_note, status="At Hub"):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_note = special_note
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    #Function to update the status based on a user-defined time
    def update_status(self, current_time):
        if self.delivery_time and current_time >= self.delivery_time:
            self.status = "Delivered"
        elif self.departure_time and current_time >= self.departure_time:
            self.status = "En Route"
        #Packages 6, 25, 28, and 32 do not arrive to the hub until 9:05
        elif (self.package_id == 6 or self.package_id == 25 or self.package_id == 28 or self.package_id == 32) and current_time < datetime.timedelta(hours=9, minutes=5):
            self.status = "Delayed on flight - Not arrived"
        else:
            self.status = "At Hub"

    # str function so that packages can be printed with the variables we need to see
    def __str__(self):
        return f"ID: {self.package_id} | Address: {self.address}, {self.city}, {self.state} {self.zip_code} | Deadline: {self.deadline} | Delivery time: {self.delivery_time} | Status: {self.status}"