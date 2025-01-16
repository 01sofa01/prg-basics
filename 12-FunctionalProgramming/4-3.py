final_grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

filtered_grades = list(filter(lambda x : x>2.0, final_grades))

if filtered_grades :
    arithmetic_mean = sum(filtered_grades)/len(filtered_grades)
print(f'The arithmetic mean of the grades is {arithmetic_mean: .2f}')
