# Hand Cursor Control

This Python script allows you to control the mouse cursor using hand gestures captured through your computer's camera. It utilizes the following libraries:

- OpenCV (cv2): Used for camera input and image processing.
- Mediapipe: Used for hand tracking and landmark detection.
- pynput.mouse: Used for controlling the mouse cursor.

## How It Works

1. The script captures video from your computer's camera (usually the built-in webcam).

2. It uses the `mediapipe` library to detect and track your hand in real-time.

3. When your index finger is extended, the script calculates the position of your finger in the camera view and maps it to the screen as the mouse cursor position.

4. A moving average is applied to smooth out the cursor movement, making it more stable.

5. You can control the cursor by moving your hand in front of the camera. To exit the application, press the 'q' key.

## Setup

1. Make sure you have Python installed on your system.

2. Install the required libraries using pip:

3. Adjust the `monitor_width` and `monitor_height` variables in the code to match your monitor's resolution.

4. Run the script:

5. Use your hand gestures to control the mouse cursor.

## Dependencies

- OpenCV
- Mediapipe
- pynput

## Author

[Your Name]

## License

This project is licensed under the [License Name] License - see the [LICENSE.md](LICENSE.md) file for details.
