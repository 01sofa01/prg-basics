# Bubble sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Traverse the array from 0 to n-i-1 (last i elements are already sorted)
        for j in range(0, n - i - 1):
            # If the element at index j is greater than the element at index j+1, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Car fuel consumption data
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print("Original car fuel consumption:", car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)

# Bank transactions data
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print("Original bank transactions:", bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Sorted bank transactions:", sorted_bank_transactions)
