```text
 ________  _______   ________  ___  _______   ________
|\   ____\|\  ___ \ |\   __  \|\  \|\  ___ \ |\   ____\
\ \  \___|\ \   __/|\ \  \|\  \ \  \ \   __/|\ \  \___|_
 \ \_____  \ \  \_|/_\ \   _  _\ \  \ \  \_|/_\ \_____  \
  \|____|\  \ \  \_|\ \ \  \\  \\ \  \ \  \_|\ \|____|\  \
    ____\_\  \ \_______\ \__\\ _\\ \__\ \_______\____\_\  \
   |\_________\|_______|\|__|\|__|\|__|\|_______|\_________\
 __________________  ________  ________ _________|______________  _______
|\   __  \|\   __  \|\   __  \|\   ____|\___   ___|\  \|\   ____\|\  ___ \
\ \  \|\  \ \  \|\  \ \  \|\  \ \  \___\|___ \  \_\ \  \ \  \___|\ \   __/|
 \ \   ____\ \   _  _\ \   __  \ \  \       \ \  \ \ \  \ \  \    \ \  \_|/__
  \ \  \___|\ \  \\  \\ \  \ \  \ \  \____   \ \  \ \ \  \ \  \____\ \  \_|\ \
   \ \__\    \ \__\\ _\\ \__\ \__\ \_______\  \ \__\ \ \__\ \_______\ \_______\
 ________  ________\|____________|\|_______|   \|__|  \|__|\|_______|\|_______|
|\   ____\|\   __  \|\   _ \  _   \|\  ___ \
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|
 \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__
  \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \
   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\
 ___\|_______|_________|________  ______________|________  ________
|\  \    /  /|\  ___ \ |\   __  \|\   ____\|\  \|\   __  \|\   ___  \
\ \  \  /  / \ \   __/|\ \  \|\  \ \  \___|\ \  \ \  \|\  \ \  \\ \  \
 \ \  \/  / / \ \  \_|/_\ \   _  _\ \_____  \ \  \ \  \\\  \ \  \\ \  \
  \ \    / /   \ \  \_|\ \ \  \\  \\|____|\  \ \  \ \  \\\  \ \  \\ \  \
   \ \__/ /     \ \_______\ \__\\ _\ ____\_\  \ \__\ \_______\ \__\\ \__\
  ______|/   __________________|\|__|\_________\|__|\|_______|\|__| \|__|
 / __  \    |\   __  \|\   ____\    \|_________|
|\/_|\  \   \ \  \|\  \ \  \___|_
\|/ \ \  \   \ \  \\\  \ \_____  \
     \ \  \ __\ \  \\\  \|____|\  \
      \ \__|\__\ \_______\____\_\  \
       \|__\|__|\|_______|\_________\
                         \|_________|        
```                                                   
TABLE OF CONTENTS
=================
1. Project Overview
2. System Requirements
3. Installation Instructions
4. Game Structure
5. Game Modes
6. Class Architecture
7. Color Scheme
8. Features
9. Database of Problems
10. Troubleshooting
11. Future Enhancements


1. PROJECT OVERVIEW
===================
Series Master is an interactive educational desktop application designed to help
students practice and master mathematical concepts related to:

- Sequence convergence
- Infinite series convergence tests (Integral, Comparison, Ratio, Root, Alternating)
- Power series (radius and interval of convergence)
- Taylor and Maclaurin series construction

The application features LaTeX rendering for professional mathematical notation,
a lives/streak scoring system, and graphical visualization of mathematical concepts.

Key Features:
- 4 complete game modes covering different topics
- Professional LaTeX math rendering
- Lives system with streak bonuses
- Graphical visualization of sequences and series
- Three difficulty levels (Easy, Medium, Hard)
- Score tracking across all games
- Consistent color scheme and interface


2. SYSTEM REQUIREMENTS
======================

Minimum Requirements:
- Operating System: Windows 10/11, macOS, or Linux
- Python Version: 3.8 or higher
- RAM: 4 GB minimum
- Disk Space: 500 MB

Required Python Packages:
- tkinter (built-in with Python)
- matplotlib 3.5.0 or higher
- Pillow 9.0.0 or higher

Optional Packages:
- numpy (for enhanced calculations)


3. INSTALLATION INSTRUCTIONS
=============================

Step 1: Install Python 3.8+ from python.org

Step 2: Install required packages using pip:
    pip install matplotlib pillow

Step 3: Save the complete Python script as 'SeriesGame.py'

Step 4: Run the application:
    python SeriesGame.py


4. GAME STRUCTURE
=================

The application uses a tabbed interface with four independent game modes:

    [1. Sequences] [2. Series Tests] [3. Power Series] [4. Taylor/Maclaurin]
    ------------------------------------------------------------------------
                          Game Content Area
    ------------------------------------------------------------------------
    Score: 0    Streak: 0    Lives: 3

Common Elements Across All Games:
- Score: Accumulated points from correct answers
- Streak: Consecutive correct answers (provides bonus multiplier)
- Lives: Number of allowed wrong answers (game ends at 0)
- Next Button: Advances to next question (enabled after answering)
- Visualize Button: Opens graph window for current problem
- Check Answer Button: Submits the user's answer


5. GAME MODES
=============

5.1 GAME 1: SEQUENCE CONVERGENCE PRACTICE
-----------------------------------------
Objective: Determine the limit of a sequence as n approaches infinity.

Interface Elements:
- LaTeX-rendered sequence expression
- Text entry field for limit answer
- Check Answer button
- Visualize button (shows sequence plot)

Example Problem:
    a_n = 1/n
    What is the limit of this sequence (as n->infinity)?
    Answer: 0

Difficulty Levels:
- Easy: Simple rational sequences, basic limits
- Medium: Sequences with logarithms, exponential decay, special limits
- Hard: Factorials, Stirling's approximation, complex limits

Scoring:
- Correct: 10 + (streak * 2) points
- Wrong: Lose 1 life, streak resets to 0


5.2 GAME 2: SERIES CONVERGENCE TEST MASTER
------------------------------------------
Objective: Identify the appropriate convergence test and determine if the series
converges or diverges.

Interface Elements:
- LaTeX-rendered series or integral
- Dropdown menu for test selection
- Dropdown menu for convergence/divergence
- Check Answer button
- Visualize button (shows partial sums)

Available Tests:
- p-series
- Geometric Series
- Ratio Test
- Root Test
- Integral Test
- Comparison Test
- Limit Comparison Test
- Alternating Series Test

Difficulty Levels:
- Easy: Direct p-series and geometric series
- Medium: Series requiring comparison or ratio tests
- Hard: Complex series requiring multiple tests

Scoring:
- Both test and result correct: 20 + (streak * 3) points
- Partially correct: 10 points
- Wrong: Lose 1 life, streak resets


5.3 GAME 3: POWER SERIES CONVERGENCE
------------------------------------
Objective: Find the radius and interval of convergence for power series.

Interface Elements:
- LaTeX-rendered power series
- Text entry for radius of convergence
- Text entry for interval of convergence
- Check Answer button
- Visualize button (shows interval on number line)

Example Problem:
    sum_{n=0}^{infinity} x^n
    Radius: 1
    Interval: (-1, 1)

Scoring:
- Both correct: 20 + (streak * 3) points
- Radius only correct: 10 points
- Wrong: Lose 1 life, streak resets


5.4 GAME 4: TAYLOR/MACLAURIN SERIES CONSTRUCTOR
-----------------------------------------------
Objective: Identify the correct term in a Taylor or Maclaurin series expansion.

Interface Elements:
- LaTeX-rendered function with its series representation
- Current series display (showing terms up to the missing one)
- Multiple choice buttons (2x2 grid) with LaTeX-rendered options
- Visualize button

Available Functions:
- e^x
- sin(x)
- cos(x)
- ln(1+x)
- arctan(x)
- 1/(1-x)
- 1/(1+x)
- 1/(1-x^2)
- arctan(x^2)
- sinh(x)
- cosh(x)
- 1/(1-x)^2

Scoring:
- Correct: 15 + (streak * 2) points
- Wrong: Lose 1 life, streak resets


6. CLASS ARCHITECTURE
======================

Main Classes and Their Methods:

LaTeXRenderer:
    - __init__(): Initializes matplotlib rendering settings
    - render(latex_expr, bg_color, size): Renders LaTeX to PhotoImage
    - render_small(latex_expr, bg_color, size): Renders smaller LaTeX for buttons
    - graph_sequence_from_latex(latex_expr, n_terms): Creates mathematical graph

SequenceGame:
    - __init__(parent): Initializes the game
    - build_sequence_database(): Creates the problem database
    - setup_gui(): Sets up the user interface
    - create_widgets(): Creates all GUI elements
    - new_question(): Loads a new sequence question
    - check_answer(): Validates user's answer
    - reset_game(): Resets game state
    - visualize_series(): Opens graph visualization window

SeriesTestGame:
    - __init__(parent): Initializes the game
    - build_series_database(): Creates the problem database
    - setup_gui(): Sets up the user interface
    - new_question(): Loads a new series question
    - check_answer(): Validates test selection and convergence result
    - change_difficulty(): Changes difficulty level
    - reset_game(): Resets game state
    - visualize_series(): Opens graph visualization window

PowerSeriesGame:
    - __init__(parent): Initializes the game
    - setup_gui(): Sets up the user interface
    - new_question(): Loads a new power series question
    - check_answer(): Validates radius and interval
    - reset_game(): Resets game state
    - visualize_series(): Opens graph visualization window

TaylorSeriesGame:
    - __init__(parent): Initializes the game
    - setup_gui(): Sets up the user interface
    - new_question(): Loads a new Taylor series question
    - check_answer(): Validates selected term
    - reset_game(): Resets game state
    - visualize_series(): Opens graph visualization window


7. COLOR SCHEME
===============

Standard Color Palette:

Element                 Hex Code      RGB               Usage
---------------------   ----------    --------------    --------------------------------
Main Background         #2c3e50       (44, 62, 80)      Primary application background
Stats Frame             #34495e       (52, 73, 94)      Score/streak/lives background
White Frame             #ecf0f1       (236, 240, 241)   Content display background
Submit Button           #3498db       (52, 152, 219)    Check Answer button
Next Button             #27ae60       (39, 174, 96)     Next question button
Visualize Button        #9b59b6       (155, 89, 182)    Graph visualization button
Text Primary            #ecf0f1       (236, 240, 241)   Main text color
Text Accent             #e74c3c       (231, 76, 60)     Streak/lives text
Correct Feedback        #2ecc71       (46, 204, 113)    Correct answer messages
Wrong Feedback          #e74c3c       (231, 76, 60)     Wrong answer messages
Partial Feedback        #f39c12       (243, 156, 18)    Partially correct messages

Graph Colors:
- Line color: Blue (#1f77b4)
- Marker: Blue circles
- Grid: Light gray with 30% opacity
- Axes lines: Black


8. FEATURES
===========

8.1 SCORING SYSTEM
------------------
Game                Correct Base    Streak Multiplier    Points per Streak
Sequences           10              x2                   +2 per streak
Series Tests        20              x3                   +3 per streak
Power Series        20              x3                   +3 per streak
Taylor Series       15              x2                   +2 per streak

8.2 LIVES SYSTEM
----------------
Game                Starting Lives
Sequences           3
Series Tests        5
Power Series        3
Taylor Series       3

8.3 GAME FLOW
-------------
1. User loads new question
2. User provides answer
3. System checks answer
4. If correct: Award points, increase streak
5. If wrong: Reduce lives, reset streak
6. If lives reach 0: Game over with reset option

8.4 VISUALIZATION FEATURE
-------------------------
Each game includes a "Visualize" button that opens a popup window showing:
- Sequences: Plot of a_n vs n
- Series: Partial sums S_n vs n
- Power Series: Number line showing interval of convergence
- Taylor Series: Plot of the function and its approximation

8.5 DIFFICULTY LEVELS
---------------------
- Easy: Basic concepts, direct application of tests
- Medium: Multiple steps, combination of concepts
- Hard: Complex problems requiring advanced reasoning


9. DATABASE OF PROBLEMS
=======================

9.1 SEQUENCE PROBLEMS (30 total)
--------------------------------
Easy (10 problems):
- a_n = 1/n
- a_n = n/(n+1)
- a_n = 2n/(3n+1)
- a_n = 1/2^n
- a_n = 2 + 1/n
- a_n = 3n/(n+2)
- a_n = 5/n^2
- a_n = n^2/(n^2+1)
- a_n = 4^n/5^n
- a_n = (-1)^n * 1/n

Medium (10 problems):
- a_n = ln n / n
- a_n = (1 + 1/n)^n
- a_n = 3^n / n!
- a_n = n * sin(1/n)
- a_n = sqrt(n^2 + n) - n
- a_n = n / ln n
- a_n = (1 + 2/n)^n
- a_n = ln(n^2) / n
- a_n = e^n / n^n
- a_n = n^100 / 1.01^n

Hard (10 problems):
- a_n = n! / n^n
- a_n = (1 + 2/n)^n
- a_n = (n^(1/n) - 1) / ln n
- a_n = sin n / n
- a_n = (n/(n+1))^n
- a_n = n^(1/n)
- a_n = arctan n / n
- a_n = (1 + 1/n^2)^n
- a_n = n^n / (3^n * n!)
- a_n = ln(n!) / (n * ln n)

9.2 SERIES TEST PROBLEMS (34 total)
-----------------------------------
Easy (10 problems):
- sum 1/n^2
- sum 1/n
- sum 1/sqrt(n)
- sum (1/2)^n
- sum 2^n
- sum 1/n^3
- sum (3/4)^n
- sum (4/3)^n
- sum 1/n^0.5
- sum 1/n^2.5

Medium (12 problems):
- sum n/(n^2+1)
- sum 1/(n^2+1)
- sum 2^n/(3^n+1)
- sum n^2/2^n
- sum n!/2^n
- sum (-1)^n/n
- integral 1/x^2 dx
- integral 1/x dx
- sum 3^n/n^3
- sum n^3/e^n
- sum (-1)^n/n^2
- sum 1/(n ln n)

Hard (12 problems):
- sum (3^n * n!)/n^n
- sum (n/(n+1))^(n^2)
- sum 1/(n (ln n)^2)
- sum (-1)^n/sqrt(n)
- sum sin n / n^2
- sum n!/n^n
- sum (-1)^n * n/(n^2+1)
- sum 1/n^(1+1/n)
- sum (1 - 1/n)^(n^2)

9.3 POWER SERIES PROBLEMS (14 total)
------------------------------------
- sum x^n
- sum x^n/n!
- sum x^n/n
- sum (-1)^n x^n/n
- sum n x^n
- sum (x-2)^n/3^n
- sum (-1)^n (x+1)^n/sqrt(n)
- sum x^(2n)/n!
- sum x^n/sqrt(n)
- sum (-1)^n x^(2n)/n
- sum (x+3)^n/2^n
- sum n! x^n/n^n
- sum (-1)^n x^(2n+1)/(2n+1)!
- sum (-1)^n x^(2n)/(2n)!

9.4 TAYLOR SERIES PROBLEMS (12 functions)
-----------------------------------------
- e^x
- sin x
- cos x
- ln(1+x)
- arctan x
- 1/(1-x)
- 1/(1+x)
- 1/(1-x^2)
- arctan(x^2)
- sinh x
- cosh x
- 1/(1-x)^2


10. TROUBLESHOOTING
===================

10.1 COMMON ISSUES AND SOLUTIONS

Issue: LaTeX images not rendering
Solution: Ensure matplotlib and Pillow are properly installed:
    pip install --upgrade matplotlib pillow

Issue: Graph window shows blank or error
Solution: Check that matplotlib backend is set to 'TkAgg':
    import matplotlib
    matplotlib.use('TkAgg')

Issue: Application window is too small
Solution: Modify the geometry in main() function:
    root.geometry("1200x900")

Issue: Difficulty dropdown is cut off
Solution: Increase window width or reduce padding on stats frame

Issue: Buttons not responding
Solution: Check that all methods are properly defined in the class

Issue: Emoji display problems on Windows
Solution: Use standard text characters instead of emojis in labels

10.2 DEBUGGING
--------------
To enable debug output, add print statements in methods:
    print(f"Debug: Current question is {self.current_question}")

Common error messages and their meanings:
- "AttributeError: object has no attribute" - Missing method or variable
- "LaTeX rendering error" - Problem with matplotlib LaTeX rendering
- "Graph error" - Issue with graph generation


11. FUTURE ENHANCEMENTS
=======================

Planned features for future versions:

1. Additional problem types:
   - Ratio and root test practice mode
   - Comparison test focused practice
   - Alternating series error estimation

2. Enhanced visualization:
   - Interactive graphs with zoom and pan
   - Side-by-side comparison of sequence and series
   - Animation of partial sums convergence

3. User features:
   - Save/load progress
   - User accounts and statistics
   - Custom problem creation
   - Performance analytics

4. Educational features:
   - Step-by-step solution explanations
   - Hint system with progressive disclosure
   - Video tutorials linked to problems
   - Practice exam mode

5. Technical improvements:
   - Export graphs as images
   - Print problem sets
   - Mobile version
   - Web deployment


================================================================================
                            END OF DOCUMENTATION
================================================================================

Document Version: 1.4
Last Updated: 2024
Author: Michael Perry
Support: For questions or bug reports, refer to the application documentation

================================================================================