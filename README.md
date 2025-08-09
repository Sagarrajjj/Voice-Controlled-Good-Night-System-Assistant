Voice-Controlled "Good Night" System Assistant
This project is a Python script that functions as a simple, voice-activated assistant for Windows. It is designed to listen for a specific command, "good night", and then automate a sequence of actions to prepare your computer for shutdown. This project demonstrates skills in voice recognition and system automation for a focused and practical use case.

Key Features
Voice-Activated Trigger: The script continuously listens for the phrase "good night" to initiate a series of actions.

Window Management: It automatically closes all open application windows, with the exception of the current active window.

System Shutdown: After a short, 9-second delay, the script safely initiates a system shutdown.

Continuous Listening: The program runs in a continuous loop, always ready to receive the voice command.

Skills Demonstrated
Python Programming

Window Management (pygetwindow library)

Speech Recognition (speech_recognition library)

Operating System Interaction (os module)

Basic Error Handling

Continuous Looping for Command Listening

Prerequisites
To run this project, you will need Python installed on your system.

Python Libraries
You can install all the required Python packages using pip:

pip install pygetwindow SpeechRecognition pyaudio

Note: pyaudio is a dependency of speech_recognition that is required to access your microphone on most systems.

System Requirements
This project is designed specifically for Windows systems as the os.system("shutdown /s /t 1") command is a Windows-specific command.

How to Use
Clone the Repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Run the Script:
Execute the Python script from your terminal:

python your_script_name.py

Give the Command:
The program will print "Listening for command..." in the terminal. When you are ready, simply say the phrase "good night" clearly.

The script will then:

Print a message confirming the command.

Begin closing all open windows except the one currently in focus.

Wait for 9 seconds.

Initiate a system shutdown.

Troubleshooting
ModuleNotFoundError: Ensure all the required libraries (pygetwindow, SpeechRecognition, pyaudio) are installed correctly.

No module named '_portaudio': This error can occur when installing pyaudio. You may need to install the PortAudio library on your system first.

Command not recognized: Make sure your microphone is working correctly and your voice is clear. The Google Speech Recognition API requires an internet connection to work.

Shutdown fails: Check that the command shutdown /s /t 1 is valid on your version of Windows.
