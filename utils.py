import csv
from book import Book

TABLE_HEADERS = ['Title', 'Author', 'Total Pages', 'Pages Read', 'Progress', 'Status']
CSV_FILE = 'books.csv'

def load_from_csv(books):
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip headers

            for row in reader:
                book = Book.retrieve_row(row)
                if book:  # Only add valid books
                    books.append(book)
    except FileNotFoundError:
        print('No previous data found. Starting fresh.')
    except Exception as e:
        print(f'Error loading CSV: {e}')

def save_to_csv(books):
    try:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(TABLE_HEADERS)

            for book in books:
                writer.writerow(book.save_to_row())
    except Exception as e:
        print(f'Error saving CSV: {e}')