import json
import os
from typing import List, Dict, Any

# constants
NEW_BOOK: Dict[str, Any] = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True,
}


def get_inventory_path() -> str:
    """Return the path to ``inventory.json`` located in the same
    directory as this script. Using an absolute path avoids
    ``FileNotFoundError`` when the module is executed from a different
    working directory."""

    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "inventory.json")


def load_inventory(path: str) -> List[Dict[str, Any]]:
    """Load the inventory from *path*.

    If the file doesn't exist, an empty list is returned so callers can
    continue working with the inventory without crashing.
    """

    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_inventory(path: str, inventory: List[Dict[str, Any]]) -> None:
    """Write ``inventory`` back to *path* using pretty formatting."""

    with open(path, "w") as file:
        json.dump(inventory, file, indent=4)


def display_inventory(inventory: List[Dict[str, Any]]) -> None:
    """Print a human‑readable summary of each book in ``inventory``."""

    if not inventory:
        print("Inventory is empty.")
        return

    print("\nUpdated Inventory:\n")
    for book in inventory:
        title = book.get("title", "Unknown")
        author = book.get("author", "Unknown")
        price = book.get("price", "N/A")
        in_stock = book.get("in_stock", False)
        print(
            f"Title: {title} | Author: {author} | Price: ${price} | In stock: {in_stock}"
        )


def main() -> None:
    inventory_file = get_inventory_path()

    inventory = load_inventory(inventory_file)
    print("Total number of books:", len(inventory))

    inventory.append(NEW_BOOK)
    save_inventory(inventory_file, inventory)
    print("New book added and inventory updated successfully.")

    display_inventory(inventory)


if __name__ == "__main__":
    main()
