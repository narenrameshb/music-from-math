"""
Complex Demonstration of the Mathematical Melody Generator
Creates a full musical composition using multiple mathematical sequences
and advanced features to showcase the project's capabilities.
"""

import time
import threading
from melody_generator import MelodyGenerator
from math_sequences import generate_fibonacci, generate_primes, generate_pi_digits, sequence_to_notes

class ComplexComposition:
    """A complex musical composition using multiple mathematical sequences."""
    
    def __init__(self):
        self.generator = MelodyGenerator()
        self.compositions = []
        
    def create_fibonacci_theme(self, n=12, tempo=120, scale_type='major'):
        """Create a Fibonacci-based musical theme."""
        print("🎵 Creating Fibonacci Theme...")
        
        # Generate Fibonacci sequence with more numbers for variety
        fib_sequence = generate_fibonacci(n)
        print(f"Fibonacci sequence: {fib_sequence}")
        
        # Convert to musical notes
        notes = sequence_to_notes(fib_sequence, scale_type)
        
        # Create composition
        comp = self.generator.composition_manager.create_composition_from_sequence(
            f"Fibonacci_Theme_{n}_Notes", "fibonacci", notes, tempo, scale_type, "waltz"
        )
        
        if comp:
            self.compositions.append(comp)
            print(f"✓ Fibonacci theme created with {len(notes)} notes")
            return comp
        return None
    
    def create_prime_counterpoint(self, n=15, tempo=90, scale_type='minor'):
        """Create a prime numbers counterpoint melody."""
        print("🎵 Creating Prime Numbers Counterpoint...")
        
        # Generate prime numbers
        prime_sequence = generate_primes(n)
        print(f"Prime sequence: {prime_sequence}")
        
        # Convert to musical notes
        notes = sequence_to_notes(prime_sequence, scale_type)
        
        # Create composition
        comp = self.generator.composition_manager.create_composition_from_sequence(
            f"Prime_Counterpoint_{n}_Numbers", "primes", notes, tempo, scale_type, "march"
        )
        
        if comp:
            self.compositions.append(comp)
            print(f"✓ Prime counterpoint created with {len(notes)} notes")
            return comp
        return None
    
    def create_pi_bridge(self, n=20, tempo=150, scale_type='pentatonic'):
        """Create a pi digits bridge section."""
        print("🎵 Creating Pi Digits Bridge...")
        
        # Generate pi digits
        pi_sequence = generate_pi_digits(n)
        print(f"Pi digits: {pi_sequence}")
        
        # Convert to musical notes
        notes = sequence_to_notes(pi_sequence, scale_type)
        
        # Create composition
        comp = self.generator.composition_manager.create_composition_from_sequence(
            f"Pi_Bridge_{n}_Digits", "pi", notes, tempo, scale_type, "simple"
        )
        
        if comp:
            self.compositions.append(comp)
            print(f"✓ Pi bridge created with {len(notes)} notes")
            return comp
        return None
    
    def create_fibonacci_variation(self, n=8, tempo=180, scale_type='major'):
        """Create a fast Fibonacci variation."""
        print("🎵 Creating Fibonacci Variation (Fast)...")
        
        # Generate Fibonacci sequence
        fib_sequence = generate_fibonacci(n)
        
        # Convert to musical notes
        notes = sequence_to_notes(fib_sequence, scale_type)
        
        # Create composition
        comp = self.generator.composition_manager.create_composition_from_sequence(
            f"Fibonacci_Variation_{n}_Notes", "fibonacci", notes, tempo, scale_type, "march"
        )
        
        if comp:
            self.compositions.append(comp)
            print(f"✓ Fibonacci variation created with {len(notes)} notes")
            return comp
        return None
    
    def create_prime_finale(self, n=10, tempo=60, scale_type='minor'):
        """Create a slow, dramatic prime numbers finale."""
        print("🎵 Creating Prime Numbers Finale...")
        
        # Generate prime numbers
        prime_sequence = generate_primes(n)
        
        # Convert to musical notes
        notes = sequence_to_notes(prime_sequence, scale_type)
        
        # Create composition
        comp = self.generator.composition_manager.create_composition_from_sequence(
            f"Prime_Finale_{n}_Numbers", "primes", notes, tempo, scale_type, "waltz"
        )
        
        if comp:
            self.compositions.append(comp)
            print(f"✓ Prime finale created with {len(notes)} notes")
            return comp
        return None
    
    def play_composition_sequence(self, delay_between=2):
        """Play all compositions in sequence with delays."""
        if not self.compositions:
            print("No compositions to play!")
            return
        
        print(f"\n🎼 Playing Complete Mathematical Symphony...")
        print(f"Total movements: {len(self.compositions)}")
        print("=" * 60)
        
        for i, comp in enumerate(self.compositions, 1):
            print(f"\n🎵 Movement {i}: {comp.name}")
            print(f"   Type: {comp.sequence_type}")
            print(f"   Tempo: {comp.tempo} BPM")
            print(f"   Scale: {comp.scale_type}")
            print(f"   Rhythm: {comp.rhythm_pattern}")
            print(f"   Notes: {len(comp.notes)}")
            
            # Play the composition
            print(f"   🎵 Playing {comp.name}...")
            self.generator.play_composition(comp)
            
            # Calculate wait time based on number of notes and tempo
            # Each note typically plays for about 0.5 seconds
            estimated_duration = len(comp.notes) * 0.5
            print(f"   ⏱️  Estimated duration: {estimated_duration:.1f} seconds")
            
            # Wait for the composition to finish
            time.sleep(estimated_duration + 1)  # Add buffer time
            
            # Small pause between movements
            if i < len(self.compositions):
                print(f"\n⏸️  Pause between movements...")
                time.sleep(delay_between)
        
        print("\n🎉 Mathematical Symphony Complete!")
    
    def create_symphony_summary(self):
        """Display a summary of the complete symphony."""
        print("\n" + "=" * 80)
        print("                    MATHEMATICAL SYMPHONY SUMMARY")
        print("=" * 80)
        
        total_notes = sum(len(comp.notes) for comp in self.compositions)
        total_duration = sum(len(comp.notes) * 0.5 for comp in self.compositions)  # Rough estimate
        
        print(f"🎼 Complete Symphony: 'Mathematical Harmony in Numbers'")
        print(f"📊 Total Movements: {len(self.compositions)}")
        print(f"🎵 Total Notes: {total_notes}")
        print(f"⏱️  Estimated Duration: {total_duration:.1f} seconds")
        print("\n📝 Movement Breakdown:")
        
        for i, comp in enumerate(self.compositions, 1):
            print(f"   {i}. {comp.name}")
            print(f"      Mathematical Basis: {comp.sequence_type}")
            print(f"      Musical Character: {comp.scale_type} scale, {comp.rhythm_pattern} rhythm")
            print(f"      Tempo: {comp.tempo} BPM")
            print(f"      Notes: {len(comp.notes)}")
            print()
        
        print("🎭 Musical Structure:")
        print("   • Movement 1: Fibonacci Theme (Majestic opening)")
        print("   • Movement 2: Prime Counterpoint (Contrasting middle)")
        print("   • Movement 3: Pi Bridge (Transitional section)")
        print("   • Movement 4: Fibonacci Variation (Energetic development)")
        print("   • Movement 5: Prime Finale (Dramatic conclusion)")
        print("\n🔬 Mathematical Concepts Demonstrated:")
        print("   • Number Theory (Prime number generation)")
        print("   • Sequences (Fibonacci progression)")
        print("   • Irrational Numbers (Pi digits)")
        print("   • Modular Arithmetic (Note mapping)")
        print("   • Frequency Calculation (Audio generation)")
        
        print("=" * 80)
    
    def save_symphony(self):
        """Save all compositions as a complete symphony."""
        print("\n💾 Saving Complete Symphony...")
        
        for comp in self.compositions:
            print(f"   ✓ {comp.name} saved")
        
        print(f"\n🎼 Symphony saved! You can reload individual movements using the main application.")
        print("   Run 'python main.py' and use option 7 to load compositions.")
    
    def interactive_demo(self):
        """Run an interactive demonstration of the symphony creation."""
        print("=" * 80)
        print("           INTERACTIVE MATHEMATICAL SYMPHONY CREATOR")
        print("=" * 80)
        print("This demo will create a complete musical composition using")
        print("multiple mathematical sequences, showcasing the full capabilities")
        print("of the Mathematical Melody Generator.")
        print("=" * 80)
        
        input("Press Enter to begin creating your mathematical symphony...")
        
        # Create all movements
        print("\n🎼 Creating Symphony Movements...")
        print("-" * 50)
        
        # Movement 1: Fibonacci Theme
        self.create_fibonacci_theme(12, 120, 'major')
        input("\nPress Enter to continue to next movement...")
        
        # Movement 2: Prime Counterpoint
        self.create_prime_counterpoint(15, 90, 'minor')
        input("\nPress Enter to continue to next movement...")
        
        # Movement 3: Pi Bridge
        self.create_pi_bridge(20, 150, 'pentatonic')
        input("\nPress Enter to continue to next movement...")
        
        # Movement 4: Fibonacci Variation
        self.create_fibonacci_variation(8, 180, 'major')
        input("\nPress Enter to continue to next movement...")
        
        # Movement 5: Prime Finale
        self.create_prime_finale(10, 60, 'minor')
        
        # Show summary
        self.create_symphony_summary()
        
        # Ask if user wants to hear the complete symphony
        print("\n🎵 Would you like to hear the complete mathematical symphony?")
        print("   This will play all movements in sequence.")
        
        play_choice = input("Play complete symphony? (y/n): ").lower().strip()
        if play_choice in ['y', 'yes']:
            print("\n🎼 Prepare for a mathematical musical journey...")
            input("Press Enter when ready to begin the symphony...")
            self.play_composition_sequence()
        else:
            print("\n🎼 Symphony movements created! You can play them individually using the main application.")
        
        # Save the symphony
        self.save_symphony()
        
        print("\n🎉 Interactive Demo Complete!")
        print("You've created a full mathematical symphony with 5 movements!")
        print("\nTo explore more options:")
        print("   • Run 'python main.py' for the full application")
        print("   • Run 'python demo.py' for basic examples")
        print("   • Load and play your saved compositions")

def run_complex_demo():
    """Run the complex demonstration."""
    try:
        symphony = ComplexComposition()
        symphony.interactive_demo()
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred during demo: {e}")
        print("Please check that all dependencies are installed correctly.")

def quick_audio_test():
    """Quick test to verify audio is working."""
    print("🎵 Quick Audio Test - Creating and playing a simple Fibonacci melody...")
    
    try:
        symphony = ComplexComposition()
        
        # Create a simple Fibonacci theme
        comp = symphony.create_fibonacci_theme(6, 120, 'major')
        
        if comp:
            print(f"\n✓ Created composition: {comp.name}")
            print(f"   Notes: {len(comp.notes)}")
            print(f"   Frequencies: {[f'{note:.1f} Hz' for note in comp.notes[:5]]}...")
            
            # Play it
            print("\n🎵 Playing the melody...")
            symphony.generator.play_composition(comp)
            
            # Wait for it to finish
            estimated_duration = len(comp.notes) * 0.5
            print(f"⏱️  Playing for approximately {estimated_duration:.1f} seconds...")
            time.sleep(estimated_duration + 1)
            
            print("✅ Audio test completed! If you heard the melody, audio is working correctly.")
        else:
            print("❌ Failed to create composition")
            
    except Exception as e:
        print(f"❌ Audio test failed: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        quick_audio_test()
    else:
        run_complex_demo()
