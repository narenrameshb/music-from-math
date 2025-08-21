"""
Audio engine using winsound for generating musical notes from mathematical sequences.
"""

import winsound
import time
import threading

class AudioEngine:
    def __init__(self):
        """Initialize the audio engine."""
        self.is_playing = False
        self.current_thread = None
        
    def play_note(self, frequency, duration_ms=500):
        """
        Play a single note using winsound.
        
        Args:
            frequency (float): Frequency in Hz
            duration_ms (int): Duration in milliseconds
        """
        try:
            # Convert frequency to integer (winsound requires int)
            freq_int = int(frequency)
            # Ensure frequency is in valid range for winsound
            freq_int = max(37, min(32767, freq_int))
            
            winsound.Beep(freq_int, duration_ms)
        except Exception as e:
            print(f"Error playing note: {e}")
    
    def play_melody(self, notes, tempo=120, note_duration=500, volume=1.0):
        """
        Play a sequence of notes as a melody.
        
        Args:
            notes (list): List of note frequencies
            tempo (int): Tempo in BPM (beats per minute)
            note_duration (int): Duration of each note in milliseconds
            volume (float): Volume multiplier (0.0 to 1.0)
        """
        if self.is_playing:
            print("Already playing a melody. Please wait...")
            return
        
        self.is_playing = True
        
        # Calculate delay between notes based on tempo
        beat_duration = 60000 / tempo  # Convert BPM to milliseconds
        note_delay = beat_duration / 4  # Assume 16th notes for now
        
        def play_sequence():
            try:
                for i, note in enumerate(notes):
                    if not self.is_playing:
                        break
                    
                    # Play the note
                    self.play_note(note, int(note_duration * volume))
                    
                    # Wait before next note (except for the last note)
                    if i < len(notes) - 1:
                        time.sleep(note_delay / 1000.0)
                
                self.is_playing = False
                print("Melody finished playing.")
                
            except Exception as e:
                print(f"Error playing melody: {e}")
                self.is_playing = False
        
        # Start playing in a separate thread
        self.current_thread = threading.Thread(target=play_sequence)
        self.current_thread.daemon = True
        self.current_thread.start()
    
    def stop_melody(self):
        """Stop the currently playing melody."""
        self.is_playing = False
        if self.current_thread and self.current_thread.is_alive():
            self.current_thread.join(timeout=0.1)
        print("Melody stopped.")
    
    def play_sequence_with_rhythm(self, notes, rhythm_pattern=None, tempo=120):
        """
        Play a sequence with a specific rhythm pattern.
        
        Args:
            notes (list): List of note frequencies
            rhythm_pattern (list): List of note durations (in milliseconds)
            tempo (int): Tempo in BPM
        """
        if not rhythm_pattern:
            # Default to equal note durations
            rhythm_pattern = [500] * len(notes)
        
        if len(notes) != len(rhythm_pattern):
            print("Warning: Notes and rhythm pattern have different lengths. Using shorter length.")
            min_length = min(len(notes), len(rhythm_pattern))
            notes = notes[:min_length]
            rhythm_pattern = rhythm_pattern[:min_length]
        
        if self.is_playing:
            print("Already playing a melody. Please wait...")
            return
        
        self.is_playing = True
        
        def play_with_rhythm():
            try:
                for i, (note, duration) in enumerate(zip(notes, rhythm_pattern)):
                    if not self.is_playing:
                        break
                    
                    # Play the note
                    self.play_note(note, duration)
                    
                    # Small pause between notes
                    if i < len(notes) - 1:
                        time.sleep(0.05)
                
                self.is_playing = False
                print("Rhythmic melody finished playing.")
                
            except Exception as e:
                print(f"Error playing rhythmic melody: {e}")
                self.is_playing = False
        
        # Start playing in a separate thread
        self.current_thread = threading.Thread(target=play_with_rhythm)
        self.current_thread.daemon = True
        self.current_thread.start()
    
    def create_rhythm_pattern(self, pattern_type='simple', num_notes=8):
        """
        Create a rhythm pattern for the melody.
        
        Args:
            pattern_type (str): Type of rhythm pattern
            num_notes (int): Number of notes in the pattern
            
        Returns:
            list: List of note durations in milliseconds
        """
        if pattern_type == 'simple':
            # Simple pattern: all notes equal duration
            return [500] * num_notes
        elif pattern_type == 'waltz':
            # Waltz pattern: 3/4 time
            pattern = []
            for i in range(num_notes):
                if i % 3 == 0:
                    pattern.append(800)  # Strong beat
                else:
                    pattern.append(400)  # Weak beat
            return pattern[:num_notes]
        elif pattern_type == 'march':
            # March pattern: 4/4 time
            pattern = []
            for i in range(num_notes):
                if i % 4 == 0:
                    pattern.append(600)  # Strong beat
                elif i % 2 == 0:
                    pattern.append(400)  # Medium beat
                else:
                    pattern.append(200)  # Weak beat
            return pattern[:num_notes]
        else:
            return [500] * num_notes
