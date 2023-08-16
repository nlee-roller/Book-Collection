from BookCollectionNode import BookCollectionNode
from Book import Book

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def getNumberOfBooks(self):
        counter = 0
        start = self.head
        while start != None:
            counter += 1
            start = start.getNext()
        return counter

    def insertBook(self, book):
        currBook = self.head
        previous = None
        stop = False
        
        while currBook != None and not stop:
            if currBook.data > book:
                stop = True
            else:
                previous = currBook
                currBook = currBook.next
                
        bookNode = BookCollectionNode(book)

        if previous == None:
            bookNode.setNext(self.head)
            self.head = bookNode
        else:
            bookNode.setNext(currBook)
            previous.setNext(bookNode)

    def getBooksByAuthor(self, author):
        current = self.head
        bookAuthor = author.title()
        author_str = ""
        stop = False
        while current.next != None and not stop:
            if bookAuthor == current.data.author:
                author_str += current.data.getBookDetails() + "\n"
            current = current.getNext()
            continue
        if current.next == None:
            if bookAuthor == current.data.author:
                author_str += current.data.getBookDetails() + "\n"
        return author_str

    def getAllBooksInCollection(self):
        current = self.head
        output = ""
        while current != None:
            output += current.data.getBookDetails() + "\n"
            current = current.next
        return output

    def removeAuthor(self, author):
        current = self.head
        previous = None
        temp = None
        stop = False
        bookAuthor = author.title()
        while current != None and not stop:
            if current.data.author != bookAuthor:
                previous = current
                current = current.next
            else:
                while current.data.author == bookAuthor:
                    temp = current
                    current = None
                    if temp.next == None:
                        stop = True
                        break
                    current = temp.next
                stop = True
            

        if previous == None:
            self.head = current
        else:
            previous.next = current

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        else:
            if bookNode.getData().getTitle().lower() == title.lower():
                return True
            return self.recursiveSearchTitle(title, bookNode.getNext())


