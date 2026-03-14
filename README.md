# HappyPaws — Pet Adoption Registry System

![Scala](https://img.shields.io/badge/Scala-DC322F?style=for-the-badge&logo=scala&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

A pet adoption registry system built with Object-Oriented Programming in Scala and Python, with a full Adopt Me-inspired web front-end.

*by Scalers*

---

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [OOP Concepts Applied](#oop-concepts-applied)
- [Python vs Scala Comparison](#python-vs-scala-comparison)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Web System](#web-system)
- [Sample Data](#sample-data)
- [Team](#team)

---

## About the Project

**HappyPaws** is a Pet Adoption Registry System that allows users to:
- Browse available pets
- Search and filter by species or name
- Adopt a pet by filling in adopter details
- Register new pets into the shelter
- View vaccination status and adoption records

The system was built in **two languages** — **Scala** and **Python** — to demonstrate Object-Oriented Programming concepts, and extended into a **web application** with an Adopt Me Roblox-inspired design.

---

## Features

| Feature | Console (Scala & Python) | Web (HTML/CSS/JS) |
|---|---|---|
| View all pets | Yes | Yes |
| Filter by species | Yes | Yes |
| Search by name / breed | Yes | Yes |
| Adopt a pet | Yes | Yes |
| Register a new pet | Yes | Yes |
| View adopted pets | Yes | Yes |
| View vaccinated pets | Yes | Yes |
| Pet photo display | No | Yes |
| Live stats dashboard | No | Yes |
| Rarity card system | No | Yes |

---

## OOP Concepts Applied

### 1. Encapsulation

Pet data (name, species, breed, age, vaccination status, adopter details) is bundled into a single `Pet` class/case class. Internal state is only modified through controlled methods.

```scala
// Scala
case class Pet(
  id                : Int,
  name              : String,
  species           : String,
  vaccinated        : Boolean = false,
  var isAdopted     : Boolean = false,
  var adopterDetails: Option[AdopterDetails] = None
)
```

```python
# Python
class Pet:
    def __init__(self, id, name, species, breed, age,
                 gender, desc, vaccinated=False, is_adopted=False):
        self.id         = id
        self.name       = name
        self.vaccinated = vaccinated
```

---

### 2. Abstraction

The `Display` object/class hides the complexity of output formatting. The main app simply calls `Display.printPet()` without needing to know how it works internally.

```scala
// Scala
Display.printPet(pet)
Display.printMenu()
Display.printStats()
```

```python
# Python
Display.print_pet(pet)
Display.print_menu()
Display.print_stats()
```

---

### 3. Singleton Pattern

`PetRegistry` is a single shared instance that acts as the central database for the entire program.

```scala
// Scala — object keyword guarantees one instance
object PetRegistry {
  val pets: ListBuffer[Pet] = ListBuffer(...)
  def findById(id: Int): Option[Pet] = ...
}
```

```python
# Python — simulated with class-level state and static methods
class PetRegistry:
    pets = [...]
    @staticmethod
    def find_by_id(id): ...
```

---

### 4. Separation of Concerns

Each component has a single responsibility:

| Component | Responsibility |
|---|---|
| `Pet` / `AdopterDetails` | Data model only |
| `PetRegistry` | Data storage and retrieval |
| `Display` | Output formatting only |
| `Petadoption` (main) | User input and program flow |

---

## Python vs Scala Comparison

| Concept | Python | Scala |
|---|---|---|
| Data Model | `class Pet` with `__init__` | `case class Pet(...)` |
| Singleton | Class with `@staticmethod` | `object PetRegistry` (built-in) |
| Type Safety | Dynamic — errors at runtime | Static — errors at compile time |
| Immutability | Opt-in | Default — must use `var` to mutate |
| Null Safety | Uses `None` | Uses `Option[T]` — safer |
| Method Style | `snake_case` | `camelCase` |
| Pattern Matching | `if/elif/else` | `match/case` — more powerful |

### Code Example — Adopting a Pet

```python
# Python
pet.is_adopted      = True
pet.adopted_by      = fullname
pet.adopter_details = { "fullname": fullname, ... }
```

```scala
// Scala
p.isAdopted      = true
p.adoptedBy      = fullname
p.adopterDetails = Some(AdopterDetails(fullname, contact, ...))
```

---

## Project Structure

```
HappyPaws/
|
|-- Petadoption.scala       <- Scala console application
|-- Petadoption.py          <- Python console application
|
|-- index.html              <- Web front-end (main page)
|-- style.css               <- Full Adopt Me-style CSS theme
|-- Petadoption.js          <- Web application logic
|
└-- Images/
    |-- Bonjong.jfif
    |-- Whiskers.jfif
    |-- Thumper.jfif
    |-- Luna.jfif
    |-- Milo.jfif
    |-- Mochi.jfif
    |-- Nemo.jfif
    └-- Daisy.jfif
```

---

## How to Run

### Scala Version

Requirements: Scala installed — [scala-lang.org](https://scala-lang.org)

```bash
# Compile
scalac Petadoption.scala

# Run
scala Petadoption
```

### Python Version

Requirements: Python 3.x installed — [python.org](https://python.org)

```bash
python Petadoption.py
```

### Console Menu Options

```
[1]  View All Pets
[2]  Filter by Species
[3]  Search by Name / Breed
[4]  View Pet Details by ID
[5]  Adopt a Pet
[6]  Register a New Pet
[7]  View Adopted Pets
[8]  View Vaccinated Pets Only
[0]  Exit
```

---

## Web System

The web version requires no installation — just open `index.html` in any browser.

Features of the web system:
- Adopt Me / Roblox-inspired full-site design
- Pet cards with rarity system (Legendary, Mega Rare, Ultra Rare, Rare, Uncommon, Common)
- Live search and species filtering
- Vaccination filter toggle
- Pet photo display with fallback avatars
- Real-time stats in the header
- Full adoption and registration forms with modals
- Toast notifications on actions
- Fully responsive and mobile-friendly

```bash
# No server needed — just open in browser
open index.html
```

---

## Sample Data

The system comes pre-loaded with 8 pets:

| ID | Name | Species | Breed | Age | Vaccinated | Status |
|---|---|---|---|---|---|---|
| 1 | Bonjong | Dog | Belgian Malinois | 2 | Yes | Available |
| 2 | Whiskers | Cat | Siamese | 3 | Yes | Available |
| 3 | Thumper | Rabbit | Holland Lop | 1 | No | Available |
| 4 | Luna | Dog | Dachshund | 4 | Yes | Available |
| 5 | Milo | Cat | Persian | 5 | Yes | Adopted by Kc Vargas |
| 6 | Mochi | Dog | Shi-poo | 2 | No | Available |
| 7 | Nemo | Fish | Goldfish | 1 | No | Available |
| 8 | Daisy | Rabbit | Mini Rex | 2 | Yes | Adopted by Erikka Dela Cruz |

---

## Team

**Scalers** — Built for every pet that deserves a loving home.

> "Every pet deserves a loving home — one paw at a time."

---

![Made with Love](https://img.shields.io/badge/Made%20with-Love-ff69b4?style=flat-square)
![Adopt Me Style](https://img.shields.io/badge/Style-Adopt%20Me-87ceeb?style=flat-square)
![OOP](https://img.shields.io/badge/OOP-Scala%20%26%20Python-green?style=flat-square)
