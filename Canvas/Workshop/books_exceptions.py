# Initialize an empty list for the book catalog
book_catalogue = []

# Function to add a book to the catalogue for testing purposes
def add_book(book_id, book_name):
    book_catalogue.append({"Id": book_id, "Book": book_name})

# Function to remove a book from the catalogue using the ID number with enhanced exception handling
def remove_book(book_id):
    try:
        # Check if the provided ID is valid
        if not isinstance(book_id, int):
            raise TypeError("ID must be an integer.")
        if book_id <= 0:
            raise ValueError("ID must be a positive integer.")

        # Loop through the catalogue by index to find the book by ID
        for index in range(len(book_catalogue)):
            if book_catalogue[index]["Id"] == book_id:
                del book_catalogue[index]  # Remove the book if ID matches
                print(f"Book with ID {book_id} has been removed.")
                break
        else:
            # Executes if the ID was not found in the catalogue
            print(f"Book with ID {book_id} not found in the catalogue.")
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while removing the book: {e}")

    # Return the updated catalogue
    return book_catalogue

# Adding books for testing
add_book(100, "Frankenstein")
add_book(200, "To Kill a Mockingbird")
add_book(300, "1984")

# Testing the remove_book function with various cases
remove_book(200)  # Valid ID, should remove the book
remove_book(400)  # Non-existent ID
remove_book(-10)  # Invalid ID - negative
remove_book("100")  # Invalid ID - not an integer

# Print the updated catalogue to verify the removals
print("\nUpdated Book Catalogue:")
print(book_catalogue)
