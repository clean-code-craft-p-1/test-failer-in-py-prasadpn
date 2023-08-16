
def print_color_map():
    color_map_output = []
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            color_map_output.append(f'{i * 5 + j} | {major} | {minor}')
    #return len(major_colors) * len(minor_colors)
    return color_map_output


result = print_color_map()
#print(result[0])
#assert(result == 25)

assert(result[0] ==  '0  | White | Blue')
assert(result[12] == '12 | Black | Green')
print("All is well (maybe!)\n")