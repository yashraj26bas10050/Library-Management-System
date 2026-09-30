# Data Design

Each book is stored with four simple fields:

```text
book_id
title
author
status
```

Example:

```json
{
    "book_id": "B101",
    "title": "Introduction to Python",
    "author": "John Smith",
    "status": "Available"
}
```

The complete library is stored as a JSON list.

Current status values:

- `Available`
- `Borrowed`
