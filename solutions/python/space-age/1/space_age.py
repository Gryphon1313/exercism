class SpaceAge:
    def __init__(self, seconds: int):
        self.seconds = seconds

    def on_earth(self, exact: bool = False) -> float:
        result = self.seconds / 31557600
        return round(result, 2) if not exact else result

    def on_mercury(self, exact: bool = False) -> float:
        result = self.on_earth(True) / 0.2408467
        return round(result, 2) if not exact else result

    def on_venus(self, exact: bool = False) -> float:
        result = self.on_earth(True) / 0.61519726
        return round(result, 2) if not exact else result

    def on_mars(self, exact: bool = False) -> float:
        result = self.on_earth(True) / 1.8808158
        return round(result, 2) if not exact else result

    def on_jupiter(self, exact: bool = False) -> float:
        result = self.on_earth(True) / 11.862208
        return round(result, 2) if not exact else result

    def on_saturn(self, exact: bool = False) -> float:
        result = self.on_earth(True) / 29.447498
        return round(result, 2) if not exact else result

    def on_uranus(self, exact: bool = False) -> float:
        result = self.on_earth(True) / 84.016846
        return round(result, 2) if not exact else result

    def on_neptune(self, exact: bool = False) -> float:
        result = self.on_earth(True) / 164.79132
        return round(result, 2) if not exact else result