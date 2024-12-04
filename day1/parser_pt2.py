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
        
        # similarity score
        score = 0

        # calculate similarity score
        left_idx, right_idx = 0, 0
        curr_number = left_list[0]
        count = 0
        while left_idx < len(left_list) and right_idx < len(right_list):
            if right_list[right_idx] == curr_number: # move forward
                count += 1
                right_idx += 1
            elif right_list[right_idx] < curr_number: # not found yet
                right_idx += 1
            else: # if greater than switch to next number on left
                score += count * curr_number
                while left_idx + 1 < len(left_list) and left_list[left_idx + 1] == curr_number:
                    score += count * curr_number
                    left_idx += 1

                # reset count and move to next number
                count = 0
                left_idx += 1
                if left_idx < len(left_list): 
                    curr_number = left_list[left_idx]

        # print similarity score
        print(score)

    except FileNotFoundError:
        print("input.txt not found")
        exit(1)