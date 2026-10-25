books =["Diary of a Wimpy Kid", "Harry Potter", "Percy Jackson", "Wizard of Oz", "Pride and Prejudice", "The Jungle Book"]

print("Library Book List:", books)
print
("Total Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[:3])

books.append("Little Women")
print
("After Adding a Book:", books)

books.remove("The Jungle Book")
print("After Removing a Book:", books)

books.sort()
print("Books Sorted Alphabetically:", books)

books.reverse()
print("Books in Reverse Order:", books)


librarian = {
    "name": "Ms. Jonas",
    "section": "Fantasy Books",
    "experience": 7
}

print("Librarian Profile:", librarian)

print("Librarian Name:", librarian["name"])
print("Library Section:", librarian["section"])
print("Experience:", librarian.get("experience"))

librarian["experience"] = 7
print("Updated Experience:", librarian)

librarian["email"] = "joans@schoollibrary.com"
print("After Adding Email:", librarian)

librarian.pop("section")
print("After Removing Section:", librarian)

book_ids = [101, 102, 103, 104, 105, 106]
book_names = ["Diary of a Wimpy Kid", "Harry Potter", "Percy Jackson", "Wizard of Oz", "Pride and Prejudice", "Little Women"]

book_directory = dict(zip(book_ids, book_names))

print("Book Directory:", book_directory)


print("================================")
print("LIBRARY ORGANISER SUMMARY")
print("================================")
print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)
print("================================")

