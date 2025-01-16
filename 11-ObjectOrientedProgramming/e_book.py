class EBook() :
    def __init__(self, title : str , author : str,total_pages : int, current_page : int = 0 ):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page
        self.is_open = False 

    def open(self):
        self.is_open = True 
        print("Book is open")
    def close(self):
        self.is_open = False 
    def change_page(self, page : int = 0):
        if self.is_open == True:
            # if page < 0 :
            #     self.current_page -= 1
            # elif page > 0 :
            #     self.current_page += 1
            self.current_page += page
        else:
            print("The book is closed.")
    
    def book_status(self):
        print(self.title)
        print(self.author)
        print(self.total_pages)
        print(self.current_page)
        
