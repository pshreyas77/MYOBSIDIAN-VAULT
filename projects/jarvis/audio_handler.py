#!/usr/bin/env python3
"""
Audio Handler
Speech-to-Text and Text-to-Speech for J.A.R.V.I.S.
"""

import threading
import queue
import time
from typing import Optional, Callable
from config import Config


class AudioHandler:
    """Handle voice input and output"""

    def __init__(self):
        self.voice_enabled = Config.VOICE_ENABLED
        self.tts_enabled = Config.TEXT_TO_SPEECH_ENABLED
        self.speech_rate = Config.SPEECH_RATE
        self.speaking = False
        self.speech_queue = queue.Queue()
        self._init_speech_recognition()
        self._init_tts()

        # Start TTS worker
        if self.tts_enabled:
            self._start_tts_worker()

    def _init_speech_recognition(self):
        """Initialize speech recognition"""
        self.recognizer = None
        self.microphone = None

        if not self.voice_enabled:
            return

        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()

            # Calibrate for ambient noise
            with self.microphone as source:
                print("Calibrating for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Calibration complete")

        except ImportError:
            print("Warning: speech_recognition not installed. Voice input disabled.")
            self.voice_enabled = False
        except Exception as e:
            print(f"Warning: Could not initialize microphone: {e}")
            self.voice_enabled = False

    def _init_tts(self):
        """Initialize text-to-speech"""
        self.tts_engine = None

        if not self.tts_enabled:
            return

        try:
            import pyttsx3
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', self.speech_rate)
            self.tts_engine.setProperty('volume', 0.9)

            # List available voices
            voices = self.tts_engine.getProperty('voices')
            if voices:
                # Prefer a male voice for JARVIS feel
                for voice in voices:
                    if 'male' in voice.name.lower() or 'british' in voice.name.lower():
                        self.tts_engine.setProperty('voice', voice.id)
                        break

        except ImportError:
            print("Warning: pyttsx3 not installed. TTS disabled.")
            self.tts_enabled = False
        except Exception as e:
            print(f"Warning: Could not initialize TTS: {e}")
            self.tts_enabled = False

    def _start_tts_worker(self):
        """Start background thread for TTS"""
        def worker():
            while True:
                try:
                    text = self.speech_queue.get()
                    if text is None:  # Shutdown signal
                        break
                    if self.tts_engine:
                        self.speaking = True
                        self.tts_engine.say(text)
                        self.tts_engine.runAndWait()
                        self.speaking = False
                except Exception as e:
                    self.speaking = False
                    if Config.DEBUG_MODE:
                        print(f"TTS error: {e}")

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
        self._tts_thread = thread

    def listen(self, timeout: int = 5, phrase_time_limit: int = 10) -> Optional[str]:
        """Listen for voice input and return text"""
        if not self.voice_enabled or not self.recognizer:
            return None

        try:
            import speech_recognition as sr

            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                print("Processing speech...")

                # Try Google Speech Recognition (requires internet)
                try:
                    text = self.recognizer.recognize_google(audio)
                    return text
                except sr.UnknownValueError:
                    return None
                except sr.RequestError as e:
                    print(f"Speech recognition error: {e}")
                    return None

        except Exception as e:
            if Config.DEBUG_MODE:
                print(f"Listen error: {e}")
            return None

    def speak(self, text: str, block: bool = False):
        """Text-to-speech output"""
        print(f"{Config.JARVIS_NAME}: {text}")

        if not self.tts_enabled:
            return

        # Add to queue
        self.speech_queue.put(text)

        if block:
            # Wait for speaking to finish (simple implementation)
            while self.speaking or not self.speech_queue.empty():
                time.sleep(0.1)

    def stop_speaking(self):
        """Stop current speech"""
        if self.tts_engine:
            try:
                self.tts_engine.stop()
            except:
                pass

    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'speech_queue'):
            self.speech_queue.put(None)  # Signal worker to exit


class WakeWordDetector:
    """Simple wake word detection using speech recognition"""

    def __init__(self, wake_word: str = None):
        self.wake_word = (wake_word or Config.WAKE_WORD).lower()
        self.audio_handler = AudioHandler()
        self._running = False

    def listen_for_wake_word(self, callback: Callable) -> None:
        """Listen for wake word and trigger callback"""
        self._running = True

        print(f"Wake word listener active. Say '{self.wake_word}' to activate.")

        while self._running:
            text = self.audio_handler.listen(timeout=None)  # Listen indefinitely

            if text:
                text_lower = text.lower()
                print(f"Heard: {text_lower}")

                if self.wake_word in text_lower:
                    print("Wake word detected!")
                    self.audio_handler.speak(f"Yes, {Config.USER_NAME}?")
                    callback()

    def stop(self):
        """Stop listening"""
        self._running = False


if __name__ == "__main__":
    # Test audio handler
    handler = AudioHandler()

    print("Testing TTS...")
    handler.speak("This is a test of the JARVIS audio system.", block=True)

    print("\nTesting speech recognition...")
    print("Say something:")
    text = handler.listen()
    if text:
        print(f"Recognized: {text}")
        handler.speak(f"You said: {text}")
    else:
        print("No speech recognized")