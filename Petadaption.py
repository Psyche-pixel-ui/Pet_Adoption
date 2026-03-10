# =====================================================
#   🐾 HAPPY PAWS — Pet Adoption Registry
#   Python version — mirrors Petadaption.scala
#   Group: Scalers
# =====================================================
#
#  SCALA                          PYTHON
#  ─────────────────────────────────────────────────
#  import scala.io.StdIn.readLine → input()  (built-in)
#  import scala.collection        → list []  (built-in)
#  case class Pet(...)            → class Pet:
#  object PetRegistry             → class PetRegistry:
#  object Display                 → class Display:
#  extends App                    → if __name__ == "__main__":
#  println()                      → print()
#  readLine()                     → input()
#  val (immutable)                → variable (no special keyword)
#  var (mutable)                  → variable (no special keyword)
#  ListBuffer[Pet]                → list []
#  match / case                   → match / case  (Python 3.10+)
#                                   or if/elif/else
# =====================================================


# =====================================================
# 1. DATA MODEL
# =====================================================
#
#  SCALA:                          PYTHON:
#  ──────────────────────────────────────────────────
#  case class Pet(                 class Pet:
#    id      : Int,                  def __init__(self, id, name,
#    name    : String,                  species, breed, age,
#    species : String,                  gender, desc,
#    breed   : String,                  is_adopted=False,
#    age     : Int,                     adopted_by=""):
#    gender  : String,
#    desc    : String,
#    var isAdopted: Boolean = false,
#    var adoptedBy: String  = ""
#  )
#
#  case class  = blueprint with auto equals/toString
#  Python class = same idea, but you write __init__ yourself
#
#  val = cannot change   → Python has no keyword; just don't reassign
#  var = can change      → Python has no keyword; just reassign freely
#
#  Boolean = True/False  → Python: True / False  (capital T and F)
#  String  = text        → Python: str
#  Int     = whole number→ Python: int
#  = false / = ""        → Python default parameter values
# =====================================================

class Pet:
    def __init__(self, id, name, species, breed, age, gender, desc,
                 is_adopted=False, adopted_by=""):
        # SCALA: id : Int        | PYTHON: no type annotation needed
        self.id         = id
        self.name       = name
        self.species    = species
        self.breed      = breed
        self.age        = age
        self.gender     = gender
        self.desc       = desc

        # SCALA: var isAdopted : Boolean = false
        # PYTHON: self.is_adopted = False
        # var in Scala means this field CAN change — same in Python,
        # all attributes are freely mutable by default
        self.is_adopted = is_adopted
        self.adopted_by = adopted_by


# =====================================================
# 2. PET REGISTRY
# =====================================================
#
#  SCALA:                          PYTHON:
#  ──────────────────────────────────────────────────
#  object PetRegistry {            class PetRegistry:
#    val pets: ListBuffer[Pet] =     pets = [ Pet(...), ... ]
#      ListBuffer( Pet(...), ... )
#
#  object   = singleton (one instance, no "new")
#  Python   = we use a class with a class-level list (same effect)
#
#  ListBuffer[Pet] = mutable list of Pets
#  Python list []  = also mutable, no type declaration needed
#
#  def findById(id: Int): Option[Pet]  →  def find_by_id(id):
#  Option[Pet] = Some(pet) or None     →  returns pet or None
#
#  pets.find(_.id == id)   →  next((p for p in pets if p.id == id), None)
#  _.id = shorthand lambda →  p.id in Python (explicit variable name)
#
#  .filter(!_.isAdopted)   →  [p for p in pets if not p.is_adopted]
#  .toList                 →  already a list in Python, no conversion needed
#
#  pets.map(_.id).max + 1  →  max(p.id for p in pets) + 1
#  .map(_.id) = extract ids→  generator expression
# =====================================================

class PetRegistry:

    # SCALA: val pets: ListBuffer[Pet] = ListBuffer( Pet(...), ... )
    # PYTHON: pets = [ Pet(...), ... ]
    # Class-level list — shared across the whole program (like a singleton)
    pets = [
        Pet(1, "Buddy",    "Dog",    "Golden Retriever", 2, "Male",   "Friendly and loves to play fetch!"),
        Pet(2, "Whiskers", "Cat",    "Siamese",          3, "Female", "Calm and loves cuddles."),
        Pet(3, "Thumper",  "Rabbit", "Holland Lop",      1, "Male",   "Very active and playful."),
        Pet(4, "Luna",     "Dog",    "Labrador",         4, "Female", "Great with kids and families."),
        Pet(5, "Milo",     "Cat",    "Persian",          5, "Male",   "Laid-back and loves napping.",    True,  "Sarah J."),
        Pet(6, "Coco",     "Dog",    "Beagle",           2, "Female", "Energetic and loves outdoor walks."),
        Pet(7, "Nemo",     "Fish",   "Goldfish",         1, "Male",   "Beautiful orange and white colors."),
        Pet(8, "Daisy",    "Rabbit", "Mini Rex",         2, "Female", "Gentle and easy to care for.",    True,  "Tom L."),
    ]

    # ── find one pet by ID ──────────────────────────
    # SCALA: def findById(id: Int): Option[Pet] =
    #          pets.find(_.id == id)
    # PYTHON: def find_by_id(id):
    #           return next((p for p in pets if p.id == id), None)
    #
    # next(..., None) = returns the first match, or None if not found
    # (p for p in ...) = generator expression (like Scala's lambda _.id)
    @staticmethod
    def find_by_id(id):
        return next((p for p in PetRegistry.pets if p.id == id), None)

    # ── filter pets by species ──────────────────────
    # SCALA: def findBySpecies(species: String): List[Pet] =
    #          pets.filter(_.species.toLowerCase == species.toLowerCase).toList
    # PYTHON: def find_by_species(species):
    #           return [p for p in pets if p.species.lower() == species.lower()]
    #
    # .toLowerCase  →  .lower()
    # .filter(...)  →  list comprehension [p for p in ... if ...]
    @staticmethod
    def find_by_species(species):
        return [p for p in PetRegistry.pets if p.species.lower() == species.lower()]

    # ── search pets by keyword ──────────────────────
    # SCALA: def search(keyword: String): List[Pet] = {
    #          val kw = keyword.toLowerCase
    #          pets.filter { p =>
    #            p.name.toLowerCase.contains(kw) ||
    #            p.breed.toLowerCase.contains(kw)
    #          }.toList
    #        }
    # PYTHON: def search(keyword):
    #           kw = keyword.lower()
    #           return [p for p in pets if kw in p.name.lower() or ...]
    #
    # .contains(kw)  →  kw in string  (Python uses "in" operator)
    # ||             →  or
    @staticmethod
    def search(keyword):
        kw = keyword.lower()
        return [p for p in PetRegistry.pets
                if kw in p.name.lower()
                or kw in p.breed.lower()
                or kw in p.species.lower()]

    # ── only pets that are available ────────────────
    # SCALA: def available: List[Pet] = pets.filter(!_.isAdopted).toList
    # PYTHON: def available():
    #           return [p for p in pets if not p.is_adopted]
    #
    # !_.isAdopted  →  not p.is_adopted
    @staticmethod
    def available():
        return [p for p in PetRegistry.pets if not p.is_adopted]

    # ── only pets that are adopted ──────────────────
    # SCALA: def adopted: List[Pet] = pets.filter(_.isAdopted).toList
    # PYTHON: def adopted():
    #           return [p for p in pets if p.is_adopted]
    @staticmethod
    def adopted():
        return [p for p in PetRegistry.pets if p.is_adopted]

    # ── add a new pet to the registry ───────────────
    # SCALA: def addPet(p: Pet): Unit = pets += p
    #   += is the ListBuffer append operator
    #   Unit = returns nothing (like void)
    # PYTHON: def add_pet(p):
    #           pets.append(p)
    #   .append() adds to the end of the list
    @staticmethod
    def add_pet(p):
        PetRegistry.pets.append(p)

    # ── auto-generate the next available ID ─────────
    # SCALA: def nextId: Int =
    #          if (pets.isEmpty) 1 else pets.map(_.id).max + 1
    # PYTHON: def next_id():
    #           return 1 if not pets else max(p.id for p in pets) + 1
    #
    # pets.isEmpty   →  not pets  (empty list is falsy in Python)
    # pets.map(_.id) →  (p.id for p in pets)  generator expression
    # .max           →  max(...)
    @staticmethod
    def next_id():
        return 1 if not PetRegistry.pets else max(p.id for p in PetRegistry.pets) + 1

    # ── live stats ──────────────────────────────────
    # SCALA: def totalPets     : Int = pets.size
    #        def totalAvailable: Int = available.size
    #        def totalAdopted  : Int = adopted.size
    # PYTHON: len() instead of .size
    @staticmethod
    def total_pets():      return len(PetRegistry.pets)
    @staticmethod
    def total_available(): return len(PetRegistry.available())
    @staticmethod
    def total_adopted():   return len(PetRegistry.adopted())


# =====================================================
# 3. DISPLAY HELPER
# =====================================================
#
#  SCALA:                          PYTHON:
#  ──────────────────────────────────────────────────
#  object Display {                class Display:
#    val emojiMap: Map[...] = Map(   emoji_map = { "Dog":"🐶", ... }
#      "Dog" -> "🐶", ...          )
#
#  Map[String,String] = key-value dictionary
#  Python dict {}     = same concept, different syntax
#
#  "Dog" -> "🐶"    →  "Dog": "🐶"   (colon instead of ->)
#
#  emojiMap.getOrElse(species, "🐾")
#    →  emoji_map.get(species, "🐾")
#  .getOrElse(k, default) = .get(k, default) in Python
#
#  println(s"Hello $name")  →  print(f"Hello {name}")
#  s"..." (s-interpolator)  →  f"..." (f-string)
#  ${variable}              →  {variable}
#
#  f"Total: ${count}%3d"   →  f"Total: {count:3d}"
#  %3d (Scala format)       →  :3d  (Python format spec)
# =====================================================

class Display:

    # SCALA: val emojiMap: Map[String, String] = Map("Dog" -> "🐶", ...)
    # PYTHON: emoji_map = {"Dog": "🐶", ...}
    emoji_map = {"Dog": "🐶", "Cat": "🐱", "Rabbit": "🐰", "Fish": "🐟"}

    # SCALA: def emoji(species: String): String =
    #          emojiMap.getOrElse(species, "🐾")
    # PYTHON: def emoji(species):
    #           return emoji_map.get(species, "🐾")
    @staticmethod
    def emoji(species):
        return Display.emoji_map.get(species, "🐾")

    # ── printStats() ────────────────────────────────
    # SCALA: println(f"Total: ${PetRegistry.totalPets}%3d ...")
    #   f"..." with %3d = 3-character wide integer
    # PYTHON: print(f"Total: {PetRegistry.total_pets():3d} ...")
    #   f"..." with :3d = same 3-character wide integer
    @staticmethod
    def print_stats():
        print("\n  " + "=" * 52)
        print("      🐾  HAPPY PAWS — Pet Adoption Registry")
        print("      Every pet deserves a loving home! 💛")
        print("  " + "=" * 52)
        print(f"   📊 Total: {PetRegistry.total_pets():3d}  "
              f"| ✅ Available: {PetRegistry.total_available():3d}  "
              f"| ❤️  Adopted: {PetRegistry.total_adopted():3d}")
        print("  " + "=" * 52)

    # ── printPet() ──────────────────────────────────
    # SCALA: def printPet(p: Pet): Unit = {
    #          val status = if (p.isAdopted) s"Adopted by ${p.adoptedBy}"
    #                       else "Available"
    #          val ageLabel = if (p.age <= 2) " 🌱 Young" else ""
    #          println(s"${emoji(p.species)} [${p.id}] ${p.name}$ageLabel")
    #        }
    # PYTHON:
    #   if/else expression:
    #   SCALA: val x = if (cond) a else b
    #   PYTHON: x = a if cond else b    ← ternary operator
    #
    #   s"text ${var}" → f"text {var}"
    @staticmethod
    def print_pet(p):
        # SCALA: val status = if (p.isAdopted) s"..." else "..."
        # PYTHON: status = "..." if p.is_adopted else "..."
        status    = f"❤️  Adopted by {p.adopted_by}" if p.is_adopted else "✅ Available for adoption"
        age_label = " 🌱 Young" if p.age <= 2 else ""

        print(f"\n  {Display.emoji(p.species)} [{p.id}] {p.name}{age_label}")
        print(f"      Species : {p.species} — {p.breed}")
        print(f"      Age     : {p.age} yr(s)  |  Gender: {p.gender}")
        print(f"      About   : {p.desc}")
        print(f"      Status  : {status}")

    # ── printList() ─────────────────────────────────
    # SCALA: def printList(pets: List[Pet], emptyMsg: String): Unit =
    #          if (pets.isEmpty) println(s"🔍 $emptyMsg")
    #          else pets.foreach(printPet)
    # PYTHON:
    #   pets.isEmpty   →  not pets  (empty list is falsy)
    #   pets.foreach() →  for p in pets: (explicit for loop)
    @staticmethod
    def print_list(pets, empty_msg):
        if not pets:                          # SCALA: if (pets.isEmpty)
            print(f"\n  🔍 {empty_msg}")
        else:
            for p in pets:                    # SCALA: pets.foreach(printPet)
                Display.print_pet(p)

    # ── printMenu() ─────────────────────────────────
    # SCALA: def printMenu(): Unit = { println("  [1] ...") ... }
    # PYTHON: def print_menu():       print("  [1] ...")
    # Both just print lines — identical concept, different syntax
    @staticmethod
    def print_menu():
        print("\n  ── MAIN MENU ───────────────────────────────")
        print("  [1] 🐾 View All Pets")
        print("  [2] 🔎 Filter by Species")
        print("  [3] 🔍 Search by Name / Breed")
        print("  [4] 📋 View Pet Details by ID")
        print("  [5] ❤️  Adopt a Pet")
        print("  [6] ➕ Register a New Pet")
        print("  [7] 🏠 View Adopted Pets")
        print("  [0] 👋 Exit")


# =====================================================
# 4. MAIN APP — Entry Point
# =====================================================
#
#  SCALA:                          PYTHON:
#  ──────────────────────────────────────────────────
#  object PetAdoptionRegistry      def main():
#    extends App {                   (no special keyword)
#
#  extends App = runs automatically  if __name__ == "__main__":
#  when the program starts             main()
#
#  readLine()         →  input()
#  .trim              →  .strip()    (removes whitespace)
#  println()          →  print()
#
#  match / case (pattern matching):
#  SCALA:                          PYTHON (3.10+):
#    choice match {                  match choice:
#      case "1" => ...                 case "1": ...
#      case "2" => ...                 case "2": ...
#      case _   => ...                 case _:   ...  (wildcard)
#    }
#
#  SCALA: case Some(p) if !p.isAdopted  ← guard condition
#  PYTHON: if pet and not pet.is_adopted ← regular if check
#
#  SCALA: .toIntOption.getOrElse(-1)    ← safe int parsing
#  PYTHON: int(x) inside try/except     ← exception handling
# =====================================================

def main():

    # ── welcome screen ───────────────────────────────
    # SCALA: Display.printStats()
    # PYTHON: Display.print_stats()
    Display.print_stats()
    name_input = input("\n  Welcome! What is your name? ").strip()

    # SCALA: val staffName = readLine().trim match {
    #          case "" => "Guest"
    #          case n  => n
    #        }
    # PYTHON: staff_name = "Guest" if not name_input else name_input
    # Ternary: value_if_true if condition else value_if_false
    staff_name = "Guest" if not name_input else name_input
    print(f"\n  Hello, {staff_name}! Welcome to Happy Paws 🐶🐱🐰")

    # SCALA: var running = true
    # PYTHON: running = True
    # Both are mutable boolean flags that control the while loop
    running = True

    while running:
        # SCALA: Display.printStats(); Display.printMenu()
        Display.print_stats()
        Display.print_menu()

        # SCALA: val choice = readLine().trim
        # PYTHON: choice = input(...).strip()
        # .trim() in Scala = .strip() in Python
        choice = input("\n  Enter your choice: ").strip()

        # SCALA: choice match { case "1" => ... case "2" => ... }
        # PYTHON: match choice: case "1": ... case "2": ...
        # (Python 3.10+ supports match/case — for older Python use if/elif)
        match choice:

            # ── [1] VIEW ALL PETS ─────────────────────
            # SCALA: case "1" =>
            #   Display.printList(PetRegistry.pets.toList, "No pets registered yet.")
            # PYTHON: case "1":
            #   Display.print_list(PetRegistry.pets, "No pets registered yet.")
            # .toList not needed in Python — it's already a list
            case "1":
                print("\n  🐾 All Pets in the Registry:")
                print("  " + "─" * 48)
                Display.print_list(PetRegistry.pets, "No pets registered yet.")

            # ── [2] FILTER BY SPECIES ─────────────────
            # SCALA: val species = readLine().trim match {
            #          case "1" => "Dog" ... case _ => ""
            #        }
            # PYTHON: species_map = {"1":"Dog",...}
            #         species = species_map.get(choice2, "")
            # Python uses a dict lookup instead of match for simple mappings
            case "2":
                print("\n  Filter by Species:")
                print("  [1] 🐶 Dog   [2] 🐱 Cat")
                print("  [3] 🐰 Rabbit  [4] 🐟 Fish  [5] 🐾 Other")

                # SCALA: match { case "1" => "Dog" ... case _ => "" }
                # PYTHON: dict.get(key, default)
                species_map = {"1":"Dog","2":"Cat","3":"Rabbit","4":"Fish","5":"Other"}
                species = species_map.get(input("  Choose: ").strip(), "")

                if not species:             # SCALA: if (species.isEmpty)
                    print("  ❌ Invalid choice.")
                else:
                    # SCALA: PetRegistry.findBySpecies(species).filter(!_.isAdopted)
                    # PYTHON: [p for p in find_by_species if not p.is_adopted]
                    results = [p for p in PetRegistry.find_by_species(species)
                               if not p.is_adopted]
                    print(f"\n  {Display.emoji(species)} Available {species}(s):")
                    print("  " + "─" * 48)
                    Display.print_list(results, f"No available {species} found.")

            # ── [3] SEARCH ────────────────────────────
            # SCALA: val keyword = readLine().trim
            #        if (keyword.isEmpty) println("...")
            #        else { val results = PetRegistry.search(keyword) ... }
            # PYTHON: keyword = input(...).strip()
            #         if not keyword: ... else: ...
            case "3":
                keyword = input("\n  🔍 Enter keyword (name / breed / species): ").strip()
                if not keyword:             # SCALA: if (keyword.isEmpty)
                    print("  ❌ Please enter a search keyword.")
                else:
                    results = PetRegistry.search(keyword)
                    print(f"\n  Search results for '{keyword}':")
                    print("  " + "─" * 48)
                    Display.print_list(results, f"No pets found matching '{keyword}'.")

            # ── [4] VIEW PET BY ID ────────────────────
            # SCALA: val id = readLine().trim.toIntOption.getOrElse(-1)
            #        PetRegistry.findById(id) match {
            #          case Some(p) => Display.printPet(p)
            #          case None    => println(s"No pet with ID #$id.")
            #        }
            # PYTHON: try int(input()) except → -1
            #         pet = PetRegistry.find_by_id(id)
            #         if pet: ... else: ...   (None check instead of Option)
            case "4":
                try:
                    id = int(input("\n  Enter Pet ID: ").strip())
                except ValueError:          # SCALA: .toIntOption → None case
                    id = -1

                pet = PetRegistry.find_by_id(id)
                if pet:                     # SCALA: case Some(p) =>
                    print("\n  📋 Pet Details:")
                    print("  " + "─" * 48)
                    Display.print_pet(pet)
                else:                       # SCALA: case None =>
                    print(f"  ❌ No pet found with ID #{id}.")

            # ── [5] ADOPT A PET ───────────────────────
            # SCALA: case Some(p) if !p.isAdopted =>  ← guard condition
            #          p.isAdopted = true              ← mutate var field
            #          p.adoptedBy = adopter           ← mutate var field
            # PYTHON: if pet and not pet.is_adopted:   ← regular if check
            #           pet.is_adopted = True           ← direct assignment
            #           pet.adopted_by = adopter
            case "5":
                print("\n  ✅ Available Pets:")
                print("  " + "─" * 48)
                Display.print_list(PetRegistry.available(), "No pets available for adoption.")

                if PetRegistry.available():  # SCALA: if (PetRegistry.available.nonEmpty)
                    try:
                        id = int(input("\n  Enter the ID of the pet to adopt: ").strip())
                    except ValueError:
                        id = -1

                    pet = PetRegistry.find_by_id(id)

                    # SCALA: case Some(p) if !p.isAdopted =>  (guard)
                    # PYTHON: if pet and not pet.is_adopted:
                    if pet and not pet.is_adopted:
                        adopter = input(f"  Enter adopter's full name: ").strip()
                        adopter = "Anonymous" if not adopter else adopter

                        # SCALA: p.isAdopted = true  (mutating var)
                        # PYTHON: pet.is_adopted = True (same thing)
                        pet.is_adopted = True
                        pet.adopted_by = adopter
                        print(f"\n  🎉 Congratulations! {pet.name} has been adopted by {adopter}!")
                        print(f"  💛 Thank you for giving {pet.name} a loving home!")

                    elif pet:               # SCALA: case Some(_) =>
                        print("  ❌ Sorry, that pet has already been adopted.")
                    else:                   # SCALA: case None =>
                        print(f"  ❌ No pet found with ID #{id}.")

            # ── [6] REGISTER A NEW PET ────────────────
            # SCALA: val newPet = Pet(PetRegistry.nextId, name, ...)
            #        PetRegistry.addPet(newPet)
            # PYTHON: new_pet = Pet(PetRegistry.next_id(), name, ...)
            #         PetRegistry.add_pet(new_pet)
            case "6":
                print("\n  ➕ Register a New Pet")
                print("  " + "─" * 40)

                name  = input("  Pet Name       : ").strip()

                print("  Species:")
                print("  [1] Dog  [2] Cat  [3] Rabbit  [4] Fish  [5] Other")
                # SCALA: match { case "1" => "Dog" ... }
                # PYTHON: dict.get(input, default)
                sp_map  = {"1":"Dog","2":"Cat","3":"Rabbit","4":"Fish"}
                species = sp_map.get(input("  Choose         : ").strip(), "Other")

                breed   = input("  Breed          : ").strip()

                try:
                    age = int(input("  Age (years)    : ").strip())
                except ValueError:          # SCALA: .toIntOption.getOrElse(0)
                    age = 0

                print("  Gender: [1] Male  [2] Female")
                gender = "Male" if input("  Choose         : ").strip() == "1" else "Female"

                desc = input("  Description    : ").strip()

                # SCALA: if (name.isEmpty || breed.isEmpty || desc.isEmpty)
                # PYTHON: if not name or not breed or not desc
                if not name or not breed or not desc:
                    print("  ❌ Name, breed, and description are required!")
                else:
                    # SCALA: val newPet = Pet(PetRegistry.nextId, ...)
                    # PYTHON: new_pet = Pet(PetRegistry.next_id(), ...)
                    new_pet = Pet(PetRegistry.next_id(), name, species, breed, age, gender, desc)
                    PetRegistry.add_pet(new_pet)
                    print(f"\n  ✅ {name} has been registered with ID #{new_pet.id}!")

            # ── [7] VIEW ADOPTED PETS ─────────────────
            # SCALA: Display.printList(PetRegistry.adopted, "...")
            # PYTHON: Display.print_list(PetRegistry.adopted(), "...")
            case "7":
                print("\n  ❤️  Adopted Pets:")
                print("  " + "─" * 48)
                Display.print_list(PetRegistry.adopted(), "No pets have been adopted yet.")

            # ── [0] EXIT ──────────────────────────────
            # SCALA: case "0" => running = false
            # PYTHON: case "0": running = False
            # Both set the mutable flag to False to stop the while loop
            case "0":
                print(f"\n  👋 Goodbye, {staff_name}! Keep helping pets find homes! 🐾")
                running = False             # SCALA: running = false

            # ── default / invalid input ───────────────
            # SCALA: case _ => println("Invalid choice.")
            # PYTHON: case _: print("Invalid choice.")
            # _ = wildcard — matches ANYTHING not listed above
            case _:
                print("  ❌ Invalid choice. Please enter a number from the menu.")


# =====================================================
# ENTRY POINT
# =====================================================
#
#  SCALA:  object PetAdoptionRegistry extends App { ... }
#          The code runs automatically when the object is loaded.
#
#  PYTHON: if __name__ == "__main__":
#              main()
#          This block only runs when the file is executed directly,
#          NOT when it is imported by another file.
#          It is the Python equivalent of "extends App".
# =====================================================

if __name__ == "__main__":
    main()
