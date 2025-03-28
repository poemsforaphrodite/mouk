import openpyxl
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os

# Read the Excel file using openpyxl
excel_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "PROJECT", "dbsolve.xlsx")
wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

# Extract data from the sheet
data = list(sheet.values)
columns = data[0]
rows = data[1:]

# Filter the rows to only include those where the "%" column is greater than 35
filtered_rows = [row for row in rows if row[columns.index("%")] > 35]

def on_table_select(event):
    selected_row_index = table.selection()[0]
    selected_row = table.item(selected_row_index, 'values')
    messagebox.showinfo("Selected Student", f"Selected Student: {selected_row[0]}")

root = tk.Tk()
root.title("Prominent Parameters")
root.geometry("1200x600")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

table = ttk.Treeview(frame, columns=columns, show='headings')
table.pack(fill=tk.BOTH, expand=True)

# Define headings
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)

# Insert data into the table
for row in filtered_rows:
    table.insert('', tk.END, values=row)

table.bind('<<TreeviewSelect>>', on_table_select)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, pady=10)

ok_button = tk.Button(button_frame, text="OK", command=lambda: on_table_select(None))
ok_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
exit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()