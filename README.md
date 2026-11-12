# MyWidowApp
A beginner Python GUI application built with Tkinter. Features a customizable window, user input, and personalized greetings. Demonstrates foundational object-oriented programming concepts, including classes, instances, methods, attributes, and event handling.


# Project 1: Hello World GUI Application

## Overview

This project is a simple graphical user interface (GUI) application built with Python and Tkinter. It allows users to enter their name and receive a personalized greeting when they click the Submit button.

The project introduces the fundamentals of GUI development and object-oriented programming (OOP) in Python.

## Features

- Creates a graphical application window.
- Allows users to customize the window title, background color, and text color.
- Provides a text input field for user input.
- Includes a Submit button to process user input.
- Displays a personalized greeting.
- Provides a message when the input field is empty.

## Technologies Used

- Python 3
- Tkinter (Python GUI library)

## Concepts Practiced

- Importing Python modules
- Creating classes and instances
- Constructors (`__init__`)
- Instance attributes (`self`)
- Methods
- Parameters and arguments
- Tkinter widgets:
  - `Tk()`
  - `Label()`
  - `Entry()`
  - `Button()`
- Event handling and callbacks
- Retrieving user input with `.get()`
- Updating widgets with `.config()`
- Conditional statements (`if/else`)
- String formatting with f-strings
- Starting the GUI event loop with `mainloop()`

## How It Works

The application uses a `MyWindow` class to organize the graphical interface and its functionality.

When an instance of the class is created, the constructor initializes the window and creates the interface components.

The user enters their name into the input field and clicks Submit.

The `greet()` method retrieves the input, checks whether a name was entered, and updates the greeting label accordingly.

The `run()` method starts the Tkinter event loop and keeps the application running.

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open the project in your Python IDE.
4. Run the Python file.

No additional third-party packages are required for standard Python installations that include Tkinter.

## Learning Objective

The primary goal of this project was to move beyond procedural programming and begin organizing application functionality using object-oriented programming.

This project serves as the foundation for more advanced Python projects involving classes, inheritance, polymorphism, and GUI development.

## Project Status

Completed: Initial GUI application with user input and personalized greetings.

Part of a 60-project Python development series.
