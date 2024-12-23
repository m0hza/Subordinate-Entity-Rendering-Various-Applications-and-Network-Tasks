S.E.R.V.A.N.T - Subordinate Entity Rendering Various Applications and Network Tasks
Project Overview
S.E.R.V.A.N.T is an AI-based assistant application designed to perform various tasks using voice and text commands. It leverages OpenAI’s GPT-3.5 for intelligent responses, integrates with web services, and interacts with the local system. This project aims to simplify everyday tasks by creating a customizable assistant capable of web searches, app control, and voice interaction.

The project includes a GUI (Graphical User Interface) powered by Tkinter and can handle a wide range of requests, such as searching the web, playing YouTube videos, opening applications, and responding to user inputs with voice feedback. The system uses a threading mechanism to perform tasks asynchronously, ensuring a smooth user experience.

Features
AI Chatbot Integration: Using OpenAI’s GPT-3.5, the assistant can converse intelligently with the user and handle various inquiries.
Voice Feedback: The assistant can speak responses using pyttsx3 and pygame, providing an interactive experience.
Web Search: The assistant can search the web (Google) based on user queries.
App Control: Ability to open local applications through commands.
GUI: A user-friendly interface using Tkinter that integrates all functionalities.
Customizable: You can modify the assistant’s behavior and functionalities according to your needs.
Installation
To run this project, you'll need the following dependencies:

Tkinter for the graphical interface.
pyttsx3 for text-to-speech functionality.
pygame for audio support.
openai for GPT-3.5 API integration.
Selenium for web search functionality.
Pillow for image handling in the GUI.
Prerequisites
Before running the project, make sure to install the required libraries using pip:

bash
Copy code
pip install pyttsx3 pygame openai selenium Pillow
Additionally, ensure that you have a working installation of the ChromeDriver and a browser (e.g., Brave or Chrome) for web search functionality.

Environment Variables
Set up your OpenAI API key by replacing the placeholder "your_openai_api_key_here" with your actual key.
Provide the path to the Brave browser and ChromeDriver in the relevant sections of the code for web searches to work correctly.
Usage
Run the script to launch the S.E.R.V.A.N.T assistant.
The GUI will appear, allowing you to input commands in the text field.
Press Ask to send your query to the assistant.
The assistant will provide a response in the text box, and you can hear the response if the voice feature is enabled.
Commands like "search web" will trigger web searches using Google, while app-related commands will open applications on your system.
Example Commands
Search the web: "What’s the weather like today?"
Open an app: "Open Notepad"
Play a video: "Play a YouTube video with ID <video_id>"
General Queries: "Tell me a joke."
Code Explanation
AI Class
The AI class is responsible for handling all AI-related tasks, such as:

Responding to User Queries: Using GPT-3.5, it processes user input and provides intelligent responses.
Web Search: If the response requires a web search, it triggers the search_web method, which opens the Brave browser with a search query.
Voice Feedback: The speak method utilizes pyttsx3 to read the response aloud.
GUI Class
The GUI class creates the user interface using Tkinter and handles interactions between the user and the AI:

Text Input: The user can type commands in the text box.
Voice Control: The user can mute or unmute the assistant’s voice via the mute button.
Animation: A torch gif is displayed to enhance the visual appeal.
Threading: The application uses threading to perform background tasks like playing sounds without freezing the interface.
Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests to improve or add new features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Additional Notes:
Replace "your_openai_api_key_here" with your actual OpenAI API key.
Ensure the paths for Brave browser and ChromeDriver executables are correctly set.
If you want to contribute or extend functionality, feel free to open issues or create pull requests.
