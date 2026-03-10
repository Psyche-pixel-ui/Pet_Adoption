// =====================================================
//   🐾 HAPPY PAWS — Pet Adoption Registry
//   Web UI version — mirrored from Petadaption.scala
//   Group: Scalers
// =====================================================
//
//  SCALA STRUCTURE         → JAVASCRIPT EQUIVALENT
//  ─────────────────────────────────────────────────
//  case class Pet          → Pet object literal / {}
//  object PetRegistry      → const PetRegistry = {}
//  object Display          → const Display = {}
//  object PetAdoptionRegistry extends App → init() + event listeners
//
//  import scala.io.StdIn.readLine       → HTML input / form fields
//  import scala.collection.mutable.ListBuffer → JavaScript Array []
// =====================================================


// =====================================================
// 1. DATA MODEL — case class Pet
// =====================================================
// SCALA:
//   case class Pet(
//     id      : Int,
//     name    : String,
//     species : String,
//     breed   : String,
//     age     : Int,
//     gender  : String,
//     desc    : String,
//     vaccinated  : Boolean = false,
//     var isAdopted : Boolean = false,
//     var adoptedBy : String  = ""
//   )
//
// case class  = blueprint for data; auto-generates equals/toString/copy
// val         = field that CANNOT change (id, name, species, etc.)
// var         = field that CAN change (isAdopted, adoptedBy)
// Boolean     = true / false
// String      = text  |  Int = whole number
// = false / = "" = default values if not provided
// =====================================================

// In JavaScript, we represent each Pet as a plain object {}.
// Fields marked "var" in Scala (isAdopted, adoptedBy, adopterDetails)
// are the ones we mutate when a pet gets adopted.

const PetRegistry = {

  // =====================================================
  // 2. PET REGISTRY — object PetRegistry
  // =====================================================
  // SCALA:
  //   object PetRegistry {
  //     val pets: ListBuffer[Pet] = ListBuffer(
  //       Pet(1, "Buddy", "Dog", "Golden Retriever", 2, "Male", "..."),
  //       ...
  //     )
  //   }
  //
  // object     = singleton — only one instance, no "new" needed
  // ListBuffer = mutable list (can add / remove items)
  // List[Pet]  = a list that holds Pet items
  // val pets   = the registry itself (the list)
  // =====================================================

  pets: [
    { id:1, name:"Buddy",    species:"Dog",    breed:"Golden Retriever", age:2, gender:"Male",   desc:"Friendly and loves to play fetch! Great with children.",      vaccinated:true,  isAdopted:false, adoptedBy:"", adopterDetails:null },
    { id:2, name:"Whiskers", species:"Cat",    breed:"Siamese",          age:3, gender:"Female", desc:"Calm and loves cuddles. Perfect indoor companion.",           vaccinated:true,  isAdopted:false, adoptedBy:"", adopterDetails:null },
    { id:3, name:"Thumper",  species:"Rabbit", breed:"Holland Lop",      age:1, gender:"Male",   desc:"Very active and playful. Loves hopping around the garden.",  vaccinated:false, isAdopted:false, adoptedBy:"", adopterDetails:null },
    { id:4, name:"Luna",     species:"Dog",    breed:"Labrador",         age:4, gender:"Female", desc:"Great with kids and families. Calm and well-trained.",        vaccinated:true,  isAdopted:false, adoptedBy:"", adopterDetails:null },
    { id:5, name:"Milo",     species:"Cat",    breed:"Persian",          age:5, gender:"Male",   desc:"Laid-back and loves napping by the window.",                 vaccinated:true,  isAdopted:true,  adoptedBy:"Sarah J.", adopterDetails:{ fullname:"Sarah Johnson", contact:"09171234567", email:"sarah.j@email.com", dob:"1990-05-14", address:"123 Mango St., Barangay Poblacion, Davao City", occupation:"Nurse",    living:"House with yard",    reason:"I have always loved cats and Milo felt like the perfect fit!" } },
    { id:6, name:"Coco",     species:"Dog",    breed:"Beagle",           age:2, gender:"Female", desc:"Energetic and loves outdoor walks. Always wagging her tail!", vaccinated:false, isAdopted:false, adoptedBy:"", adopterDetails:null },
    { id:7, name:"Nemo",     species:"Fish",   breed:"Goldfish",         age:1, gender:"Male",   desc:"Beautiful orange and white colors. Very soothing to watch.", vaccinated:false, isAdopted:false, adoptedBy:"", adopterDetails:null },
    { id:8, name:"Daisy",    species:"Rabbit", breed:"Mini Rex",         age:2, gender:"Female", desc:"Gentle and easy to care for. Loves soft petting.",           vaccinated:true,  isAdopted:true,  adoptedBy:"Tom L.",   adopterDetails:{ fullname:"Tom Ladera",    contact:"09289876543", email:"tomladera@email.com",  dob:"1988-11-22", address:"45 Rizal Ave., Toril, Davao City",                     occupation:"Engineer", living:"House with yard",    reason:"My kids have been begging for a rabbit. Daisy is perfect!" } },
  ],

  // ── find one pet by ID ─────────────────────────────
  // SCALA:
  //   def findById(id: Int): Option[Pet] =
  //     pets.find(_.id == id)
  //
  // Option[Pet] = either Some(pet) if found, or None
  // .find()     = returns the FIRST item that matches
  // _.id        = shorthand for "each pet's id field"
  // JavaScript: Array.find() returns the object or undefined
  findById(id) {
    return this.pets.find(p => p.id === id);
  },

  // ── filter pets by species ─────────────────────────
  // SCALA:
  //   def findBySpecies(species: String): List[Pet] =
  //     pets.filter(_.species.toLowerCase == species.toLowerCase).toList
  //
  // .filter()    = keep only items that match the condition
  // .toLowerCase = makes the comparison case-insensitive
  // .toList      = convert ListBuffer → immutable List
  findBySpecies(species) {
    return this.pets.filter(p => p.species.toLowerCase() === species.toLowerCase());
  },

  // ── search pets by keyword ─────────────────────────
  // SCALA:
  //   def search(keyword: String): List[Pet] = {
  //     val kw = keyword.toLowerCase
  //     pets.filter { p =>
  //       p.name.toLowerCase.contains(kw)    ||
  //       p.breed.toLowerCase.contains(kw)   ||
  //       p.species.toLowerCase.contains(kw)
  //     }.toList
  //   }
  //
  // .contains() = checks if a string has the keyword
  // ||          = OR — match name OR breed OR species
  // { p => ...} = lambda / anonymous function
  search(keyword) {
    const kw = keyword.toLowerCase();
    return this.pets.filter(p =>
      p.name.toLowerCase().includes(kw)    ||
      p.breed.toLowerCase().includes(kw)   ||
      p.species.toLowerCase().includes(kw)
    );
  },

  // ── only pets that are available ───────────────────
  // SCALA:
  //   def available: List[Pet] = pets.filter(!_.isAdopted).toList
  //
  // !_.isAdopted = keep only pets where isAdopted is false
  available() {
    return this.pets.filter(p => !p.isAdopted);
  },

  // ── only pets that are adopted ─────────────────────
  // SCALA:
  //   def adopted: List[Pet] = pets.filter(_.isAdopted).toList
  adopted() {
    return this.pets.filter(p => p.isAdopted);
  },

  // ── add a new pet to the registry ──────────────────
  // SCALA:
  //   def addPet(p: Pet): Unit = pets += p
  //
  // += is the ListBuffer "append" operator
  // Unit means the function returns nothing (like void)
  // JavaScript: Array.push() appends to the end
  addPet(p) {
    this.pets.push(p);
  },

  // ── auto-generate the next available ID ────────────
  // SCALA:
  //   def nextId: Int =
  //     if (pets.isEmpty) 1 else pets.map(_.id).max + 1
  //
  // .map(_.id) = extract all id values into a new list
  // .max       = get the biggest number in that list
  // isEmpty    = true if the list has no items
  nextId() {
    if (this.pets.length === 0) return 1;
    return Math.max(...this.pets.map(p => p.id)) + 1;
  },

  // ── live stats (shown in the header) ───────────────
  // SCALA:
  //   def totalPets     : Int = pets.size
  //   def totalAvailable: Int = available.size
  //   def totalAdopted  : Int = adopted.size
  totalPets()      { return this.pets.length; },
  totalAvailable() { return this.available().length; },
  totalAdopted()   { return this.adopted().length; },
  totalVaccinated(){ return this.pets.filter(p => p.vaccinated).length; },
};


// =====================================================
// 3. DISPLAY HELPER — object Display
// =====================================================
// SCALA:
//   object Display {
//     val emojiMap: Map[String, String] = Map(
//       "Dog" -> "🐶", "Cat" -> "🐱", ...
//     )
//     def emoji(species: String): String =
//       emojiMap.getOrElse(species, "🐾")
//
//     def printStats(): Unit  = { ... }
//     def printPet(p: Pet): Unit = { ... }
//     def printList(...): Unit   = { ... }
//     def printMenu(): Unit   = { ... }
//   }
//
// Map[String,String] = key-value dictionary
// ->                 = maps a key to a value (like : in JS objects)
// .getOrElse(k, v)   = get value for key k, or use v if not found
// def printXxx(): Unit = prints to screen (CLI); here we render HTML
// =====================================================

const Display = {

  // ── emoji map — species to emoji ───────────────────
  // SCALA: val emojiMap: Map[String, String] = Map(...)
  emojiMap: { Dog:"🐶", Cat:"🐱", Rabbit:"🐰", Fish:"🐟" },
  classMap: { Dog:"dog", Cat:"cat", Rabbit:"rabbit", Fish:"fish" },

  // SCALA: def emoji(species: String): String =
  //          emojiMap.getOrElse(species, "🐾")
  emoji(species)    { return this.emojiMap[species] || "🐾"; },
  cssClass(species) { return this.classMap[species] || "other"; },

  // ── printStats() → updateStats() ───────────────────
  // SCALA:
  //   def printStats(): Unit = {
  //     println(f"Total: ${PetRegistry.totalPets}%3d ...")
  //   }
  // f"..." = formatted string interpolation (%3d = 3-char wide int)
  // In the web version we update the header DOM elements instead of println
  updateStats() {
    document.getElementById("statTotal").textContent    = PetRegistry.totalPets();
    document.getElementById("statAvail").textContent    = PetRegistry.totalAvailable();
    document.getElementById("statAdopted").textContent  = PetRegistry.totalAdopted();
    document.getElementById("statVacc").textContent     = PetRegistry.totalVaccinated();
  },

  // ── printPet(p) → buildPetCard(pet, index) ─────────
  // SCALA:
  //   def printPet(p: Pet): Unit = {
  //     val status = if (p.isAdopted) s"Adopted by ${p.adoptedBy}"
  //                  else "Available"
  //     val ageLabel = if (p.age <= 2) " 🌱 Young" else ""
  //     println(s"${emoji(p.species)} [${p.id}] ${p.name}$ageLabel")
  //     println(s"  Species: ${p.species} — ${p.breed}")
  //     println(s"  Status : $status")
  //   }
  //
  // if/else as expression = returns a value (not just branching)
  // s"..." = string interpolation — embeds $variable into a string
  buildPetCard(pet, index) {
    // SCALA: val ageLabel = if (p.age <= 2) " 🌱 Young" else ""
    const youngBadge = pet.age <= 2 ? `<span class="young-tag">Young</span>` : "";

    // SCALA: val vaccStatus = if (p.vaccinated) "💉 Yes" else "❌ No"
    const vaccBadge = pet.vaccinated
      ? `<span class="vacc-tag yes">💉 Vaccinated</span>`
      : `<span class="vacc-tag no">❌ Not Vaccinated</span>`;

    // SCALA: val status = if (p.isAdopted) s"Adopted by ${p.adoptedBy}" else "Available"
    const footer = pet.isAdopted
      ? `<span class="status-tag adopted">❤️ Adopted</span>
         <span class="adopted-by-label">by ${pet.adoptedBy}</span>`
      : `<span class="status-tag available">✅ Available</span>
         <button class="btn-adopt"
           onclick="event.stopPropagation(); PetAdoptionRegistry.openAdoptModal(${pet.id})">
           Adopt Me!
         </button>`;

    return `
      <div class="pet-card"
           style="animation-delay:${index * 0.05}s"
           onclick="PetAdoptionRegistry.openDetailModal(${pet.id})">
        <div class="card-top">
          <div class="pet-avatar ${this.cssClass(pet.species)}">
            ${this.emoji(pet.species)}
            ${youngBadge}
          </div>
          <div class="card-info">
            <div class="pet-name">${pet.name}</div>
            <div class="pet-meta">${pet.species} · ${pet.breed}</div>
            <div class="pet-meta">${pet.age} yr(s) · ${pet.gender}</div>
          </div>
          ${vaccBadge}
          <div class="pet-id-tag">#${pet.id}</div>
        </div>
        <div class="card-desc">${pet.desc}</div>
        <div class="card-footer">${footer}</div>
      </div>
    `;
  },

  // ── printList(pets, emptyMsg) → renderGrid(list) ───
  // SCALA:
  //   def printList(pets: List[Pet], emptyMsg: String): Unit =
  //     if (pets.isEmpty) println(s"🔍 $emptyMsg")
  //     else pets.foreach(printPet)
  //
  // .isEmpty = true if the list has no items
  // .foreach = loop through every item and call printPet on it
  renderGrid(list) {
    const grid = document.getElementById("petGrid");
    if (list.length === 0) {
      grid.innerHTML = `<div class="empty-state"><div class="e-icon">🔍</div><p>No pets found matching your search.</p></div>`;
      return;
    }
    // SCALA: pets.foreach(printPet) — here we map each pet to an HTML card string
    grid.innerHTML = list.map((pet, i) => this.buildPetCard(pet, i)).join("");
  },

  // ── printMenu() → controls are always visible in the web UI ──
  // SCALA:
  //   def printMenu(): Unit = {
  //     println("  [1] 🐾 View All Pets")
  //     println("  [2] 🔎 Filter by Species")
  //     ...
  //   }
  // In the CLI, the menu is printed every loop iteration.
  // In the web version, the filter buttons/search bar ARE the menu — always shown.

  // ── buildAdopterDetails(d) — helper for detail modal ──
  buildAdopterDetails(d) {
    return `
      <div class="detail-section-title">👤 Adopter Information</div>
      <div class="detail-grid">
        <div class="detail-item"><div class="detail-label">Full Name</div><div class="detail-value">${d.fullname}</div></div>
        <div class="detail-item"><div class="detail-label">Contact</div><div class="detail-value">${d.contact}</div></div>
        <div class="detail-item"><div class="detail-label">Email</div><div class="detail-value">${d.email}</div></div>
        <div class="detail-item"><div class="detail-label">Date of Birth</div><div class="detail-value">${d.dob || "—"}</div></div>
        <div class="detail-item detail-full"><div class="detail-label">Address</div><div class="detail-value">${d.address}</div></div>
        <div class="detail-item"><div class="detail-label">Occupation</div><div class="detail-value">${d.occupation || "—"}</div></div>
        <div class="detail-item"><div class="detail-label">Living Situation</div><div class="detail-value">${d.living || "—"}</div></div>
        ${d.reason ? `<div class="detail-item detail-full"><div class="detail-label">Reason for Adopting</div><div class="detail-value">${d.reason}</div></div>` : ""}
      </div>
    `;
  },
};


// =====================================================
// 4. MAIN APP — object PetAdoptionRegistry extends App
// =====================================================
// SCALA:
//   object PetAdoptionRegistry extends App {
//     Display.printStats()
//     var running = true
//     while (running) {
//       Display.printMenu()
//       val choice = readLine().trim
//       choice match {
//         case "1" => ... // view all
//         case "2" => ... // filter by species
//         case "3" => ... // search
//         case "4" => ... // view by id
//         case "5" => ... // adopt
//         case "6" => ... // add new pet
//         case "7" => ... // view adopted
//         case "0" => running = false
//         case _   => println("Invalid choice.")
//       }
//     }
//   }
//
// extends App = makes this the program entry point
// readLine()  = reads user input from the terminal
// .trim       = removes leading/trailing whitespace
// var running = true; while(running){} = the main loop
//
// In the web version:
//   - "extends App" → window.addEventListener("DOMContentLoaded", init)
//   - "while(running)" → replaced by event-driven clicks/inputs
//   - "readLine()" → replaced by HTML input fields and buttons
//   - "choice match { case ... }" → replaced by onclick handlers
// =====================================================

const PetAdoptionRegistry = {

  // ── App State ──────────────────────────────────────
  // SCALA: var running = true (mutable state variables)
  // var = can change; these drive what's visible on screen
  currentFilter : "All",
  showAdopted   : false,
  vaccOnly      : false,
  adoptingId    : -1,

  // ── match case "2" → setFilter ─────────────────────
  // SCALA:
  //   case "2" =>
  //     val species = readLine().trim match {
  //       case "1" => "Dog"
  //       case "2" => "Cat"
  //       case _   => ""
  //     }
  //     val results = PetRegistry.findBySpecies(species).filter(!_.isAdopted)
  //     Display.printList(results, s"No available $species found.")
  setFilter(filter, btn) {
    this.currentFilter = filter;
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    this.renderPets();
  },

  // ── Toggle adopted / vaccinated view ───────────────
  // SCALA: match case "7" => Display.printList(PetRegistry.adopted, ...)
  toggleAdopted() {
    this.showAdopted = !this.showAdopted;
    document.getElementById("toggleAdoptedBtn").classList.toggle("active", this.showAdopted);
    this.renderPets();
  },

  toggleVacc() {
    this.vaccOnly = !this.vaccOnly;
    document.getElementById("toggleVaccBtn").classList.toggle("active", this.vaccOnly);
    this.renderPets();
  },

  clearSearch() {
    document.getElementById("searchInput").value = "";
    document.getElementById("clearSearch").classList.remove("visible");
    this.renderPets();
  },

  // ── match case "1" / "2" / "3" → renderPets ───────
  // SCALA:
  //   case "1" => Display.printList(PetRegistry.pets.toList, "No pets registered yet.")
  //   case "2" => val results = PetRegistry.findBySpecies(species).filter(!_.isAdopted)
  //   case "3" => val results = PetRegistry.search(keyword)
  //
  // .filter(!_.isAdopted) = keep only available pets
  // .toList               = convert ListBuffer to immutable List
  renderPets() {
    const kw = document.getElementById("searchInput").value.trim().toLowerCase();
    document.getElementById("clearSearch").classList.toggle("visible", kw.length > 0);

    // SCALA: var list = pets.toList (start with all pets)
    let list = [...PetRegistry.pets];

    // SCALA: if (currentFilter != "All") list = PetRegistry.findBySpecies(currentFilter)
    if (this.currentFilter !== "All") {
      list = list.filter(p => p.species === this.currentFilter);
    }

    // SCALA: list = list.filter(!_.isAdopted)  (unless showAdopted)
    if (!this.showAdopted) {
      list = list.filter(p => !p.isAdopted);
    }

    if (this.vaccOnly) {
      list = list.filter(p => p.vaccinated);
    }

    // SCALA: val results = PetRegistry.search(keyword)
    if (kw) {
      list = list.filter(p =>
        p.name.toLowerCase().includes(kw)    ||
        p.breed.toLowerCase().includes(kw)   ||
        p.species.toLowerCase().includes(kw)
      );
    }

    const label = this.currentFilter === "All"
      ? (this.showAdopted ? "All Pets" : "Available Pets")
      : `${Display.emoji(this.currentFilter)} ${this.currentFilter}s`;

    document.getElementById("sectionLabel").textContent = label;
    document.getElementById("petCount").textContent     = list.length;

    // SCALA: Display.printList(list, "No pets found.")
    Display.renderGrid(list);
    Display.updateStats();
  },

  // ── match case "4" → openDetailModal ───────────────
  // SCALA:
  //   case "4" =>
  //     val id = readLine().trim.toIntOption.getOrElse(-1)
  //     PetRegistry.findById(id) match {
  //       case Some(p) => Display.printPet(p)
  //       case None    => println(s"No pet found with ID #$id.")
  //     }
  //
  // .toIntOption = safely parse String → Int; returns Some(n) or None
  // .getOrElse(-1) = use -1 if parsing failed (None case)
  openDetailModal(id) {
    // SCALA: PetRegistry.findById(id) match { case Some(p) => ... case None => ... }
    const pet = PetRegistry.findById(id);
    if (!pet) return;

    // SCALA: val status = if (p.isAdopted) s"Adopted by ${p.adoptedBy}" else "Available"
    const statusTag = pet.isAdopted
      ? `<span class="status-tag adopted" style="font-size:0.88rem">❤️ Adopted by ${pet.adoptedBy}</span>`
      : `<span class="status-tag available" style="font-size:0.88rem">✅ Available for Adoption</span>`;

    const vaccStatus = pet.vaccinated
      ? `<span style="color:#1a7a45;font-weight:700">💉 Vaccinated</span>`
      : `<span style="color:#b83232;font-weight:700">❌ Not Vaccinated</span>`;

    // SCALA: if (p.isAdopted && p.adoptedBy != "") Display.printAdopter(p)
    const adopterSection = (pet.isAdopted && pet.adopterDetails)
      ? Display.buildAdopterDetails(pet.adopterDetails)
      : "";

    const adoptBtn = !pet.isAdopted
      ? `<button class="btn-confirm adopt-confirm"
           onclick="closeModal('detailModal'); PetAdoptionRegistry.openAdoptModal(${pet.id})">
           ❤️ Adopt ${pet.name}
         </button>`
      : "";

    document.getElementById("detailContent").innerHTML = `
      <div class="modal-header">
        <h2>${Display.emoji(pet.species)} ${pet.name}</h2>
        <button class="modal-close" onclick="closeModal('detailModal')">✕</button>
      </div>
      <p class="modal-sub">Pet ID #${pet.id} · ${pet.species}</p>
      <div class="detail-grid">
        <div class="detail-item"><div class="detail-label">Breed</div><div class="detail-value">${pet.breed}</div></div>
        <div class="detail-item"><div class="detail-label">Age</div><div class="detail-value">${pet.age} yr(s) ${pet.age <= 2 ? "🌱 Young" : ""}</div></div>
        <div class="detail-item"><div class="detail-label">Gender</div><div class="detail-value">${pet.gender}</div></div>
        <div class="detail-item"><div class="detail-label">Vaccination</div><div class="detail-value">${vaccStatus}</div></div>
        <div class="detail-item detail-full"><div class="detail-label">About</div><div class="detail-value">${pet.desc}</div></div>
        <div class="detail-item detail-full"><div class="detail-label">Status</div><div class="detail-value" style="margin-top:4px">${statusTag}</div></div>
      </div>
      ${adopterSection}
      <div class="modal-actions">
        <button class="btn-cancel" onclick="closeModal('detailModal')">Close</button>
        ${adoptBtn}
      </div>
    `;
    openModal("detailModal");
  },

  // ── match case "6" → openAddModal / addPet ─────────
  // SCALA:
  //   case "6" =>
  //     print("Pet Name: ");       val name    = readLine().trim
  //     print("Species [1-5]: ");  val species = readLine().trim match { case "1"=>"Dog" ... }
  //     print("Breed: ");          val breed   = readLine().trim
  //     print("Age: ");            val age     = readLine().trim.toIntOption.getOrElse(0)
  //     print("Gender [1/2]: ");   val gender  = readLine().trim match { case "1"=>"Male" case _=>"Female" }
  //     print("Description: ");    val desc    = readLine().trim
  //     if (name.isEmpty || breed.isEmpty || desc.isEmpty)
  //       println("Name, breed and description are required!")
  //     else {
  //       val newPet = Pet(PetRegistry.nextId, name, species, breed, age, gender, desc)
  //       PetRegistry.addPet(newPet)
  //       println(s"$name registered with ID #${newPet.id}!")
  //     }
  openAddModal() {
    ["newName","newBreed","newDesc"].forEach(id => document.getElementById(id).value = "");
    document.getElementById("newAge").value        = 1;
    document.getElementById("newSpecies").value    = "Dog";
    document.getElementById("newGender").value     = "Male";
    document.getElementById("newVaccinated").value = "true";
    openModal("addModal");
  },

  addPet() {
    const name       = document.getElementById("newName").value.trim();
    const species    = document.getElementById("newSpecies").value;
    const breed      = document.getElementById("newBreed").value.trim();
    const age        = parseInt(document.getElementById("newAge").value) || 0;
    const gender     = document.getElementById("newGender").value;
    const vaccinated = document.getElementById("newVaccinated").value === "true";
    const desc       = document.getElementById("newDesc").value.trim();

    // SCALA: if (name.isEmpty || breed.isEmpty || desc.isEmpty) { println("Required!") }
    if (!name || !breed || !desc) {
      showToast("❌ Name, breed, and description are required!", "error");
      return;
    }

    // SCALA: val newPet = Pet(PetRegistry.nextId, name, species, breed, age, gender, desc)
    const newPet = {
      id: PetRegistry.nextId(), name, species, breed, age, gender, desc,
      vaccinated, isAdopted:false, adoptedBy:"", adopterDetails:null
    };

    // SCALA: PetRegistry.addPet(newPet)  →  pets += newPet
    PetRegistry.addPet(newPet);
    closeModal("addModal");
    this.renderPets();
    showToast(`✅ ${name} has been registered with ID #${newPet.id}!`, "success");
  },

  // ── match case "5" → openAdoptModal / confirmAdopt ─
  // SCALA:
  //   case "5" =>
  //     Display.printList(PetRegistry.available, "No pets available.")
  //     print("Enter ID to adopt: ")
  //     val id = readLine().trim.toIntOption.getOrElse(-1)
  //     PetRegistry.findById(id) match {
  //       case Some(p) if !p.isAdopted =>         ← guard condition
  //         print("Enter adopter's full name: ")
  //         val adopter = readLine().trim match {
  //           case "" => "Anonymous"
  //           case n  => n
  //         }
  //         p.isAdopted = true    ← mutating the var field
  //         p.adoptedBy = adopter ← mutating the var field
  //         println(s"${p.name} adopted by $adopter!")
  //       case Some(_) => println("Already adopted.")
  //       case None    => println(s"No pet with ID #$id.")
  //     }
  openAdoptModal(id) {
    // SCALA: PetRegistry.findById(id) match { case Some(p) if !p.isAdopted => ... }
    const pet = PetRegistry.findById(id);
    if (!pet || pet.isAdopted) return;

    this.adoptingId = id;
    ["adopterFullname","adopterContact","adopterEmail",
     "adopterDob","adopterAddress","adopterOccupation","adopterReason"
    ].forEach(fid => document.getElementById(fid).value = "");
    document.getElementById("adopterLiving").value = "House with yard";

    document.getElementById("adoptPetPreview").innerHTML = `
      <div class="adopt-pet-preview">
        <div class="adopt-preview-avatar">${Display.emoji(pet.species)}</div>
        <div>
          <div class="adopt-preview-name">${pet.name}</div>
          <div class="adopt-preview-meta">
            ${pet.species} · ${pet.breed} · ${pet.age} yr(s) · ${pet.gender}
            · ${pet.vaccinated ? "💉 Vaccinated" : "❌ Not Vaccinated"}
          </div>
        </div>
      </div>
    `;
    openModal("adoptModal");
  },

  confirmAdopt() {
    const fullname   = document.getElementById("adopterFullname").value.trim();
    const contact    = document.getElementById("adopterContact").value.trim();
    const email      = document.getElementById("adopterEmail").value.trim();
    const dob        = document.getElementById("adopterDob").value;
    const address    = document.getElementById("adopterAddress").value.trim();
    const occupation = document.getElementById("adopterOccupation").value.trim();
    const living     = document.getElementById("adopterLiving").value;
    const reason     = document.getElementById("adopterReason").value.trim();

    if (!fullname || !contact || !email || !address) {
      showToast("❌ Full name, contact, email, and address are required!", "error");
      return;
    }

    // SCALA: PetRegistry.findById(adoptingId) match { case Some(p) if !p.isAdopted => ... }
    const pet = PetRegistry.findById(this.adoptingId);
    if (!pet) return;

    // SCALA: p.isAdopted = true  (mutating var field)
    // SCALA: p.adoptedBy = adopter (mutating var field)
    pet.isAdopted      = true;
    pet.adoptedBy      = fullname;
    pet.adopterDetails = { fullname, contact, email, dob, address, occupation, living, reason };

    closeModal("adoptModal");
    this.renderPets();
    showToast(`🎉 ${pet.name} has been adopted by ${fullname}! Thank you! 💛`, "success");
  },

  // ── extends App → init() — entry point ─────────────
  // SCALA:
  //   object PetAdoptionRegistry extends App {
  //     Display.printStats()   ← runs immediately on launch
  //     var running = true
  //     while (running) { ... }
  //   }
  //
  // extends App = the code runs automatically when the program starts
  // In the web version, init() is called by DOMContentLoaded (page load)
  // The "while loop" is replaced by event-driven interactions (clicks)
  init() {
    this.renderPets();    // SCALA: Display.printList(PetRegistry.pets.toList, ...)
    Display.updateStats(); // SCALA: Display.printStats()
  },
};


// =====================================================
// MODAL HELPERS & TOAST
// =====================================================
// These have no direct Scala equivalent — they handle
// the browser UI (opening/closing popups, notifications)
// that replace the CLI's println() and readLine() calls.
// =====================================================

function openModal(id) {
  document.getElementById(id).classList.add("open");
  document.body.style.overflow = "hidden";
}

function closeModal(id) {
  document.getElementById(id).classList.remove("open");
  document.body.style.overflow = "";
}

function overlayClose(event, modalId) {
  if (event.target === document.getElementById(modalId)) closeModal(modalId);
}

function showToast(message, type = "") {
  const t = document.getElementById("toast");
  t.textContent = message;
  t.className = `toast show ${type}`;
  clearTimeout(t._timer);
  t._timer = setTimeout(() => { t.className = "toast"; }, 3500);
}

function scrollToGrid() {
  document.getElementById("petSection").scrollIntoView({ behavior: "smooth" });
}

// Close any open modal on Escape key — like pressing "0" to exit in Scala CLI
document.addEventListener("keydown", e => {
  if (e.key === "Escape")
    document.querySelectorAll(".modal-overlay.open").forEach(m => closeModal(m.id));
});

// ── extends App — program starts here ─────────────────
// SCALA: object PetAdoptionRegistry extends App { ... }
// The DOMContentLoaded event = the moment the "program" starts in the browser
window.addEventListener("DOMContentLoaded", () => PetAdoptionRegistry.init());
