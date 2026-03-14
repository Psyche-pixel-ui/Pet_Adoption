// =====================================================
// 1. DATA MODEL — case class Pet
// =====================================================
const PetRegistry = {

pets: [
  { id:1, name:"Bonjong",  species:"Dog",    breed:"Belgian Malinois", age:2, gender:"Male",   desc:"Friendly and loves to play fetch! Great with children.",      vaccinated:true,  isAdopted:false, adoptedBy:"", adopterDetails:null, image:"Images/Bonjong.jfif" },
  { id:2, name:"Whiskers", species:"Cat",    breed:"Siamese",          age:3, gender:"Female", desc:"Calm and loves cuddles. Perfect indoor companion.",           vaccinated:true,  isAdopted:false, adoptedBy:"", adopterDetails:null, image:"Images/Whiskers.jfif" },
  { id:3, name:"Thumper",  species:"Rabbit", breed:"Holland Lop",      age:1, gender:"Male",   desc:"Very active and playful. Loves hopping around the garden.",  vaccinated:false, isAdopted:false, adoptedBy:"", adopterDetails:null, image:"Images/Thumper.jfif" },
  { id:4, name:"Luna",     species:"Dog",    breed:"Dachshund",        age:4, gender:"Female", desc:"Great with kids and families. Calm and well-trained.",        vaccinated:true,  isAdopted:false, adoptedBy:"", adopterDetails:null, image:"Images/Luna.jfif" },
  { id:5, name:"Milo",     species:"Cat",    breed:"Persian",          age:5, gender:"Male",   desc:"Laid-back and loves napping by the window.",                 vaccinated:true,  isAdopted:true,  adoptedBy:"Kc Vargas",
    adopterDetails:{ fullname:"Kc Vargas", contact:"09171234567", email:"kc.vargas@email.com", dob:"1990-05-14", address:"123 Mango St., Barangay Poblacion, Davao City", occupation:"Nurse", living:"House", reason:"I have always loved cats and Milo felt like the perfect fit!" },
    image:"Images/Milo.jfif" },
  { id:6, name:"Mochi",    species:"Dog",    breed:"Shi-poo",          age:2, gender:"Female", desc:"Energetic and loves outdoor walks. Always wagging her tail!", vaccinated:false, isAdopted:false, adoptedBy:"", adopterDetails:null, image:"Images/Mochi.jfif" },
  { id:7, name:"Nemo",     species:"Fish",   breed:"Goldfish",         age:1, gender:"Male",   desc:"Beautiful orange and white colors. Very soothing to watch.", vaccinated:false, isAdopted:false, adoptedBy:"", adopterDetails:null, image:"Images/Nemo.jfif" },
  { id:8, name:"Daisy",    species:"Rabbit", breed:"Mini Rex",         age:2, gender:"Female", desc:"Gentle and easy to care for. Loves soft petting.",           vaccinated:true,  isAdopted:true,  adoptedBy:"Erikka Dela Cruz",
    adopterDetails:{ fullname:"Erikka Dela Cruz", contact:"09289876543", email:"erikka.dela.cruz@email.com", dob:"1988-11-22", address:"45 Rizal Ave., Toril, Davao City", occupation:"Engineer", living:"House", reason:"My kids have been begging for a rabbit. Daisy is perfect!" },
    image:"Images/Daisy.jfif" },
],

  findById(id)       { return this.pets.find(p => p.id === id); },
  findBySpecies(s)   { return this.pets.filter(p => p.species.toLowerCase() === s.toLowerCase()); },
  search(keyword)    {
    const kw = keyword.toLowerCase();
    return this.pets.filter(p =>
      p.name.toLowerCase().includes(kw) ||
      p.breed.toLowerCase().includes(kw) ||
      p.species.toLowerCase().includes(kw)
    );
  },
  available()        { return this.pets.filter(p => !p.isAdopted); },
  adopted()          { return this.pets.filter(p => p.isAdopted); },
  addPet(p)          { this.pets.push(p); },
  nextId()           { return this.pets.length === 0 ? 1 : Math.max(...this.pets.map(p => p.id)) + 1; },
  totalPets()        { return this.pets.length; },
  totalAvailable()   { return this.available().length; },
  totalAdopted()     { return this.adopted().length; },
  totalVaccinated()  { return this.pets.filter(p => p.vaccinated).length; },
};


// =====================================================
// 2. DISPLAY HELPER
// =====================================================
const Display = {
  emojiMap: { Dog:"", Cat:"", Rabbit:"", Fish:"" },
  classMap: { Dog:"dog", Cat:"cat", Rabbit:"rabbit", Fish:"fish" },
  emoji(species)    { return this.emojiMap[species] || ""; },
  cssClass(species) { return this.classMap[species] || "other"; },

  fallbackAvatar(species) {
    const colors = { Dog:"#f4a74b", Cat:"#a78bfa", Rabbit:"#6ee7b7", Fish:"#60a5fa" };
    const bg = colors[species] || "#e5e7eb";
    const em = this.emoji(species);
    const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='400' height='300'>
      <rect width='400' height='300' fill='${bg}' rx='12'/>
      <text x='200' y='175' font-size='100' text-anchor='middle' dominant-baseline='middle'>${em}</text>
    </svg>`;
    return "data:image/svg+xml," + encodeURIComponent(svg);
  },

  updateStats() {
    document.getElementById("statTotal").textContent   = PetRegistry.totalPets();
    document.getElementById("statAvail").textContent   = PetRegistry.totalAvailable();
    document.getElementById("statAdopted").textContent = PetRegistry.totalAdopted();
    document.getElementById("statVacc").textContent    = PetRegistry.totalVaccinated();
  },

  // buildPetCard is overridden in index.html script tag for Adopt Me style
  buildPetCard(pet, index) {
    return `<div class="am-pet-card" style="animation-delay:${index*0.06}s">${pet.name}</div>`;
  },

  renderGrid(list) {
    const grid = document.getElementById("petGrid");
    if (list.length === 0) {
      grid.innerHTML = `<div class="am-empty-state"><div class="e-icon"></div><p>No pets found matching your search!</p></div>`;
      return;
    }
    grid.innerHTML = list.map((pet, i) => this.buildPetCard(pet, i)).join("");
  },

  buildAdopterDetails(d) {
    return `
      <div class="detail-section-title">Adopter Information</div>
      <div class="detail-grid">
        <div class="detail-item"><div class="detail-label">Full Name</div><div class="detail-value">${d.fullname}</div></div>
        <div class="detail-item"><div class="detail-label">Contact</div><div class="detail-value">${d.contact}</div></div>
        <div class="detail-item"><div class="detail-label">Email</div><div class="detail-value">${d.email}</div></div>
        <div class="detail-item"><div class="detail-label">Date of Birth</div><div class="detail-value">${d.dob || "—"}</div></div>
        <div class="detail-item detail-full"><div class="detail-label">Address</div><div class="detail-value">${d.address}</div></div>
        <div class="detail-item"><div class="detail-label">Occupation</div><div class="detail-value">${d.occupation || "—"}</div></div>
        <div class="detail-item"><div class="detail-label">Living Situation</div><div class="detail-value">${d.living || "—"}</div></div>
        ${d.reason ? `<div class="detail-item detail-full"><div class="detail-label">Reason for Adopting</div><div class="detail-value">${d.reason}</div></div>` : ""}
      </div>`;
  },

  buildDetailPhoto(pet) {
    const imgSrc = pet.image || this.fallbackAvatar(pet.species);
    return `
      <div class="am-detail-photo-wrap">
        <img class="am-detail-photo" src="${imgSrc}" alt="${pet.name}"
             onerror="this.src='${this.fallbackAvatar(pet.species)}'"/>
      </div>`;
  },
};


// =====================================================
// 3. MAIN APP
// =====================================================
const PetAdoptionRegistry = {
  currentFilter : "All",
  showAdopted   : false,
  vaccOnly      : false,
  adoptingId    : -1,

  setFilter(filter, btn) {
    this.currentFilter = filter;
    document.querySelectorAll(".am-filter-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    this.renderPets();
  },

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

  renderPets() {
    const kw = document.getElementById("searchInput").value.trim().toLowerCase();
    const clearBtn = document.getElementById("clearSearch");
    if (clearBtn) clearBtn.classList.toggle("visible", kw.length > 0);

    let list = [...PetRegistry.pets];
    if (this.currentFilter !== "All") list = list.filter(p => p.species === this.currentFilter);
    list = list.filter(p => this.showAdopted ? p.isAdopted : !p.isAdopted);
    if (this.vaccOnly) list = list.filter(p => p.vaccinated);
    if (kw) list = list.filter(p =>
      p.name.toLowerCase().includes(kw) ||
      p.breed.toLowerCase().includes(kw) ||
      p.species.toLowerCase().includes(kw)
    );

    const emoji = { Dog:"", Cat:"", Rabbit:"", Fish:"" };
    const label = this.currentFilter === "All"
      ? (this.showAdopted ? "Adopted Pets" : "Available Pets")
      : `${emoji[this.currentFilter]||""}${this.currentFilter}s${this.showAdopted ? " (Adopted)" : ""}`;

    document.getElementById("sectionLabel").textContent = label;
    document.getElementById("petCount").textContent     = list.length;

    Display.renderGrid(list);
    Display.updateStats();
  },

  openDetailModal(id) {
    // Overridden in index.html <script> for full Adopt Me style
    const pet = PetRegistry.findById(id);
    if (!pet) return;
    openModal("detailModal");
  },

  openAddModal() {
    ["newName","newBreed","newDesc"].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.value = "";
    });
    document.getElementById("newAge").value        = 1;
    document.getElementById("newSpecies").value    = "Dog";
    document.getElementById("newGender").value     = "Male";
    document.getElementById("newVaccinated").value = "true";
    const fileInput = document.getElementById("newImage");
    if (fileInput) fileInput.value = "";
    const preview = document.getElementById("newImagePreview");
    if (preview) { preview.src = ""; preview.style.display = "none"; }
    const previewWrap = document.getElementById("newImagePreviewWrap");
    if (previewWrap) previewWrap.style.display = "none";
    const photoLabel = document.getElementById("newImageLabel");
    if (photoLabel) photoLabel.textContent = "Choose a photo…";
    openModal("addModal");
  },

  previewImage(input) {
    const file = input.files[0];
    const preview     = document.getElementById("newImagePreview");
    const previewWrap = document.getElementById("newImagePreviewWrap");
    const photoLabel  = document.getElementById("newImageLabel");
    if (!file) {
      if (preview)     { preview.src = ""; preview.style.display = "none"; }
      if (previewWrap) previewWrap.style.display = "none";
      if (photoLabel)  photoLabel.textContent = "Choose a photo…";
      return;
    }
    if (photoLabel) photoLabel.textContent = file.name;
    const reader = new FileReader();
    reader.onload = (e) => {
      if (preview) { preview.src = e.target.result; preview.style.display = "block"; }
      if (previewWrap) previewWrap.style.display = "block";
    };
    reader.readAsDataURL(file);
  },

  addPet() {
    const name       = document.getElementById("newName").value.trim();
    const species    = document.getElementById("newSpecies").value;
    const breed      = document.getElementById("newBreed").value.trim();
    const age        = parseInt(document.getElementById("newAge").value) || 0;
    const gender     = document.getElementById("newGender").value;
    const vaccinated = document.getElementById("newVaccinated").value === "true";
    const desc       = document.getElementById("newDesc").value.trim();

    if (!name || !breed || !desc) {
      showToast("Name, breed, and description are required!", "error");
      return;
    }

    const newPet = {
      id: PetRegistry.nextId(), name, species, breed, age, gender, desc,
      vaccinated, isAdopted: false, adoptedBy: "", adopterDetails: null, image: null
    };

    const fileInput = document.getElementById("newImage");
    const file      = fileInput && fileInput.files[0];

    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        newPet.image = e.target.result;
        PetRegistry.addPet(newPet);
        closeModal("addModal");
        PetAdoptionRegistry.renderPets();
        showToast(`${name} has been registered with ID #${newPet.id}!`, "success");
      };
      reader.readAsDataURL(file);
    } else {
      PetRegistry.addPet(newPet);
      closeModal("addModal");
      PetAdoptionRegistry.renderPets();
      showToast(`${name} has been registered with ID #${newPet.id}!`, "success");
    }
  },

  openAdoptModal(id) {
    // Overridden in index.html <script>
    const pet = PetRegistry.findById(id);
    if (!pet || pet.isAdopted) return;
    this.adoptingId = id;
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
      showToast("Full name, contact, email, and address are required!", "error");
      return;
    }

    const pet = PetRegistry.findById(this.adoptingId);
    if (!pet) return;

    pet.isAdopted      = true;
    pet.adoptedBy      = fullname;
    pet.adopterDetails = { fullname, contact, email, dob, address, occupation, living, reason };

    closeModal("adoptModal");
    this.renderPets();
    showToast(`${pet.name} has been adopted by ${fullname}! Thank you!`, "success");
  },

  init() {
    this.renderPets();
    Display.updateStats();
  },
};


// =====================================================
// MODAL HELPERS & TOAST
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
  t.className = `am-toast show ${type}`;
  clearTimeout(t._timer);
  t._timer = setTimeout(() => { t.className = "am-toast"; }, 3500);
}

function scrollToGrid() {
  document.getElementById("petSection").scrollIntoView({ behavior: "smooth" });
}

document.addEventListener("keydown", e => {
  if (e.key === "Escape")
    document.querySelectorAll(".am-modal-overlay.open").forEach(m => closeModal(m.id));
});

window.addEventListener("DOMContentLoaded", () => PetAdoptionRegistry.init());
