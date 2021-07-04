"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""""
sample = """75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def max_path_in_triangle(triangle_string):
    triangle = [level.strip() for level in triangle_string.split('\n')]
    tri_len = len(triangle)
    # Convert the string triangle to int, pad the extra space with 0's
    for row in triangle:
        level = [int(n) for n in row.split(" ")]
        i = len(level) - 1
        if len(level) < tri_len:
            level = level + [0]*(tri_len - len(level))
        triangle[i] = level
    
    # Start at second to last row
    for row in range(len(triangle)-2, -1, -1):
        for col in range(row+1):
            # Check on the next row which of the adjacent values is larger
            if triangle[row+1][col] > triangle[row+1][col+1]:
                triangle[row][col] += triangle[row+1][col]
            else:
                triangle[row][col] += triangle[row+1][col+1]
    print(f"Max path value: {triangle[0][0]}")
        

if __name__ == '__main__':
    max_path_in_triangle(sample)