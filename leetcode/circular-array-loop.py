class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def get_next(x):
            return (x + nums [x]) % n
        for i in range (n):
            if nums[i] == 0 :
                continue
            slow  = i
            fast = get_next(i)
            while nums[slow] * nums[fast] >0 and nums[slow] * nums[get_next(fast)] >0:
                if slow == fast:
                    if slow != get_next(slow):
                        return True
                    break
                slow = get_next(slow)
                fast = get_next(get_next(fast))
        index = i
        while nums[index] * nums[get_next(index)] > 0:
            next_index = get_next(index)
            nums[index] = 0
            index = next_index

        # If no loop is found, return False
        return False




        # length = len(nums)

        # # Define a function to find the next index in a circular manner
        # def get_next_index(current_index):
        #     # Calculate the next index considering wrapping around
        #     return (current_index + nums[current_index]) % length

        # # Iterate over all elements in the array
        # for i in range(length):
        #     # Skip if the current element is already marked as 0, indicating it's not part of a loop
        #     if nums[i] == 0:
        #         continue
          
        #     # Initialize the slow and fast pointers for cycle detection
        #     slow_pointer = i
        #     fast_pointer = get_next_index(i)
          
        #     # Continue moving pointers while the signs of the elements indicate a potential loop
        #     # This also ensures that we are not mixing cycles of different directions
        #     while nums[slow_pointer] * nums[fast_pointer] > 0 and nums[slow_pointer] * nums[get_next_index(fast_pointer)] > 0:
        #         # If the slow and fast pointers meet, a cycle is detected
        #         if slow_pointer == fast_pointer:
        #             # Check to ensure the loop is longer than 1 element
        #             if slow_pointer != get_next_index(slow_pointer):
        #                 return True
        #             # If the loop is just one element, break and mark it as non-looping
        #             break
              
        #         # Move slow pointer by one step and fast pointer by two steps
        #         slow_pointer = get_next_index(slow_pointer)
        #         fast_pointer = get_next_index(get_next_index(fast_pointer))
          
        #     # Mark all visited elements as 0 to avoid revisiting and repeated calculations
        #     # This process will also ensure elimination of non-loop elements
        #     index = i
        #     while nums[index] * nums[get_next_index(index)] > 0:
        #         next_index = get_next_index(index)
        #         nums[index] = 0
        #         index = next_index

        # # If no loop is found, return False
        # return False