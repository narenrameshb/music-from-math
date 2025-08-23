# Demo script for the Mathematical Melody Generator
# Shows examples of different mathematical sequences converted to music

import time
from melody_generator import MelodyGenerator

def run_demo():
    # Run the demo showcasing different mathematical melodies
    print("=" * 60)
    print("           MATHEMATICAL MELODY GENERATOR DEMO")
    print("=" * 60)
    print("This demo will showcase different mathematical sequences")
    print("converted to musical melodies.")
    print("=" * 60)
    
    generator = MelodyGenerator()
    
    # Demo 1: Fibonacci Sequence
    print("\nDEMO 1: Fibonacci Sequence Melody")
    print("-" * 40)
    print("The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13...")
    print("Each number maps to a musical note in the C major scale.")
    
    input("Press Enter to generate and play Fibonacci melody...")
    
    comp1 = generator.generate_fibonacci_melody(
        n=8, tempo=120, scale_type='major', rhythm_pattern='simple'
    )
    
    if comp1:
        print("\nPlaying Fibonacci melody...")
        generator.play_composition(comp1)
        time.sleep(1)  # Wait for melody to finish
        
        # Show composition info
        generator.get_composition_info(comp1)
    
    # Demo 2: Prime Numbers
    print("\nDEMO 2: Prime Numbers Melody")
    print("-" * 40)
    print("Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19...")
    print("Converted to a minor scale for a different mood.")
    
    input("Press Enter to generate and play Prime Numbers melody...")
    
    comp2 = generator.generate_prime_melody(
        n=8, tempo=90, scale_type='minor', rhythm_pattern='waltz'
    )
    
    if comp2:
        print("\nPlaying Prime Numbers melody...")
        generator.play_composition(comp2)
        time.sleep(1)  # Wait for melody to finish
        
        # Show composition info
        generator.get_composition_info(comp2)
    
    # Demo 3: Pi Digits Melody
    print("\nDEMO 3: Pi Digits Melody")
    print("-" * 40)
    print("Pi digits: 3, 1, 4, 1, 5, 9, 2, 6...")
    print("Using pentatonic scale for a folk-like sound.")
    
    input("Press Enter to generate and play Pi Digits melody...")
    
    comp3 = generator.generate_pi_melody(
        n=10, tempo=150, scale_type='pentatonic', rhythm_pattern='march'
    )
    
    if comp3:
        print("\nPlaying Pi Digits melody...")
        generator.play_composition(comp3)
        time.sleep(1)  # Wait for melody to finish
        
        # Show composition info
        generator.get_composition_info(comp3)
    
    # Demo 4: Show saved compositions
    print("\nDEMO 4: Saved Compositions")
    print("-" * 40)
    print("All generated compositions are automatically saved.")
    
    input("Press Enter to view saved compositions...")
    
    generator.list_saved_compositions()
    
    # Final message
    print("\n" + "=" * 60)
    print("DEMO COMPLETED!")
    print("=" * 60)
    print("You've experienced:")
    print("• Fibonacci sequences in major scale")
    print("• Prime numbers in minor scale with waltz rhythm")
    print("• Pi digits in pentatonic scale with march rhythm")
    print("\nAll compositions have been saved and can be:")
    print("• Reloaded and played again")
    print("• Modified with different parameters")
    print("• Deleted if no longer needed")
    print("\nTo explore more options, run: python main.py")
    print("=" * 60)

if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred during demo: {e}")
        print("Please check that all dependencies are installed correctly.")
    
    input("\nPress Enter to exit...")
