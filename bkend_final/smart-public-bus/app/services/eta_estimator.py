from datetime import datetime, timedelta

class ETAEstimator:
    def __init__(self, average_speed_kmh: float):
        self.average_speed_kmh = average_speed_kmh

    def estimate_eta(self, current_location: tuple, target_location: tuple) -> dict:
        distance_km = self.calculate_distance(current_location, target_location)
        travel_time_hours = distance_km / self.average_speed_kmh
        eta = datetime.now() + timedelta(hours=travel_time_hours)
        return {"eta": eta.isoformat()}

    def calculate_distance(self, loc1: tuple, loc2: tuple) -> float:
        # Simple Euclidean distance for demonstration purposes
        return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5