class BinarySearch:
    def __init__(self, sorted_list):
        self.sorted_list = sorted_list

    def search(self, target):
        low, high = 0, len(self.sorted_list) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_element = self.sorted_list[mid]

            if mid_element == target:
                return mid  # Target found, return the index
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1  # Target not found in the list

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 8

binary_search_instance = BinarySearch(sorted_list)
result_index = binary_search_instance.search(target_element)

if result_index != -1:
    print(f"Element {target_element} found at index {result_index}.")
else:
    print(f"Element {target_element} not found in the list.")
