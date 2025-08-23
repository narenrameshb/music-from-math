# Main melody generator that combines mathematical sequences with audio generation

from math_sequences import (
    generate_fibonacci, generate_primes, generate_pi_digits, sequence_to_notes
)
from audio_engine import AudioEngine
from composition import CompositionManager

class MelodyGenerator:
    def __init__(self):
        # Initialize the melody generator
        self.audio_engine = AudioEngine()
        self.composition_manager = CompositionManager()
        self.current_composition = None
        
    def generate_fibonacci_melody(self, n=10, tempo=120, scale_type='major', 
                                 rhythm_pattern='simple', save=True):
        # Generate and play a Fibonacci sequence melody
        # n: number of Fibonacci numbers to use
        # tempo: tempo in BPM
        # scale_type: musical scale type
        # rhythm_pattern: rhythm pattern type
        # save: whether to save the composition
        # returns: generated composition
        print(f"Generating Fibonacci melody with {n} numbers...")
        
        # Generate Fibonacci sequence
        fib_seq = generate_fibonacci(n)
        print(f"Fibonacci sequence: {fib_seq}")
        
        # Convert to musical notes
        notes = sequence_to_notes(fib_seq, scale_type)
        print(f"Generated {len(notes)} musical notes")
        
        # Create composition
        comp_name = f"Fibonacci_{n}_Notes"
        comp = self.composition_manager.create_composition_from_sequence(
            comp_name, "fibonacci", notes, tempo, scale_type, rhythm_pattern
        )
        
        if comp and save:
            self.current_composition = comp
            print(f"Composition '{comp.name}' created and saved.")
        
        return comp
    
    def generate_prime_melody(self, n=10, tempo=120, scale_type='major', 
                             rhythm_pattern='simple', save=True):
        # Generate and play a prime numbers melody
        # n: number of prime numbers to use
        # tempo: tempo in BPM
        # scale_type: musical scale type
        # rhythm_pattern: rhythm pattern type
        # save: whether to save the composition
        # returns: generated composition
        print(f"Generating prime numbers melody with {n} numbers...")
        
        # Generate prime numbers
        prime_seq = generate_primes(n)
        print(f"Prime sequence: {prime_seq}")
        
        # Convert to musical notes
        notes = sequence_to_notes(prime_seq, scale_type)
        print(f"Generated {len(notes)} musical notes")
        
        # Create composition
        comp_name = f"Primes_{n}_Numbers"
        comp = self.composition_manager.create_composition_from_sequence(
            comp_name, "primes", notes, tempo, scale_type, rhythm_pattern
        )
        
        if comp and save:
            self.current_composition = comp
            print(f"Composition '{comp.name}' created and saved.")
        
        return comp
    
    def generate_pi_melody(self, n=20, tempo=120, scale_type='major', 
                           rhythm_pattern='simple', save=True):
        # Generate and play a pi digits melody
        # n: number of pi digits to use
        # tempo: tempo in BPM
        # scale_type: musical scale type
        # rhythm_pattern: rhythm pattern type
        # save: whether to save the composition
        # returns: generated composition
        print(f"Generating pi digits melody with {n} digits...")
        
        # Generate pi digits
        pi_digits = generate_pi_digits(n)
        print(f"Pi digits: {pi_digits}")
        
        # Convert to musical notes
        notes = sequence_to_notes(pi_digits, scale_type)
        print(f"Generated {len(notes)} musical notes")
        
        # Create composition
        comp_name = f"Pi_{n}_Digits"
        comp = self.composition_manager.create_composition_from_sequence(
            comp_name, "pi", notes, tempo, scale_type, rhythm_pattern
        )
        
        if comp and save:
            self.current_composition = comp
            print(f"Composition '{comp.name}' created and saved.")
        
        return comp
    
    def play_composition(self, composition=None, use_rhythm=True):
        # Play a composition
        # composition: composition to play (uses current if None)
        # use_rhythm: whether to use rhythm patterns
        if composition is None:
            composition = self.current_composition
        
        if composition is None:
            print("No composition to play. Generate one first.")
            return
        
        print(f"Playing composition: {composition.name}")
        print(f"Sequence type: {composition.sequence_type}")
        print(f"Tempo: {composition.tempo} BPM")
        print(f"Scale: {composition.scale_type}")
        print(f"Rhythm: {composition.rhythm_pattern}")
        
        if use_rhythm:
            # Create rhythm pattern
            rhythm_pattern = self.audio_engine.create_rhythm_pattern(
                composition.rhythm_pattern, len(composition.notes)
            )
            self.audio_engine.play_sequence_with_rhythm(
                composition.notes, rhythm_pattern, composition.tempo
            )
        else:
            # Play with simple timing
            self.audio_engine.play_melody(
                composition.notes, 
                composition.tempo, 
                500,  # Default note duration
                1.0   # Default volume
            )
    
    def stop_playing(self):
        # Stop the currently playing melody
        self.audio_engine.stop_melody()
    
    def list_saved_compositions(self):
        # List all saved compositions
        compositions = self.composition_manager.list_compositions()
        
        if not compositions:
            print("No saved compositions found.")
            return
        
        print("\nSaved Compositions:")
        print("-" * 50)
        for i, comp in enumerate(compositions, 1):
            print(f"{i}. {comp['name']}")
            print(f"   Type: {comp['sequence_type']}")
            print(f"   Tempo: {comp['tempo']} BPM")
            print(f"   Scale: {comp['scale_type']}")
            print(f"   Notes: {len(comp['notes'])}")
            print(f"   Created: {comp['created_date'][:10]}")
            print()
    
    def load_composition(self, filename):
        # Load a composition from file
        # filename: name of the file to load
        # returns: loaded composition or None if failed
        composition = self.composition_manager.load_composition(filename)
        if composition:
            self.current_composition = composition
        return composition
    
    def delete_composition(self, name):
        # Delete a composition
        # name: name of the composition to delete
        # returns: True if successful, False otherwise
        return self.composition_manager.delete_composition(name)
    
    def get_composition_info(self, composition=None):
        # Get information about a composition
        # composition: composition to get info for (uses current if None)
        if composition is None:
            composition = self.current_composition
        
        if composition is None:
            print("No composition loaded.")
            return
        
        print(f"\nComposition Information:")
        print("-" * 30)
        print(f"Name: {composition.name}")
        print(f"Sequence Type: {composition.sequence_type}")
        print(f"Number of Notes: {len(composition.notes)}")
        print(f"Tempo: {composition.tempo} BPM")
        print(f"Scale: {composition.scale_type}")
        print(f"Rhythm Pattern: {composition.rhythm_pattern}")
        print(f"Created: {composition.created_date[:19]}")
        print(f"Modified: {composition.modified_date[:19]}")
        
        # Show first few notes
        if composition.notes:
            print(f"\nFirst 10 notes (frequencies in Hz):")
            for i, note in enumerate(composition.notes[:10]):
                print(f"  Note {i+1}: {note:.2f} Hz")
            if len(composition.notes) > 10:
                print(f"  ... and {len(composition.notes) - 10} more notes")
