try:
    hex_value = input("Enter a hexadecimal value: ")

    decimal_value = int(hex_value, 16)
    binary_value = bin(decimal_value)[2:]

    print("\n--- Conversion Results ---")
    print(f"Hexadecimal : {hex_value}")
    print(f"Decimal     : {decimal_value}")
    print(f"Binary      : {binary_value}")

except ValueError:
    print("Invalid hexadecimal input!")
