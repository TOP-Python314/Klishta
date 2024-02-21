class Tetrahedron:
    
    def __init__(self, edge: float):
        self.edge = edge
        
    def surface(self) -> float:
        """возвращает площадь поверхности"""
        return (self.edge**2) * (3**0.5)
    def volume(self) -> float:
        """Возвращает объём тела"""  
        return (self.edge**3) /12 * (2**0.5)

# ПРОВЕРКА:
# >>> example = Tetrahedron(5)
# >>> example.surface()
# 43.30127018922193
# >>> example.volume()
# 14.73139127471974
# >>> example.edge = 6
# >>> example.surface()
# 62.35382907247958
# >>> example.volume()
# 25.455844122715714