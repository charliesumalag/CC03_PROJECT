import json
from pyscript import Element

# Getting the message HTML element for displaying messages.
message = Element('message_el')

# _____________________CREATING A CLASS: STOCKCOUNTER_______________________________________
class StockCounter:
    # declaare a local storage key name
    STORAGE_KEY = "inventory_data"


    # _________CREATING A CONSTRUCTOR_____________
    def __init__(self):
        # Load inventory data from localStorage if available, else start with an empty inventory
        self.inventory = self.load_inventory()

    # _______________LOAD INVENTORY METHOD___________________
    def load_inventory(self):
        # datas store in localstorage
        data = js.localStorage.getItem(self.STORAGE_KEY)
        return json.loads(data) #return a json text file format
    # _______________SAVE INVENTORY METHOD___________________
    def save_inventory(self):
        # Save the inventory dictionary as a JSON string in localStorage
        js.localStorage.setItem(self.STORAGE_KEY, json.dumps(self.inventory))

    # _______________ADD METHOD___________________
    def add_stock(self, item_name, quantity):
        # Add new stock or update existing stock
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
            message.write(f"{quantity} units added to {item_name} in the inventory.")
        else:
            self.inventory[item_name] = quantity
            message.write(f"{quantity} units of {item_name} added to inventory.")

        # Save updated inventory to localStorage
        self.save_inventory()

    # _______________REMOVE METHOD___________________
    def remove_stock(self, item_name):
        # Removing an item from the inventory
        if item_name in self.inventory:
            self.inventory.pop(item_name)
            message.write(f"Item '{item_name}' removed from inventory.")
            self.save_inventory()  # Save changes to localStorage
        else:
            message.write(f"Item '{item_name}' not found in inventory.")

    # _______________UPDATE METHOD___________________
    def update_stock(self, item_name, new_quantity):
        # Update the stock quantity for an existing item
        if item_name in self.inventory:
            self.inventory[item_name] = new_quantity
            message.write(f"Stock for '{item_name}' updated to {new_quantity}.")
            self.save_inventory()  # Save changes to localStorage
        else:
            message.write(f"Item '{item_name}' not found in inventory. Cannot update.")

# _____________INSTANCE OF STOCKCOUNTER_________________________
stock_counter = StockCounter()

# __________________Getting the HTML elements__________________
add_stock_button = Element('add-stock-btn')
remove_stock_button = Element('remove-stock-btn')
update_stock_button = Element('update-stock-btn')
view_inventory_button = Element('view-btn')
add_menu_btn = Element('add-btn')
remove_menu_btn = Element('remove-btn')
update_menu_btn = Element('update-btn')
cancel_btn = Element('cancel-btn')

# Function to be called when buttons clicked
# _________________ONCLICK ON ADD BUTTON_____________________
def on_add_stock(trigger_on_click):
    item_name_el = Element('item-name')
    item_quantity_el = Element('item-quantity')

    # Get the values inputted
    item_value = item_name_el.element.value.strip()
    item_quantity = int(item_quantity_el.element.value)  # Convert input into int


    # Call the add_stock method
    stock_counter.add_stock(item_value, item_quantity)

    # Clear the input fields
    item_name_el.element.value = ""
    item_quantity_el.element.value = ""

# _________________ONCLICK ON REMOVE BUTTON_____________________
def on_remove_stock(trigger_on_click):
    item_name_el = Element('remove-item-name')

    # Get the values from input fields and normalize
    item_value = item_name_el.element.value.strip()

    # Call the remove_stock method
    stock_counter.remove_stock(item_value)

    # Clear input fields after removing stock
    item_name_el.element.value = ""

# _________________ONCLICK ON UPDATE BUTTON_____________________
def on_update_stock(trigger_on_click):
    item_name_el = Element('update-item-name')  # Use the correct ID for item name
    item_quantity_el = Element('update-item-quantity')  # Use the correct ID for quantity

    # Get the values from input fields
    item_value = item_name_el.element.value.strip()
    item_quantity = int(item_quantity_el.element.value)  # Convert quantity to an integer

    # Call the update_stock method
    stock_counter.update_stock(item_value, item_quantity)

    # Clear the input fields
    item_name_el.element.value = ""
    item_quantity_el.element.value = ""

# _________________ONCLICK ON VIEW BUTTON_____________________
def on_view_inventory(trigger_on_click):
    message.write("")  # Clear previous messages
    inventory_display_el = Element('inventory-display')  # Get the inventory display element
    inventory_display_el.element.innerHTML = ""  # Clear previous inventory

    if not stock_counter.inventory:
        inventory_display_el.element.innerHTML = "Inventory is empty."
    else:
        # Table header
        inventory_content = "<table><thead><tr><th>Item</th><th>Quantity</th></tr></thead><tbody>"
        # Loop through each item in the inventory
        for item_name, quantity in stock_counter.inventory.items():
            # Create a table row for each item
            inventory_content += f"<tr><td>{item_name}</td><td>{quantity}</td></tr>"
        inventory_content += "</tbody></table>"  # Close the table
        inventory_display_el.element.innerHTML = inventory_content  # Write it to HTML/browser

# _________________CLEAR THE MESSAGE OUTPUT_____________________
def clear_message(trigger_on_click):
    message.write("")  # Clear the message display

# Applying onclick on buttons
add_stock_button.element.onclick = on_add_stock
remove_stock_button.element.onclick = on_remove_stock
update_stock_button.element.onclick = on_update_stock
view_inventory_button.element.onclick = on_view_inventory
add_menu_btn.element.onclick = clear_message
remove_menu_btn.element.onclick = clear_message
update_menu_btn.element.onclick = clear_message
