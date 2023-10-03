Deadman Switch with Alarm in Python
Overview
This Python application serves as a Deadman Switch with an alarm feature. It is designed for situations where a user wants to reach an alterd state of mind while lying in bed. 
The user starts the application, holds the mouse button to keep it running, and if they fall asleep or release the mouse button, an alarm will be triggered.

Features
Fullscreen display for minimal distractions.
Simple interface with a single button to start/stop the application.
Alarm sound ('TF001.wav') plays continuously when the button is not pressed.
"Exit" button provided for easy termination of the application.
Installation
Clone or download this repository to your computer.
bash
Copy code
git clone https://github.com/yourusername/deadman-switch.git
Install the required Python libraries if you haven't already:
bash
Copy code
pip install pygame pyautogui
Place your alarm sound file ('TF001.wav') in the same directory as the script.
Usage
Run the Python script:
bash
Copy code
python deadman_switch.py
The application will open in fullscreen mode.

Click and hold the mouse button to keep the application running and prevent the alarm from sounding.

If you release the mouse button or fall asleep, the alarm will play.

You can exit the application by clicking the "Exit" button.

Safety Warning
This application is designed for entertainment purposes and should not be used to induce altered states of consciousness or hallucinations. 
Using technology in such a manner can be potentially dangerous and is not advisable. Please prioritize your safety and well-being.

License
This project is licensed under the MIT License.
