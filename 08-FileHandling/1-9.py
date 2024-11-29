###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

with open(name) as file:
   file_content = read_from_file('it_company.csv')  
   file_lines = file_content.splitlines() 
   for line in file_lines:
      if job_title in file_lines:
         print(job_title)