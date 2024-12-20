class Song:
   def __init__(self, performer, title, album, year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year
   def __str__(self):
      return f"{self.performer} {self.title} {self.album} {self.year}"
      ...
      ...

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

## object usage
print('================')
print(f'Performer:{song1.performer}') 
print(f'Title:{song1.title}') 
print(f'Album:{song1.album}')
print(f'Year:{song1.year}') 
print("================")
print(f'Performer:{song2.performer}') 
print(f'Title:{song2.title}') 
print(f'Album:{song2.album}')
print(f'Year:{song2.year}')         
