# VirtualAssistant-Oreo
# Oreo: Your Personal Assistant
Oreo is a Python-based virtual personal assistant designed to perform various tasks and engage in conversations with users. 
This project showcases my proficiency in the Python programming language. With Oreo, you can easily control your computer, 
interact with popular websites, get the current time, and engage in conversations.

## Features

### 1. Speech Recognition and Text-to-Speech
Oreo utilizes the `speech_recognition` library to recognize and interpret spoken commands from the user. It can understand
and respond to various voice inputs.

### 2. Web Interaction
You can instruct Oreo to open various websites such as YouTube, Google, Instagram, Wikipedia, GitHub, Stack Overflow, Amazon,
and LinkedIn. Just say "open [website name]" and watch Oreo seamlessly open your preferred site in your default web browser.

### 3. File Explorer Access
Oreo can launch the Windows File Explorer to a specific directory of your choice. Simply mention "file explorer" in your command,
and Oreo will open the specified directory using the `subprocess` module.

### 4. Current Time
Ask Oreo about the current time, and it will promptly respond with the accurate time using the `datetime` module.

### 5. Greetings
Oreo knows the appropriate greetings based on the time of day. It will greet you with a tailored message depending on whether 
it's morning, afternoon, or night.

### 6. Engaging Conversations
Oreo uses the OpenAI API to engage in conversations. Feel free to chat with Oreo on various topics, and it will provide relevant 
responses based on the provided prompts.

## Getting Started
1. Ensure you have Python installed on your system.
2. Install the required libraries using the following command:

   ```
   pip install speech_recognition pyttsx3 openai
   ```
3. Set up your OpenAI API key by placing it in the `APIKEY` variable within the `myapi.py` file.

4. Run the `main.py` script to start interacting with Oreo. You can speak your commands, and Oreo will respond accordingly.

## Usage

1. Open websites: Say "open [website name]" to open various websites.
2. Access File Explorer: Mention "file explorer" to open the Windows File Explorer.
3. Check the time: Ask "what's the time" or "what is the time" to get the current time.
4. Greetings: Oreo will greet you with appropriate messages based on the time of day.
5. Conversations: Engage in conversations with Oreo by asking questions or providing prompts.

## Acknowledgements

This project is brought to you by xq_ankit. Special thanks to the developers of the `speech_recognition`, `pyttsx3`, and 
OpenAI libraries.

## Contributions

Contributions to this project are welcome. Feel free to fork the repository, make improvements, and submit pull requests.

## Contact

For any inquiries or feedback, please contact guptankit1712004@gmail.com.

---

**Note:** This project is for demonstration purposes and may require additional setup and customization to suit your environment 
and preferences. Make sure to review and modify the code as needed before using it in a production environment.
