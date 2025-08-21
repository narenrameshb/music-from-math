# Music From Math 🎼

Convert mathematical sequences into musical melodies using Python and Windows sound.

## What It Does

This project transforms mathematical sequences (Fibonacci, prime numbers, pi digits) into audible music.

## Quick Start

**Hear a complete mathematical symphony:**
```bash
python auto_symphony.py
```

**Try individual examples:**
```bash
python demo.py
```

**Full interactive experience:**
```bash
python main.py
```

## What You Will Hear

- **Fibonacci sequences** in major scales with waltz rhythms
- **Prime numbers** in minor scales with march patterns  
- **Pi digits** in pentatonic scales with simple rhythms
- **Complete symphony** with 5 movements (about 32 seconds total)

## Features

- Generate melodies from mathematical sequences
- Multiple musical scales (major, minor, pentatonic)
- Different rhythm patterns (waltz, march, simple)
- Adjustable tempo (60-180 BPM)
- Save and load compositions
- No external audio libraries needed (uses Windows winsound)

## Requirements

- Windows OS
- Python 3.7+
- `pip install -r requirements.txt`

## How It Works

1. **Math Sequences**: Generates Fibonacci, primes, or pi digits
2. **Note Mapping**: Converts numbers to musical frequencies
3. **Scale Selection**: Maps to major, minor, or pentatonic scales
4. **Rhythm Patterns**: Applies waltz, march, or simple rhythms
5. **Audio Output**: Plays through Windows sound system

## Project Structure

```
├── auto_symphony.py      # Automatic symphony player
├── demo.py               # Basic examples
├── main.py               # Full application
├── melody_generator.py   # Core logic
├── math_sequences.py     # Math sequence generators
├── audio_engine.py       # Sound generation
├── composition.py        # Save/load system
└── test_*.py            # Test files
```

## Example Output

The automatic symphony creates 5 movements:
1. **Fibonacci Theme** - Majestic opening (12 notes, 120 BPM)
2. **Prime Counterpoint** - Contrasting middle (15 notes, 90 BPM)
3. **Pi Bridge** - Transitional section (20 notes, 150 BPM)
4. **Fibonacci Variation** - Energetic development (8 notes, 180 BPM)
5. **Prime Finale** - Dramatic conclusion (10 notes, 60 BPM)

## Future Ideas

- MIDI export functionality
- More mathematical sequences
- Web interface
- Audio file generation
- Visual representations

---
