def mirrored_right_triangle(n):
    for i in range(1, n+1):
        # Print spaces first
        print(' ' * (n - i), end='')
        # Print stars
        print('1' * i)

# Example usage
rows = int(input("Enter the number of rows: "))
mirrored_right_triangle(rows)