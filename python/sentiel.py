NOT_SPECIFIED = object()

class Home:
    def __init__(a: int = 0, b: int = 0, name = NOT_SPECIFIED):
        self.a = a
        self.b = b
        self.name = name

    def __repr__(self):
        return f"Name={self.name}"

    
    
