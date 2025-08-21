"""
Automatic Mathematical Symphony Player
Creates and plays a complete mathematical symphony automatically.
No user input required - just run and listen!
"""

import time
from complex_demo import ComplexComposition

def play_automatic_symphony():
    """Create and play a complete mathematical symphony automatically."""
    print("=" * 80)
    print("           AUTOMATIC MATHEMATICAL SYMPHONY")
    print("=" * 80)
    print("Creating and playing a complete mathematical symphony...")
    print("Sit back, relax, and enjoy the mathematical music!")
    print("=" * 80)
    
    try:
        # Create the symphony
        symphony = ComplexComposition()
        
        print("\n🎼 Creating Symphony Movements...")
        print("-" * 50)
        
        # Create all movements automatically
        print("🎵 Creating Movement 1: Fibonacci Theme...")
        symphony.create_fibonacci_theme(12, 120, 'major')
        time.sleep(1)
        
        print("🎵 Creating Movement 2: Prime Counterpoint...")
        symphony.create_prime_counterpoint(15, 90, 'minor')
        time.sleep(1)
        
        print("🎵 Creating Movement 3: Pi Bridge...")
        symphony.create_pi_bridge(20, 150, 'pentatonic')
        time.sleep(1)
        
        print("🎵 Creating Movement 4: Fibonacci Variation...")
        symphony.create_fibonacci_variation(8, 180, 'major')
        time.sleep(1)
        
        print("🎵 Creating Movement 5: Prime Finale...")
        symphony.create_prime_finale(10, 60, 'minor')
        
        # Show symphony summary
        symphony.create_symphony_summary()
        
        # Play the complete symphony
        print("\n🎼 Prepare for a mathematical musical journey...")
        print("Starting in 3 seconds...")
        time.sleep(3)
        
        symphony.play_composition_sequence()
        
        # Save the symphony
        symphony.save_symphony()
        
        print("\n🎉 Symphony Complete!")
        print("You've experienced a full mathematical symphony with 5 movements!")
        print("\nAll compositions have been saved and can be reloaded later.")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check that all dependencies are installed correctly.")

if __name__ == "__main__":
    play_automatic_symphony()
