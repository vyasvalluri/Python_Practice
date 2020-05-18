import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('A Polygon must have at lesat 3 vertices')
        self._n = n
        self._R = R

        self._interialangle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._parimeter = None

    def __repr__(self):
        return f'Polygon(n = {self._n}, R = {self._R})'

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def curcumradius(self):
        return self._R

    @property
    def interialangle(self):
        if self._interialangle is None :
            self._interialangle = (self._n - 2) * 180 / self._n
        return self._interialangle

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_lenght = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_lenght

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area
    
    @property
    def perimeter(self):
        if self._parimeter is None:
            self._parimeter = self._n * self.side_length
        return self._parimeter

    def __eq__(self, obj):
        if isinstance(obj, self.__class__):
            return ((self.count_edges == obj.count_edges 
            and self.curcumradius == obj.curcumradius))
        else :
            return NotImplemented
    
    def __gt__(self, obj):
        if isinstance(obj, self.__class__):
            return (self.count_vertices > obj.count_vertices)
        else: 
            return NotImplemented

def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    try:
        p = Polygon(2,10)
        assert False, ('creating polygon with 2 vertices: '
        'exception expeted, not received')
    except ValueError:
        pass

    n = 3
    R = 1
    p = Polygon(n,R)
    assert str(p) == 'Polygon(n = 3, R = 1)', f'actual: {str(p)}'
    assert p.count_vertices == n, f'actual: {p.count_vertices}, expected : {n}'
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.curcumradius == R, f'actual: {p.curcumradius}, expectex: {R}'
    assert p.interialangle == 60, f'actual : {p.interialangle}, expected: 60'

    n = 4
    R = 1
    p = Polygon(n, R)
    assert math.isclose(p.area, 2, rel_tol = rel_tol, abs_tol= abs_tol), (f'actual: {p.area}, expected: 2.0')
    assert math.isclose(p.apothem, 0.707, rel_tol = rel_tol, abs_tol= abs_tol), f'actual: {p.parimeter}, expected: {0.707}'

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    assert p2 > p1, f'expeted: {p1} is greater, actual: {p2} is greater'

test_polygon()