"""
Composition management for saving and loading musical compositions.
"""

import json
import os
from datetime import datetime

class Composition:
    def __init__(self, name="Untitled", sequence_type="fibonacci", notes=None, 
                 tempo=120, scale_type="major", rhythm_pattern="simple"):
        """
        Initialize a composition.
        
        Args:
            name (str): Name of the composition
            sequence_type (str): Type of mathematical sequence
            notes (list): List of note frequencies
            tempo (int): Tempo in BPM
            scale_type (str): Musical scale type
            rhythm_pattern (str): Rhythm pattern type
        """
        self.name = name
        self.sequence_type = sequence_type
        self.notes = notes or []
        self.tempo = tempo
        self.scale_type = scale_type
        self.rhythm_pattern = rhythm_pattern
        self.created_date = datetime.now().isoformat()
        self.modified_date = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert composition to dictionary for saving."""
        return {
            'name': self.name,
            'sequence_type': self.sequence_type,
            'notes': self.notes,
            'tempo': self.tempo,
            'scale_type': self.scale_type,
            'rhythm_pattern': self.rhythm_pattern,
            'created_date': self.created_date,
            'modified_date': self.modified_date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create composition from dictionary."""
        comp = cls(
            name=data.get('name', 'Untitled'),
            sequence_type=data.get('sequence_type', 'fibonacci'),
            notes=data.get('notes', []),
            tempo=data.get('tempo', 120),
            scale_type=data.get('scale_type', 'major'),
            rhythm_pattern=data.get('rhythm_pattern', 'simple')
        )
        comp.created_date = data.get('created_date', datetime.now().isoformat())
        comp.modified_date = data.get('modified_date', datetime.now().isoformat())
        return comp
    
    def update(self, **kwargs):
        """Update composition properties."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.modified_date = datetime.now().isoformat()

class CompositionManager:
    def __init__(self, save_directory="compositions"):
        """
        Initialize the composition manager.
        
        Args:
            save_directory (str): Directory to save compositions
        """
        self.save_directory = save_directory
        self.compositions = {}
        self.ensure_save_directory()
    
    def ensure_save_directory(self):
        """Ensure the save directory exists."""
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
    
    def save_composition(self, composition):
        """
        Save a composition to file.
        
        Args:
            composition (Composition): Composition to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filename = f"{composition.name.replace(' ', '_')}.json"
            filepath = os.path.join(self.save_directory, filename)
            
            # Update modified date
            composition.modified_date = datetime.now().isoformat()
            
            with open(filepath, 'w') as f:
                json.dump(composition.to_dict(), f, indent=2)
            
            self.compositions[composition.name] = composition
            print(f"Composition '{composition.name}' saved successfully.")
            return True
            
        except Exception as e:
            print(f"Error saving composition: {e}")
            return False
    
    def load_composition(self, filename):
        """
        Load a composition from file.
        
        Args:
            filename (str): Name of the file to load
            
        Returns:
            Composition: Loaded composition or None if failed
        """
        try:
            filepath = os.path.join(self.save_directory, filename)
            
            if not os.path.exists(filepath):
                print(f"File '{filename}' not found.")
                return None
            
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            composition = Composition.from_dict(data)
            self.compositions[composition.name] = composition
            print(f"Composition '{composition.name}' loaded successfully.")
            return composition
            
        except Exception as e:
            print(f"Error loading composition: {e}")
            return None
    
    def list_compositions(self):
        """List all available compositions."""
        compositions = []
        
        if not os.path.exists(self.save_directory):
            return compositions
        
        for filename in os.listdir(self.save_directory):
            if filename.endswith('.json'):
                try:
                    filepath = os.path.join(self.save_directory, filename)
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                    compositions.append(data)
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
        
        return compositions
    
    def delete_composition(self, name):
        """
        Delete a composition.
        
        Args:
            name (str): Name of the composition to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filename = f"{name.replace(' ', '_')}.json"
            filepath = os.path.join(self.save_directory, filename)
            
            if os.path.exists(filepath):
                os.remove(filepath)
                if name in self.compositions:
                    del self.compositions[name]
                print(f"Composition '{name}' deleted successfully.")
                return True
            else:
                print(f"Composition '{name}' not found.")
                return False
                
        except Exception as e:
            print(f"Error deleting composition: {e}")
            return False
    
    def create_composition_from_sequence(self, name, sequence_type, notes, 
                                       tempo=120, scale_type="major", 
                                       rhythm_pattern="simple"):
        """
        Create and save a new composition from a mathematical sequence.
        
        Args:
            name (str): Name of the composition
            sequence_type (str): Type of mathematical sequence
            notes (list): List of note frequencies
            tempo (int): Tempo in BPM
            scale_type (str): Musical scale type
            rhythm_pattern (str): Rhythm pattern type
            
        Returns:
            Composition: Created composition
        """
        composition = Composition(
            name=name,
            sequence_type=sequence_type,
            notes=notes,
            tempo=tempo,
            scale_type=scale_type,
            rhythm_pattern=rhythm_pattern
        )
        
        if self.save_composition(composition):
            return composition
        else:
            return None
