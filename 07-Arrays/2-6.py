###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
      n -= 1
      weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
      return weekdays[n]
#or return weekdays[n-1] and without line 2
print(weekday(1))