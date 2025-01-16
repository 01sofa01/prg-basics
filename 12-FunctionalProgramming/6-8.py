

# Scores obtained by the students
scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

# Higher-order function
def min_pts(limit):
    return lambda pts: pts >= limit

# Minimum points thresholds
thresholds = [70, 40, 30]

# Process each threshold and display the results
for threshold in thresholds:
    passing_scores = list(filter(min_pts(threshold), scores))
    print(f"Scores greater than or equal to {threshold}: {passing_scores}")
