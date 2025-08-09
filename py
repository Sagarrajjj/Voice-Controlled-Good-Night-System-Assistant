#Skills Used:
#Python Programming
#Window Management (pygetwindow library for interacting with windows)
#Speech Recognition (speech_recognition library for listening to voice commands)
#Time Management (time module for adding delays)
#Operating System Interaction (os module for initiating system shutdown)
#Basic Error Handling (try...except blocks)
#Continuous Looping for Command Listening
import pygetwindow as gw
import time
import speech_recognition as sr
import os

def close_all_windows_except_current():
    # Get the current active window
    current_window = gw.getActiveWindow()

    if current_window is None:
        print("No active window found.")
        return

    current_title = current_window.title
    print(f"Current active window: {current_title}")

    # Get all open windows
    all_windows = gw.getAllTitles()

    # Close all windows except the current active window
    for title in all_windows:
        if title != current_title:
            try:
                print(f"Closing window: {title}")
                window = gw.getWindowsWithTitle(title)[0]
                window.close()
                time.sleep(0.5)  # Optional: Add a small delay between closing windows
            except Exception as e:
                print(f"Failed to close window: {title}, Error: {e}")

def listen_for_command():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")

        # Check for specific commands
        if "good night" in command:
            print("Good night! Closing all windows except current.")
            close_all_windows_except_current()
            time.sleep(9)  # Wait for 9 seconds before shutdown
            print("Shutting down...")
            os.system("shutdown /s /t 1")  # Initiates shutdown with a 1-second delay
        else:
            print("Command not recognized.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error fetching results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:
        listen_for_command()
