"""Inventory Management System

This module provides functions to manage a simple inventory,
including adding, removing, saving, and loading items securely.
It follows Python best practices for style, safety, and readability.
"""

import json
from datetime import datetime

# In-memory stock data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a new item or update its quantity in the stock."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid item name or quantity type.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a quantity of an item, deleting it if quantity becomes zero."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")
    except (TypeError, ValueError) as err:
        print(f"Invalid operation while removing item: {err}")


def get_qty(item):
    """Return quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Inventory file not found. Starting with empty data.")
        return {}


def save_data(file_path="inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)


def print_data():
    """Print all items and quantities."""
    print("Items Report:")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """Return items below the given stock threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function demonstrating inventory operations."""
    data = load_data()
    stock_data.update(data)

    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    print_data()


if __name__ == "__main__":
    main()
