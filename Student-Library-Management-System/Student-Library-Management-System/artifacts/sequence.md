# Sequence Diagram

Example: borrowing a book.

```text
User              main.py              books.json
 |                   |                     |
 |-- choose Borrow ->|                     |
 |-- enter Book ID ->|                     |
 |                   |-- find book ------->|
 |                   |<-- book data --------|
 |                   |                     |
 |                   |-- check status       |
 |                   |-- set Borrowed       |
 |                   |-- save -------------->|
 |                   |<-- saved -------------|
 |<-- success -------|                     |
```
