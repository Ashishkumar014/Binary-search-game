# Binary-search-game

## Overview

The Binary Search Game is an interactive web application where players guess a randomly generated number between 1 and 1000. The game provides feedback on whether the guessed number is too high or too low and tracks the number of attempts taken to guess correctly. The project uses C++ for backend logic and Flask for the frontend.

## Features

- **Web Interface:** A user-friendly web interface built with HTML and CSS.
- **Guessing Range:** Users guess a number between 1 and 1000.
- **Feedback Mechanism:** The game provides hints if the guess is high or low.
- **Attempt Tracking:** Tracks the number of attempts and displays the result.
- **Animations and Styling:** Enhanced visual appeal with animations and styling.
- **Submit on Enter:** Users can submit their guesses by pressing the "Enter" key.

## Getting Started

### Prerequisites

- **C++ Compiler:** To compile and run the C++ backend logic.
- **Python 3.x:** To run the Flask server.
- **Flask:** Python web framework used for the frontend.
- **Git:** To clone the repository.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/binary-search-game.git
   cd binary-search-game

    Setup the Backend:

        Ensure you have a C++ compiler installed.

        Compile the C++ code:

        bash

    g++ -o game game.cpp

Setup the Frontend:

    Install Flask if you haven't already:

    bash

    pip install Flask

Run the Flask Server:

    Navigate to the project directory where app.py is located and run:

    bash

        python app.py

        The server will start and you can access the game at http://127.0.0.1:5000/.

    Playing the Game:
        Open a web browser and go to http://127.0.0.1:5000/.
        Enter a guess between 1 and 1000 and click "Submit" or press "Enter" to submit your guess.
        The game will provide feedback and track the number of attempts.

Project Structure

    game.cpp: C++ source file containing the game logic.
    app.py: Python Flask server script.
    templates/index.html: HTML file for the game’s frontend.
    static/: Directory for CSS and JavaScript files (if any).

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
License

For any questions or feedback, please contact ashishkumar.nitrr@gmail.com or open an issue in the repository.
