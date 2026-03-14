# =====================================================
# 1. DATA MODEL
# =====================================================
class Pet:
    def __init__(self, id, name, species, breed, age, gender, desc,
                 vaccinated=False, is_adopted=False, adopted_by="",
                 adopter_details=None):
        self.id              = id
        self.name            = name
        self.species         = species
        self.breed           = breed
        self.age             = age
        self.gender          = gender
        self.desc            = desc
        self.vaccinated      = vaccinated
        self.is_adopted      = is_adopted
        self.adopted_by      = adopted_by
        self.adopter_details = adopter_details  # dict with full adopter info


# =====================================================
# 2. PET REGISTRY
# =====================================================
class PetRegistry:

    pets = [
        Pet(1, "Bonjong",  "Dog",    "Belgian Malinois", 2, "Male",
            "Friendly and loves to play fetch! Great with children.",
            vaccinated=True),

        Pet(2, "Whiskers", "Cat",    "Siamese",          3, "Female",
            "Calm and loves cuddles. Perfect indoor companion.",
            vaccinated=True),

        Pet(3, "Thumper",  "Rabbit", "Holland Lop",      1, "Male",
            "Very active and playful. Loves hopping around the garden.",
            vaccinated=False),

        Pet(4, "Luna",     "Dog",    "Dachshund",        4, "Female",
            "Great with kids and families. Calm and well-trained.",
            vaccinated=True),

        Pet(5, "Milo",     "Cat",    "Persian",          5, "Male",
            "Laid-back and loves napping by the window.",
            vaccinated=True, is_adopted=True, adopted_by="Kc Vargas",
            adopter_details={
                "fullname"   : "Kc Vargas",
                "contact"    : "09171234567",
                "email"      : "kc.vargas@email.com",
                "dob"        : "1990-05-14",
                "address"    : "123 Mango St., Barangay Poblacion, Davao City",
                "occupation" : "Nurse",
                "living"     : "House with yard",
                "reason"     : "I have always loved cats and Milo felt like the perfect fit!"
            }),

        Pet(6, "Mochi",    "Dog",    "Shi-poo",          2, "Female",
            "Energetic and loves outdoor walks. Always wagging her tail!",
            vaccinated=False),

        Pet(7, "Nemo",     "Fish",   "Goldfish",         1, "Male",
            "Beautiful orange and white colors. Very soothing to watch.",
            vaccinated=False),

        Pet(8, "Daisy",    "Rabbit", "Mini Rex",         2, "Female",
            "Gentle and easy to care for. Loves soft petting.",
            vaccinated=True, is_adopted=True, adopted_by="Erikka Dela Cruz",
            adopter_details={
                "fullname"   : "Erikka Dela Cruz",
                "contact"    : "09289876543",
                "email"      : "erikka.dela.cruz@email.com",
                "dob"        : "1988-11-22",
                "address"    : "45 Rizal Ave., Toril, Davao City",
                "occupation" : "Engineer",
                "living"     : "House with yard",
                "reason"     : "My kids have been begging for a rabbit. Daisy is perfect!"
            }),
    ]

    @staticmethod
    def find_by_id(id):
        return next((p for p in PetRegistry.pets if p.id == id), None)

    @staticmethod
    def find_by_species(species):
        return [p for p in PetRegistry.pets if p.species.lower() == species.lower()]

    @staticmethod
    def search(keyword):
        kw = keyword.lower()
        return [p for p in PetRegistry.pets
                if kw in p.name.lower()
                or kw in p.breed.lower()
                or kw in p.species.lower()]

    @staticmethod
    def available():
        return [p for p in PetRegistry.pets if not p.is_adopted]

    @staticmethod
    def adopted():
        return [p for p in PetRegistry.pets if p.is_adopted]

    @staticmethod
    def add_pet(p):
        PetRegistry.pets.append(p)

    @staticmethod
    def next_id():
        return 1 if not PetRegistry.pets else max(p.id for p in PetRegistry.pets) + 1

    @staticmethod
    def total_pets():       return len(PetRegistry.pets)
    @staticmethod
    def total_available():  return len(PetRegistry.available())
    @staticmethod
    def total_adopted():    return len(PetRegistry.adopted())
    @staticmethod
    def total_vaccinated(): return len([p for p in PetRegistry.pets if p.vaccinated])


# =====================================================
# 3. DISPLAY HELPER
# =====================================================
class Display:

    W = 54

    @staticmethod
    def divider(char="-"):
        print("  " + char * Display.W)

    @staticmethod
    def print_stats():
        Display.divider("=")
        print(f"  {'HAPPY PAWS -- Pet Adoption Registry':^{Display.W}}")
        print(f"  {'Every pet deserves a loving home!':^{Display.W}}")
        print(f"  {'by: Scalers':^{Display.W}}")
        Display.divider("=")
        print(
            f"  Total : {PetRegistry.total_pets():>3}  "
            f"|  Available  : {PetRegistry.total_available():>3}  "
            f"|  Adopted    : {PetRegistry.total_adopted():>3}  "
            f"|  Vaccinated : {PetRegistry.total_vaccinated():>3}"
        )
        Display.divider("=")

    @staticmethod
    def print_pet(p):
        vacc_label  = "Yes" if p.vaccinated  else "No"
        age_label   = " [Young]"   if p.age <= 2   else ""
        adopted_mk  = " [ADOPTED]" if p.is_adopted  else ""
        status      = f"Adopted by {p.adopted_by}" if p.is_adopted else "Available for adoption"

        Display.divider()
        print(f"  ID          : #{p.id}")
        print(f"  Name        : {p.name}{age_label}{adopted_mk}")
        print(f"  Species     : {p.species} -- {p.breed}")
        print(f"  Age         : {p.age} yr(s)  |  Gender: {p.gender}")
        print(f"  Vaccinated  : {vacc_label}")
        print(f"  About       : {p.desc}")
        print(f"  Status      : {status}")

        # Show full adopter info if adopted
        if p.is_adopted and p.adopter_details:
            d = p.adopter_details
            Display.divider()
            print(f"  -- ADOPTER INFORMATION --")
            print(f"  Full Name   : {d.get('fullname', '—')}")
            print(f"  Contact     : {d.get('contact', '—')}")
            print(f"  Email       : {d.get('email', '—')}")
            print(f"  Date of Birth: {d.get('dob', '—')}")
            print(f"  Address     : {d.get('address', '—')}")
            print(f"  Occupation  : {d.get('occupation', '—')}")
            print(f"  Living      : {d.get('living', '—')}")
            print(f"  Reason      : {d.get('reason', '—')}")

    @staticmethod
    def print_list(pets, empty_msg):
        if not pets:
            Display.divider()
            print(f"  >> {empty_msg}")
            Display.divider()
        else:
            for p in pets:
                Display.print_pet(p)
            Display.divider()

    @staticmethod
    def print_menu():
        print()
        Display.divider()
        print(f"  {'-- MAIN MENU --':^{Display.W}}")
        Display.divider()
        print("  [1]  View All Pets")
        print("  [2]  Filter by Species")
        print("  [3]  Search by Name / Breed")
        print("  [4]  View Pet Details by ID")
        print("  [5]  Adopt a Pet")
        print("  [6]  Register a New Pet")
        print("  [7]  View Adopted Pets")
        print("  [8]  View Vaccinated Pets Only")
        print("  [0]  Exit")
        Display.divider()


# =====================================================
# 4. MAIN APP
# =====================================================
def main():

    Display.print_stats()
    name_input = input("\n  Welcome! What is your name? ").strip()
    staff_name = "Guest" if not name_input else name_input
    print(f"\n  Hello, {staff_name}! Welcome to Happy Paws.")

    running = True

    while running:

        Display.print_stats()
        Display.print_menu()
        choice = input("\n  Enter your choice: ").strip()

        # ── 1. View All Pets ──────────────────────────
        if choice == "1":
            print("\n  >> All Pets in the Registry:")
            Display.print_list(PetRegistry.pets, "No pets registered yet.")

        # ── 2. Filter by Species ──────────────────────
        elif choice == "2":
            print()
            Display.divider()
            print("  Filter by Species:")
            print("  [1] Dog   [2] Cat   [3] Rabbit   [4] Fish   [5] Other")
            Display.divider()
            species_map = {"1": "Dog", "2": "Cat", "3": "Rabbit", "4": "Fish", "5": "Other"}
            species = species_map.get(input("  Choose: ").strip(), "")
            if not species:
                print("  >> Invalid choice.")
            else:
                results = [p for p in PetRegistry.find_by_species(species) if not p.is_adopted]
                print(f"\n  >> Available {species}(s):")
                Display.print_list(results, f"No available {species} found.")

        # ── 3. Search ─────────────────────────────────
        elif choice == "3":
            keyword = input("\n  Enter keyword (name / breed / species): ").strip()
            if not keyword:
                print("  >> Please enter a search keyword.")
            else:
                results = PetRegistry.search(keyword)
                print(f"\n  >> Search results for '{keyword}':")
                Display.print_list(results, f"No pets found matching '{keyword}'.")

        # ── 4. View by ID ─────────────────────────────
        elif choice == "4":
            try:
                id = int(input("\n  Enter Pet ID: ").strip())
            except ValueError:
                id = -1
            pet = PetRegistry.find_by_id(id)
            if pet:
                print("\n  >> Pet Details:")
                Display.print_pet(pet)
                Display.divider()
            else:
                print(f"  >> No pet found with ID #{id}.")

        # ── 5. Adopt a Pet ────────────────────────────
        elif choice == "5":
            print("\n  >> Available Pets:")
            Display.print_list(PetRegistry.available(), "No pets available for adoption.")
            if PetRegistry.available():
                try:
                    id = int(input("  Enter the ID of the pet to adopt: ").strip())
                except ValueError:
                    id = -1
                pet = PetRegistry.find_by_id(id)
                if pet and not pet.is_adopted:
                    Display.divider()
                    print("  -- ADOPTER INFORMATION --")
                    Display.divider()
                    fullname   = input("  Full Name        : ").strip() or "Anonymous"
                    contact    = input("  Contact Number   : ").strip()
                    email      = input("  Email Address    : ").strip()
                    dob        = input("  Date of Birth    : ").strip()
                    address    = input("  Complete Address : ").strip()
                    occupation = input("  Occupation       : ").strip()
                    print("  Living Situation: [1] House  [2] Apartment/Condo  [3] Farm")
                    living_map = {"1": "House", "2": "Apartment/Condo", "3": "Farm"}
                    living     = living_map.get(input("  Choose           : ").strip(), "House")
                    reason     = input("  Reason for Adopting: ").strip()

                    pet.is_adopted      = True
                    pet.adopted_by      = fullname
                    pet.adopter_details = {
                        "fullname": fullname, "contact": contact, "email": email,
                        "dob": dob, "address": address, "occupation": occupation,
                        "living": living, "reason": reason
                    }
                    Display.divider("=")
                    print(f"  Congratulations! {pet.name} has been adopted by {fullname}!")
                    print(f"  Thank you for giving {pet.name} a loving home!")
                    Display.divider("=")
                elif pet:
                    print("  >> Sorry, that pet has already been adopted.")
                else:
                    print(f"  >> No pet found with ID #{id}.")

        # ── 6. Register a New Pet ─────────────────────
        elif choice == "6":
            print()
            Display.divider()
            print("  Register a New Pet")
            Display.divider()
            name = input("  Pet Name       : ").strip()
            print("  Species: [1] Dog  [2] Cat  [3] Rabbit  [4] Fish  [5] Other")
            sp_map  = {"1": "Dog", "2": "Cat", "3": "Rabbit", "4": "Fish"}
            species = sp_map.get(input("  Choose         : ").strip(), "Other")
            breed   = input("  Breed          : ").strip()
            try:
                age = int(input("  Age (years)    : ").strip())
            except ValueError:
                age = 0
            print("  Gender: [1] Male  [2] Female")
            gender     = "Male" if input("  Choose         : ").strip() == "1" else "Female"
            print("  Vaccinated? [1] Yes  [2] No")
            vaccinated = input("  Choose         : ").strip() == "1"
            desc       = input("  Description    : ").strip()

            if not name or not breed or not desc:
                print("  >> Name, breed, and description are required!")
            else:
                new_pet = Pet(PetRegistry.next_id(), name, species, breed,
                              age, gender, desc, vaccinated=vaccinated)
                PetRegistry.add_pet(new_pet)
                Display.divider("=")
                print(f"  {name} has been registered with ID #{new_pet.id}!")
                Display.divider("=")

        # ── 7. View Adopted Pets ──────────────────────
        elif choice == "7":
            print("\n  >> Adopted Pets:")
            Display.print_list(PetRegistry.adopted(), "No pets have been adopted yet.")

        # ── 8. View Vaccinated Pets ───────────────────
        elif choice == "8":
            vaccinated_pets = [p for p in PetRegistry.pets if p.vaccinated]
            print("\n  >> Vaccinated Pets:")
            Display.print_list(vaccinated_pets, "No vaccinated pets found.")

        # ── 0. Exit ───────────────────────────────────
        elif choice == "0":
            Display.divider("=")
            print(f"  Goodbye, {staff_name}! Keep helping pets find homes!")
            Display.divider("=")
            running = False

        else:
            print("  >> Invalid choice. Please enter a number from the menu.")


# =====================================================
# ENTRY POINT
# =====================================================
if __name__ == "__main__":
    main()
