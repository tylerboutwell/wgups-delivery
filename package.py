class Package:
    def __init__(self, package_id, address, deadline, city, zip_code, weight, special_note, status="At Hub"):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.special_note = special_note
        self.status = status
        self.delivery_time = None  # Update when delivered