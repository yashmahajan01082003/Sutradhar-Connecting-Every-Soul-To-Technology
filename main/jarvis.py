"""
ADVANCED CONVERSATIONAL JARVIS
Interactive | Backend Safe | Django Compatible
"""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import requests
import sys
import traceback
import pyautogui
import pyperclip
import time
import time
import pyautogui
import subprocess

ENGINE_RATE = 170
VOICE_INDEX = 1


class Jarvis:
    """Advanced Voice Assistant with Automation Capabilities."""

    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[VOICE_INDEX].id)
        self.engine.setProperty("rate", ENGINE_RATE)

    # ---------------- SPEAK ----------------
    def speak(self, text: str) -> None:
        """Convert text to speech."""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    # ---------------- LISTEN ----------------
    def listen(self) -> str | None:
        """Listen to user voice input."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio, language="en-in")
            print("User:", query)
            return query.lower()
        except Exception:
            return None

    # ---------------- ASK ----------------
    def ask(self, question: str) -> str | None:
        """Ask user a question and return response."""
        self.speak(question)
        return self.listen()

    # ---------------- GREETING ----------------
    def wish(self) -> None:
        """Greet user based on time."""
        hour = datetime.datetime.now().hour
        if hour < 12:
            self.speak("Good Morning")
        elif hour < 18:
            self.speak("Good Afternoon")
        else:
            self.speak("Good Evening")

        self.speak("I am Jarvis. How can I assist you?")

    # ---------------- TYPE TEXT HELPER ----------------
    def type_text(self, text: str) -> None:
        """Paste text using clipboard for stable automation."""
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")

    # ---------------- AUTONOMOUS FLIGHT AGENT ----------------
    def find_flight(self) -> None:
        """Automate Google Flights using Brave and PyAutoGUI with smart date handling."""

        import time
        import pyautogui
        import subprocess

        source = self.ask("What is your source city?")
        destination = self.ask("What is your destination city?")
        travel_type = self.ask("When do you want to travel? Say today, tomorrow, or other.")

        if not source or not destination or not travel_type:
            self.speak("Missing required details.")
            return

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.4

        self.speak("Opening Brave browser.")

        # Launch Brave
        try:
            subprocess.Popen("brave")
        except Exception:
            subprocess.Popen(
                r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            )

        time.sleep(5)

        # Open Google Flights
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write("https://www.google.com/travel/flights", interval=0.05)
        pyautogui.press("enter")
        time.sleep(7)

        # ---- SOURCE FIELD ----
        for _ in range(8):
            pyautogui.press("tab")

        pyautogui.press("enter")
        time.sleep(1)

        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        pyautogui.write(source, interval=0.05)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)

        # ---- DESTINATION FIELD (2 tabs as you specified) ----
        pyautogui.press("tab")
        pyautogui.press("tab")

        pyautogui.press("enter")
        time.sleep(1)

        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        pyautogui.write(destination, interval=0.05)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)

        # ---- DATE SELECTION (2 tabs after destination) ----
        pyautogui.press("tab")
        pyautogui.press("tab")

        pyautogui.press("enter")
        time.sleep(2)

        # ---- HANDLE DATE LOGIC ----
        travel_type = travel_type.lower()

        if "today" in travel_type:
            # Default date already selected
            pyautogui.press("enter")

        elif "tomorrow" in travel_type:
            pyautogui.press("right")
            pyautogui.press("enter")

        else:
            # Ask specific date details
            day = self.ask("Tell me the date number.")
            month = self.ask("Tell me the month number.")
            year = self.ask("Tell me the year.")

            try:
                day = int(day)
                month = int(month)
                year = int(year)
            except:
                self.speak("Invalid date input.")
                return

            from datetime import datetime

            today = datetime.today()
            target = datetime(year, month, day)

            difference = (target - today).days

            if difference < 0:
                self.speak("That date is in the past.")
                return

            for _ in range(difference):
                pyautogui.press("right")

            pyautogui.press("enter")

        time.sleep(2)

        # ---- NAVIGATE TO SEARCH BUTTON ----
        for _ in range(4):
            pyautogui.press("tab")

        pyautogui.press("enter")

        self.speak("Flight search completed successfully.")
            

    def send_email(self) -> None:
        """Automate Gmail sending using Brave + PyAutoGUI with spoken email conversion."""

        import time
        import pyautogui
        import subprocess

        recipient = self.ask("Who should I send the email to?")
        subject = self.ask("What is the subject?")
        body = self.ask("What should I write in the email?")

        if not recipient or not subject or not body:
            self.speak("Missing email details.")
            return

        # ---- CLEAN & CONVERT SPOKEN EMAIL ----
        recipient = recipient.lower().strip()
        recipient = recipient.replace(" at ", "@")
        recipient = recipient.replace(" dot ", ".")
        recipient = recipient.replace(" ", "")

        self.speak("Opening Gmail.")

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.3

        # ---- OPEN BRAVE ----
        try:
            subprocess.Popen("brave")
        except Exception:
            subprocess.Popen(
                r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            )

        time.sleep(5)

        # ---- OPEN GMAIL ----
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write("https://mail.google.com", interval=0.05)
        pyautogui.press("enter")

        time.sleep(8)

        self.speak("Navigating to compose button.")

        # ---- 13 TABS TO REACH COMPOSE ----
        for _ in range(13):
            pyautogui.press("tab")

        # Open compose window
        pyautogui.press("enter")
        time.sleep(3)

        # ---- RECIPIENT ----
        pyautogui.write(recipient, interval=0.05)
        pyautogui.press("tab")
        pyautogui.press("tab")
        time.sleep(0.5)  # give time for focus to switch

        # ---- SUBJECT ----
        pyautogui.write(subject, interval=0.05)
        pyautogui.press("tab")
        time.sleep(0.5)

        # ---- BODY ----
        pyautogui.write(body, interval=0.03)
        # ---- SEND EMAIL (RELIABLE METHOD) ----
        pyautogui.hotkey("ctrl", "enter")

        self.speak("Email sent successfully.")

    # ---------------- YOUTUBE ----------------
    def play_song(self) -> None:
        song = self.ask("Which song would you like to play?")
        if song:
            self.speak(f"Playing {song} on YouTube")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={song}"
            )

    # ---------------- GOOGLE SEARCH ----------------
    def google_search(self) -> None:
        query = self.ask("What should I search on Google?")
        if query:
            self.speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    # ---------------- SEARCH INSIDE WEBSITE ----------------
    def search_website(self) -> None:
        site = self.ask("Which website should I search on?")
        if not site:
            return

        query = self.ask(f"What should I search on {site}?")
        if not query:
            return

        site = site.lower()

        search_urls = {
            "youtube": f"https://www.youtube.com/results?search_query={query}",
            "google": f"https://www.google.com/search?q={query}",
            "amazon": f"https://www.amazon.in/s?k={query}",
            "wikipedia": f"https://en.wikipedia.org/wiki/{query}",
            "stackoverflow": f"https://stackoverflow.com/search?q={query}",
            "github": f"https://github.com/search?q={query}",
        }

        if site in search_urls:
            self.speak(f"Searching {query} on {site}")
            webbrowser.open(search_urls[site])
        else:
            self.speak("Website not supported. Opening generic search.")
            webbrowser.open(f"https://{site}.com/search?q={query}")

    # ---------------- WIKIPEDIA ----------------
    def wikipedia_search(self) -> None:
        topic = self.ask("What topic should I search on Wikipedia?")
        if topic:
            try:
                result = wikipedia.summary(topic, sentences=2)
                self.speak(result)
            except Exception:
                self.speak("Sorry, I could not find information.")

    # ---------------- WEATHER ----------------
    def get_weather(self) -> None:
        city = self.ask("Which city?")
        if city:
            try:
                api_key = "YOUR_OPENWEATHER_API_KEY"
                url = (
                    f"http://api.openweathermap.org/data/2.5/weather?"
                    f"q={city}&appid={api_key}&units=metric"
                )
                data = requests.get(url, timeout=10).json()

                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]

                self.speak(
                    f"The temperature in {city} is "
                    f"{temp} degree Celsius with {desc}"
                )
            except Exception:
                self.speak("Unable to fetch weather.")

    # ---------------- OPEN WEBSITE ----------------
    def open_website(self) -> None:
        site = self.ask("Which website should I open?")
        if site:
            self.speak(f"Opening {site}")
            webbrowser.open(f"https://{site}")

    # ---------------- SCREENSHOT ----------------
    def take_screenshot(self) -> None:
        filename = (
            f"screenshot_{datetime.datetime.now().strftime('%H%M%S')}.png"
        )
        pyautogui.screenshot(filename)
        self.speak("Screenshot taken and saved.")

    # ---------------- OPEN APPLICATION ----------------
    def open_application(self) -> None:
        app = self.ask("Which application should I open?")
        if not app:
            return

        if "notepad" in app:
            os.system("notepad")
        elif "chrome" in app:
            os.system("start chrome")
        elif "vscode" in app or "visual studio" in app:
            os.system("code")
        else:
            self.speak("Application not found.")

    # ---------------- TIME ----------------
    def tell_time(self) -> None:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.speak(f"The time is {current_time}")

    # ---------------- DATE ----------------
    def tell_date(self) -> None:
        today = datetime.datetime.now().strftime("%d %B %Y")
        self.speak(f"Today is {today}")

    # ---------------- JOKE ----------------
    def tell_joke(self) -> None:
        self.speak(pyjokes.get_joke())

    # ---------------- SHUTDOWN ----------------
    def shutdown(self) -> None:
        confirm = self.ask("Are you sure you want to shut down?")
        if confirm and "yes" in confirm:
            self.speak("Shutting down system")
            os.system("shutdown /s /t 5")

    # ---------------- COMMAND HANDLER ----------------
    def handle_command(self, query: str) -> None:
        if not query:
            return

        if "flight" in query:
            self.find_flight()

        elif "play" in query:
            self.play_song()

        elif "search" in query and "on" in query:
            self.search_website()

        elif "search" in query:
            self.google_search()

        elif "wikipedia" in query:
            self.wikipedia_search()

        elif "weather" in query:
            self.get_weather()

        elif "open website" in query:
            self.open_website()

        elif "open application" in query:
            self.open_application()

        elif "time" in query:
            self.tell_time()

        elif "date" in query:
            self.tell_date()

        elif "joke" in query:
            self.tell_joke()

        elif "screenshot" in query:
            self.take_screenshot()

        elif "shutdown" in query:
            self.shutdown()
        elif "send email" in query:
            self.send_email()
        elif "exit" in query or "stop" in query:
            self.speak("Goodbye")
            sys.exit()

        else:
            self.speak("I did not understand that command.")

    # ---------------- RUN ----------------
    def run(self) -> None:
        self.wish()
        active = True

        while True:
            try:
                query = self.listen()

                if not query:
                    continue

                if not active:
                    if "wake up jarvis" in query:
                        self.speak("I am back online.")
                        active = True
                    continue

                if "sleep" in query:
                    self.speak("Going to sleep.")
                    active = False
                    continue

                self.handle_command(query)

            except Exception as error:
                print("Error:", error)
                traceback.print_exc()


if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()