import math
from decimal import Decimal, getcontext

# Set precision level for Decimals class
getcontext().prec = 30


class Vector(object):

    """Vector class for storing vectors and calculating basic vector operations

    Args:
        coordinates (int, float)
    Attributes:
        coordinates (Decimal)
        dimensions (int)

    Returns:
        Vector object -- an object with coordinates and number of dimentsions
    """

    # Constructor for a Vector object
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be non empty!")

        except TypeError:
            raise TypeError("The coordinates must be an iterable!")

    def __add__(self, v):
        """Function to add two vectors by operator overload (plus sign)
        Args:
            Vector object

        Returns:
            Vector object - the sum of two vectors
        """
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        """Function to subtract two vectors by operator overload (minus sign)
        Args:
            Vector object

        Returns:
            Vector object - the difference of two vectors
        """
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def dot(self, v):
        """Function to calculate the dot product of two vectors
        Args:
            Vector object

        Returns:
            Decimal object - dot product of two vectors
        """
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])
