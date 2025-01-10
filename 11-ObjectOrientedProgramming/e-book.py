class EBook() :
    def __init__(self, title, author,total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0
        self.is_open = False 
        
    def open(self):
        self.is_open = True 
    def close(self):
        self.is_close = False 
    def change_page(self, page):
    
