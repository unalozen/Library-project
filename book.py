class Book:
    def __init__(self, name, author, release_date, number_of_pages):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.number_of_pages = number_of_pages
    
    def __str__(self):
        return " - " + self.name + ", " + self.author
    
    def __repr__(self):
        return self.__str__()
    
    def show_details(self):
        return self.__str__() + " [ " + self.number_of_pages + " page(s), released in " + self.release_date + " ]"
    