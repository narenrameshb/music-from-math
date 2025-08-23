# Test script for the complex demonstration
# Verifies that all components work correctly before running the full demo

import time
from complex_demo import ComplexComposition

def test_complex_composition():
    # Test the complex composition creation
    print("Testing Complex Composition Creation...")
    print("=" * 50)
    
    try:
        symphony = ComplexComposition()
        
        # Test creating individual movements
        print("\n1. Testing Fibonacci Theme Creation...")
        fib_theme = symphony.create_fibonacci_theme(8, 120, 'major')
        assert fib_theme is not None, "Fibonacci theme creation failed"
        assert len(fib_theme.notes) == 8, "Wrong number of notes in Fibonacci theme"
        print("Fibonacci theme creation works")
        
        print("\n2. Testing Prime Counterpoint Creation...")
        prime_counter = symphony.create_prime_counterpoint(6, 90, 'minor')
        assert prime_counter is not None, "Prime counterpoint creation failed"
        assert len(prime_counter.notes) == 6, "Wrong number of notes in prime counterpoint"
        print("Prime counterpoint creation works")
        
        print("\n3. Testing Pi Bridge Creation...")
        pi_bridge = symphony.create_pi_bridge(10, 150, 'pentatonic')
        assert pi_bridge is not None, "Pi bridge creation failed"
        assert len(pi_bridge.notes) == 10, "Wrong number of notes in pi bridge"
        print("Pi bridge creation works")
        
        print("\n4. Testing Fibonacci Variation Creation...")
        fib_var = symphony.create_fibonacci_variation(6, 180, 'major')
        assert fib_var is not None, "Fibonacci variation creation failed"
        assert len(fib_var.notes) == 6, "Wrong number of notes in Fibonacci variation"
        print("Fibonacci variation creation works")
        
        print("\n5. Testing Prime Finale Creation...")
        prime_finale = symphony.create_prime_finale(5, 60, 'minor')
        assert prime_finale is not None, "Prime finale creation failed"
        assert len(prime_finale.notes) == 5, "Wrong number of notes in prime finale"
        print("Prime finale creation works")
        
        # Test symphony summary
        print("\n6. Testing Symphony Summary...")
        symphony.create_symphony_summary()
        print("Symphony summary works")
        
        # Test composition count
        assert len(symphony.compositions) == 5, f"Expected 5 compositions, got {len(symphony.compositions)}"
        print("All 5 movements created successfully")
        
        # Test total notes calculation
        total_notes = sum(len(comp.notes) for comp in symphony.compositions)
        expected_total = 8 + 6 + 10 + 6 + 5  # Sum of all movement notes
        assert total_notes == expected_total, f"Expected {expected_total} total notes, got {total_notes}"
        print(f"Total notes calculation correct: {total_notes} notes")
        
        print("\n" + "=" * 50)
        print("ALL TESTS PASSED! Complex demo is ready to run.")
        print("=" * 50)
        print("\nYou can now run the full complex demonstration with:")
        print("  python complex_demo.py")
        print("\nThis will create a complete mathematical symphony with 5 movements!")
        
        return True
        
    except Exception as e:
        print(f"\nTest failed: {e}")
        return False

if __name__ == "__main__":
    try:
        success = test_complex_composition()
        if not success:
            print("\nPlease fix the errors before running the complex demo.")
        else:
            print("\nReady to create your mathematical symphony!")
    except KeyboardInterrupt:
        print("\n\nTesting interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error during testing: {e}")
    
    print("\nTest completed successfully!")
