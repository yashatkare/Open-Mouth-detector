# Real-time Mouth Recognition with OpenCV

This project implements real-time mouth recognition using OpenCV. It detects mouths in a video stream from the default camera and applies visual markers on the edges of the detected mouth. It also applies a filter effect to differentiate when the mouth is opened wider than a specified threshold.

## Usage

1. Make sure you have Python and OpenCV installed.
2. Clone this repository.
3. Install the required dependencies using the command `pip install -r requirements.txt`.
4. Run the script `mouth_recognition.py` using the command `python mouth_recognition.py`.
5. A video window will open showing the live camera stream with mouth detection.
6. Press 'q' to quit the script.

## Requirements

- Python 3.7 or higher
- OpenCV 4.5.3 or compatible version (install via `pip install opencv-python==4.5.3.56`)

## Customization

- Adjust the `frame_width` and `frame_height` variables in the code to set the desired video frame size.
- Customize the `mouth_open_threshold` value to change the threshold for detecting an open mouth.

## Notes

- The `haarcascade_mouth.xml` file is required for mouth detection. Please ensure that you have a valid Haar cascade XML file for mouth detection and update the code accordingly.
- The accuracy of mouth detection may vary depending on factors such as lighting conditions and the quality of the input video stream.

Feel free to explore and modify the code to suit your specific needs!

