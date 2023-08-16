
def print_color_map():
    color_map_output = []
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map_value = f'{(i * 5 + j):3} | {major} | {minor}'
            print(color_map_value)
            color_map_output.append(color_map_value)
    return color_map_output


table_color_map_output = print_color_map()

assert(table_color_map_output[0].strip() ==  '0 | White | Blue')
assert(table_color_map_output[12].strip() == '12 | Black | Green')
print("All is well (maybe!)\n")