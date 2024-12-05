# Data lists
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

# Sort distances_traveled from lowest to highest value (ascending order)
sorted_distances = sorted(distances_traveled)
print("Distances traveled sorted (ascending):", sorted_distances)

# Sort daily_temperatures from highest to lowest value (descending order)
sorted_temperatures = sorted(daily_temperatures, reverse=True)
print("Daily temperatures sorted (descending):", sorted_temperatures)

# Sort file_names in ascending alphabetical order
sorted_files = sorted(file_names)
print("File names sorted (ascending):", sorted_files)
