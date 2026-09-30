# Student Library Management System

## About the project

This is a small terminal-based Python project for keeping track of books.

The program lets a user add books, look through the collection, search for a book, borrow and return books, remove books, and check the current library status.

The project is deliberately simple. It uses Python fundamentals and a JSON file instead of a GUI, web framework, database server, or external package.

## Run it

You need Python 3.

```bash
python main.py
```

No external packages are required.

## Project structure

```text
Student-Library-Management-System/
├── main.py
├── data/
│   └── books.json
├── artifacts/
├── tests/
├── README.md
├── statement.md
├── requirements.txt
└── Project_Report.md
```

`main.py` is the entry point and contains the complete working application.

`data/books.json` keeps the book records between runs.

`artifacts/` contains the design notes used for the project diagrams.

`tests/` contains the testing material.

## Main features

- Add a book
- View all books
- Search by ID, title, or author
- Borrow a book
- Return a book
- Remove a book
- View library statistics
- Save changes automatically

## Python concepts used

The project mainly uses variables, strings, lists, dictionaries, conditions, loops, functions, terminal input/output, JSON, file handling, and basic exception handling.

## Scope

This is an academic project for a small library. It does not include accounts, online access, fines, GUI development, or a database server.
