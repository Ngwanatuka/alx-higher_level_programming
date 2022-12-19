#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a counter variable to keep track of the number of elements printed
    counter = 0

    # Try to print x elements of the list
    try:
        for i in range(x):
            # Print the element at index i, followed by a space
            print(my_list[i], end=' ')
            # Increment the counter
            counter += 1
        # Print a new line after all the elements have been printed
        print()
        # Return the counter
        return counter
    # If an IndexError exception is raised, indicating that the index is out of bounds
    except IndexError:
        # Print all the remaining elements of the list
        for i in range(x):
            try:
                # Print the element at index i, followed by a space
                print(my_list[i], end=' ')
            # If an IndexError exception is raised, stop printing elements
            except IndexError:
                break
            # Increment the counter
            counter += 1
        # Print a new line after all the elements have been printed
        print()
        # Return the counter
        return counter
