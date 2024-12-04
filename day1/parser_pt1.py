import os

def insertion_sort(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    arr.insert(left, x)

if __name__ == "__main__":
    try:
        # open file and populate left and right arrays
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            # initialize left and right arrays
            left_list, right_list = [], []

            # read each line in the file
            for line in file:
                # split the line into left and right integers
                chars = [char for char in line.strip().split(" ") if char != ""]
                left_int, right_int = int(chars[0]), int(chars[1])

                # insertion sort
                insertion_sort(left_list, left_int)
                insertion_sort(right_list, right_int)
        
        # get total difference between each array
        diff = 0
        for i in range(len(left_list)):
            diff += abs(left_list[i] - right_list[i])

        # print out diff
        print(diff)
        
    except FileNotFoundError:
        print("input.txt not found")
        exit(1)