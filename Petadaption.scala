// =====================================================
//   HAPPY PAWS — Pet Adoption Registry
//   by: Scalers
// =====================================================

import scala.io.StdIn.readLine
import scala.collection.mutable.ListBuffer

// =====================================================
// 1. DATA MODEL — case class
// =====================================================
case class Pet(
  id      : Int,
  name    : String,
  species : String,
  breed   : String,
  age     : Int,
  gender  : String,
  desc    : String,
  var isAdopted : Boolean = false,
  var adoptedBy : String  = ""
)

// =====================================================
// 2. PET REGISTRY — object (singleton)
// =====================================================
object PetRegistry {

  val pets: ListBuffer[Pet] = ListBuffer(
    Pet(1, "Tokkio", "Dog",    "Golden Retriever", 2, "Male",   "Friendly and loves to play fetch!"),
    Pet(2, "BB",     "Cat",    "Siamese",          3, "Female", "Calm and loves cuddles."),
    Pet(3, "Bunny",  "Rabbit", "American",         1, "Male",   "Very active and playful."),
    Pet(4, "Luna",   "Dog",    "Dachshund",         4, "Female", "Great with kids and families."),
    Pet(5, "Milo",   "Cat",    "Persian",          5, "Male",   "Laid-back and loves napping.",   true, "Sarah J."),
    Pet(6, "Coco",   "Dog",    "Beagle",           2, "Female", "Energetic and loves outdoor walks."),
    Pet(7, "Nemo",   "Fish",   "Goldfish",         1, "Male",   "Beautiful orange and white colors."),
    Pet(8, "Daisy",  "Rabbit", "Cinnamon",         2, "Female", "Gentle and easy to care for.",   true, "Tom L.")
  )

  def findById(id: Int): Option[Pet]       = pets.find(_.id == id)
  def findBySpecies(species: String): List[Pet] =
    pets.filter(_.species.toLowerCase == species.toLowerCase).toList

  def search(keyword: String): List[Pet] = {
    val kw = keyword.toLowerCase
    pets.filter { p =>
      p.name.toLowerCase.contains(kw)  ||
      p.breed.toLowerCase.contains(kw) ||
      p.species.toLowerCase.contains(kw)
    }.toList
  }

  def available: List[Pet]  = pets.filter(!_.isAdopted).toList
  def adopted  : List[Pet]  = pets.filter(_.isAdopted).toList
  def addPet(p: Pet): Unit  = pets += p
  def nextId: Int           = if (pets.isEmpty) 1 else pets.map(_.id).max + 1

  def totalPets     : Int = pets.size
  def totalAvailable: Int = available.size
  def totalAdopted  : Int = adopted.size
}

// =====================================================
// 3. DISPLAY HELPER — object
// =====================================================
object Display {

  val W = 54  // console width

  def divider(char: Char = '-'): Unit =
    println("  " + char.toString * W)

  def printStats(): Unit = {
    divider('=')
    println(s"  ${"HAPPY PAWS -- Pet Adoption Registry".padTo(W, ' ')}")
    println(s"  ${"Every pet deserves a loving home!".padTo(W, ' ')}")
    println(s"  ${"by: Scalers".padTo(W, ' ')}")
    divider('=')
    println(
      f"  Total : ${PetRegistry.totalPets}%3d  " +
      f"|  Available : ${PetRegistry.totalAvailable}%3d  " +
      f"|  Adopted : ${PetRegistry.totalAdopted}%3d"
    )
    divider('=')
  }

  def printPet(p: Pet): Unit = {
    val status      = if (p.isAdopted) s"Adopted by ${p.adoptedBy}" else "Available for adoption"
    val ageLabel    = if (p.age <= 2) " [Young]" else ""
    val adoptedMark = if (p.isAdopted) " [ADOPTED]" else ""

    divider()
    println(s"  ID      : #${p.id}")
    println(s"  Name    : ${p.name}$ageLabel$adoptedMark")
    println(s"  Species : ${p.species} -- ${p.breed}")
    println(s"  Age     : ${p.age} yr(s)  |  Gender: ${p.gender}")
    println(s"  About   : ${p.desc}")
    println(s"  Status  : $status")
  }

  def printList(pets: List[Pet], emptyMsg: String): Unit = {
    if (pets.isEmpty) {
      divider()
      println(s"  >> $emptyMsg")
      divider()
    } else {
      pets.foreach(printPet)
      divider()
    }
  }

  def printMenu(): Unit = {
    println()
    divider()
    println(s"  ${"-- MAIN MENU --".padTo(W, ' ')}")
    divider()
    println("  [1]  View All Pets")
    println("  [2]  Filter by Species")
    println("  [3]  Search by Name / Breed")
    println("  [4]  View Pet Details by ID")
    println("  [5]  Adopt a Pet")
    println("  [6]  Register a New Pet")
    println("  [7]  View Adopted Pets")
    println("  [0]  Exit")
    divider()
  }
}

// =====================================================
// 4. MAIN APP
// =====================================================
object Petadaption extends App {

  Display.printStats()
  print("\n  Welcome! What is your name? ")

  val staffName = readLine().trim match {
    case "" => "Guest"
    case n  => n
  }
  println(s"\n  Hello, $staffName! Welcome to Happy Paws.")

  var running = true

  while (running) {

    Display.printStats()
    Display.printMenu()

    val choice = readLine().trim

    choice match {

      // ── [1] VIEW ALL PETS ───────────────────────
      case "1" =>
        println("\n  >> All Pets in the Registry:")
        Display.printList(PetRegistry.pets.toList, "No pets registered yet.")

      // ── [2] FILTER BY SPECIES ───────────────────
      case "2" =>
        println()
        Display.divider()
        println("  Filter by Species:")
        println("  [1] Dog   [2] Cat   [3] Rabbit   [4] Fish   [5] Other")
        Display.divider()
        print("  Choose: ")

        val species = readLine().trim match {
          case "1" => "Dog"
          case "2" => "Cat"
          case "3" => "Rabbit"
          case "4" => "Fish"
          case "5" => "Other"
          case _   => ""
        }

        if (species.isEmpty) {
          println("  >> Invalid choice.")
        } else {
          val results = PetRegistry.findBySpecies(species).filter(!_.isAdopted)
          println(s"\n  >> Available $species(s):")
          Display.printList(results, s"No available $species found.")
        }

      // ── [3] SEARCH ──────────────────────────────
      case "3" =>
        print("\n  Enter keyword (name / breed / species): ")
        val keyword = readLine().trim

        if (keyword.isEmpty) {
          println("  >> Please enter a search keyword.")
        } else {
          val results = PetRegistry.search(keyword)
          println(s"\n  >> Search results for '$keyword':")
          Display.printList(results, s"No pets found matching '$keyword'.")
        }

      // ── [4] VIEW PET BY ID ──────────────────────
      case "4" =>
        print("\n  Enter Pet ID: ")
        val id = readLine().trim.toIntOption.getOrElse(-1)

        PetRegistry.findById(id) match {
          case Some(p) =>
            println("\n  >> Pet Details:")
            Display.printPet(p)
            Display.divider()
          case None =>
            println(s"  >> No pet found with ID #$id.")
        }

      // ── [5] ADOPT A PET ─────────────────────────
      case "5" =>
        println("\n  >> Available Pets:")
        Display.printList(PetRegistry.available, "No pets available for adoption.")

        if (PetRegistry.available.nonEmpty) {
          print("  Enter the ID of the pet to adopt: ")
          val id = readLine().trim.toIntOption.getOrElse(-1)

          PetRegistry.findById(id) match {
            case Some(p) if !p.isAdopted =>
              print("  Enter adopter's full name: ")
              val adopter = readLine().trim match {
                case "" => "Anonymous"
                case n  => n
              }
              p.isAdopted = true
              p.adoptedBy = adopter
              Display.divider('=')
              println(s"  Congratulations! ${p.name} has been adopted by $adopter!")
              println(s"  Thank you for giving ${p.name} a loving home!")
              Display.divider('=')

            case Some(_) =>
              println("  >> Sorry, that pet has already been adopted.")

            case None =>
              println(s"  >> No pet found with ID #$id.")
          }
        }

      // ── [6] REGISTER A NEW PET ──────────────────
      case "6" =>
        println()
        Display.divider()
        println("  Register a New Pet")
        Display.divider()

        print("  Pet Name       : "); val name = readLine().trim

        println("  Species: [1] Dog  [2] Cat  [3] Rabbit  [4] Fish  [5] Other")
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

        if (name.isEmpty || breed.isEmpty || desc.isEmpty) {
          println("  >> Name, breed, and description are required!")
        } else {
          val newPet = Pet(PetRegistry.nextId, name, species, breed, age, gender, desc)
          PetRegistry.addPet(newPet)
          Display.divider('=')
          println(s"  $name has been registered with ID #${newPet.id}!")
          Display.divider('=')
        }

      // ── [7] VIEW ADOPTED PETS ───────────────────
      case "7" =>
        println("\n  >> Adopted Pets:")
        Display.printList(PetRegistry.adopted, "No pets have been adopted yet.")

      // ── [0] EXIT ────────────────────────────────
      case "0" =>
        Display.divider('=')
        println(s"  Goodbye, $staffName! Keep helping pets find homes!")
        Display.divider('=')
        running = false

      // ── DEFAULT ─────────────────────────────────
      case _ =>
        println("  >> Invalid choice. Please enter a number from the menu.")
    }
  }
}
