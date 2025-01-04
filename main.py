import csv
from colorama import Fore, Style, init
from pyfiglet import Figlet
from tabulate import tabulate
from utils import load_from_csv, save_to_csv
from book import Book

init(autoreset=True)

books = []

def main():
    load_from_csv(books)
    
    while True:
        print(Fore.CYAN + Style.BRIGHT + '=' * 40)
        print(Fore.CYAN + Style.BRIGHT + 'Welcome to')
        print(Fore.CYAN + Style.BRIGHT + Figlet(font='slant').renderText('The Reading list!'))
        print('1. Add a new book')
        print('2. View all books')
        print('3. Update book status')
        print('4. Search books')
        print('5. Remove a book')
        print(Fore.YELLOW + '6. Exit')

        choice = input(Fore.CYAN + Style.BRIGHT + 'Please choose an option (1-6): ')

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            update_reading_progress()
        elif choice == '4':
            search_books()
        elif choice == '5':
            remove_book()
        elif choice == '6':
            save_to_csv(books)
            print(Fore.YELLOW + Style.BRIGHT + 'Goodbye!')
            break
        else:
            print(Fore.RED + 'Invalid choice, please try again.')

def does_book_exist(title, author):
    for book in books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower():
            return True
    return False

def add_book():
    try:
        title = input('Enter book title: ')
        author = input('Enter book author: ')
        total_pages = int(input('Enter book\'s total pages: '))
    except ValueError:
        print(Fore.RED + 'Enter a valid number for total pages.')
        return

    if does_book_exist(title, author):
        print(Fore.RED + f'The book \'{title}\' by {author} already exists in the list.')
        return

    new_book = Book(title.title(), author.title(), total_pages)
    books.append(new_book)
    save_to_csv(books)
    print(Fore.GREEN + f'Book \'{title.title()}\' by {author.title()} has been added to the list.')
    table = [[new_book.title, new_book.author, new_book.total_pages, new_book.pages_read, f'{new_book.progress:.2f}%', new_book.status]]
    headers = ['Title', 'Author', 'Total Pages', 'Pages Read', 'Progress', 'Status']
    print(Fore.WHITE + tabulate(table, headers, tablefmt='grid'))

def view_books():
    if not books:
        print('No books in the list yet.')
    else:
        table = [[book.title, book.author, book.total_pages, book.pages_read, f'{book.progress:.2f}%', book.status] for book in books]
        headers = ['Title', 'Author', 'Total Pages', 'Pages Read', 'Progress', 'Status']
        print(Fore.WHITE + tabulate(table, headers, tablefmt='grid'))

def update_reading_progress():
    title = input('Enter the title of the book: ')

    for book in books:
        if book.title.lower() == title.lower():
            try:
                pages_read = int(input(f'Enter the number of pages read for \'{title}\': '))
                book.update_status(pages_read)
                print(Fore.GREEN + f'Updated progress for \'{title}\':')
                table = [[book.title, book.author, book.total_pages, book.pages_read, f'{book.progress:.2f}%', book.status]]
                headers = ['Title', 'Author', 'Total Pages', 'Pages Read', 'Progress', 'Status']
                print(Fore.WHITE + tabulate(table, headers, tablefmt='grid'))
                return
            except ValueError:
                print(Fore.RED + 'Enter a valid number for pages read.')
                return

    print(Fore.RED + f'Book \'{title}\' not found in the list.')

def search_books():
    search_term = input('Enter title or author to search: ')
    found_books = [book for book in books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]

    if found_books:
        print(Fore.GREEN + 'Found books:')
        for book in found_books:
            table = [[book.title, book.author, book.total_pages, book.pages_read, f'{book.progress:.2f}%', book.status] for book in found_books]
            headers = ['Title', 'Author', 'Total Pages', 'Pages Read', 'Progress', 'Status']
            print(Fore.WHITE + tabulate(table, headers, tablefmt='grid'))
    else:
        print(Fore.RED + 'No books found.')

def remove_book():
    title = input('Enter the title of the book to remove: ')

    for book in books:
        if book.title.lower() == title.lower():
            books.remove(book)
            print(Fore.GREEN + f'Book \'{title}\' has been removed from the list.')
            return

    print(Fore.RED + f'Book \'{title}\' not found in the list.')

if __name__ == '__main__':
    main()