# 📚 E-Library Management System

A simple command-line based E-Library system written in Python. It allows you to manage books using a doubly linked list and supports borrowing, returning, undo operations, and search functionality.

---

## 🚀 Features

- ✅ Add new books to the library
- 📖 Borrow and return books
- ↩ Undo the last borrow or return operation
- 🔍 Search books by title or author
- 📋 Display current inventory with availability status
- 🧠 Uses doubly linked list + stack (for undo)

---

## 🛠️ Requirements

- Python 3.6+

No external libraries required except `collections` (standard library).

---

## ▶️ How to Run

1. Save the code as `elibrary.py`.
2. Run it using Python:

```bash
python elibrary.py


📘 Sample Output
✅ Book Added: [1] '1984' by George Orwell
✅ Book Added: [2] 'To Kill a Mockingbird' by Harper Lee
✅ Book Added: [3] 'The Great Gatsby' by F. Scott Fitzgerald

📚 E-Library Inventory:
 - [1] 1984 by George Orwell [Available]
 - [2] To Kill a Mockingbird by Harper Lee [Available]
 - [3] The Great Gatsby by F. Scott Fitzgerald [Available]

📚 You borrowed '1984'
📦 You returned '1984'
↩ Undo: Return of '1984' undone.
↩ Undo: Borrow of '1984' undone.
⚠ No actions to undo.

📂 Project Structure
elibrary/
├── elibrary.py       # Main program
├── README.md         # Project documentation


🔧 Possible Improvements

#Save data to a file (JSON or DB)

#Track users and their borrowed books

#Add GUI (Tkinter or PyQt)

#Add due dates and fine calculation
