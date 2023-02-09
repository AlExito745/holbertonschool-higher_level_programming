class MyList(list):
    """Represent a derived class Mylist."""

    def print_sorted(self):
        """Function that print a list in ascending sort."""
        all(isinstance(item, int) for item in self)
        print(sorted(self))
