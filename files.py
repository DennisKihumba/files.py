def modify_content(content):
    """
    Modify the content of the file.
    This example converts all text to uppercase.
    You can customize this function to do more!
    """
    return content.upper()

try:
    # Ask user for the input filename
    input_filename = input("Enter the name of the file to read: ")
    with open(input_filename, "r") as infile:
        original_content = infile.read()

    # Modify the content
    modified_content = modify_content(original_content)

    # Create a new output file
    output_filename = "modified_" + input_filename
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ File processed successfully! Modified content saved to '{output_filename}'.")

except FileNotFoundError:
    print(f"❌ Error: The file '{input_filename}' was not found.")
except IOError:
    print(f"❌ Error: Could not read or write to the file '{input_filename}'.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
