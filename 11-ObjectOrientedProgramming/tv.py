# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
   def turn_off(self):
      self.is_off = True
   def turn_on(self):
      self.is_on = False
   def show_status(self) :
       if self.is_on :
          print('The TV is ON')
       else:
          print('The TV is OFF')
         