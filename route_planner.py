import tkinter as tk
from PIL import Image, ImageTk
import turtle

gui = tk.Tk()
gui.geometry('1920x1080')
gui.title('Route Planner Preview')

canvas = tk.Canvas(gui, width=1920, height=1080, bg="black")
canvas.pack()

image_path = r'C:\Users\Rezwan\PycharmProjects\internProject\Route_Builder\Advanced_AI.png'
img = Image.open(image_path)
photo_image = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)

img20 = Image.open(r'C:\Users\Rezwan\PycharmProjects\internProject\Route_Builder\Advanced_AI.png')
img20 = img20.resize((1285, 670))
img20 = ImageTk.PhotoImage(img20)


class Command:
    def __init__(self, sequence, action_type, dm1, dm2, dm3, ai_on_off, steer_on_off, distance_mode, run_with_prev):
        self.sequence = sequence
        self.action_type = action_type
        self.dm1 = dm1
        self.dm2 = dm2
        self.dm3 = dm3
        self.ai_on_off = ai_on_off
        self.steer_on_off = steer_on_off
        self.distance_mode = distance_mode
        self.run_with_prev = run_with_prev


# parsing the commands from the txt file
def parse_command(line):
    parts = line.strip().split(',')
    return Command(
        sequence=parts[0],
        action_type=parts[1],
        dm1=parts[2],
        dm2=parts[3],
        dm3=parts[4],
        ai_on_off=parts[5],
        steer_on_off=parts[6],
        distance_mode=parts[7],
        run_with_prev=parts[8]
    )


# the total distance of the route
def calculate_total_distance(commands):
    total_distance = 0
    for cmd in commands:
        if cmd.action_type in ["Move Forward", "Move Backward", "Slide Left", "Slide Right"]:
            total_distance += int(cmd.dm2) if cmd.dm2.isdigit() else 100
    return total_distance


file_name = 'sample_txt.txt'
commands = []
with open(file_name, 'r') as file:
    for line in file:
        command = parse_command(line)
        commands.append(command)

total_distance = calculate_total_distance(commands)


def calculate_scaling_factor(total_distance, max_distance):
    return min(1, max_distance / total_distance) if total_distance > 0 else 1


# on clicking the button the route will be previewed
def on_button_click():
    abc.clear()
    abc.penup()
    abc.setposition(600, -80)
    abc.setheading(0)
    abc.color("#8C52FF")
    abc.showturtle()
    abc.pendown()
    abc.dot(20, '#00BF63')
    abc.shape('square')
    abc.speed(10)
    abc.dot(20, '#00BF63')
    execute_commands(commands, abc)


border_frame = tk.Frame(gui, background='blue', borderwidth=1)
border_frame.place(x=1300, y=660)
button = tk.Button(border_frame, text="Preview", command=on_button_click, bg='black', fg='white')
button.pack(padx=1, pady=1)

max_distance = 180

scaling_factor = calculate_scaling_factor(total_distance, max_distance)


# commands will be executed according to the txt file
def execute_commands(commands, turtle_obj):
    for i, cmd in enumerate(commands):
        distance_or_angle = int(cmd.dm2) if cmd.dm2.isdigit() else 100
        scaled_distance = distance_or_angle * scaling_factor
        run_with_previous = cmd.run_with_prev == '1'

        if i > 0 and run_with_previous:
            continue

        if cmd.action_type == "Move Forward":
            turtle_obj.forward(scaled_distance)
        elif cmd.action_type == "Move Backward":
            turtle_obj.backward(scaled_distance)
        elif cmd.action_type == "Turn Left":
            abc.dot(20, '#FFDE59')
            if cmd.steer_on_off == '0':
                turtle_obj.left(distance_or_angle)
            else:
                for _ in range(int(distance_or_angle / 10)):
                    turtle_obj.forward(10)
                    turtle_obj.left(10)
        elif cmd.action_type == "Turn Right":
            abc.dot(20, '#FFDE59')
            if cmd.steer_on_off == '0':
                turtle_obj.right(distance_or_angle)
            else:
                for _ in range(int(distance_or_angle / 10)):
                    turtle_obj.forward(10)
                    turtle_obj.right(10)
        elif cmd.action_type == "Slide Left":
            abc.dot(20, '#FFDE59')
            turtle_obj.left(90)
            turtle_obj.forward(scaled_distance)
            turtle_obj.right(90)
        elif cmd.action_type == "Slide Right":
            abc.dot(20, '#FFDE59')
            turtle_obj.right(90)
            turtle_obj.forward(scaled_distance)
            turtle_obj.left(90)
        elif cmd.action_type == "Stop":
            abc.dot(20, '#FF3131')
            turtle_obj.penup()
            break
        elif cmd.action_type.startswith("Preset: CIRCLE"):
            turtle_obj.circle(scaled_distance)
        elif cmd.action_type.startswith("Preset: Rectangle"):
            for _ in range(2):
                turtle_obj.forward(scaled_distance)
                turtle_obj.left(90)
                turtle_obj.forward(scaled_distance / 2)
                turtle_obj.left(90)
        elif cmd.action_type.startswith("Preset: Triangle"):
            for _ in range(3):
                turtle_obj.forward(scaled_distance)
                turtle_obj.left(120)
        if i < len(commands) - 1 and commands[i + 1].run_with_prev == '1':
            next_cmd = commands[i + 1]
            next_distance_or_angle = int(next_cmd.dm2) if next_cmd.dm2.isdigit() else 100
            scaled_distance = next_distance_or_angle * scaling_factor
            if next_cmd.action_type == "Move Forward":
                turtle_obj.forward(scaled_distance)
            elif next_cmd.action_type == "Move Backward":
                turtle_obj.backward(scaled_distance)
            elif next_cmd.action_type == "Turn Left":
                turtle_obj.left(next_distance_or_angle)
            elif next_cmd.action_type == "Turn Right":
                turtle_obj.right(next_distance_or_angle)


x_position = -1920 // 4
y_position = -1080 // 4
# left and right is 180 and down in 180 and up is 180
abc = turtle.RawTurtle(canvas)
canvas.create_image(x_position, y_position, anchor=tk.NW, image=img20)

canvas.mainloop()
