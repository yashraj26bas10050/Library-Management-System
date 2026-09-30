# Test Cases

| ID | Test | Expected result |
|---|---|---|
| T01 | Start the program | Main menu appears |
| T02 | View books | Saved books are displayed |
| T03 | Add a new book | Book is added as Available |
| T04 | Add an existing Book ID | Duplicate is rejected |
| T05 | Search by title or author | Matching books are displayed |
| T06 | Search for an unknown term | No-match message appears |
| T07 | Borrow an available book | Status becomes Borrowed |
| T08 | Borrow an already borrowed book | Operation is refused |
| T09 | Return a borrowed book | Status becomes Available |
| T10 | Return an available book | Operation is refused |
| T11 | Remove an available book | Book is removed |
| T12 | Remove a borrowed book | Operation is refused |
| T13 | Invalid menu choice | Program remains running |
| T14 | Empty required input | Program asks again |
| T15 | Restart after a change | Saved data remains |

## Manual flow

Start → View → Add → Search → Borrow → Return → Remove → Status → Exit.
