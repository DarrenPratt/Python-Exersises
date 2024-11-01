# Initialize an empty list for the book catalog
book_catalogue = []

# Function to add a book to the catalogue
def add_book(book_id, book_name):
    try:
        # Validation checks for the book ID
        if book_id is None:
            return "Error: ID cannot be null."
        if not isinstance(book_id, int) or book_id <= 0:
            return "Error: ID must be a positive number."
        if book_id > 1000:
            return "Error: ID cannot exceed 1000."
        
        # Check if the ID already exists in the catalogue
        for book in book_catalogue:
            if book["Id"] == book_id:
                return f"Error: ID {book_id} already exists in the catalogue."
        
        # Add the book to the catalogue
        book_catalogue.append({"Id": book_id, "Book": book_name})
        return f"Book '{book_name}' with ID {book_id} has been added to the catalogue."
    except Exception as e:
        return f"An error occurred while adding the book: {e}"

# Function to remove a book from the catalogue using the ID number
def remove_book(book_id):
    try:
        # Loop through the catalogue by index to find the book by ID
        for index in range(len(book_catalogue)):
            if book_catalogue[index]["Id"] == book_id:
                del book_catalogue[index]  # Remove the book if ID matches
                print(f"Book with ID {book_id} has been removed.")
                break
        else:
            # This else block executes if the for loop completes without finding the ID
            print(f"Book with ID {book_id} not found in the catalogue.")
    except Exception as e:
        print(f"An error occurred while removing the book: {e}")

    # Return the updated catalogue
    return book_catalogue

# Function to modify the book title for a given ID
def modify_book_title(book_id, new_title):
    try:
        # Loop through the catalogue by index to find the book by ID
        for index in range(len(book_catalogue)):
            if book_catalogue[index]["Id"] == book_id:
                # Update the book title if ID matches
                book_catalogue[index]["Book"] = new_title
                print(f"Book title for ID {book_id} has been updated to '{new_title}'.")
                break
        else:
            # This else block executes if the for loop completes without finding the ID
            print(f"Book with ID {book_id} not found in the catalogue.")
    except Exception as e:
        print(f"An error occurred while modifying the book title: {e}")

    # Return the updated catalogue
    return book_catalogue

# Testing the functions with try-except handling
try:
    print(add_book(100, "Frankenstein"))
    print(add_book(200, "To Kill a Mockingbird"))
    print(add_book(300, "1984"))
    
    # Attempt to modify the title of a book with a valid ID and an invalid ID
    modify_book_title(200, "To Kill a Mockingbird - Revised Edition")  # Valid ID
    modify_book_title(400, "The Great Gatsby")  # Invalid ID

    # Attempt to remove a book with a valid ID and an invalid ID
    remove_book(200)  # This ID exists in the catalogue
    remove_book(400)  # This ID does not exist in the catalogue

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Print the updated catalogue to verify the modification
print("\nUpdated Book Catalogue:")
print(book_catalogue)
