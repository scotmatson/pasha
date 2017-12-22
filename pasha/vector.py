# ~*~ coding: utf-8 ~*~

class Vector(object):

    def __init__(self, coordinates):
        try:
            if not all([
                coordinates,
                all(isinstance(element, int) for element in coordinates)
            ]): raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError :
            raise ValueError('The coordinates must be a nonempty list of integers.')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

################################################################################
if __name__ == '__main__':
    pass
