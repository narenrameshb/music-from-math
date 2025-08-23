# Mathematical sequence generators for the melody generator

import math

def generate_fibonacci(n):
    # Generate first n Fibonacci numbers
    # n: number of Fibonacci numbers to generate
    # returns: list of Fibonacci numbers
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    
    return fib_seq

def is_prime(num):
    # Check if a number is prime
    # num: number to check
    # returns: True if prime, False otherwise
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

def generate_primes(n):
    # Generate first n prime numbers
    # n: number of prime numbers to generate
    # returns: list of prime numbers
    prime_list = []
    current_num = 2
    
    while len(prime_list) < n:
        if is_prime(current_num):
            prime_list.append(current_num)
        current_num += 1
    
    return prime_list

def generate_pi_digits(n):
    # Generate first n digits of pi
    # n: number of pi digits to generate
    # returns: list of pi digits
    # Using a simple approximation for pi
    # For more accuracy, you could use a library like mpmath
    pi_string = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    
    # Remove decimal point and convert to list of integers
    digit_list = [int(d) for d in pi_string.replace('.', '')]
    
    return digit_list[:n]

def sequence_to_notes(sequence, scale_type='major'):
    # Convert a mathematical sequence to musical notes
    # sequence: list of numbers
    # scale_type: type of scale ('major', 'minor', 'pentatonic')
    # returns: list of note frequencies in Hz
    # Define basic note frequencies (C major scale)
    if scale_type == 'major':
        base_notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]  # C, D, E, F, G, A, B, C
    elif scale_type == 'minor':
        base_notes = [261.63, 293.66, 311.13, 349.23, 392.00, 415.30, 466.16, 523.25]  # C, D, Eb, F, G, Ab, Bb, C
    elif scale_type == 'pentatonic':
        base_notes = [261.63, 293.66, 329.63, 392.00, 440.00, 523.25]  # C, D, E, G, A, C
    else:
        base_notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
    
    note_list = []
    for num in sequence:
        # Map number to note using modulo
        note_idx = abs(num) % len(base_notes)
        # Determine octave based on number magnitude
        octave = abs(num) // len(base_notes)
        # Calculate frequency with octave
        freq = base_notes[note_idx] * (2 ** octave)
        # Limit frequency to reasonable range (20Hz - 20000Hz)
        freq = max(20, min(20000, freq))
        note_list.append(freq)
    
    return note_list
