"""
Simple Todo List Application
A command-line todo list manager for learning Git workflows
"""

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, task):
        """Add a new todo item"""
        self.todos.append({"task": task, "completed": False})
        print(f"✓ Added: {task}")

    def list_todos(self):
        """Display all todos"""
        if not self.todos:
            print("No todos yet! Add one to get started.")
            return

        print("\n=== Your Todos ===")
        for idx, todo in enumerate(self.todos, 1):
            status = "✓" if todo["completed"] else "○"
            print(f"{idx}. [{status}] {todo['task']}")
        print()

    def complete_todo(self, index):
        """Mark a todo as completed"""
        if 0 <= index < len(self.todos):
            self.todos[index]["completed"] = True
            print(f"✓ Completed: {self.todos[index]['task']}")
        else:
            print("Invalid todo number!")

    def delete_todo(self, index):
        """Delete a todo item"""
        if 0 <= index < len(self.todos):
            task = self.todos.pop(index)
            print(f"✗ Deleted: {task['task']}")
        else:
            print("Invalid todo number!")


def main():
    """Main application loop"""
    todo_list = TodoList()

    print("=" * 40)
    print("  Welcome to Git Workshop Todo App!")
    print("=" * 40)

    while True:
        print("\nCommands: [a]dd, [l]ist, [c]omplete, [d]elete, [q]uit")
        choice = input("What would you like to do? ").lower().strip()

        if choice == 'a':
            task = input("Enter todo: ")
            todo_list.add_todo(task)
        elif choice == 'l':
            todo_list.list_todos()
        elif choice == 'c':
            todo_list.list_todos()
            try:
                num = int(input("Which todo to complete? ")) - 1
                todo_list.complete_todo(num)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == 'd':
            todo_list.list_todos()
            try:
                num = int(input("Which todo to delete? ")) - 1
                todo_list.delete_todo(num)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()


class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        """Register a new user"""
        if username in self.users:
            print("User already exists!")
            return False
        self.users[username] = password
        return True

    def login(self, username, password):
        """Login a user"""
        if username not in self.users:
            print("User not found!")
            return False
        if self.users[username] == password:
            print(f"Welcome back, {username}!")
            return True
        print("Invalid password!")
        return False

    def validate_password(self, password):
        """Validate password strength"""
        if len(password) < 8:
            return False
        return True


def print_header():
    """Print a nice header"""
    print("╔════════════════════════════════════════╗")
    print("║   Git Workshop Todo List Manager      ║")
    print("╔════════════════════════════════════════╗")


def print_menu():
    """Print menu options"""
    print("\n┌─ Menu ─────────────────────────┐")
    print("│ [a]dd    - Add a new todo      │")
    print("│ [l]ist   - List all todos      │")
    print("│ [c]omplete - Mark as done      │")
    print("│ [d]elete - Remove a todo       │")
    print("│ [q]uit   - Exit program        │")
    print("└────────────────────────────────┘")


def save_to_file(todos, filename="todos.txt"):
    """Save todos to a file"""
    with open(filename, 'w') as f:
        for idx, todo in enumerate(todos, 1):
            status = "DONE" if todo["completed"] else "TODO"
            f.write(f"{idx}. [{status}] {todo['task']}\n")
    print(f"✓ Saved to {filename}")


class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        """Register a new user"""
        if username in self.users:
            print("User already exists!")
            return False
        self.users[username] = password
        return True

    def login(self, username, password):
        """Login a user"""
        if username not in self.users:
            print("User not found!")
            return False
        if self.users[username] == password:
            print(f"Welcome back, {username}!")
            return True
        print("Invalid password!")
        return False

    def validate_password(self, password):
        """Validate password strength"""
        if len(password) < 8:
            return False
        return True


def print_header():
    """Print a nice header"""
    print("╔════════════════════════════════════════╗")
    print("║   Git Workshop Todo List Manager      ║")
    print("╔════════════════════════════════════════╗")


def print_menu():
    """Print menu options"""
    print("\n┌─ Menu ─────────────────────────┐")
    print("│ [a]dd    - Add a new todo      │")
    print("│ [l]ist   - List all todos      │")
    print("│ [c]omplete - Mark as done      │")
    print("│ [d]elete - Remove a todo       │")
    print("│ [q]uit   - Exit program        │")
    print("└────────────────────────────────┘")


def save_to_file(todos, filename="todos.txt"):
    """Save todos to a file"""
    with open(filename, 'w') as f:
        for idx, todo in enumerate(todos, 1):
            status = "DONE" if todo["completed"] else "TODO"
            f.write(f"{idx}. [{status}] {todo['task']}\n")
    print(f"✓ Saved to {filename}")
