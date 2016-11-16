# O(n)
def zigzag_conversion(string, n):
    if n > 1:
        rows = [""] * n
        isDown = True
        row = 0
        for i, char in enumerate(string):
            rows[row] += char

            if row == 0:
                isDown = True
            elif row == n - 1:
                isDown = False

            if isDown:
                row += 1
            else:
                row -= 1

        return "".join(rows)
    else:
        return string

print(zigzag_conversion("PAYPALISHIRING", 3))
print(zigzag_conversion("AB", 1))
