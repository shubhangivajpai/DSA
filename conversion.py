input_str = "double2"

# Find the numeric part of the string
numeric_part = ""
for char in input_str:
    if char.isdigit():
        numeric_part += char

# Convert the numeric part to an integer
numeric_value = int(numeric_part)

# Repeat the numeric part
result_str = str(numeric_value) * numeric_value

print(result_str)
