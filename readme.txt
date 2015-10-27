The code is run as an executable python file "lineplot.py"
I ran it from a Bash terminal using the command: ./lineplot.py

First the user is prompted to enter the name of the file eg. Input1.txt

If a flood fill is appropriate the user is asked weather or not they want to flood fill the polygon (or the union of polygons).
If the user types y (case insensitive) it flood fills,
Otherwise it doesn't.

Two flood fill functions were created:
The first (not used) is called "flood_fill_Recursive" - This is the traditional flood fill algorithm described in the project sheet. In python this goes too deeply into recusion and causes a runtime error. So I created a second algorithm.

The second algorithm (Used) is called "flood_fill_pathplanner" - This is based on a pth planning algorithm that builds a stack of unknown pixel values and tests them if they have been filled. This worked much faster and did not use recursion.
