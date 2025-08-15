# File Content Modifier

This Python script reads a text file, modifies its content, and saves the result into a new file.
By default, it converts all text to **uppercase**, but you can easily customize the transformation logic.

## 📌 Features

* Reads any text file from your system.
* Modifies its content (currently converts text to uppercase).
* Saves the modified content into a **new file** prefixed with `modified_`.
* Handles common file errors (e.g., file not found, read/write issues).

## 🚀 How It Works

1. The script prompts you to enter the name of the file you want to read (e.g., `example.txt`).
2. It reads the file content.
3. It applies the transformation defined in `modify_content()` function (currently `content.upper()`).
4. It creates a new file with the prefix `modified_` and writes the transformed content.
5. Prints a success message or an error message if something goes wrong.

## 🛠️ Usage

### **1. Save the script**

Save the Python code to a file, for example:

```bash
file_modifier.py
```

### **2. Prepare a text file**

Make sure you have a `.txt` file in the same directory as the script.
Example:

```
example.txt
```

### **3. Run the script**

Open a terminal in the same directory and run:

```bash
python file_modifier.py
```

### **4. Enter the filename**

When prompted:

```
Enter the name of the file to read: example.txt
```

### **5. Output**

A new file will be created:

```
modified_example.txt
```

This file will contain the modified content.

## ✏️ Customization

To apply a different transformation, edit the `modify_content()` function:

```python
def modify_content(content):
    # Example: Replace spaces with underscores
    return content.replace(" ", "_")
```

## ⚠️ Error Handling

The script handles:

* `FileNotFoundError` → If the input file does not exist.
* `IOError` → If there is a problem reading/writing the file.
* `Exception` → Any unexpected error.

## 📄 License

This script is free to use and modify.

