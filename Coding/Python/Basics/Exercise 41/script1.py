# if __name__ ** __main__: (this script can be imported OR run standalone)
#                           Functions and classes in this module can be reused
#                           without the main block of code executing
# Good practice to include because:
#                           Code is modular,
#                           Helps readability,
#                           Leaves no global variables
#                           Avoids unintended execution 

# ex. library = Import library for functionality
#               When running library directly, display a help page

def favourite_food(food):
    print(f"Your favourite food is {food}")

def main():
    print("This is script 1")
    favourite_food("lasagna & brownies")
    print("Goodbye")

if __name__ == '__main__':
    main()