#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Nov 18
#

# This function takes a list as input and returns a new list with all duplicate elements removed
def remove_similarities(list):
    clean_list = []
    for element in list:
        if element not in clean_list:
            clean_list.append(element)
    return clean_list


# The main function of the program
def main():
    # Print a message to the user explaining the purpose of the program
    print(
        "This program asks the user for a list of elements (strings, float, int). Then returns a new list removing all duplicate elements."
    )
    # Initialize an empty list to store the user's input
    get_user_list = []
    # Prompt the user for a list of elements
    user_input = input("Enter a comma-separated list of elements: ")
    # Split the user input into a list of individual elements, stripping leading and trailing whitespace from each element
    get_user_list = [word.strip() for word in user_input.split(",")]
    # Call the remove_similarities() function to remove duplicates from the list
    clean_list = remove_similarities(get_user_list)
    # Print the resulting list to the user
    print(f"The list after removing all duplicates is: {clean_list}")


# Run the main function if this script is being run directly
if __name__ == "__main__":
    main()
