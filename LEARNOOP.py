import json
class Apartment:
    def __init__(self, address, num_rooms, rent_price, pet_friendly, is_available=True):
        self.address = address
        self.num_rooms = num_rooms
        self.rent_price = rent_price
        self.is_available = is_available
        self.pet_friendly = pet_friendly
        self.tenant = None

    def show_available_apts(apartments):
        available_apts = [apt for apt in apartments if apt.is_available]
        return "\n".join(
            f"Address: {apt.address}, Bedrooms: {apt.num_rooms}, Price: {apt.rent_price}, Pet Friendly: {apt.pet_friendly}"
            for apt in available_apts)

    def assign_tenant(self, tenant):
        if self.is_available:
            self.tenant = tenant
            self.is_available = False
            print(f"{tenant.first_name} {tenant.last_name} has successfully moved into {self.address}.")
        else:
            print(f"Sorry, the apartment at {self.address} is already rented.")

    def show_all_apts(apartments):
        return "\n\n".join(
            f"Apartment Details:\nAddress: {apt.address}\nRooms: {apt.num_rooms}\nRent: ${apt.rent_price}\nPet Friendly: {apt.pet_friendly}\nTenant: {apt.tenant.first_name + ' ' + apt.tenant.last_name if apt.tenant else 'No tenant assigned'}\nAvailability: {'Not Available' if not apt.is_available else 'Available'}"
            for apt in apartments
        )


class Tenant:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


apt1 = Apartment("123 Main St", 2, 1200, True)
apt2 = Apartment("456 Elm St", 3, 1500, True)
apt3 = Apartment("789 Oak St", 1, 800, True)
apt4 = Apartment("101 Pine St", 2, 1100, True)
apt5 = Apartment("202 Maple St", 3, 1600, True)

apartments = [apt1, apt2, apt3, apt4, apt5]

tenant1 = Tenant("juvenson", "lazarre", "123 Main St")
apt1.assign_tenant(tenant1)



#print(Apartment.show_available_apts(apartments))
print(Apartment.show_all_apts(apartments))
