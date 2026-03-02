# Testing Strategy – Quick-Calc

## Overview

This document describes the testing strategy applied in the Quick-Calc project.  
The goal of the testing process was to ensure correctness, reliability, and maintainability of the calculator application using a layered testing approach.

---

## What Was Tested

### Functional Testing

The following functional behaviors were tested:

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero handling
- Clear (C) functionality
- Full user interaction flow (input → operation → result)

### Edge Cases Tested

- Division by zero
- Negative numbers
- Decimal numbers
- Large numbers

---

## What Was NOT Tested

The following aspects were intentionally not tested:

- Performance testing (not required for a simple local calculator)
- Security testing (no external input sources or APIs)
- GUI rendering (this project focuses on logic and testing strategy)

---

## Testing Pyramid

The test suite follows the Testing Pyramid principle:

- **Unit Tests (Majority)**  
  Focus on isolated logic inside `core.py`.  
  These are fast, independent, and verify small pieces of functionality.

- **Integration Tests (Fewer)**  
  Verify interaction between CLI input handling and calculation logic.

This structure ensures:

- Fast execution
- High confidence in core logic
- Reduced testing cost
- Better maintainability

---

## Black-Box vs White-Box Testing

### White-Box Testing

Unit tests are primarily white-box tests because they directly call internal functions and validate specific outputs and exceptions.

### Black-Box Testing

Integration tests simulate user interactions (pressing numbers and operators) without relying on internal implementation details.

---

## Functional vs Non-Functional Testing

### Functional Testing

- Correct arithmetic operations
- Proper state reset with Clear
- Correct error handling for division by zero

### Non-Functional Testing (Not Covered)

- Performance
- Scalability
- Security
- Usability testing

These were not included because they are outside the scope of this small academic project.

---

## Regression Testing Strategy

The pytest test suite serves as a regression safety net.

If new features are added in future versions:

- Existing tests will detect unintended behavior changes
- New tests can be added without removing old ones
- Running `pytest` ensures stability before each release

---

## Test Results Summary

| Test Name | Type | Status |
|------------|-------|--------|
| Core operation tests | Unit | Pass |
| Edge case tests | Unit | Pass |
| User flow addition | Integration | Pass |
| Clear reset behavior | Integration | Pass |
| Division by zero display | Integration | Pass |

All tests pass successfully.