###
# Prints employees employed in a specified position.
#

# Employee List
file_name = '08-FileHandling\it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name) as file:
   file_content = file.read()  
   print(file_content)
   file_lines = file_content.splitlines() 
   for line in file_lines:
      dane = line.split(",")
      if job_title in dane:
         print(dane)
