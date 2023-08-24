def filter_and_square(nums, threshold):
    """
    Filters numbers greater than a threshold and returns their squares.

    Parameters:
    - nums (list): A list of numbers.
    - threshold (int): The threshold value for filtering.

    Returns:
    - list: A list of squared numbers that are greater than the threshold.
    """
    return [x**2 for x in filter(lambda x: x > threshold, nums)]

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
threshold_value = 5
squared_numbers = filter_and_square(numbers, threshold_value)

print(f"Original numbers: {numbers}")
print(f"Numbers greater than {threshold_value} squared: {squared_numbers}")

# Expected Output:
# Original numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Numbers greater than 5 squared: [36, 49, 64, 81, 100]
