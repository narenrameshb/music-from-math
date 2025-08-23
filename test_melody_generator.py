# Test script for the Mathematical Melody Generator
# Tests all major components to ensure they work correctly

import os
import sys
import time

def test_math_sequences():
    # Test mathematical sequence generation
    print("Testing mathematical sequences...")
    
    try:
        from math_sequences import generate_fibonacci, generate_primes, generate_pi_digits, sequence_to_notes
        
        # Test Fibonacci
        fib = generate_fibonacci(8)
        expected_fib = [0, 1, 1, 2, 3, 5, 8, 13]
        assert fib == expected_fib, f"Fibonacci test failed: {fib} != {expected_fib}"
        print("Fibonacci sequence generation works")
        
        # Test Primes
        primes = generate_primes(5)
        expected_primes = [2, 3, 5, 7, 11]
        assert primes == expected_primes, f"Primes test failed: {primes} != {expected_primes}"
        print("Prime numbers generation works")
        
        # Test Pi digits
        pi_digits = generate_pi_digits(5)
        expected_pi = [3, 1, 4, 1, 5]
        assert pi_digits == expected_pi, f"Pi digits test failed: {pi_digits} != {expected_pi}"
        print("Pi digits generation works")
        
        # Test sequence to notes conversion
        notes = sequence_to_notes([1, 2, 3], 'major')
        assert len(notes) == 3, f"Notes conversion failed: expected 3 notes, got {len(notes)}"
        assert all(isinstance(note, (int, float)) for note in notes), "Notes should be numbers"
        print("Sequence to notes conversion works")
        
        return True
        
    except Exception as e:
        print(f"Math sequences test failed: {e}")
        return False

def test_audio_engine():
    # Test audio engine functionality
    print("\nTesting audio engine...")
    
    try:
        from audio_engine import AudioEngine
        
        engine = AudioEngine()
        
        # Test single note (very short duration for testing)
        print("  Testing single note (you should hear a short beep)...")
        engine.play_note(440, 100)  # A4 note, 100ms
        time.sleep(0.2)  # Wait for note to finish
        
        print("Audio engine initialization works")
        print("Single note playback works")
        
        return True
        
    except Exception as e:
        print(f"Audio engine test failed: {e}")
        return False

def test_composition_management():
    # Test composition management
    print("\nTesting composition management...")
    
    try:
        from composition import Composition, CompositionManager
        
        # Test composition creation
        comp = Composition("Test", "fibonacci", [440, 494, 523], 120, "major", "simple")
        assert comp.name == "Test", "Composition name not set correctly"
        assert comp.sequence_type == "fibonacci", "Sequence type not set correctly"
        print("Composition creation works")
        
        # Test composition manager
        manager = CompositionManager("test_compositions")
        assert os.path.exists("test_compositions"), "Save directory not created"
        print("Composition manager initialization works")
        
        # Test saving and loading
        success = manager.save_composition(comp)
        assert success, "Composition save failed"
        print("Composition saving works")
        
        # Clean up test directory
        import shutil
        if os.path.exists("test_compositions"):
            shutil.rmtree("test_compositions")
        
        return True
        
    except Exception as e:
        print(f"✗ Composition management test failed: {e}")
        return False

def test_melody_generator():
    # Test the main melody generator
    print("\nTesting melody generator...")
    
    try:
        from melody_generator import MelodyGenerator
        
        generator = MelodyGenerator()
        
        # Test Fibonacci melody generation
        comp = generator.generate_fibonacci_melody(5, 120, 'major', 'simple', save=False)
        assert comp is not None, "Fibonacci melody generation failed"
        assert comp.name == "Fibonacci_5_Notes", "Composition name incorrect"
        assert len(comp.notes) == 5, "Wrong number of notes generated"
        print("Fibonacci melody generation works")
        
        # Test composition info
        generator.current_composition = comp
        generator.get_composition_info()
        print("Composition info display works")
        
        return True
        
    except Exception as e:
        print(f"Melody generator test failed: {e}")
        return False

def run_all_tests():
    # Run all tests and report results
    print("=" * 60)
    print("           RUNNING TESTS")
    print("=" * 60)
    
    tests = [
        ("Mathematical Sequences", test_math_sequences),
        ("Audio Engine", test_audio_engine),
        ("Composition Management", test_composition_management),
        ("Melody Generator", test_melody_generator)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        if test_func():
            passed += 1
        else:
            print(f"  {test_name} test failed!")
    
    print("\n" + "=" * 60)
    print(f"TEST RESULTS: {passed}/{total} tests passed")
    print("=" * 60)
    
    if passed == total:
        print("All tests passed! The melody generator is working correctly.")
        print("\nYou can now run the main application with:")
        print("  python main.py")
    else:
        print("Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    try:
        success = run_all_tests()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nTesting interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error during testing: {e}")
        sys.exit(1)
