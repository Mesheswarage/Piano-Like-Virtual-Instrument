# Piano-Like-Virtual-Instrument
This repository houses an interactive virtual instrument that resembles a piano. While it may not produce sound like a traditional piano just yet, it offers a unique and engaging experience for users interested in exploring the world of digital music creation.And this offers two distinct ways to play music.

1. Keyboard Mode
2. Computer Vision Mode

## Keyboard Mode: 

The keyboard mode allows you to play music using your computer keyboard keys as piano keys. It provides a simple and intuitive way to create melodies. The user-friendly interface and easy key mapping make it accessible to musicians and beginners alike.

### Project Structure

- `piano.py`: This file contains the main functions responsible for mapping keyboard keys to piano keys. It handles the logic for keyboard input and translating it into virtual piano key presses.

- `notesKeys.py`: This file contains lists of white and black piano key names. These lists are used for reference in the project to associate keys with musical notes.



https://github.com/Mesheswarage/Piano-Like-Virtual-Instrument/assets/97176530/02655fc6-312c-4e49-82cb-3d35eb72ac20

## Computer Vision Mode:

The computer vision mode harnesses the power of OpenCV to transform your webcam into a musical instrument. This mode detects hand movements and recognizes gestures to generate musical notes. It's an interactive and unique way to create music by using hand gestures as input.

### Project Structure

- `hand_detection.py`: This file contains functions needed to detect hand gestures. It leverages computer vision techniques,  using OpenCV, to recognize hand movements and gestures, which can then be translated into musical notes.

- `Vpiano.py`: The `Vpiano.py` file contains the main functions responsible for mapping sounds in the `assets` folder to index finger landmarks. It defines the logic for translating hand gestures or keypresses into musical actions. This file serves as the core of the virtual piano interaction.(assets folder is not in the repository)

- `notes.py`: The `notes.py` file includes lists of white and black piano key names. These lists are used as reference guides within the project to associate keys with musical notes.This aids in accurately mapping keyboard inputs or hand gestures to the correct musical notes.



https://github.com/Mesheswarage/Piano-Like-Virtual-Instrument/assets/97176530/301a9d7c-67ad-4295-af9d-2653ee19d7eb

## Key Features:

Enjoy an aesthetically pleasing digital representation of a piano keyboard on your screen.

Use your computer keyboard keys or hand gestures via computer vision (OpenCV) to simulate playing the piano.

See visual cues for key presses or hand gestures to enhance your virtual playing experience


