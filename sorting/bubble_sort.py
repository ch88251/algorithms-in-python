##############################################################################
# Bubble sort algorithm
# This algorithm has a quadratic runtime performance. As the size of the
# input array grows, the number of steps executed grows exponentially.
##############################################################################
def bubble_sort(num_list):
    unsorted_until_index = len(num_list) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_until_index):
            if num_list[i] > num_list[i + 1]:
                is_sorted = False
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        unsorted_until_index = unsorted_until_index - 1


my_list = [65, 55, 45, 35, 25, 15, 10]
bubble_sort(my_list)

print(my_list)