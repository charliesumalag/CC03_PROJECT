# getting the message html element for displaying message.
message = Element('message_el')


# _____________________CREATING A CLASS: STOCKCOUNTER_______________________________________
class StockCounter:

        #___________CREATING A CONTRUCTOR_____________
            def __init__(self):
                self.inventory = {}

        # _______________ADD METHOD___________________
            def add_stock(self, item_name, quantity):
            # Add new stock or update existing stock
                #__update the quantity in the list if exist.
                if item_name in self.inventory:
                    self.inventory[item_name] += quantity
                    message.write(f"{quantity} units added to {item_name} in the inventory.")
                #__add new list if not exisit.
                else:
                    self.inventory[item_name] = quantity
                    message.write(f"{quantity} units of {item_name} added to inventory.")

        # _______________REMOVE METHOD___________________
            def remove_stock(self, item_name):
                # RemovING an item from the inventory.
                if item_name in self.inventory:
                    self.inventory.pop(item_name)
                    message.write(f"Item '{item_name}' removed from inventory.")
                else:
                    message.write(f"Item '{item_name}' not found in inventory.")

        # _______________UPDATE METHOD___________________
            def update_stock(self, item_name, new_quantity):
                # Update the stock quantity for an existing item.
                if item_name in self.inventory:
                    self.inventory[item_name] = new_quantity
                    message.write(f"Stock for '{item_name}' updated to {new_quantity}.")
                else:
                   message.write(f"Item '{item_name}' not found in inventory. Cannot update.")

#_____________INSTANCE OF STOCKCOUNTER_________________________
stock_counter = StockCounter()

#__________________Getting the html elements__________________
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
def on_add_stock(triger_on_click):
    item_name_el = Element('item-name')
    item_quantity_el = Element('item-quantity')

    # Get the values inputed
    item_value = item_name_el.element.value
    item_quantity = int(item_quantity_el.element.value) # convert input into int

    # Call the add_stock method
    stock_counter.add_stock(item_value, item_quantity)

    # clearing the input field
    item_name_el.element.value = ""
    item_quantity_el.element.value = ""


# _________________ONCLICK ON REMOVE BUTTON_____________________
def on_remove_stock(triger_on_click):
    item_name_el = Element('remove-item-name')

    # Get the values from input fields and normalize
    item_value = item_name_el.element.value.strip()

    # Call the remove_stock method
    stock_counter.remove_stock(item_value)

    # Clear input fields after removing stock
    item_name_el.element.value = ""

# _________________ONCLICK ON UPDATE BUTTON_____________________
def on_update_stock(triger_on_click):
    item_name_el = Element('update-item-name')  # Use the correct ID for item name
    item_quantity_el = Element('update-item-quantity')  # Use the correct ID for quantity

    # Get the values from input fields
    item_value = item_name_el.element.value
    item_quantity = int(item_quantity_el.element.value)  # Convert quantity to an integer

    # Call the update_stock method
    stock_counter.update_stock(item_value, item_quantity)

     # clearing the input field
    item_name_el.element.value = ""
    item_quantity_el.element.value = ""

# _________________ONCLICK ON VIEW BUTTON_____________________
def on_view_inventory(triger_on_click):
    message.write("")
    inventory_display_el = Element('inventory-display')  # Get the inventory display element
    inventory_display_el.element.innerHTML = ""  # Clear previous inventory

    if stock_counter.inventory == {}:
        inventory_display_el.element.innerHTML = "Inventory is empty."
    else:
        # table header
        inventory_content = "<table><thead><tr><th>Item</th><th>Quantity</th></tr></thead><tbody>"
        # looping each item in the list with each key values.
        for each_item_keys in stock_counter.inventory.keys():
            quantity = stock_counter.inventory[each_item_keys]
            # Create a table row for each item
            inventory_content += f"<tr><td>{each_item_keys}</td><td>{quantity}</td></tr>"
        inventory_content += "</tbody></table>"  # Close the table
        inventory_display_el.element.innerHTML = inventory_content # writing it it hmtl/browser
        message.write("")

# _________________CLEAR THE MESSAGE OUTPUT_____________________
def clear_message(triger_on_click):
     message.write("")

# ApPlying onclick on buttons
add_stock_button.element.onclick = on_add_stock
remove_stock_button.element.onclick = on_remove_stock
update_stock_button.element.onclick = on_update_stock
view_inventory_button.element.onclick = on_view_inventory
add_menu_btn.element.onclick = clear_message
remove_menu_btn.element.onclick = clear_message
update_menu_btn.element.onclick = clear_message
