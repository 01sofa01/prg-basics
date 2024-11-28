tree_circumference = int(input("Enter the tree circumference:"))
diameter = tree_circumference/ 3.14
tree_can_be_cut_down = diameter >=50
print(f'Tree can be cut down: {tree_can_be_cut_down}')