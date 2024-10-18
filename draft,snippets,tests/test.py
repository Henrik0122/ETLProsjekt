num = '42'
try:
    num = float(num)
    result = isinstance(num, (int, float)) and num.is_integer()
except ValueError:
    result = False

if result:
    num_type = "int" if num.is_integer() else "float"
    print(f"{num} is a {num_type}")
else:
    print(f"{num} is not a number")
