# =====================================================
# 1. DATA MODEL
# =====================================================
class Pet:
    def __init__(self, id, name, species, breed, age, gender, desc,
                 is_adopted=False, adopted_by=""):
        self.id         = id
        self.name       = name
        self.species    = species
        self.breed      = breed
        self.age        = age
        self.gender     = gender
        self.desc       = desc
        self.is_adopted = is_adopted
        self.adopted_by = adopted_by


# =====================================================
# 2. PET REGISTRY
# =====================================================
class PetRegistry:

    pets = [
        Pet(1, "Tokkio", "Dog",    "Golden Retriever", 2, "Male",   "Friendly and loves to play fetch!"),
        Pet(2, "BB",     "Cat",    "Siamese",          3, "Female", "Calm and loves cuddles."),
        Pet(3, "Bunny",  "Rabbit", "American",         1, "Male",   "Very active and playful."),
        Pet(4, "Luna",   "Dog",    "Dachshund",         4, "Female", "Great with kids and families."),
        Pet(5, "Milo",   "Cat",    "Persian",          5, "Male",   "Laid-back and loves napping.",   True, "Abegail O."),
        Pet(6, "Coco",   "Dog",    "Beagle",           2, "Female", "Energetic and loves outdoor walks."),
        Pet(7, "Nemo",   "Fish",   "Goldfish",         1, "Male",   "Beautiful orange and white colors."),
        Pet(8, "Daisy",  "Rabbit", "Cinnamon",         2, "Female", "Gentle and easy to care for.",   True, "Marie Claire A."),
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
    def total_pets():      return len(PetRegistry.pets)
    @staticmethod
    def total_available(): return len(PetRegistry.available())
    @staticmethod
    def total_adopted():   return len(PetRegistry.adopted())


# =====================================================
# 3. DISPLAY HELPER
# =====================================================
class Display:

    W = 54  # console width

    @staticmethod
    def divider(char="-"):
        print("  " + char * Display.W)

    @staticmethod
    def header(title):
        Display.divider("=")
        print(f"  {'HAPPY PAWS -- Pet Adoption Registry':^{Display.W}}")
        print(f"  {'Every pet deserves a loving home!':^{Display.W}}")
        print(f"  {'by: Scalers':^{Display.W}}")
        Display.divider("=")

    @staticmethod
    def print_stats():
        Display.header("HAPPY PAWS")
        print(
            f"  Total : {PetRegistry.total_pets():>3}  "
            f"|  Available : {PetRegistry.total_available():>3}  "
            f"|  Adopted : {PetRegistry.total_adopted():>3}"
        )
        Display.divider("=")

    @staticmethod
    def print_pet(p):
        status    = f"Adopted by {p.adopted_by}" if p.is_adopted else "Available for adoption"
        age_label = " [Young]" if p.age <= 2 else ""
        adopted_marker = " [ADOPTED]" if p.is_adopted else ""

        Display.divider()
        print(f"  ID      : #{p.id}")
        print(f"  Name    : {p.name}{age_label}{adopted_marker}")
        print(f"  Species : {p.species} -- {p.breed}")
        print(f"  Age     : {p.age} yr(s)  |  Gender: {p.gender}")
        print(f"  About   : {p.desc}")
        print(f"  Status  : {status}")

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
        Display.divider("-")
        print(f"  {'-- MAIN MENU --':^{Display.W}}")
        Display.divider("-")
        print("  [1]  View All Pets")
        print("  [2]  Filter by Species")
        print("  [3]  Search by Name / Breed")
        print("  [4]  View Pet Details by ID")
        print("  [5]  Adopt a Pet")
        print("  [6]  Register a New Pet")
        print("  [7]  View Adopted Pets")
        print("  [0]  Exit")
        Display.divider("-")


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

        # ── [1] VIEW ALL PETS ─────────────────────
        if choice == "1":
            print("\n  >> All Pets in the Registry:")
            Display.print_list(PetRegistry.pets, "No pets registered yet.")

        # ── [2] FILTER BY SPECIES ─────────────────
        elif choice == "2":
            print()
            Display.divider("-")
            print("  Filter by Species:")
            print("  [1] Dog   [2] Cat   [3] Rabbit   [4] Fish   [5] Other")
            Display.divider("-")
            species_map = {"1": "Dog", "2": "Cat", "3": "Rabbit", "4": "Fish", "5": "Other"}
            species = species_map.get(input("  Choose: ").strip(), "")

            if not species:
                print("  >> Invalid choice.")
            else:
                results = [p for p in PetRegistry.find_by_species(species) if not p.is_adopted]
                print(f"\n  >> Available {species}(s):")
                Display.print_list(results, f"No available {species} found.")

        # ── [3] SEARCH ────────────────────────────
        elif choice == "3":
            keyword = input("\n  Enter keyword (name / breed / species): ").strip()
            if not keyword:
                print("  >> Please enter a search keyword.")
            else:
                results = PetRegistry.search(keyword)
                print(f"\n  >> Search results for '{keyword}':")
                Display.print_list(results, f"No pets found matching '{keyword}'.")

        # ── [4] VIEW PET BY ID ────────────────────
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

        # ── [5] ADOPT A PET ───────────────────────
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
                    adopter = input("  Enter adopter's full name: ").strip()
                    adopter = "Anonymous" if not adopter else adopter
                    pet.is_adopted = True
                    pet.adopted_by = adopter
                    Display.divider("=")
                    print(f"  Congratulations! {pet.name} has been adopted by {adopter}!")
                    print(f"  Thank you for giving {pet.name} a loving home!")
                    Display.divider("=")
                elif pet:
                    print("  >> Sorry, that pet has already been adopted.")
                else:
                    print(f"  >> No pet found with ID #{id}.")

        # ── [6] REGISTER A NEW PET ───────────────
        elif choice == "6":
            print()
            Display.divider("-")
            print("  Register a New Pet")
            Display.divider("-")

            name = input("  Pet Name       : ").strip()

            print("  Species: [1] Dog  [2] Cat  [3] Rabbit  [4] Fish  [5] Other")
            sp_map  = {"1": "Dog", "2": "Cat", "3": "Rabbit", "4": "Fish"}
            species = sp_map.get(input("  Choose         : ").strip(), "Other")

            breed = input("  Breed          : ").strip()

            try:
                age = int(input("  Age (years)    : ").strip())
            except ValueError:
                age = 0

            print("  Gender: [1] Male  [2] Female")
            gender = "Male" if input("  Choose         : ").strip() == "1" else "Female"

            desc = input("  Description    : ").strip()

            if not name or not breed or not desc:
                print("  >> Name, breed, and description are required!")
            else:
                new_pet = Pet(PetRegistry.next_id(), name, species, breed, age, gender, desc)
                PetRegistry.add_pet(new_pet)
                Display.divider("=")
                print(f"  {name} has been registered with ID #{new_pet.id}!")
                Display.divider("=")

        # ── [7] VIEW ADOPTED PETS ─────────────────
        elif choice == "7":
            print("\n  >> Adopted Pets:")
            Display.print_list(PetRegistry.adopted(), "No pets have been adopted yet.")

        # ── [0] EXIT ──────────────────────────────
        elif choice == "0":
            Display.divider("=")
            print(f"  Goodbye, {staff_name}! Keep helping pets find homes!")
            Display.divider("=")
            running = False

        # ── DEFAULT ───────────────────────────────
        else:
            print("  >> Invalid choice. Please enter a number from the menu.")


# =====================================================
# ENTRY POINT
# =====================================================
if __name__ == "__main__":
    main()
