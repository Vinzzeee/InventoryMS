import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Menu

class InventorySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        
        # Set fixed window size
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Add a menu bar
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create File menu
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Create Help menu
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        # Initial Interface
        self.start_interface()

        # Inventory data structure with price
        self.inventory = {
            'Raw Materials': {'Steel': {'quantity': 100, 'price': 10.0}, 'Plastic': {'quantity': 200, 'price': 5.0}},
            'Work-in-Progress': {'Engine': {'quantity': 50, 'price': 500.0}, 'Chassis': {'quantity': 30, 'price': 300.0}},
            'Finished Goods': {'Car Model A': {'quantity': 20, 'price': 20000.0}, 'Car Model B': {'quantity': 15, 'price': 25000.0}}
        }

        # Users data
        self.users = {'admin': 'password'}

        # Supplier data structure
        self.suppliers = {
            'Steel Supplier': {'Contact': '123456789', 'Materials': ['Steel']},
            'Plastic Supplier': {'Contact': '987654321', 'Materials': ['Plastic']}
        }

        # Production plan structure
        self.production_plan = []

    def start_interface(self):
        self.clear_frame()
        
        header = tk.Frame(self.root, bg="lightblue", height=50)
        header.pack(fill='x')
        tk.Label(header, text="Inventory Management System", font=("Arial", 20), bg="lightblue").pack(pady=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="Welcome!", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(main_frame, text="New User", command=self.new_user_interface, width=20).pack(pady=5)
        tk.Button(main_frame, text="Login", command=self.login_interface, width=20).pack(pady=5)

        self.status_bar = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def new_user_interface(self):
        self.clear_frame()

        header = tk.Frame(self.root, bg="lightblue", height=50)
        header.pack(fill='x')
        tk.Label(header, text="Create New User", font=("Arial", 20), bg="lightblue").pack(pady=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="Username").pack()
        self.new_username_entry = tk.Entry(main_frame)
        self.new_username_entry.pack()
        
        tk.Label(main_frame, text="Password").pack()
        self.new_password_entry = tk.Entry(main_frame, show="*")
        self.new_password_entry.pack()
        
        tk.Button(main_frame, text="Create User", command=self.create_user, width=20).pack(pady=10)
        tk.Button(main_frame, text="Back", command=self.start_interface, width=20).pack(pady=5)

    def create_user(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        
        if username and password:
            self.users[username] = password
            messagebox.showinfo("Success", "User created successfully!")
            self.start_interface()
        else:
            messagebox.showerror("Error", "Both fields are required!")

    def login_interface(self):
        self.clear_frame()

        # Creating a frame to act as a card
        card_frame = tk.Frame(self.root, bg="white", bd=2, relief="solid", padx=20, pady=20)
        card_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        tk.Label(card_frame, text="Login", font=("Arial", 15, "bold"), bg="white").pack(pady=10)

        # Username entry
        tk.Label(card_frame, text="Username", font=("Arial", 10), bg="white").pack(pady=5)
        self.username_entry = tk.Entry(card_frame, font=("Arial", 10))
        self.username_entry.pack(pady=5)

        # Password entry
        tk.Label(card_frame, text="Password", font=("Arial", 10), bg="white").pack(pady=5)
        self.password_entry = tk.Entry(card_frame, show="*", font=("Arial", 10))
        self.password_entry.pack(pady=5)

        # Login button
        tk.Button(card_frame, text="Login", command=self.login, width=10, font=("Arial", 10), bg="blue", fg="white", relief="flat").pack(pady=20)
        # Back button
        tk.Button(card_frame, text="Back", command=self.start_interface, width=5).pack(pady=5)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.users.get(username) == password:
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def show_dashboard(self):
        self.clear_frame()

        header = tk.Frame(self.root, bg="lightblue", height=50)
        header.pack(fill='x')
        tk.Label(header, text="Dashboard", font=("Arial", 20), bg="lightblue").pack(pady=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Button(main_frame, text="Product Inquiry", command=self.product_inquiry_interface, width=20).pack(pady=5)
        tk.Button(main_frame, text="Supplier Management", command=self.supplier_management_interface, width=20).pack(pady=5)
        tk.Button(main_frame, text="Production Planning", command=self.production_planning_interface, width=20).pack(pady=5)
        tk.Button(main_frame, text="Generate Report", command=self.generate_report, width=20).pack(pady=5)
        tk.Button(main_frame, text="Logout", command=self.start_interface, width=20).pack(pady=5)

    def product_inquiry_interface(self):
        self.clear_frame()

        header = tk.Frame(self.root, bg="lightblue", height=50)
        header.pack(fill='x')
        tk.Label(header, text="Product Inquiry", font=("Arial", 20), bg="lightblue").pack(pady=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        # Combobox for category selection
        tk.Label(main_frame, text="Select Category").pack()
        self.category_combobox = ttk.Combobox(main_frame, values=list(self.inventory.keys()))
        self.category_combobox.pack()

        # Treeview for displaying products
        self.tree = ttk.Treeview(main_frame, columns=('Name', 'Quantity', 'Price'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Price', text='Price')
        self.tree.pack()

        # Entry fields for quantity and price updates
        tk.Label(main_frame, text="Name").pack()
        self.name_entry = tk.Entry(main_frame)
        self.name_entry.pack()
        
        tk.Label(main_frame, text="Quantity").pack()
        self.quantity_entry = tk.Entry(main_frame)
        self.quantity_entry.pack()

        tk.Label(main_frame, text="Price").pack()
        self.price_entry = tk.Entry(main_frame)
        self.price_entry.pack()

        main_frame = tk.Frame(main_frame)
        main_frame.pack(pady=10)

          # Buttons for inventory operations in a grid
        tk.Button(main_frame, text="Add to Raw Materials", command=self.add_to_raw_materials, width=20).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(main_frame, text="Add to WIP", command=self.add_to_wip, width=20).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(main_frame, text="Add to Finished Goods", command=self.add_to_finished_goods, width=20).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(main_frame, text="Update Quantity/Price", command=self.update_quantity_price, width=20).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(main_frame, text="Check Stock Level", command=self.check_stock_level, width=20).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(main_frame, text="Back", command=self.show_dashboard, width=20).grid(row=1, column=2, padx=5, pady=5)

        # Show products in the selected category
        self.category_combobox.bind("<<ComboboxSelected>>", self.show_products)

    def show_products(self, event=None):
        category = self.category_combobox.get()
        if category:
            for item in self.tree.get_children():
                self.tree.delete(item)
            for name, details in self.inventory[category].items():
                self.tree.insert('', 'end', values=(name, details['quantity'], details['price']))

    def add_to_raw_materials(self):
        name = self.name_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number!")
            return
        try:
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number!")
            return
        
        self.inventory['Raw Materials'][name] = {'quantity': quantity, 'price': price}
        messagebox.showinfo("Success", "Product added to Raw Materials!")

    def add_to_wip(self):
        name = self.name_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number!")
            return
        try:
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number!")
            return
        
        self.inventory['Work-in-Progress'][name] = {'quantity': quantity, 'price': price}
        messagebox.showinfo("Success", "Product added to Work-in-Progress!")

    def add_to_finished_goods(self):
        name = self.name_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number!")
            return
        try:
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number!")
            return
        
        self.inventory['Finished Goods'][name] = {'quantity': quantity, 'price': price}
        messagebox.showinfo("Success", "Product added to Finished Goods!")

    def update_quantity_price(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        try:
            quantity = int(quantity) if quantity else None
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number!")
            return

        try:
            price = float(price) if price else None
        except ValueError:
            messagebox.showerror("Error", "Price must be a number!")
            return

        updated = False
        for category in self.inventory:
            if name in self.inventory[category]:
                if quantity is not None:
                    self.inventory[category][name]['quantity'] = quantity
                if price is not None:
                    self.inventory[category][name]['price'] = price
                updated = True
                break
        
        if updated:
            messagebox.showinfo("Success", "Quantity/Price updated successfully!")
        else:
            messagebox.showerror("Error", "Product not found!")

    def check_stock_level(self):
        name = self.name_entry.get()

        for category, products in self.inventory.items():
            if name in products:
                messagebox.showinfo("Stock Level", f"{name} has {products[name]['quantity']} on stocks in {category} at PHP{products[name]['price']} each.")
                return
        
        messagebox.showerror("Error", "Product not found!")

    def supplier_management_interface(self):
        self.clear_frame()

        header = tk.Frame(self.root, bg="lightblue", height=50)
        header.pack(fill='x')
        tk.Label(header, text="Supplier Management", font=("Arial", 20), bg="lightblue").pack(pady=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        # Entry fields for supplier details
        tk.Label(main_frame, text="Supplier Name").pack()
        self.supplier_name_entry = tk.Entry(main_frame)
        self.supplier_name_entry.pack()
    
        tk.Label(main_frame, text="Contact").pack()
        self.supplier_contact_entry = tk.Entry(main_frame)
        self.supplier_contact_entry.pack()

        tk.Label(main_frame, text="Materials Supplied (comma-separated)").pack()
        self.supplier_materials_entry = tk.Entry(main_frame)
        self.supplier_materials_entry.pack()

        # Buttons for supplier operations
        tk.Button(main_frame, text="Add Supplier", command=self.add_supplier, width=20).pack(pady=5)
        tk.Button(main_frame, text="Update Supplier", command=self.update_supplier, width=20).pack(pady=5)
        tk.Button(main_frame, text="Delete Supplier", command=self.delete_supplier, width=20).pack(pady=5)

        # Treeview for displaying suppliers
        self.supplier_tree = ttk.Treeview(main_frame, columns=('Name', 'Contact', 'Materials'), show='headings')
        self.supplier_tree.heading('Name', text='Name')
        self.supplier_tree.heading('Contact', text='Contact')
        self.supplier_tree.heading('Materials', text='Materials')
        self.supplier_tree.pack(pady=10)

        # Back button
        tk.Button(main_frame, text="Back", command=self.show_dashboard, width=20).pack(pady=5)

        # Load suppliers into the treeview
        self.show_suppliers()

    def show_suppliers(self):
        for item in self.supplier_tree.get_children():
            self.supplier_tree.delete(item)
        for name, details in self.suppliers.items():
            self.supplier_tree.insert('', 'end', values=(name, details['Contact'], ', '.join(details['Materials'])))

    def add_supplier(self):
        name = self.supplier_name_entry.get()
        contact = self.supplier_contact_entry.get()
        materials = self.supplier_materials_entry.get().split(',')

        if name and contact and materials:
            self.suppliers[name] = {'Contact': contact, 'Materials': materials}
            messagebox.showinfo("Success", "Supplier added successfully!")
            self.show_suppliers()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def update_supplier(self):
        selected_item = self.supplier_tree.selection()
        if not selected_item:
         messagebox.showerror("Error", "Select a supplier to update!")
       

        name = self.supplier_name_entry.get()
        contact = self.supplier_contact_entry.get()
        materials = self.supplier_materials_entry.get().split(',')

        if name and contact and materials:
            self.suppliers[name] = {'Contact': contact, 'Materials': materials}
            messagebox.showinfo("Success", "Supplier updated successfully!")
            self.show_suppliers()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def delete_supplier(self):
        selected_item = self.supplier_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a supplier to delete!")
        

        supplier_name = self.supplier_tree.item(selected_item)['values'][0]
        del self.suppliers[supplier_name]
        messagebox.showinfo("Success", "Supplier deleted successfully!")
        self.show_suppliers()


    def production_planning_interface(self):
        self.clear_frame()

        header = tk.Frame(self.root, bg="lightblue", height=50)
        header.pack(fill='x')
        tk.Label(header, text="Production Planning", font=("Arial", 20), bg="lightblue").pack(pady=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        # Entry field for production plan details
        tk.Label(main_frame, text="Plan Details").pack()
        self.production_plan_entry = tk.Entry(main_frame)
        self.production_plan_entry.pack()
    
        # Buttons for production plan operations
        tk.Button(main_frame, text="Add Plan", command=self.add_production_plan, width=20).pack(pady=5)
        tk.Button(main_frame, text="Update Plan", command=self.update_production_plan, width=20).pack(pady=5)
        tk.Button(main_frame, text="Delete Plan", command=self.delete_production_plan, width=20).pack(pady=5)

        # Treeview for displaying production plans with a Done column
        self.production_plan_tree = ttk.Treeview(main_frame, columns=('Plan', 'Done'), show='headings')
        self.production_plan_tree.heading('Plan', text='Plan')
        self.production_plan_tree.heading('Done', text='Double Click to Mark Done')
        self.production_plan_tree.pack(pady=10)

        # Bind double-click event to toggle done status
        self.production_plan_tree.bind('<Double-1>', self.toggle_done)

        # Back button
        tk.Button(main_frame, text="Back", command=self.show_dashboard, width=20).pack(pady=5)

        # Load production plans into the treeview
        self.show_production_plans()

    def show_production_plans(self):
        for item in self.production_plan_tree.get_children():
            self.production_plan_tree.delete(item)
        for plan, done in self.production_plan:
            self.production_plan_tree.insert('', 'end', values=(plan, 'Yes' if done else 'No'))

    def add_production_plan(self):
        plan = self.production_plan_entry.get()

        if plan:
            self.production_plan.append((plan, False))  # False indicates the plan is not done
            messagebox.showinfo("Success", "Production plan added successfully!")
            self.show_production_plans()
        else:
            messagebox.showerror("Error", "Plan details are required!")

    def update_production_plan(self):
        selected_item = self.production_plan_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a plan to update!")

        plan = self.production_plan_entry.get()
        index = self.production_plan_tree.index(selected_item[0])

        if plan:
            done = self.production_plan[index][1]  # Preserve the done status
            self.production_plan[index] = (plan, done)
            messagebox.showinfo("Success", "Production plan updated successfully!")
            self.show_production_plans()
        else:
            messagebox.showerror("Error", "Plan details are required!")

    def delete_production_plan(self):
        selected_item = self.production_plan_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a plan to delete!")

        index = self.production_plan_tree.index(selected_item[0])
        del self.production_plan[index]
        messagebox.showinfo("Success", "Production plan deleted successfully!")
        self.show_production_plans()

    def toggle_done(self, event):
        selected_item = self.production_plan_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a plan to mark as done!")

        index = self.production_plan_tree.index(selected_item[0])
        plan, done = self.production_plan[index]
        self.production_plan[index] = (plan, not done)  # Toggle the done status
        messagebox.showinfo("Success", f"Production plan marked as {'done' if not done else 'not done'}!")
        self.show_production_plans()

    def generate_report(self):
        report = "INVENTORY REPORT\n\n"
        
        for category, items in self.inventory.items():
            report += f"{category}:\n"
            for name, details in items.items():
                report += f"  {name} - Quantity: {details['quantity']}, Price: PHP{details['price']}\n"
            report += "\n"
        
        # Create a new window for the report
        report_window = tk.Toplevel(self.root)
        report_window.title("Inventory Report")
        
        report_text = tk.Text(report_window, wrap='word')
        report_text.insert('1.0', report)
        report_text.config(state=tk.DISABLED)
        report_text.pack(expand=True, fill='both')
        
        tk.Button(report_window, text="Close", command=report_window.destroy).pack(pady=5)


    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_about(self):
        messagebox.showinfo("About", "Inventory Management System v1.0")

root = tk.Tk()
app = InventorySystem(root)
root.mainloop()