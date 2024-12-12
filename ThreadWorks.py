import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox, StringVar, Listbox, END
from PIL import Image, ImageTk
import sqlite3

DATABASE_FILE = "threadworksdb"

def initialize_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
                   users(user_id INT PRIMARY KEY, 
                   username TEXT NOT NULL, 
                   password TEXT NOT NULL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
                   inventory(product_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   product_name TEXT NOT NULL, 
                   price INT NOT NULL, 
                   stock INT NOT NULL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
                   orders(order_id INTEGER PRIMARY KEY AUTOINCREMENT, customer_name TEXT NOT NULL, product_name TEXT NOT NULL, quantity INT NOT NULL, order_date DATE NOT NULL)""")

    conn.commit()
    conn.close()

def load_login_data(username):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT username, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()
    
    if user:
        return {"username": user[0], "password": user[1]}
    return None

def save_login_data(username, password):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def load_inventory_data():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT product_id, product_name, stock, price FROM inventory")
    items = cursor.fetchall()

    conn. close()
    return [{"id": item[0], "name": item[1], "quantity": [2], "price": [3]} for item in items]

def save_inventory_data(item_name, quantity, price):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO inventory(product_name, stock, price) VALUES (?, ?, ?)", (item_name, quantity, price))
    conn.commit()
    conn.close()

def load_order_data():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT order_id, customer_name, product_name, quantity, order_date FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders

def save_order_data(order_id, customer_name, product_name, quantity, order_date):

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO order(order_id, customer_name, product_name, quantity, order_date) VALUES (?, ?, ? ,?, ?)", (order_id, customer_name, product_name, quantity, order_date))
    conn.commit()
    conn.close()

initialize_database()
inventory_date = load_inventory_data()
login_data = load_login_data("admin")

def switch_frame(current_frame, new_frame):
    if current_frame:
        current_frame.pack_forget()
    new_frame.pack(fill="both", expand=True)

# signup page interface
def signup_page(threadw):
    signup_frame = ctk.CTkFrame(threadw, fg_color="#E3DED1")

    ctk.CTkLabel(signup_frame, text="Sign Up", font=("Arial", 20, "bold"), text_color="black").pack(pady=20)
    
    username_var = ctk.StringVar()
    password_var = ctk.StringVar()
    
    ctk.CTkLabel(signup_frame, text="Username:", text_color="black").pack(pady=5)
    ctk.CTkEntry(signup_frame, textvariable=username_var).pack(pady=5)
    
    ctk.CTkLabel(signup_frame, text="Password:", text_color="black").pack(pady=5)
    ctk.CTkEntry(signup_frame, textvariable=password_var, show="*").pack(pady=5)
    
    # To begin using the program, the first step is to create a user account by providing your personal information and setting up login credentials.
    def register_user():
        username = username_var.get().strip()
        password = password_var.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and Password cannot be empty!")
            return

        user_data = load_login_data(username)
    
        if user_data:
            messagebox.showerror("Error", "Username already exists!")
        else:
            save_login_data(username, password)
            messagebox.showinfo("Success", "Account created successfully!")
            switch_frame(signup_frame, login_page(threadw))
    
    ctk.CTkButton(signup_frame, text="Sign Up", fg_color= "#523F31", hover_color= "#070504", command=register_user).pack(pady=10)
    ctk.CTkButton(signup_frame, text="Go to Login", fg_color= "#2D1E17", hover_color= "#070504", command=lambda: switch_frame(signup_frame, login_page(threadw))).pack(pady=10)

    return signup_frame

# login page interface
def login_page(threadw):
    login_frame = ctk.CTkFrame(threadw, fg_color="#E3DED1")

    ctk.CTkLabel(login_frame, text="Login", font=("Arial", 20, "bold"), text_color="black").pack(pady=20)
    
    username_var = ctk.StringVar()
    password_var = ctk.StringVar()
    
    ctk.CTkLabel(login_frame, text="Username:", text_color="black").pack(pady=5)
    ctk.CTkEntry(login_frame, textvariable=username_var).pack(pady=5)
    
    ctk.CTkLabel(login_frame, text="Password:", text_color="black").pack(pady=5)
    ctk.CTkEntry(login_frame, textvariable=password_var, show="*").pack(pady=5)
    
    # authenticates the user by verifying their submitted credentials with data that has been stored.
    def login_user():
        username = username_var.get().strip()
        password = password_var.get().strip()

        user_data = load_login_data(username)
    
        if user_data and user_data["password"] == password:
            messagebox.showinfo("Success", "Login successful!")
            switch_frame(login_frame, main_page(threadw))
        else:
            messagebox.showerror("Error", "Invalid Username or Password!")

    ctk.CTkButton(login_frame, text="Login", fg_color= "#523F31", hover_color= "#070504", command=login_user).pack(pady=10)
    ctk.CTkButton(login_frame, text="Sign Up", fg_color= "#2D1E17", hover_color= "#070504", command=lambda: switch_frame(login_frame, signup_page(threadw))).pack(pady=10)

    return login_frame

# main window
def main_page(threadw):
    main_frame = ctk.CTkFrame(threadw, fg_color= "#E3DED1")
    main_frame.pack(fill="both", expand = True)

    left_frame = ctk.CTkFrame(main_frame, fg_color="#E3DED1")
    left_frame.pack(side="left", fill="y", expand = True)
    
    # instering the image in the left frame
    try:
        image = Image.open("ct2.jpg")
        left_frame_height = threadw.winfo_height()
        image = image.resize((400, left_frame_height))
        photo = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(left_frame, text="", image=photo).pack(pady=20)
        image_label.image = photo
        image_label.pack(fill="both", expand = True)
    except:
        ctk.CTkLabel(left_frame, text="Image not Available", font=("Arial", 16)).pack(pady=20)

    right_frame = ctk.CTkFrame(main_frame, fg_color="#E3DED1")
    right_frame.pack(side="right", fill="both", expand=True)


    ctk.CTkLabel(right_frame, text="ThreadWorks!", font=("Arial", 20, "bold"), text_color="black").pack(pady=25)
    ctk.CTkLabel(right_frame, text="Manage your crochet products, orders,\nand sales all in one place.",font=("Arial", 14), text_color="black").pack(pady=20)

    # buttons
    ctk.CTkButton(right_frame, text="Inventory", fg_color= "#523F31", hover_color= "#070504", width=200, command=lambda: switch_frame(main_frame, inventory_page(threadw))).pack(pady=10)
    ctk.CTkButton(right_frame, text="View Orders", fg_color= "#523F31", hover_color= "#070504", width=200, command=lambda: switch_frame(main_frame, orders_page(threadw))).pack(pady=10)
    ctk.CTkButton(right_frame, text="View Sales Report", fg_color= "#523F31", hover_color= "#070504", width=200, command=lambda: switch_frame(main_frame, sales_page(threadw))).pack(pady=10)
    ctk.CTkButton(right_frame, text="View Invoice", fg_color= "#523F31", hover_color= "#070504", width=200, command=lambda: switch_frame(main_frame, invoice_page(threadw))).pack(pady=10)
    ctk.CTkButton(right_frame, text="Exit Application", width=200, fg_color= "#2D1E17", hover_color= "#070504", command=threadw.quit).pack(pady=20)

    return main_frame

# inventory interface
def inventory_page(threadw):
    inventory_frame = ctk.CTkFrame(threadw, fg_color= "#E3DED1")

    # updates the listbox with the latest inventory data.
    def update_listbox():
        inventory_listbox.delete(0, END)
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT product_name, price, stock FROM inventory")
        items = cursor.fetchall()
        conn.close()

        for item in items:
            inventory_listbox.insert(END, f"{item[0]} - Price: ₱{item[1]} - Stock: {item[2]}")
    
    # adding items in the inventory
    def add_item():
        name = item_name.get().strip()
        try:
            price = float(item_price.get().strip())
            stock = int(item_stock.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Price and Stock must be numeric values!")
            return

        if not name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM inventory WHERE product_name = ?", (name,))
        if cursor.fetchone():
            messagebox.showerror("Item already exists!")
            conn.close()
            return
        
        cursor.execute("INSERT INTO inventory (product_name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
        conn.commit()
        conn. close()

        update_listbox()
        clear_form()
    
    def clear_form():
        item_name.set("")
        item_price.set("")
        item_stock.set("")

    # updates the selected item in the inventory.
    def update_item():
        selected = inventory_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No item selected!")
            return
        index = selected[0]
        item_details = inventory_listbox.get(index).split("-")
        old_name = item_details[0].strip()

        new_name = item_name.get().strip()

        try:
            price = float(item_price.get().strip())
            stock = int(item_stock.get().strip())
        except ValueError:
            messagebox.showerror("Price and Stock must be numeric values!")
            return

        if not new_name:
            messagebox.showerror("Name cannot be empty!")
            return
        
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM inventory WHERE product_name = ?", (new_name,))
        if cursor.fetchone():
            messagebox.showerror("Error")
            conn.close()

        cursor.execute("UPDATE inventory SET product_name = ?, price = ?, stock = ? WHERE product_name = ?", (new_name, price, stock, old_name))

        conn.commit()
        conn.close()
        update_listbox()

    # deletes the selected item from the inventory.
    def delete_item():
        selected = inventory_listbox.curselection()
        if not selected:
            messagebox.showerror("No item selected!")
        
        index = selected[0]
        item_details = inventory_listbox.get(index).split("-")
        name = item_details[0].strip()

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM inventory WHERE product_name = ?", (name,))
        conn.commit()
        conn.close()

        update_listbox()
        clear_form()

    ctk.CTkLabel(inventory_frame, text="Manage Inventory", font=("Arial", 20, "bold"), text_color="black").pack(pady=10)

    inventory_listbox = Listbox(inventory_frame, height=10, width=50)
    inventory_listbox.pack(pady=10)
    update_listbox()

    input_frame = ctk.CTkFrame(inventory_frame, fg_color="#C1B59F")
    input_frame.pack(pady=10, fill="x", padx=20)

    # variables
    item_name = StringVar()
    item_price = StringVar()
    item_stock = StringVar()

    # product infos entry
    ctk.CTkLabel(input_frame, text="Item Name:", font=("Arial", 14), text_color="black").grid(row=0, column=0, padx=5, pady=5)
    ctk.CTkEntry(input_frame, textvariable=item_name, placeholder_text="Enter item name", width=120).grid(row=0, column=1, padx=5, pady=5)
    ctk.CTkLabel(input_frame, text="Price:", font=("Arial", 14), text_color="black").grid(row=0, column=2, padx=5, pady=5)
    ctk.CTkEntry(input_frame, textvariable=item_price, placeholder_text="Enter price", width=120).grid(row=0, column=3, padx=5, pady=5)
    ctk.CTkLabel(input_frame, text="Stock:", font=("Arial", 14), text_color="black").grid(row=0, column=4, padx=5, pady=5)
    ctk.CTkEntry(input_frame, textvariable=item_stock, placeholder_text="Enter stock quantity", width=120).grid(row=0, column=5, padx=5, pady=5)

    # buttons
    ctk.CTkButton(inventory_frame, text="Add Item", fg_color= "#523F31", hover_color= "#070504", command=add_item).pack(pady=5)
    ctk.CTkButton(inventory_frame, text="Update Item", fg_color= "#523F31", hover_color= "#070504", command=update_item).pack(pady=5)
    ctk.CTkButton(inventory_frame, text="Delete Item", fg_color= "#523F31", hover_color= "#070504", command=delete_item).pack(pady=5)
    ctk.CTkButton(inventory_frame, text="Go Back", fg_color= "#2D1E17", hover_color= "#070504", command=lambda: switch_frame(inventory_frame, main_page(threadw))).pack(pady=20)

    return inventory_frame

# order deatils interface
def orders_page(threadw):
    orders_frame = ctk.CTkFrame(threadw, fg_color="#E3DED1")

    def update_order_listbox():
        orders_listbox.delete(0, "end")

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("""SELECT o.rowid AS order_id, o.customer_name, i.product_name, o.quantity, o.order_date FROM orders o JOIN inventory i ON o.product_name = i.product_name""")
        orders = cursor.fetchall()
        conn.close()

        for order in orders:
            orders_listbox.insert("end", f"{order[0]} - {order[1]} - {order[2]} - Quantity: {order[3]} - Purchased Date: {order[4]}")

    #                         
    def add_order():
        customer_name = customer_name_var.get().strip()
        product_name = product_name_var.get().strip()
        quantity = quantity_var.get().strip()
        order_date = order_date_var.get().strip()

        if not customer_name or not product_name or not quantity or not order_date:
            messagebox.showerror("Error", "All fields are required!")
            return
    
        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a numeric value!")
            return
    
        if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be a positive integer!")
            return
    
        try:
            formatted_date = datetime.strptime(order_date, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Invalid date format! Use YYYY-MM-DD.")
            return

        try:
        # Check if the item exists and has sufficient stock
            conn = sqlite3.connect(DATABASE_FILE)
            cursor = conn.cursor()

            cursor.execute("SELECT stock FROM inventory WHERE product_name = ?", (product_name,))
            result = cursor.fetchone()

            if not result:
                messagebox.showerror("Error", f"Item '{product_name}' not found in inventory!")
                conn.close()
                return

            current_stock = result[0]
            if current_stock < quantity:
                messagebox.showerror("Error", "Insufficient stock available!")
                conn.close()
                return

        # Reduce the stock in the inventory
            new_stock = current_stock - quantity
            cursor.execute("UPDATE inventory SET stock = ? WHERE product_name = ?", (new_stock, product_name))
        
        # Add the order to the orders table
            cursor.execute("INSERT INTO orders (customer_name, product_name, quantity, order_date) VALUES (?, ?, ?, ?)",
                       (customer_name, product_name, quantity, formatted_date))
            conn.commit()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error", str(e))

        finally:
            update_order_listbox()
            customer_name_var.set("")
            product_name_var.set("")
            quantity_var.set("")
            order_date_var.set("")

    def delete_order():
        selected = orders_listbox.curselection()
        
        if not selected:
            messagebox.showerror("No item selected!")
            return
        
        index = selected[0]
        order_details = orders_listbox.get(index).split("-")
        order_id = order_details[0].replace("Order #", "").strip()

        try:
            conn = sqlite3.connect(DATABASE_FILE)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM orders WHERE rowid = ?", (order_id,))
            conn.commit()

        except Exception as e:
            messagebox.showerror("Error")
        
        finally:
            conn.close()
 
        update_order_listbox()
        
    ctk.CTkLabel(orders_frame, text="Manage Orders", font=("Arial", 20, "bold"), text_color="black").pack(pady=10)

    # listbox for orders
    orders_listbox = Listbox(orders_frame, width=70, height=10)
    orders_listbox.pack(pady=10)
    update_order_listbox()

    input_frame = ctk.CTkFrame(orders_frame, fg_color="#C1B59F")
    input_frame.pack(pady=10)

    customer_name_var = ctk.StringVar()
    product_name_var = ctk.StringVar()
    quantity_var = ctk.StringVar()
    order_date_var = ctk.StringVar()

    ctk.CTkLabel(input_frame, text="Customer Name:", text_color="black").grid(row=0, column=0, padx=5, pady=5)
    ctk.CTkEntry(input_frame, textvariable=customer_name_var).grid(row=0, column=1, padx=5, pady=5)

    ctk.CTkLabel(input_frame, text="Product Name:", text_color="black").grid(row=0, column=2, padx=5, pady=5)
    ctk.CTkEntry(input_frame, textvariable=product_name_var).grid(row=0, column=3, padx=5, pady=5)

    ctk.CTkLabel(input_frame, text="Quantity:", text_color="black").grid(row=1, column=0, padx=5, pady=5)
    ctk.CTkEntry(input_frame, textvariable=quantity_var).grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkLabel(input_frame, text="Purchased Date:", text_color="black").grid(row=1, column=2, padx=5, pady=5)
    ctk.CTkEntry(input_frame, textvariable=order_date_var).grid(row=1, column=3, padx=5, pady=5)

    # buttons
    ctk.CTkButton(orders_frame, text="Add Order", fg_color= "#523F31", hover_color= "#070504", command=add_order).pack(pady=5)
    ctk.CTkButton(orders_frame, text="Delete Order", fg_color= "#523F31", hover_color= "#070504", command=delete_order).pack(pady=5)
    ctk.CTkButton(orders_frame, text="Go Back", fg_color= "#2D1E17", hover_color= "#070504", command=lambda: switch_frame(orders_frame, main_page(threadw))).pack(pady=15)

    return orders_frame

def sales_page(threadw):
    sales_frame = ctk.CTkFrame(threadw, fg_color="#E3DED1")

    def generate_sales_report():
        sales_listbox.delete(0, "end")  # Clear the listbox before inserting new data

        # Connect to the SQLite database and fetch orders
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT product_name, quantity FROM orders")
        orders = cursor.fetchall()
        conn.close()

        if not orders:
            messagebox.showinfo("No orders available to generate a sales report!")
            return

        # Calculate total sales by product
        sales_summary = {}
        for order in orders:
            product_name = order[0]
            quantity = order[1]
            if product_name in sales_summary:
                sales_summary[product_name] += quantity
            else:
                sales_summary[product_name] = quantity

        # Display sales report in the Listbox
        for product, total_quantity in sales_summary.items():
            sales_listbox.insert("end", f"{product}: {total_quantity} units sold")


    ctk.CTkLabel(sales_frame, text="Sales Report", font=("Arial", 20, "bold"), text_color="black").pack(pady=10)

    # listbox to display sales report
    sales_listbox = Listbox(sales_frame, width=50, height=10)
    sales_listbox.pack(pady=10)

    # buttons
    ctk.CTkButton(sales_frame, text="Generate Sales Report", fg_color= "#523F31", hover_color= "#070504", command=generate_sales_report).pack(pady=10)
    ctk.CTkButton(sales_frame, text="Go Back", fg_color= "#2D1E17", hover_color= "#070504", command=lambda: switch_frame(sales_frame, main_page(threadw))).pack(pady=10)

    return sales_frame

def invoice_page(threadw):
    invoice_frame = ctk.CTkFrame(threadw, fg_color="#E3DED1")

    def calculate_invoices():
        invoice_listbox.delete(0, END)  # Clear the listbox before inserting new data
        
        # Connect to the SQLite database
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("""SELECT o.rowid AS order_id, o.customer_name, i.product_name, o.quantity, i.price, (o.quantity * i.price) AS total_price, o.order_date FROM orders o JOIN inventory i ON o.product_name = i.product_name""")
        
        orders = cursor.fetchall()

        if not orders:
            invoice_listbox.insert(END, "No orders available.")
        else:
            for order in orders:
                order_id, customer_name, product_name, quantity, price, total_price, order_date = order
                invoice_text = f"Order #{order_id}: {customer_name} bought {quantity} x {product_name} @ ₱{price:.2f} each - Total: ₱{total_price:.2f} - {order_date}"
                invoice_listbox.insert(END, invoice_text)

        # Close the database connection
            conn.close()
            
    ctk.CTkLabel(invoice_frame, text="Invoices", font=("Arial", 20, "bold"), text_color="black").pack(pady=10)

    # invoice listbox
    invoice_listbox = Listbox(invoice_frame, height=15, width=80)
    invoice_listbox.pack(pady=10)

    # button
    ctk.CTkButton(invoice_frame, text="Generate Invoices", fg_color= "#523F31", hover_color= "#070504", command=calculate_invoices).pack(pady=10)
    ctk.CTkButton(invoice_frame, text="Go Back", fg_color= "#2D1E17", hover_color= "#070504", command=lambda: switch_frame(invoice_frame, main_page(threadw))).pack(pady=10)
    
    return invoice_frame

def ThreadWorks():
    threadw = ctk.CTk()
    threadw.title("ThreadWorks - Crochet Sales Management")
    threadw.geometry("800x500")
    threadw.resizable(False, False)

    switch_frame(None, login_page(threadw))
    threadw.mainloop()
    
ThreadWorks()