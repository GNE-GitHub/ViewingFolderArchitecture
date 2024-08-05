import os
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_selected)

def get_directory_structure(rootdir):
    structure = []
    for dirpath, dirnames, filenames in os.walk(rootdir):
        level = dirpath.replace(rootdir, '').count(os.sep)
        indent = '│   ' * (level)
        structure.append((f"{indent}├── {os.path.basename(dirpath)}/", level))
        subindent = '│   ' * (level + 1)
        for f in filenames:
            structure.append((f"{subindent}├── {f}", level + 1))
    return structure

def display_structure():
    folder_path = folder_path_entry.get()
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path")
        return
    structure = get_directory_structure(folder_path)
    output_text.delete(1.0, tk.END)
    for line, level in structure:
        output_text.insert(tk.END, line + "\n", f"level_{level % 6}")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, tk.END))
    messagebox.showinfo("Copied", "Text copied to clipboard")

root = tk.Tk()
root.title("Folder Structure Viewer")
root.geometry("600x500")
root.resizable(False, False)

folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.pack(padx=10, pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(padx=10, pady=5)

display_button = tk.Button(root, text="Display Structure", command=display_structure)
display_button.pack(padx=10, pady=5)

output_text = tk.Text(root, wrap=tk.NONE, width=80, height=20)
output_text.pack(padx=10, pady=5)

# Define tags with different colors for different levels
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A5", "#A533FF", "#33FFF3"]
for i, color in enumerate(colors):
    output_text.tag_configure(f"level_{i}", foreground=color)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(padx=10, pady=5)

root.mainloop()
