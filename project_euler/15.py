"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?"""

# Pass the amount of verticies (e.g. a 1x1 grid is 2, 2)
def path_counter(grid_w, grid_h):
    path_count = 1
    # Using combinatorics https://towardsdatascience.com/understanding-combinatorics-number-of-paths-on-a-grid-bddf08e28384
    for i in range(grid_h, (grid_w + grid_h -1)):
        path_count *= i
        path_count //= (i - grid_h + 1)
    return path_count

if __name__ == '__main__':
    print(path_counter(21, 21))