class Dog:
    def __init__(self, name: str, breed: str, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        print(f"Dog name: {self.name}, Breed: {self.breed}")

    def bark(self):
        print("whoof whoof")

    def phase(self):
        user_input = input("How old is the dog (in months): ")

        # Check if the user input is a valid number
        if user_input.isdigit():
            age_in_months = int(user_input)  # Convert the input to an integer
            print(f"You entered: {age_in_months} months.")

            # Determine the dog's phase
            if age_in_months <= 3:
                phase = "Puppy"
            elif 4 <= age_in_months <= 24:
                phase = "Mid-range"
            else:
                phase = "Old"

            print(f"The dog is {age_in_months} months old, so it is in the '{phase}' phase.")
        else:
            print("That's not a valid number!")

    def update_owner(self, name, address, phone_number):
        self.owner = {
            'name': name,
            'address': address,
            'phone_number': phone_number
        }
        print(f"Owner's info updated: {self.owner}")

# Create a dog instance
dog1 = Dog("Bruno", "Pilot","Tosin")
dog1.update_owner("Tessy", "303 avalanche road", "333-333")