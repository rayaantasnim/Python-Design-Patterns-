# -------------------------------
# Singleton Pattern in Python
# -------------------------------
# GOF (Gang of Four) Design Pattern
# Intent: Ensure a class has only ONE instance
# and provide a global point of access to it.
# -------------------------------

class Settings:
    # Class-level variable to hold the single instance
    _instance = None

    def __new__(cls):
        # __new__ is responsible for creating a new instance
        # It runs BEFORE __init__ and controls object creation.
        
        if cls._instance is None:
            # If no instance exists yet, create one
            cls._instance = super().__new__(cls)
            
            # Initialize attributes directly here
            # because __init__ may run multiple times
            cls._instance.volume = 0  
            # Default value for demonstration
        
        # If an instance already exists, return the same one
        return cls._instance


# -------------------------------
# Demonstration of Singleton behavior
# -------------------------------

# First object creation
s2 = Settings()
s2.volume = 30   # Modify the shared instance's attribute

# Second object creation
s1 = Settings()
s1.volume = 50   # This modifies the SAME instance

# Since both s1 and s2 point to the same object,
# the volume attribute reflects the latest change.
print(s2.volume)   # Output: 50
