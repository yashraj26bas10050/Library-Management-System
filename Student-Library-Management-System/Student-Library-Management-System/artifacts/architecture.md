# Architecture Diagram

The project has one clear entry point: `main.py`.

```text
                 USER
                   |
                   v
             TERMINAL MENU
                   |
                   v
                main.py
          _________|_________
         |         |         |
         v         v         v
      Book      Search    Borrow /
    Management             Return
         |         |         |
         |_________|_________|
                   |
                   v
            Library Status
                   |
                   v
              books.json
```

The JSON file is used for keeping the data after the program closes.
