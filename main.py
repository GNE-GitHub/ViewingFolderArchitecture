# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox

# def browse_folder():
#     folder_selected = filedialog.askdirectory()
#     folder_path_entry.delete(0, tk.END)
#     folder_path_entry.insert(0, folder_selected)

# def get_directory_structure(rootdir):
#     structure = []
#     for dirpath, dirnames, filenames in os.walk(rootdir):
#         level = dirpath.replace(rootdir, '').count(os.sep)
#         indent = '│   ' * (level)
#         structure.append((f"{indent}├── {os.path.basename(dirpath)}/", level))
#         subindent = '│   ' * (level + 1)
#         for f in filenames:
#             structure.append((f"{subindent}├── {f}", level + 1))
#     return structure

# def display_structure():
#     folder_path = folder_path_entry.get()
#     if not os.path.isdir(folder_path):
#         messagebox.showerror("Error", "Invalid folder path")
#         return
#     structure = get_directory_structure(folder_path)
#     output_text.delete(1.0, tk.END)
#     for line, level in structure:
#         output_text.insert(tk.END, line + "\n", f"level_{level % 6}")

# def copy_to_clipboard():
#     root.clipboard_clear()
#     root.clipboard_append(output_text.get(1.0, tk.END))
#     messagebox.showinfo("Copied", "Text copied to clipboard")

# root = tk.Tk()
# root.title("Folder Structure Viewer")
# root.geometry("600x500")
# root.resizable(False, False)

# folder_path_entry = tk.Entry(root, width=50)
# folder_path_entry.pack(padx=10, pady=5)

# browse_button = tk.Button(root, text="Browse", command=browse_folder)
# browse_button.pack(padx=10, pady=5)

# display_button = tk.Button(root, text="Display Structure", command=display_structure)
# display_button.pack(padx=10, pady=5)

# output_text = tk.Text(root, wrap=tk.NONE, width=80, height=20)
# output_text.pack(padx=10, pady=5)

# # Define tags with different colors for different levels
# colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A5", "#A533FF", "#33FFF3"]
# for i, color in enumerate(colors):
#     output_text.tag_configure(f"level_{i}", foreground=color)

# copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
# copy_button.pack(padx=10, pady=5)

# root.mainloop()

# GN-Toolkit
# GN-Toolkit
import os
import tkinter as tk
from tkinter import messagebox, filedialog
import pyperclip

def generate_structure(path, indent=0):
    structure = ""
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                structure += " " * indent + "|-- " + entry.name + "\n"
                if entry.is_dir(follow_symlinks=False):
                    structure += generate_structure(entry.path, indent + 4)
    except PermissionError:
        structure += " " * indent + "|-- [Permission Denied]\n"
    return structure

def display_structure():
    folder_path = entry.get()
    if os.path.isdir(folder_path):
        structure = generate_structure(folder_path)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, structure)
    else:
        messagebox.showerror("Error", "Invalid folder path")

def copy_to_clipboard():
    structure = text_area.get(1.0, tk.END)
    pyperclip.copy(structure)
    messagebox.showinfo("Copied", "Directory structure copied to clipboard")

def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)
        display_structure()

root = tk.Tk()
root.title("GN-Toolkit - Directory Structure Generator")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="Enter folder path:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

button = tk.Button(frame, text="Generate", command=display_structure)
button.pack(side=tk.LEFT)

browse_button = tk.Button(frame, text="Browse", command=choose_folder)
browse_button.pack(side=tk.LEFT, padx=5)

text_area = tk.Text(root, width=80, height=20)
text_area.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

root.mainloop()
