"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 100):
        """Make generator at start"""
        self.start = self.next = start
    
    def _repr__(self):
        """Show representation"""
        return f'<SerialGenerator start={self.start} next={self.next}>'

    def generate(self):
        """Generate next serial number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to start"""
        self.next = self.start
    
