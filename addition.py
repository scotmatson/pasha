# ~*~ coding: utf-8 ~*~

from .vector import Vector

def add(v1, v2):
    solution = []
    try:
        if v1.dimension != v2.dimension:
            raise ValueError
        for i, num in enumerate(v1.coordinates):
            solution.append(num + v2.coordinates[i])
    except ValueError:
        raise ValueError('The dimensions must be the same.')

    result = Vector(solution)
    print(result.coordinates)

    return result

################################################################################
if __name__ == '__main__':
    pass
