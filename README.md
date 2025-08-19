# 🐍 Python File Handling Example

This project demonstrates basic file handling operations in Python, including writing, reading, appending, and using exception handling with a `.pdf` file (used here as a text container, not a true PDF format).

## 📄 Description

The script performs the following operations sequentially:

1. **Write Mode (`"w"`)**  
   Creates or overwrites a file named `files.pdf` and writes an initial line of text.

2. **Read Mode (`"r"`)**  
   Opens the file and prints its contents to the console.

3. **Append Mode (`"a"`)**  
   Adds two additional lines to the file without overwriting existing content.

4. **Try-Except-Finally Block**  
   - Attempts to read the file again.
   - Handles the case where the file might not exist.
   - Ensures the file is closed properly after reading.

## 📦 File Used

Although the file is named `files.pdf`, it is treated as a plain text file. This naming is purely illustrative and does not follow the PDF binary format.

## 🧠 Key Concepts Demonstrated

- File modes: `"w"`, `"r"`, `"a"`
- File object methods: `.write()`, `.read()`, `.close()`
- Exception handling: `try`, `except`, `finally`
- Console output using `print()`

## 🚀 How to Run

Make sure you have Python installed. Then run the script using:

```bash
python filename.py

