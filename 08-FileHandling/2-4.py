###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = '08-FileHandling/it_company.csv'
position_file = '08-FileHandling/software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file) as file:
   with open(position_file, 'w') as file2:
      podzielone = file.read().splitlines()
      for line in podzielone:
         najpodzielniejsze = line.split(',')
         if job_title in najpodzielniejsze:
            file2.write(line)
            file2.write("\n")