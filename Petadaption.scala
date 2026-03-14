import scala.io.StdIn.readLine
import scala.collection.mutable.ListBuffer

// =====================================================
// 1. DATA MODEL — case class
// =====================================================
case class AdopterDetails(
  fullname   : String,
  contact    : String,
  email      : String,
  dob        : String,
  address    : String,
  occupation : String,
  living     : String,
  reason     : String
)

case class Pet(
  id      : Int,
  name    : String,
  species : String,
  breed   : String,
  age     : Int,
  gender  : String,
  desc    : String,
  vaccinated       : Boolean = false,
  var isAdopted    : Boolean = false,
  var adoptedBy    : String  = "",
  var adopterDetails: Option[AdopterDetails] = None
)

// =====================================================
// 2. PET REGISTRY — object (singleton)
// =====================================================
object PetRegistry {

  val pets: ListBuffer[Pet] = ListBuffer(

    Pet(1, "Bonjong",  "Dog",    "Belgian Malinois", 2, "Male",
        "Friendly and loves to play fetch! Great with children.",
        vaccinated = true),

    Pet(2, "Whiskers", "Cat",    "Siamese",          3, "Female",
        "Calm and loves cuddles. Perfect indoor companion.",
        vaccinated = true),

    Pet(3, "Thumper",  "Rabbit", "Holland Lop",      1, "Male",
        "Very active and playful. Loves hopping around the garden.",
        vaccinated = false),

    Pet(4, "Luna",     "Dog",    "Dachshund",        4, "Female",
        "Great with kids and families. Calm and well-trained.",
        vaccinated = true),

    Pet(5, "Milo",     "Cat",    "Persian",          5, "Male",
        "Laid-back and loves napping by the window.",
        vaccinated = true, isAdopted = true, adoptedBy = "Kc Vargas",
        adopterDetails = Some(AdopterDetails(
          fullname   = "Kc Vargas",
          contact    = "09171234567",
          email      = "kc.vargas@email.com",
          dob        = "1990-05-14",
          address    = "123 Mango St., Barangay Poblacion, Davao City",
          occupation = "Nurse",
          living     = "House with yard",
          reason     = "I have always loved cats and Milo felt like the perfect fit!"
        ))),

    Pet(6, "Mochi",    "Dog",    "Shi-poo",          2, "Female",
        "Energetic and loves outdoor walks. Always wagging her tail!",
        vaccinated = false),

    Pet(7, "Nemo",     "Fish",   "Goldfish",         1, "Male",
        "Beautiful orange and white colors. Very soothing to watch.",
        vaccinated = false),

    Pet(8, "Daisy",    "Rabbit", "Mini Rex",         2, "Female",
        "Gentle and easy to care for. Loves soft petting.",
        vaccinated = true, isAdopted = true, adoptedBy = "Erikka Dela Cruz",
        adopterDetails = Some(AdopterDetails(
          fullname   = "Erikka Dela Cruz",
          contact    = "09289876543",
          email      = "erikka.dela.cruz@email.com",
          dob        = "1988-11-22",
          address    = "45 Rizal Ave., Toril, Davao City",
          occupation = "Engineer",
          living     = "House with yard",
          reason     = "My kids have been begging for a rabbit. Daisy is perfect!"
        )))
  )

  def findById(id: Int): Option[Pet]     = pets.find(_.id == id)
  def findBySpecies(s: String): List[Pet]= pets.filter(_.species.toLowerCase == s.toLowerCase).toList
  def search(keyword: String): List[Pet] = {
    val kw = keyword.toLowerCase
    pets.filter(p =>
      p.name.toLowerCase.contains(kw)    ||
      p.breed.toLowerCase.contains(kw)   ||
      p.species.toLowerCase.contains(kw)
    ).toList
  }

  def available   : List[Pet] = pets.filter(!_.isAdopted).toList
  def adopted     : List[Pet] = pets.filter(_.isAdopted).toList
  def vaccinated  : List[Pet] = pets.filter(_.vaccinated).toList
  def addPet(p: Pet): Unit    = pets += p
  def nextId      : Int       = if (pets.isEmpty) 1 else pets.map(_.id).max + 1

  def totalPets       : Int = pets.size
  def totalAvailable  : Int = available.size
  def totalAdopted    : Int = adopted.size
  def totalVaccinated : Int = vaccinated.size
}

// =====================================================
// 3. DISPLAY HELPER — object
// =====================================================
object Display {

  val W = 54

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
      f"|  Available  : ${PetRegistry.totalAvailable}%3d  " +
      f"|  Adopted    : ${PetRegistry.totalAdopted}%3d  " +
      f"|  Vaccinated : ${PetRegistry.totalVaccinated}%3d"
    )
    divider('=')
  }

  def printPet(p: Pet): Unit = {
    val vaccLabel   = if (p.vaccinated)  "Yes"        else "No"
    val ageLabel    = if (p.age <= 2)    " [Young]"   else ""
    val adoptedMark = if (p.isAdopted)   " [ADOPTED]" else ""
    val status      = if (p.isAdopted)   s"Adopted by ${p.adoptedBy}" else "Available for adoption"

    divider()
    println(s"  ID          : #${p.id}")
    println(s"  Name        : ${p.name}$ageLabel$adoptedMark")
    println(s"  Species     : ${p.species} -- ${p.breed}")
    println(s"  Age         : ${p.age} yr(s)  |  Gender: ${p.gender}")
    println(s"  Vaccinated  : $vaccLabel")
    println(s"  About       : ${p.desc}")
    println(s"  Status      : $status")

    // Show full adopter info if adopted
    p.adopterDetails.foreach { d =>
      divider()
      println(s"  -- ADOPTER INFORMATION --")
      println(s"  Full Name    : ${d.fullname}")
      println(s"  Contact      : ${d.contact}")
      println(s"  Email        : ${d.email}")
      println(s"  Date of Birth: ${d.dob}")
      println(s"  Address      : ${d.address}")
      println(s"  Occupation   : ${d.occupation}")
      println(s"  Living       : ${d.living}")
      println(s"  Reason       : ${d.reason}")
    }
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
    println("  [8]  View Vaccinated Pets Only")
    println("  [0]  Exit")
    divider()
  }
}

// =====================================================
// 4. MAIN APP
// =====================================================
object Petadoption extends App {

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
    print("\n  Enter your choice: ")
    val choice = readLine().trim

    choice match {

      // ── 1. View All Pets ────────────────────────
      case "1" =>
        println("\n  >> All Pets in the Registry:")
        Display.printList(PetRegistry.pets.toList, "No pets registered yet.")

      // ── 2. Filter by Species ─────────────────────
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
        if (species.isEmpty) println("  >> Invalid choice.")
        else {
          val results = PetRegistry.findBySpecies(species).filter(!_.isAdopted)
          println(s"\n  >> Available $species(s):")
          Display.printList(results, s"No available $species found.")
        }

      // ── 3. Search ────────────────────────────────
      case "3" =>
        print("\n  Enter keyword (name / breed / species): ")
        val keyword = readLine().trim
        if (keyword.isEmpty) println("  >> Please enter a search keyword.")
        else {
          val results = PetRegistry.search(keyword)
          println(s"\n  >> Search results for '$keyword':")
          Display.printList(results, s"No pets found matching '$keyword'.")
        }

      // ── 4. View by ID ────────────────────────────
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

      // ── 5. Adopt a Pet ───────────────────────────
      case "5" =>
        println("\n  >> Available Pets:")
        Display.printList(PetRegistry.available, "No pets available for adoption.")
        if (PetRegistry.available.nonEmpty) {
          print("  Enter the ID of the pet to adopt: ")
          val id = readLine().trim.toIntOption.getOrElse(-1)
          PetRegistry.findById(id) match {
            case Some(p) if !p.isAdopted =>
              Display.divider()
              println("  -- ADOPTER INFORMATION --")
              Display.divider()
              print("  Full Name        : "); val fullname   = readLine().trim match { case "" => "Anonymous"; case n => n }
              print("  Contact Number   : "); val contact    = readLine().trim
              print("  Email Address    : "); val email      = readLine().trim
              print("  Date of Birth    : "); val dob        = readLine().trim
              print("  Complete Address : "); val address    = readLine().trim
              print("  Occupation       : "); val occupation = readLine().trim
              println("  Living Situation: [1] House  [2] Apartment/Condo  [3] Farm")
              print("  Choose           : ")
              val living = readLine().trim match {
                case "1" => "House"
                case "2" => "Apartment/Condo"
                case "3" => "Farm"
                case _   => "House"
              }
              print("  Reason for Adopting: "); val reason = readLine().trim

              p.isAdopted     = true
              p.adoptedBy     = fullname
              p.adopterDetails= Some(AdopterDetails(
                fullname, contact, email, dob, address, occupation, living, reason
              ))
              Display.divider('=')
              println(s"  Congratulations! ${p.name} has been adopted by $fullname!")
              println(s"  Thank you for giving ${p.name} a loving home!")
              Display.divider('=')

            case Some(_) =>
              println("  >> Sorry, that pet has already been adopted.")
            case None =>
              println(s"  >> No pet found with ID #$id.")
          }
        }

      // ── 6. Register a New Pet ────────────────────
      case "6" =>
        println()
        Display.divider()
        println("  Register a New Pet")
        Display.divider()
        print("  Pet Name       : "); val name = readLine().trim
        println("  Species: [1] Dog  [2] Cat  [3] Rabbit  [4] Fish  [5] Other")
        print("  Choose         : ")
        val species = readLine().trim match {
          case "1" => "Dog";    case "2" => "Cat"
          case "3" => "Rabbit"; case "4" => "Fish"; case _ => "Other"
        }
        print("  Breed          : "); val breed = readLine().trim
        print("  Age (years)    : ")
        val age = readLine().trim.toIntOption.getOrElse(0)
        println("  Gender: [1] Male  [2] Female")
        print("  Choose         : ")
        val gender = if (readLine().trim == "1") "Male" else "Female"
        println("  Vaccinated? [1] Yes  [2] No")
        print("  Choose         : ")
        val vaccinated = readLine().trim == "1"
        print("  Description    : "); val desc = readLine().trim

        if (name.isEmpty || breed.isEmpty || desc.isEmpty) {
          println("  >> Name, breed, and description are required!")
        } else {
          val newPet = Pet(PetRegistry.nextId, name, species, breed, age, gender, desc, vaccinated)
          PetRegistry.addPet(newPet)
          Display.divider('=')
          println(s"  $name has been registered with ID #${newPet.id}!")
          Display.divider('=')
        }

      // ── 7. View Adopted Pets ─────────────────────
      case "7" =>
        println("\n  >> Adopted Pets:")
        Display.printList(PetRegistry.adopted, "No pets have been adopted yet.")

      // ── 8. View Vaccinated Pets ──────────────────
      case "8" =>
        println("\n  >> Vaccinated Pets:")
        Display.printList(PetRegistry.vaccinated, "No vaccinated pets found.")

      // ── 0. Exit ──────────────────────────────────
      case "0" =>
        Display.divider('=')
        println(s"  Goodbye, $staffName! Keep helping pets find homes!")
        Display.divider('=')
        running = false

      case _ =>
        println("  >> Invalid choice. Please enter a number from the menu.")
    }
  }
}
