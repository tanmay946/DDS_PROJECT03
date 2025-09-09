

from collections import deque

# Node representing a single book in the library (Doubly Linked List Node)
class BookNode:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False  # Borrowed status
        self.prev = None
        self.next = None

# Action class to support undo functionality
class Action:
    def __init__(self, action_type, book_id):
        self.action_type = action_type  # 'borrow' or 'return'
        self.book_id = book_id

# Main E-Library system
class ELibrary:
    def __init__(self):
        self.head = None  # Head of doubly linked list
        self.tail = None  # Tail of doubly linked list
        self.book_count = 0
        self.undo_stack = deque()  # Stack to track undo actions

    # Internal method to find book by ID
    def _find_by_id(self, book_id):
        current = self.head
        while current:
            if current.book_id == book_id:
                return current
            current = current.next
        return None

    # Internal method to find book by exact title
    def _find_by_title(self, title):
        current = self.head
        while current:
            if current.title.lower() == title.lower():
                return current
            current = current.next
        return None

    # Add a new book to the library
    def add_book(self, title, author):
        self.book_count += 1
        new_book = BookNode(self.book_count, title, author)
        if not self.head:
            self.head = self.tail = new_book
        else:
            self.tail.next = new_book
            new_book.prev = self.tail
            self.tail = new_book
        print(f"✅ Book Added: [{self.book_count}] '{title}' by {author}")

    # Borrow a book by title
    def borrow_book(self, title):
        book = self._find_by_title(title)
        if not book:
            print(f"❌ Book '{title}' not found.")
            return
        if book.is_borrowed:
            print(f"⚠ '{title}' is already borrowed.")
            return
        book.is_borrowed = True
        self.undo_stack.append(Action('borrow', book.book_id))
        print(f"📚 You borrowed '{title}'")

    # Return a borrowed book
    def return_book(self, title):
        book = self._find_by_title(title)
        if not book:
            print(f"❌ Book '{title}' not found.")
            return
        if not book.is_borrowed:
            print(f"⚠ '{title}' was not borrowed.")
            return
        book.is_borrowed = False
        self.undo_stack.append(Action('return', book.book_id))
        print(f"📦 You returned '{title}'")

    # Undo the last borrow or return action
    def undo_last_action(self):
        if not self.undo_stack:
            print("⚠ No actions to undo.")
            return
        last_action = self.undo_stack.pop()
        book = self._find_by_id(last_action.book_id)
        if not book:
            print(f"Undo failed: Book ID {last_action.book_id} not found.")
            return
        if last_action.action_type == 'borrow':
            book.is_borrowed = False
            print(f"↩ Undo: Borrow of '{book.title}' undone.")
        elif last_action.action_type == 'return':
            book.is_borrowed = True
            print(f"↩ Undo: Return of '{book.title}' undone.")

    # Search for books by title keyword
    def search_by_title(self, keyword):
        current = self.head
        found = False
        print(f"\n🔍 Searching by title '{keyword}':")
        while current:
            if keyword.lower() in current.title.lower():
                status = "Borrowed" if current.is_borrowed else "Available"
                print(f" - [{current.book_id}] {current.title} by {current.author} [{status}]")
                found = True
            current = current.next
        if not found:
            print("No books found.")

    # Search for books by author keyword
    def search_by_author(self, keyword):
        current = self.head
        found = False
        print(f"\n🔍 Searching by author '{keyword}':")
        while current:
            if keyword.lower() in current.author.lower():
                status = "Borrowed" if current.is_borrowed else "Available"
                print(f" - [{current.book_id}] {current.title} by {current.author} [{status}]")
                found = True
            current = current.next
        if not found:
            print("No books found.")

    # Display all books in the library
    def display_inventory(self):
        if not self.head:
            print("📭 Inventory is empty.")
            return
        print("\n📚 E-Library Inventory:")
        current = self.head
        while current:
            status = "Borrowed" if current.is_borrowed else "Available"
            print(f" - [{current.book_id}] {current.title} by {current.author} [{status}]")
            current = current.next

# Sample usage
if __name__ == "__main__":
    lib = ELibrary()
    lib.add_book("1984", "George Orwell")
    lib.add_book("To Kill a Mockingbird", "Harper Lee")
    lib.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    lib.display_inventory()
    lib.borrow_book("1984")
    lib.return_book("1984")
    lib.undo_last_action()
    lib.undo_last_action()
    lib.undo_last_action()
    lib.search_by_title("great")
    lib.search_by_author("Orwell")
    lib.display_inventory()
