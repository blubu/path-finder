# Steps to Recreate Path Finder
This README provides a step-by-step guide to help you recreate the Path Finder project from scratch on your local machine.
## Prerequisites
Make sure you have the following software installed on your system:
- Python (version 3.6 or higher)
- Pygame (version 2.5.0 or higher)
- Any GUI library compatible with Python
- Git (optional, for cloning the repository)

Choose a GUI library that suits your preferences and requirements. Some popular options include:
- PyQt5
- Tkinter
- wxPython
- Kivy
- PySide2

Install the chosen GUI library using the library-specific installation instructions.
## Steps
**1. Create a Window:**
- Import the necessary libraries.
- Set up a graphical user interface (GUI) window.

**2. Create a Grid on the Window:**
- Define the dimensions and properties of the grid.
- Display the grid on the GUI window.

**3. Allow User to Select Start and Endpoint:**
- Create another window for user input.
- Allow the user to select the start and endpoint within the grid.
- 
**4. Allow User to Create a Maze on the Grid:**
- Implement functionality to let the user draw obstacles or walls on the grid.
- Update the grid accordingly to represent the maze.

**5. Code the Pathfinding Algorithm:**
- Choose a pathfinding algorithm to implement (e.g., A*, Dijkstra's algorithm).
- Write the code for the chosen algorithm.
- Test the algorithm's functionality.

**6. Visualize the Steps of the Algorithm:**
- Implement code to visualize the steps followed by the algorithm.
- Update the grid in each step to reflect the algorithm's progress.
- 
**7. Show the Final Solution Path:**
- Implement code to display the final solution path on the grid.
- Highlight the cells or draw a line to represent the path.

**8. Allow Selection of Different Algorithms:**
-Provide options for the user to select different pathfinding algorithms.
-Modify the code to accommodate the selected algorithm.

**9. Provide Option to Show/Hide Steps:**
- Implement functionality to allow the user to choose whether to display the algorithm's steps or not.

**10. Create a Window to Show Path Metrics:**
- Develop a separate window to show metrics related to the found path (e.g., path length, time taken).

**11. Clean and Organize Code:**
- Refactor the code into smaller, understandable parts (functions or classes).
- Add comments and documentation to improve readability.
- Ensure proper code structure and organization.
