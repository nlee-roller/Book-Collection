# Lab05, CS9, Nick Lee-Roller
class Book:
    def __init__(self, title = "", author = "", year=None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author
    
    def getYear(self):
        return self.year
    
    def getBookDetails(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __gt__(self, rhs):
        if rhs == None or self.author == None:
            return self.author > rhs
        elif self.author != rhs.author:
            return self.author > rhs.author
        elif self.year != rhs.year:
            return self.year > rhs.year
        else:
            return self.title > rhs.title
