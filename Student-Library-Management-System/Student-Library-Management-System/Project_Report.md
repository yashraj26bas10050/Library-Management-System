# Student Library Management System
## Project Report

### 1. Introduction
The Student Library Management System is a simple terminal-based Python program for managing a small collection of books. It was kept intentionally small so that the implementation stays within the Python fundamentals covered by the course.

### 2. Problem Statement
Manual book tracking can make it difficult to know which books are available and which have been borrowed. The program provides a single place to maintain these records.

### 3. Functional Requirements
- **Book management:** add, view, and remove books.
- **Book search:** search by ID, title, or author.
- **Borrow and return:** change the availability of a book.
- **Library status:** show total, available, and borrowed books.

### 4. Non-Functional Requirements
- **Usability:** simple numbered terminal menu.
- **Reliability:** common invalid inputs are handled without closing the program.
- **Performance:** designed for a small collection and immediate normal operations.
- **Maintainability:** related work is separated into functions in `main.py`.
- **Portability:** only Python's standard library is required.

### 5. System Design
The user interacts with `main.py` through the terminal. The program performs the selected operation and uses `data/books.json` for persistent book records.

```text
User
  |
  v
Terminal Menu
  |
  v
main.py
  |
  +-- Book Management
  +-- Search
  +-- Borrow / Return
  +-- Library Status
  |
  v
books.json
```

### 6. Workflow

```text
Start
  ↓
Load saved books
  ↓
Show menu
  ↓
Choose operation
  ↓
Validate input
  ↓
Perform operation
  ↓
Save changes if required
  ↓
Show result
  ↓
Return to menu
  ↓
Exit
```

### 7. Implementation
The complete working application is in `main.py`. It uses lists and dictionaries for book records and functions for individual operations. JSON is used to save the records.

### 8. Data Storage
Each book contains a Book ID, title, author, and status. The records are stored in `data/books.json`.

### 9. Testing
Testing covers normal operations and common mistakes such as duplicate IDs, missing books, invalid choices, borrowing an already borrowed book, and returning an available book. The detailed test list is in `tests/test_cases.md`.

### 10. Results
For the final report, screenshots should be added showing the main menu, book operations, search, borrowing/returning, library status, and an error case.

### 11. Challenges and Solutions
The main implementation challenges were keeping Book IDs unique, maintaining the correct borrowed/available status, saving data between runs, and handling simple user mistakes.

### 12. Learning Outcomes
The project gave practical experience with functions, lists, dictionaries, loops, conditions, file handling, JSON, input validation, and organizing a small Python project.

### 13. Future Scope
Possible future additions include student/member records, due dates, fine calculation, a GUI, or database storage.

### 14. References
- Python 3 documentation: https://docs.python.org/3/
- Course project requirements document
