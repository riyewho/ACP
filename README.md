## I. PROJECT OVERVIEW

This program addresses the challenges faced by small crochet business owners and independent artisans lacking sophisticated inventory, order, and sales management tools.  It provides a user-friendly, offline solution for organizing and automating these critical business activities, empowering users to focus on crafting and customer relationships.

**Included Features:**

* **Inventory Management:** Add, update, and monitor crochet products (name, price, stock).
* **Order Management:** Track customer orders (customer name, product, quantity, date). Maintain a client database.
* **Sales Tracking:** Track and analyze sales data (product name, quantity sold over time).
* **Invoice Generation:** Generate invoices displaying order details.

**Excluded Features:**

* **E-commerce Integration:**  Integration with online marketplaces or payment gateways is outside the scope to maintain simplicity.

**Target Users:**

* Small business owners selling handmade crochet products.
* Independent artisans selling handmade crafts.
* Entrepreneurs selling at local markets or boutiques.
* Artisans needing an offline solution.
* Crafters transitioning to small-scale business operations.

**Specific Goal:** Develop an offline management system for small handmade businesses to manage, track orders, sales, and generate invoices without internet connectivity.

**Measurable Result:** Reduce time spent on manual administrative tasks by at least 30% within six months, based on task completion analysis and user feedback.

**Achievable Objective:** Develop an easily installable and usable system. 85% of beta testers will adopt the system within three months.

**Relevant Purpose:** Deliver features enhancing operations for small crochet and handmade business owners, promoting growth and sustainability.

**Time-bound Milestone:** Launch the system and onboard at least 50 businesses in the first year, measuring productivity improvements.


## II. EXPLANATION OF PYTHON CONCEPTS AND LIBRARIES

**Libraries:**

* **`tkinter` (from `tkinter import messagebox, StringVar, Listbox, END`):**  Used for the GUI (graphical user interface), creating widgets like labels, listboxes, buttons, and entry fields. `messagebox` provides pop-up dialogs for user feedback.
* **`customtkinter` (import `customtkinter as ctk`):** A modern, customizable alternative to `tkinter` for improved GUI aesthetics.
* **`datetime` (from `datetime import datetime`):** Used for date and time management in reporting and order tracking.
* **`Pillow` (from `PIL import Image, ImageTk`):** Used to display images in the GUI.
* **`sqlite3` (import `sqlite3`):**  For database management (creating tables, querying, updating data).


**Concepts:**

The project utilizes several core Python concepts:

1.  **Modular Programming:** The code is organized into functions for better readability, maintainability, and reusability.  Each function has a specific, well-defined task.

2.  **Database Interaction (SQLite3):**  The application interacts with a SQLite database using SQL commands for data persistence. This includes creating tables, inserting data, querying information, updating records, and deleting entries.  The use of parameterized queries is highly recommended for security.

3.  **GUI Programming (Tkinter/CustomTkinter):**  The graphical user interface is built using Tkinter or CustomTkinter, creating widgets, handling user events, and managing the layout.

4.  **Event Handling:** The GUI responds to user actions (button clicks, data entry) through event handling mechanisms.

5.  **Data Structures:**  Python data structures like lists and dictionaries (or custom classes) are used to organize and manage data (users, inventory, orders, sales).

6.  **Input Validation:**  Input validation is implemented to ensure data integrity and security, checking for empty fields, correct data types, and appropriate formats.

7.  **File I/O (Implicit):**  Database operations involve file I/O for data persistence.

8.  **Exception Handling (Implicit):**  Error handling (using `try...except` blocks) is implemented to manage potential errors during database operations or GUI interactions.

9.  **Data Aggregation and Reporting:** Data aggregation and reporting functions summarize sales data from the database.

10. **State Management:**  A mechanism (e.g., using frames) manages the application's state, switching between different views.


## III. DETAILS OF THE CHOSEN SDG AND ITS INTEGRATION

This project aligns with **SDG 8: Decent Work and Economic Growth** and **SDG 9: Industry, Innovation, and Infrastructure**.

* **SDG 8:** By providing efficient tools, ThreadWorks enhances productivity for small crochet businesses, allowing artisans to focus on creative work and customer interaction, leading to improved income and economic growth.

* **SDG 9:** ThreadWorks promotes innovation by providing a digital solution tailored to the needs of micro-entrepreneurs in the handmade crafts industry, often overlooked in broader industrial development.  It facilitates access to technology and improves operational efficiency, contributing to sustainable growth.


## IV. INSTRUCTIONS FOR RUNNING THE PROGRAM

1. **Download Files:** Download the following files and save them to the same directory:

   * `threadworksdb` (database file)
   * `threadworks.py` (main Python script)
     
2. **Install Libraries:**

   * **Open your terminal or command prompt.**
   * **Install the required libraries using pip:** 
```bash
     pip install customtkinter Pillow sqlite3

3. **Running the Program:**

   1. Open a code editor or IDE (Integrated Development Environment) that supports Python.  Examples include VS Code, PyCharm, or Thonny.
   2. Navigate to the directory where you saved `threadworks.py`.
   3. Run the `threadworks.py` file by using the appropriate method for your code editor (e.g., pressing the "Run" button or typing `python threadworks.py` in the terminal if your editor supports it).


4. **Login:** A login screen will appear.  If this is your first time using the application, you will need to create a new user account.

5. **Main Page:** The main page provides buttons for navigating to different sections of the application: Inventory, Orders, Sales Report, and Invoices.  An "Exit" button is available to close the program.

6. **Inventory Page:** Manage your inventory by adding, updating, or deleting items.

7. **Orders Page:**  View, add, and delete order information.

8. **Sales Report Page:**  View a summary report of your sales data.

9. **Invoice Page:** Access and view generated invoices for completed orders.
