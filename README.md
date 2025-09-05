Wikipedia Assistant

A Python-based voice-enabled assistant that allows users to search Wikipedia, listen to summaries, and interact through both text and speech.
It integrates speech recognition, text-to-speech (TTS), and the Wikipedia API to create a hands-free knowledge tool.

Features
	•	Voice Input – Speak your topic instead of typing.
	•	Wikipedia Integration – Fetches concise summaries using the wikipedia library.
	•	Text-to-Speech Output – Uses pyttsx3 to read out search results.
	•	Ambient Noise Adjustment – Automatically optimizes speech recognition in noisy environments.
	•	Error Handling – Handles unknown topics, speech recognition issues, and Wikipedia errors gracefully.
	•	Text Fallback – If you prefer, you can type your topic instead of speaking.

Modules Used

pyttsx3: Text-to-speech conversion
speech_recognition: Captures and processes voice input
wikipedia: Fetches Wikipedia summaries
time: Adds delays for smoother interactions

Installation

1. Clone the Repository:
  git clone https://github.com/AaryanD762/WikipediaAssistant.git
  cd WikipediaAssistant
2. Create a Virtual Environment (Recommended)
   python -m venv venv
  source venv/bin/activate  # On macOS/Linux
  venv\Scripts\activate     # On Windows
3. Install Dependencies
   pip install pyttsx3 speechrecognition wikipedia
Note:
On some systems, you may need to install PyAudio separately:
  pip install pipwin
  pipwin install pyaudio

Usage

Run the Script:

python main.py

How It Works
	1.	The assistant asks whether you want to type or speak your topic.
	2.	If speaking, you have 10 seconds to say your topic.
	3.	It confirms what it heard.
	4.	Optionally, you can specify a category (e.g., Science, History).
	5.	The assistant fetches the Wikipedia summary.
	6.	It prints the result and reads it aloud.

Example

Type your topic or Press Enter to speak:
> (Press Enter)

Say your topic! You have 10 seconds.
> "Albert Einstein"

I heard Albert Einstein, is that correct? (yes/no)
> yes

Type which category your topic is in for a better result:
> Physics

[Assistant speaks and prints]
"Albert Einstein was a German-born theoretical physicist widely acknowledged
to be one of the greatest and most influential physicists of all time..."

Common Issues & Fixes

Microphone Not Detected
	•	Check that your microphone is properly connected.
	•	Update your microphone device index in the code if necessary.

No Voice Output
	•	Ensure that pyttsx3 is installed correctly.
	•	Try switching to another available voice in the code.

Wikipedia Disambiguation Errors
	•	If a topic has multiple meanings, try adding a category when prompted.

⸻

Future Improvements
	•	Add multilingual support.
	•	Integrate voice-based confirmation instead of typing “yes” or “no”.
	•	Create a GUI for better user interaction.
	•	Cache frequent searches for offline mode.

⸻

License

This project is licensed under the MIT License – feel free to modify and distribute.

Author

Aaryan Diwan

aaryandiwan762@gmail.com
