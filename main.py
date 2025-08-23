# Main entry point for the Mathematical Melody Generator
# Provides a command-line interface for user interaction

from melody_generator import MelodyGenerator
import os

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    # Print the application banner
    print("=" * 60)
    print("           MATHEMATICAL MELODY GENERATOR")
    print("=" * 60)
    print("Convert mathematical sequences into beautiful melodies!")
    print("=" * 60)

def print_main_menu():
    # Print the main menu options
    print("\nMain Menu:")
    print("1. Generate Fibonacci Melody")
    print("2. Generate Prime Numbers Melody")
    print("3. Generate Pi Digits Melody")
    print("4. Play Current Composition")
    print("5. Stop Playing")
    print("6. List Saved Compositions")
    print("7. Load Composition")
    print("8. Delete Composition")
    print("9. Show Current Composition Info")
    print("0. Exit")
    print("-" * 40)

def get_user_input(prompt, input_type=str, default=None):
    # Get user input with error handling
    # prompt: input prompt
    # input_type: type to convert input to  
    # default: default value if input is empty
    # returns: user input converted to specified type
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input and default is not None:
                return default
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def generate_melody_menu(generator, melody_type):
    # Menu for generating melodies with parameters
    # generator: the melody generator instance
    # melody_type: type of melody to generate
    print(f"\nGenerate {melody_type} Melody")
    print("-" * 30)
    
    # Get parameters from user
    n = get_user_input("Number of elements (default 10): ", int, 10)
    if n is None:
        return
    
    tempo = get_user_input("Tempo in BPM (default 120): ", int, 120)
    if tempo is None:
        return
    
    print("\nScale types:")
    print("1. Major (bright, happy)")
    print("2. Minor (sad, melancholic)")
    print("3. Pentatonic (simple, folk-like)")
    
    scale_choice = get_user_input("Choose scale (1-3, default 1): ", int, 1)
    if scale_choice is None:
        return
    
    scale_map = {1: 'major', 2: 'minor', 3: 'pentatonic'}
    scale_type = scale_map.get(scale_choice, 'major')
    
    print("\nRhythm patterns:")
    print("1. Simple (equal note durations)")
    print("2. Waltz (3/4 time signature)")
    print("3. March (4/4 time signature)")
    
    rhythm_choice = get_user_input("Choose rhythm (1-3, default 1): ", int, 1)
    if rhythm_choice is None:
        return
    
    rhythm_map = {1: 'simple', 2: 'waltz', 3: 'march'}
    rhythm_pattern = rhythm_map.get(rhythm_choice, 'simple')
    
    # Generate the melody
    print(f"\nGenerating {melody_type} melody...")
    
    if melody_type == "Fibonacci":
        composition = generator.generate_fibonacci_melody(
            n, tempo, scale_type, rhythm_pattern
        )
    elif melody_type == "Prime Numbers":
        composition = generator.generate_prime_melody(
            n, tempo, scale_type, rhythm_pattern
        )
    elif melody_type == "Pi Digits":
        composition = generator.generate_pi_melody(
            n, tempo, scale_type, rhythm_pattern
        )
    
    if composition:
        print(f"\n{melody_type} melody generated successfully!")
        
        # Ask if user wants to play it
        play_now = input("\nWould you like to play it now? (y/n): ").lower().strip()
        if play_now in ['y', 'yes']:
            generator.play_composition(composition)
    else:
        print("Failed to generate melody.")

def load_composition_menu(generator):
    # Menu for loading compositions
    print("\nLoad Composition")
    print("-" * 20)
    
    compositions = generator.composition_manager.list_compositions()
    if not compositions:
        print("No saved compositions found.")
        return
    
    print("\nAvailable compositions:")
    for idx, comp in enumerate(compositions, 1):
        print(f"{idx}. {comp['name']} ({comp['sequence_type']})")
    
    choice = get_user_input("\nEnter composition number to load: ", int)
    if choice is None or choice < 1 or choice > len(compositions):
        print("Invalid choice.")
        return
    
    selected_comp = compositions[choice - 1]
    fname = f"{selected_comp['name'].replace(' ', '_')}.json"
    
    if generator.load_composition(fname):
        print(f"Composition '{selected_comp['name']}' loaded successfully.")
    else:
        print("Failed to load composition.")

def delete_composition_menu(generator):
    # Menu for deleting compositions
    print("\nDelete Composition")
    print("-" * 20)
    
    compositions = generator.composition_manager.list_compositions()
    if not compositions:
        print("No saved compositions found.")
        return
    
    print("\nAvailable compositions:")
    for idx, comp in enumerate(compositions, 1):
        print(f"{idx}. {comp['name']} ({comp['sequence_type']})")
    
    choice = get_user_input("\nEnter composition number to delete: ", int)
    if choice is None or choice < 1 or choice > len(compositions):
        print("Invalid choice.")
        return
    
    selected_comp = compositions[choice - 1]
    
    confirm = input(f"\nAre you sure you want to delete '{selected_comp['name']}'? (y/n): ").lower().strip()
    if confirm in ['y', 'yes']:
        if generator.delete_composition(selected_comp['name']):
            print("Composition deleted successfully.")
        else:
            print("Failed to delete composition.")
    else:
        print("Deletion cancelled.")

def main():
    # Main application loop
    generator = MelodyGenerator()
    
    while True:
        clear_screen()
        print_banner()
        print_main_menu()
        
        choice = get_user_input("\nEnter your choice (0-9): ", int)
        if choice is None:
            continue
        
        if choice == 0:
            print("\nThank you for using Mathematical Melody Generator!")
            break
        elif choice == 1:
            generate_melody_menu(generator, "Fibonacci")
        elif choice == 2:
            generate_melody_menu(generator, "Prime Numbers")
        elif choice == 3:
            generate_melody_menu(generator, "Pi Digits")
        elif choice == 4:
            if generator.current_composition:
                generator.play_composition()
            else:
                print("No composition loaded. Generate one first.")
        elif choice == 5:
            generator.stop_playing()
        elif choice == 6:
            generator.list_saved_compositions()
        elif choice == 7:
            load_composition_menu(generator)
        elif choice == 8:
            delete_composition_menu(generator)
        elif choice == 9:
            generator.get_composition_info()
        else:
            print("Invalid choice. Please enter a number between 0 and 9.")
        
        if choice != 0:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        input("Press Enter to exit...")
