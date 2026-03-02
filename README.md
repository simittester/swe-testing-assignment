# Quick-Calc

Quick-Calc is a lightweight calculator application developed for the Advanced Software Engineering course.  
It supports the four basic arithmetic operations (addition, subtraction, multiplication, and division) and includes robust unit and integration testing to ensure correctness and reliability.

This project demonstrates practical application of software engineering principles such as version control, semantic versioning, layered testing strategies, clean architecture, and structured documentation.

---

## Features

- Addition  
- Subtraction  
- Multiplication  
- Division (with graceful handling of division by zero)  
- Clear (C) operation to reset state  
- Unit and Integration test suite  

---

## Project Structure

```
swe-testing-assignment/
│
├── quick_calc/
│   ├── __init__.py
│   ├── core.py
│   └── cli.py
│
├── tests/
│   ├── test_unit_core.py
│   ├── test_integration_cli.py
│   └── conftest.py
│
├── requirements.txt
├── README.md
└── TESTING.md
```

---

## Setup Instructions

### Requirements

- Python 3.10 or higher  
- pip  

### Installation

```bash
git clone https://github.com/simittester/swe-testing-assignment.git
cd swe-testing-assignment
pip install -r requirements.txt
```

---

## How to Run Tests

All tests can be executed with a single command:

```bash
pytest
```

The test suite includes:

- **Unit tests** - verify core calculation logic in isolation.  
- **Integration tests** - verify interaction between the CLI layer and calculation logic.  

---

## Testing Framework Research: Pytest vs Unittest

Python provides the built-in `unittest` framework, which follows a class-based structure inspired by JUnit. It is stable, part of the standard library, and suitable for structured enterprise environments. However, it requires more boilerplate code and can be more verbose for smaller projects.

`pytest` is a modern and widely adopted alternative that emphasizes simplicity and readability. Tests can be written as plain functions, assertions are clearer, and fixtures reduce repetitive setup code. Pytest also provides improved error reporting and has a large plugin ecosystem.

For this project, `pytest` was selected because it allows concise test writing, better readability, and easier maintenance while maintaining professional-level testing capabilities.

---

## Versioning

This project follows **Semantic Versioning (SemVer)**.

Version format:

MAJOR.MINOR.PATCH

- **MAJOR** - incompatible API changes  
- **MINOR** - new features added  
- **PATCH** - bug fixes  

The first stable release is tagged as:

v1.0.0
