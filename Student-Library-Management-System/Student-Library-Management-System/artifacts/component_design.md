# Component / Function Design

The project intentionally uses functions instead of a complicated class hierarchy.

| Function | What it does |
|---|---|
| `load_books()` | Reads saved records |
| `save_books()` | Saves records |
| `get_required_input()` | Handles required text input |
| `find_book()` | Finds a book by ID |
| `print_books()` | Displays book records |
| `add_book()` | Adds a new book |
| `view_books()` | Shows all books |
| `search_books()` | Searches the collection |
| `borrow_book()` | Borrows an available book |
| `return_book()` | Returns a borrowed book |
| `remove_book()` | Removes an available book |
| `show_library_status()` | Counts available/borrowed books |
| `show_menu()` | Displays the menu |
| `main()` | Runs the application |

This keeps the code readable for a beginner while still giving each operation a clear responsibility.
