def print_tree(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    print(" " * (height - 1) + "|")


tree_height = int(input("Enter the height of the Christmas tree: "))
print_tree(tree_height)