# Introducing the project S.E.R.V.A.N.T OR (Subordinate Entity Rendering Various Applications and Network Tasks)
# Improved GUI version

from tkinter import *
import datetime
import os

from pyttsx3 import init
import pygame
from openai import OpenAI
import pyttsx3
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tkinter import Tk, Entry, Button, Text, LEFT, END
from PIL import Image, ImageTk, ImageSequence
import threading
from playsound import playsound
import webbrowser

class AI:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"  # Replace with your OpenAI API key
        self.message_history = [] 
        self.client = OpenAI()
        self.message_history = []
        self.engine = pyttsx3.init()  # Initialize the speech engine

    def search_web(self, query):
        # Path to the Brave browser executable
        brave_path = 'path_to_brave_browser_executable'  # Replace with the path to the Brave browser executable

        # Path to the ChromeDriver executable
        chromedriver_path = 'path_to_chromedriver_executable'  # Replace with the actual path to ChromeDriver executable
        option = webdriver.ChromeOptions()
        option.binary_location = brave_path
        option.add_argument("--disable-chrome-browser-cloud-management")

        option.add_experimental_option("detach", True)  # This will keep the browser open

        base_url = "https://www.google.com/search?q=" 
        s = Service(chromedriver_path)
        driver = webdriver.Chrome(service=s, options=option)
        url = base_url + query
        driver.get(url)
        
    def play_youtube_video(self, video_id):
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        webbrowser.open(youtube_url)
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def respond(self, command):
        try:
            # Get the current date and time
            now = datetime.datetime.now()

            # Prepare the system message with the current date and time, and the last AI response
            system_message = f"The current date and time is {now}. "
            if self.message_history:
                system_message += f"You said last message: {self.message_history[-1]['content']}"

            # Add your custom system message
            system_message += """
            You are a unique AI designed by me, I live in [your place of living]. When I tell you 'you said past message' or anything similar, your answer should be built based on what I told you that you said. you have been granted a gift; you have the ability to open apps and search the web. When I ask you to open an app, your response shall be 'os.startfile(path_to_app_executable)'. When I ask you to search the web or search for something, your response shall be 'search_web("https://www.google.com/search?q=" + search_query)'. Remember to replace search_query with the actual search query and if I ask you a question that needs a real-time response like what the weather is or what's tomorrow's date, search the web for that without asking me if I would like you to do so.
            """

            self.message_history.append({"role": "user", "content": command})  # Store the user's command in the history
            response = self.client.chat.completions.create (
                model="gpt-3.5-turbo",
                messages=self.message_history + [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": command},
                ]
            )
            ai_suggestion = response.choices[0].message.content
            self.message_history.append({"role": "assistant", "content": ai_suggestion})

            # Check if the AI's response contains a command to open an application
            if "os.startfile" in ai_suggestion:
                app_path = ai_suggestion.split("(")[1].split(")")[0]  # Extract the app path from the response
                os.startfile(app_path)

            # Check if the AI's response contains a command to search the web
            if "search_web" in ai_suggestion:
                query = ai_suggestion.split('("https://www.google.com/search?q=')[1].split('")')[0]
                self.search_web(query)

            print(f"AI suggestion: {ai_suggestion}")  # Print the AI response
            threading.Thread(target=self.speak, args=(ai_suggestion,)).start()  # Speak the AI response in a separate thread

            return ai_suggestion

        except Exception as e:
            return f"An unexpected error occurred: {e}"


class GUI:
    def __init__(self, ai):
        self.ai = ai
        self.window = Tk()
        self.window.title("Your Loyal Servant")
        self.window.configure(bg="#322c24")  # Set background color

        self.entry = Entry(self.window, bg="#555555", fg="white", insertbackground="white")  # Set entry widget colors
        self.button = Button(self.window, text="Ask", command=self.ask, bg="#555555", fg="white")  # Set button colors
        self.clear_button = Button(self.window, text="Clear", command=self.clear_chat, bg="#555555", fg="white")  # Set button colors
        self.entry.focus_set()
        self.mute_button = Button(self.window, text="🔥", command=self.toggle_voice, bg="#555555", fg="white")  # Set button colors and emoji
        self.mute_button.pack(side=LEFT, padx=5, pady=5)  # Position the button beside the ask button

        self.voice_muted = False  # Initialize voice muted variable
        self.text = Text(self.window, bg="#222222", fg="white", wrap=WORD)  # Set text widget colors and enable word wrapping
        self.text.tag_configure('user', foreground='blue')
        self.text.tag_configure('ai', foreground='green')

        # Load the torch gif and resize it
        self.torch_gif = Image.open(r"path_to_torch_gif")  # Replace with the path to the Torch2.gif file
        self.frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.torch_gif)]

        # Create labels to display the torch gif
        self.label_left = Label(self.window, bg="#322c24")
        self.label_right = Label(self.window, bg="#322c24")

        # Start the animation
        self.animate(self.label_left)
        self.animate(self.label_right)

        self.voice_thread = None  

        # Bind the Enter key to the ask function
        self.window.bind('<Return>', self.ask)
        # Bind the Escape key to exit the program
        self.window.bind('<Escape>', self.exit_program)
        # Remove the binding for the "/" key
        # self.window.bind('<slash>', self.start_entry)  # Fix the AttributeError by removing this line

    def start(self):
        self.entry.pack(pady=5)
        self.button.pack(pady=2)
        self.clear_button.pack(pady=2)
        self.label_left.pack(side=LEFT)
        self.text.pack(side=LEFT, padx=5, pady=5)
        self.label_right.pack(side=LEFT)
        self.window.mainloop()

    def ask(self, event=None):
        command = self.entry.get()
        self.text.insert(END, f"You: {command}\n", 'user')
        response = self.ai.respond(command)
        self.text.insert(END, f"AI: {response}\n", 'ai')
        self.entry.delete(0, END)  # Clear the entry field after asking

    def clear_chat(self):
        self.text.delete(1.0, END)  # Clear the chat box

    def animate(self, label, i=0):
        # Resize each frame
        frames = [ImageTk.PhotoImage(frame.resize((frame.width // 4, frame.height // 4), 3)) for frame in ImageSequence.Iterator(self.torch_gif)]
        frame_count = len(frames)
        tk_frame = frames[i]
        label.config(image=tk_frame)
        label.image = tk_frame  # Keep a reference to the image
        i = (i + 1) % frame_count  # Loop over frames
        self.window.after(100, self.animate, label, i)  # Schedule next frame after 100 ms

    def play_voice(self):
        voice_path = r"path_to_voice_file"  # Replace with the path to the fireSound.wav file
        pygame.mixer.init()
        pygame.mixer.music.load(voice_path)
        pygame.mixer.music.set_volume(0.1)  
        try:
            if not self.voice_muted:
                # Create a new thread to play the sound in the background
                voice_thread = threading.Thread(target=pygame.mixer.music.play, args=(-1,))
                voice_thread.start()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            else:
                pygame.mixer.music.stop()  # Stop the sound immediately
        except pygame.error:
            pass

    def start_voice_thread(self):
        if self.voice_thread is None or not self.voice_thread.is_alive():
            self.voice_thread = threading.Thread(target=self.play_voice)
            self.voice_thread.start()