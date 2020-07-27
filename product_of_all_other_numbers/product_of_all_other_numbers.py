'''
Input: a List of integers
Returns: a List of integers
'''

# This is a naive solution because it makes too many calls to for more space and is O(n + n) time complexiy
def product_of_all_other_numbers(arr):

    copy_of_arr = arr
    multiplied_arr = arr
    counter = 0

    for i in range(0, len(arr)):
        multiplied_arr = [element * arr[i] for element in multiplied_arr]
        multiplied_arr[i] = copy_of_arr[i]
        copy_of_arr = multiplied_arr
        counter=counter+1
    
    for i in range(0, len(arr)):
        multiplied_arr[i] = multiplied_arr[i] / arr[i]

    return multiplied_arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 7, 3, 4]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
