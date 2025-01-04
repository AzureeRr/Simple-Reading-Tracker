class Book:
    def __init__(self, title, author, total_pages, pages_read=0, progress=0, status='Unread'):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.pages_read = pages_read
        self.progress = progress
        self.status = status

    def __str__(self):
        return f'Book Title: {self.title} by {self.author} is {self.status}, Progress: {self.progress:.2f}%'

    def update_status(self, pages_read):
        if pages_read < 0:
            raise ValueError('Pages read cannot be negative.')
        if pages_read > self.total_pages:
            raise ValueError('Pages read can\'t exceed total pages.')

        self.pages_read = pages_read
        self.progress = (self.pages_read / self.total_pages) * 100

        if self.pages_read == 0:
            self.status = 'Not Read'
        elif self.pages_read == self.total_pages:
            self.status = 'Finished'
        else:
            self.status = 'Currently Reading'

    def save_to_row(self):
        return [self.title, self.author, self.total_pages, self.pages_read, self.progress, self.status]
    
    @staticmethod
    def retrieve_row(row):
        try:
            return Book(row[0], row[1], int(row[2]), int(row[3]), float(row[4]), row[5])
        except ValueError:
            print('Book Corrupted')
            return None