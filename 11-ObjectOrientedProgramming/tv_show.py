# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
   my_tv = TV()

   # object usage
   my_tv.show_status()  # Display initial status

   my_tv.turn_on()  # Turn the TV on
   my_tv.show_status()  # Display status

   my_tv.turn_off()  # Turn the TV off
   my_tv.show_status()  # Display status

if __name__ == "__main__":
   main() 