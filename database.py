import sqlite3

library = sqlite3.connect(":memory:")
lib = library.cursor()
lib.execute("""CREATE TABLE book (
    name TEXT,
    number_of_pages INTEGER,
    type_of_book_cover TEXT,
    category TEXT
)""")
data = [
    ('The Da Vinci Code', 454, 'Paperback', 'Mystery'),
    ('The Hobbit', 310, 'Hardcover', 'Fantasy'),
    ('A Game of Thrones', 694, 'Paperback', 'Fantasy'),
    ('The Girl with the Dragon Tattoo', 465, 'Paperback', 'Mystery'),
    ('Gone with the Wind', 1037, 'Hardcover', 'Historical'),
    ('The Alchemist', 197, 'Paperback', 'Adventure'),
    ('The Shining', 447, 'Paperback', 'Horror'),
    ('Wuthering Heights', 342, 'Hardcover', 'Romance'),
    ('The Catcher in the Rye', 277, 'Paperback', 'Coming-of-Age'),
    ('The Martian', 369, 'Paperback', 'Adventure')
]
lib.executemany("INSERT INTO book VALUES(?, ?, ?, ?)", data)

res = lib.execute("SELECT AVG(number_of_pages) FROM book")
print(f"Average number of pages in all given books is {res.fetchone()[0]}")
res = lib.execute("SELECT MAX(number_of_pages), name FROM book ")
ans = res.fetchone()
maxpages = ans[0]
booknamewithmaxpages = ans[1]
print(f"maximum number of pages is {maxpages} in book '{booknamewithmaxpages}'")
library.commit()
library.close()
