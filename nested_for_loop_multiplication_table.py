 nested_for_loop_multiplication_table.py

# Outer loop for rows (1 to 5)
for i in range(1, 6):  
    # Inner loop for columns (1 to 5)
    for j in range(1, 6):  
        product = i * j  # Calculate the product of i and j
        print(f"{product:4}", end="")  # Print the product with formatting
    print()  # New line after each row