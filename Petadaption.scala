// =====================================================
//   🐾 HAPPY PAWS — Pet Adoption Registry
//   Pure Scala CLI — converted from Web UI
// =====================================================
//
//  WEB UI FEATURE → SCALA EQUIVALENT
//  ─────────────────────────────────────────────────
//  View All Pets     → Menu option 1
//  Filter by species → Menu option 2 (Dog/Cat/etc.)
//  Search by name    → Menu option 3
//  View pet by ID    → Menu option 4
//  Adopt a Pet       → Menu option 5
//  Add New Pet       → Menu option 6
//  View Adopted Pets → Menu option 7
//  Live Stats Banner → Shown on every menu screen
// =====================================================

import scala.io.StdIn.readLine
import scala.collection.mutable.ListBuffer

// =====================================================
// 1. DATA MODEL — case class
// =====================================================
// case class  = blueprint for storing data
// var         = field that CAN be changed later
// val         = field that CANNOT be changed
// String      = text   |  Int = whole number
// Boolean     = true/false  |  = "" means default value

case class Pet(
  id      : Int,
  name    : String,
  species : String,
  breed   : String,
  age     : Int,
  gender  : String,
  desc    : String,
  var isAdopted : Boolean = false,   // default = false
  var adoptedBy : String  = ""       // default = empty
)

// =====================================================
// 2. PET REGISTRY — object (singleton)
// =====================================================
// object      = a single shared module (no need for "new")
// ListBuffer  = a mutable list (can add / remove items)
// List[Pet]   = a list that holds Pet items

object PetRegistry {

  // Pre-loaded pets — same as the web UI data
  val pets: ListBuffer[Pet] = ListBuffer(
    Pet(1, "Buddy",    "Dog",    "Golden Retriever", 2, "Male",   "Friendly and loves to play fetch!"),
    Pet(2, "Whiskers", "Cat",    "Siamese",          3, "Female", "Calm and loves cuddles."),
    Pet(3, "Thumper",  "Rabbit", "Holland Lop",      1, "Male",   "Very active and playful."),
    Pet(4, "Luna",     "Dog",    "Labrador",         4, "Female", "Great with kids and families."),
    Pet(5, "Milo",     "Cat",    "Persian",          5, "Male",   "Laid-back and loves napping.",    true, "Sarah J."),
    Pet(6, "Coco",     "Dog",    "Beagle",           2, "Female", "Energetic and loves outdoor walks."),
    Pet(7, "Nemo",     "Fish",   "Goldfish",         1, "Male",   "Beautiful orange and white colors."),
    Pet(8, "Daisy",    "Rabbit", "Mini Rex",         2, "Female", "Gentle and easy to care for.",    true, "Tom L.")
  )

  // ── find one pet by ID ──────────────────────────
  // Option[Pet] = either Some(pet) if found, or None
  // .find()     = returns the FIRST item that matches
  // _.id        = shorthand for "each pet's id field"
  def findById(id: Int): Option[Pet] =
    pets.find(_.id == id)

  // ── filter pets by species ──────────────────────
  // .filter()       = keep only items that match
  // .toLowerCase    = makes search case-insensitive
  // .toList         = convert ListBuffer to List
  def findBySpecies(species: String): List[Pet] =
    pets.filter(_.species.toLowerCase == species.toLowerCase).toList

  // ── search pets by keyword ──────────────────────
  // .contains()  = checks if a string has the keyword
  // ||           = OR — match name OR breed OR species
  def search(keyword: String): List[Pet] = {
    val kw = keyword.toLowerCase
    pets.filter { p =>
      p.name.toLowerCase.contains(kw)    ||
      p.breed.toLowerCase.contains(kw)   ||
      p.species.toLowerCase.contains(kw)
    }.toList
  }

  // ── only pets that are available ────────────────
  // !p.isAdopted = pets where isAdopted is false
  def available: List[Pet] = pets.filter(!_.isAdopted).toList

  // ── only pets that are adopted ──────────────────
  def adopted: List[Pet] = pets.filter(_.isAdopted).toList

  // ── add a new pet to the registry ───────────────
  // += is the ListBuffer "append" operator
  def addPet(p: Pet): Unit = pets += p

  // ── auto-generate the next available ID ─────────
  // .map(_.id) = extract all id values into a list
  // .max       = get the biggest number in that list
  def nextId: Int =
    if (pets.isEmpty) 1 else pets.map(_.id).max + 1

  // ── live stats (shown in the header) ────────────
  def totalPets     : Int = pets.size
  def totalAvailable: Int = available.size
  def totalAdopted  : Int = adopted.size
}

// =====================================================
// 3. DISPLAY HELPER — object
// =====================================================
// Handles all the printing / formatting logic

object Display {

  // ── emoji map — species to emoji ────────────────
  // Map[String, String] = a key-value dictionary
  val emojiMap: Map[String, String] = Map(
    "Dog"    -> "🐶",
    "Cat"    -> "🐱",
    "Rabbit" -> "🐰",
    "Fish"   -> "🐟"
  )

  // .getOrElse = use the value if key exists,
  //              otherwise use the fallback "🐾"
  def emoji(species: String): String =
    emojiMap.getOrElse(species, "🐾")

  // ── print the stats banner (like the web hero) ───
  def printStats(): Unit = {
    println("\n  " + "=" * 52)
    println("      🐾  HAPPY PAWS — Pet Adoption Registry")
    println("      Every pet deserves a loving home! 💛")
    println("  " + "=" * 52)
    // f"..." = formatted string interpolation
    // %3d = integer with 3-character width padding
    println(f"   📊 Total: ${PetRegistry.totalPets}%3d  " +
            f"| ✅ Available: ${PetRegistry.totalAvailable}%3d  " +
            f"| ❤️  Adopted: ${PetRegistry.totalAdopted}%3d")
    println("  " + "=" * 52)
  }

  // ── print a single pet card ──────────────────────
  // if / else used as an expression returning a value
  def printPet(p: Pet): Unit = {
    val status =
      if (p.isAdopted) s"❤️  Adopted by ${p.adoptedBy}"
      else             "✅ Available for adoption"

    val ageLabel = if (p.age <= 2) " 🌱 Young" else ""

    println(s"\n  ${emoji(p.species)} [${p.id}] ${p.name}$ageLabel")
    println(s"      Species : ${p.species} — ${p.breed}")
    println(s"      Age     : ${p.age} yr(s)  |  Gender: ${p.gender}")
    println(s"      About   : ${p.desc}")
    println(s"      Status  : $status")
  }

  // ── print a list of pets ─────────────────────────
  // foreach = loop through every item in the list
  def printList(pets: List[Pet], emptyMsg: String): Unit = {
    if (pets.isEmpty)
      println(s"\n  🔍 $emptyMsg")
    else
      pets.foreach(printPet)   // call printPet for each pet
  }

  // ── print the main menu ──────────────────────────
  def printMenu(): Unit = {
    println("\n  ── MAIN MENU ───────────────────────────────")
    println("  [1] 🐾 View All Pets")
    println("  [2] 🔎 Filter by Species")
    println("  [3] 🔍 Search by Name / Breed")
    println("  [4] 📋 View Pet Details by ID")
    println("  [5] ❤️  Adopt a Pet")
    println("  [6] ➕ Register a New Pet")
    println("  [7] 🏠 View Adopted Pets")
    println("  [0] 👋 Exit")
    print("\n  Enter your choice: ")
  }
}

// =====================================================
// 4. MAIN APP — object with App trait
// =====================================================
// extends App = makes this the entry point of the program
// readLine()  = reads a line of text the user types
// .trim       = removes leading/trailing whitespace

object PetAdoptionRegistry extends App {

  // ── welcome screen ───────────────────────────────
  Display.printStats()
  print("\n  Welcome! What is your name? ")

  // match / case = pattern matching (like a smart switch)
  // case ""  = if the user typed nothing
  // case n   = capture the input as variable n
  val staffName = readLine().trim match {
    case "" => "Guest"
    case n  => n
  }
  println(s"\n  Hello, $staffName! Welcome to Happy Paws 🐶🐱🐰")

  // ── main loop ────────────────────────────────────
  // var running = true  → mutable flag to keep loop alive
  // while(running)      → keep looping until running=false
  var running = true

  while (running) {
    Display.printStats()   // show live stats on every screen
    Display.printMenu()

    val choice = readLine().trim

    // match on the user's choice
    choice match {

      // ── [1] VIEW ALL PETS ───────────────────────
      case "1" =>
        println("\n  🐾 All Pets in the Registry:")
        println("  " + "─" * 48)
        // .toList converts ListBuffer to an immutable List
        Display.printList(PetRegistry.pets.toList, "No pets registered yet.")

      // ── [2] FILTER BY SPECIES ───────────────────
      case "2" =>
        println("\n  Filter by Species:")
        println("  [1] 🐶 Dog   [2] 🐱 Cat")
        println("  [3] 🐰 Rabbit  [4] 🐟 Fish  [5] 🐾 Other")
        print("  Choose: ")

        // match the species choice to a species name string
        val species = readLine().trim match {
          case "1" => "Dog"
          case "2" => "Cat"
          case "3" => "Rabbit"
          case "4" => "Fish"
          case "5" => "Other"
          case _   => ""   // _ = catch-all / default case
        }

        if (species.isEmpty) {
          println("  ❌ Invalid choice.")
        } else {
          val results = PetRegistry.findBySpecies(species)
                                   .filter(!_.isAdopted)
          println(s"\n  ${Display.emoji(species)} Available $species(s):")
          println("  " + "─" * 48)
          Display.printList(results, s"No available $species found.")
        }

      // ── [3] SEARCH ──────────────────────────────
      case "3" =>
        print("\n  🔍 Enter keyword (name / breed / species): ")
        val keyword = readLine().trim

        if (keyword.isEmpty) {
          println("  ❌ Please enter a search keyword.")
        } else {
          val results = PetRegistry.search(keyword)
          println(s"\n  Search results for '$keyword':")
          println("  " + "─" * 48)
          Display.printList(results, s"No pets found matching '$keyword'.")
        }

      // ── [4] VIEW PET BY ID ──────────────────────
      case "4" =>
        print("\n  Enter Pet ID: ")

        // .toIntOption = safely parse a String to Int
        // returns Some(number) or None if parsing fails
        val id = readLine().trim.toIntOption.getOrElse(-1)

        // Option pattern matching: Some(p) or None
        PetRegistry.findById(id) match {
          case Some(p) =>
            println("\n  📋 Pet Details:")
            println("  " + "─" * 48)
            Display.printPet(p)
          case None =>
            println(s"  ❌ No pet found with ID #$id.")
        }

      // ── [5] ADOPT A PET ─────────────────────────
      case "5" =>
        println("\n  ✅ Available Pets:")
        println("  " + "─" * 48)
        Display.printList(PetRegistry.available, "No pets available for adoption.")

        // .nonEmpty = true if the list has at least 1 item
        if (PetRegistry.available.nonEmpty) {
          print("\n  Enter the ID of the pet to adopt: ")
          val id = readLine().trim.toIntOption.getOrElse(-1)

          PetRegistry.findById(id) match {

            // guard: pet found AND not yet adopted
            // "if !p.isAdopted" is called a GUARD condition
            case Some(p) if !p.isAdopted =>
              print(s"  Enter adopter's full name: ")
              val adopter = readLine().trim match {
                case "" => "Anonymous"
                case n  => n
              }
              // Update the mutable fields directly
              p.isAdopted = true
              p.adoptedBy = adopter
              println(s"\n  🎉 Congratulations! ${p.name} has been adopted by $adopter!")
              println(s"  💛 Thank you for giving ${p.name} a loving home!")

            // pet found BUT already adopted
            case Some(_) =>
              println("  ❌ Sorry, that pet has already been adopted.")

            // pet not found at all
            case None =>
              println(s"  ❌ No pet found with ID #$id.")
          }
        }

      // ── [6] REGISTER A NEW PET ──────────────────
      case "6" =>
        println("\n  ➕ Register a New Pet")
        println("  " + "─" * 40)

        print("  Pet Name       : "); val name = readLine().trim

        println("  Species:")
        println("  [1] Dog  [2] Cat  [3] Rabbit  [4] Fish  [5] Other")
        print("  Choose         : ")
        val species = readLine().trim match {
          case "1" => "Dog"
          case "2" => "Cat"
          case "3" => "Rabbit"
          case "4" => "Fish"
          case _   => "Other"
        }

        print("  Breed          : "); val breed = readLine().trim
        print("  Age (years)    : ")
        val age = readLine().trim.toIntOption.getOrElse(0)

        println("  Gender: [1] Male  [2] Female")
        print("  Choose         : ")
        val gender = readLine().trim match {
          case "1" => "Male"
          case _   => "Female"
        }

        print("  Description    : "); val desc = readLine().trim

        // Validate required fields are not empty
        if (name.isEmpty || breed.isEmpty || desc.isEmpty) {
          println("  ❌ Name, breed, and description are required!")
        } else {
          // Create a new Pet instance and add it
          val newPet = Pet(PetRegistry.nextId, name, species, breed, age, gender, desc)
          PetRegistry.addPet(newPet)
          println(s"\n  ✅ $name has been registered with ID #${newPet.id}!")
        }

      // ── [7] VIEW ADOPTED PETS ───────────────────
      case "7" =>
        println("\n  ❤️  Adopted Pets:")
        println("  " + "─" * 48)
        Display.printList(PetRegistry.adopted, "No pets have been adopted yet.")

      // ── [0] EXIT ────────────────────────────────
      case "0" =>
        println(s"\n  👋 Goodbye, $staffName! Keep helping pets find homes! 🐾")
        running = false   // stops the while loop

      // ── default: invalid input ───────────────────
      // _ matches ANYTHING not listed above
      case _ =>
        println("  ❌ Invalid choice. Please enter a number from the menu.")
    }
  }
}