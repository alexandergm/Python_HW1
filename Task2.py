def check_case(x, y, z):
    return not(x or y or z) == (not x and not y and not z)


result = True
for i in range(8):
    result = result and check_case(bool(i % 2), bool(i / 2 % 2), bool(i / 4 % 2))
print(f'Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z {"истинно" if result else "ложно"}.')
