import turtle

def read_coordinates(filename):
    coordinates = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split()
            coordinates.append((float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])))
    return coordinates

def draw_line(start_x, start_y, end_x, end_y):
    turtle.penup()
    turtle.goto(start_x, -start_y)
    turtle.pendown()
    turtle.goto(end_x, -end_y)

def draw_map(coordinates):
    turtle.speed(0)
    for coords in coordinates:
        draw_line(*coords)
    turtle.hideturtle()
    turtle.done()

def main():
    turtle.setup(width=800, height=600)
    turtle.title("Turkey Map")
    turtle.bgcolor("white")

    coordinates = read_coordinates("TurkeyMap.txt")
    draw_map(coordinates)

if __name__ == "__main__":
    main()