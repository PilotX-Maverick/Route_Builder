# Route_Builder

This is a new tab of the software, for which an image has been provided, use that image as a background to create a tkinter Canvas of size 1920 by 1080 (Standard Size).
The goal is to create a path (using turtle graphics) which replicates a route planned by the user in the software. This path is created when user clicks "Preview" button, after entering all the path details, that he/she wants his/her rover to move onto.

The path specified by user is saved in a .txt file, which has a standard format, as mentioned below: 
Sequence Number, Action Type, Dynamic Value 1 (DM1), Dynamic Value 2 (DM2), Dynamic Value 3 (DM3), AI ON/OFF, Steerability ON/OFF, Distance Mode, Run With Previous

Here:
Sequence number defines the order in which each line of the text file is executed.
Action Type defines the type of action such as [Move Forward, Move Backward, Turn Left, Turn Right, Slide Left, Slide Right, Stop, Preset:C ricle, Preset: Rectangle, Preset: Triangle]
For move forward or backward, the DM1 takes time & DM2 takes distance for which rover moves forward or backward. User will enter only either time or distance.
For turn left and turn right user enters the degree (directional angle, like 0 for North, 180 for South) to which the rover must move, if steerability is OFF (0), rover moves on its axis, else its moves by forming an arc similar to how a car takes turn. 
For slide left and slide right, user enters the distance for which vehicle should slide leftways or rightways. 

If a step has Run with previous variable TRUE (1), then it must run along with the previous step.

All other unspecified variables are not to be considered for this task.

Your task is to develop a Python code that generates a route plan preview (using turtle graphic, within the black area on "AdvancedAI.png file, titled as "Route Planner") based on data saved in the given .txt file. Utilize the "Advanced_AI.png" file as the background image for this route planner.
Additionally, there is a file with the name, "sample_turtle_code" which you can use for reference to understand how turtle code works.

Modify the .txt file to test your code to find out if it follows all the types of user inputs. 

Challenge: The major challenge here is, the graphic/path drawn by turtle must not go outside the black area on left side in the Advanced AI.png. Depending on the number of steps (number of lines) in the .txt file, the graphic must scale down or scale up but should never outflow the specified black area.
