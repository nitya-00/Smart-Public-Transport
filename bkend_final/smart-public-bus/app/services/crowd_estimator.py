from typing import Dict

class CrowdEstimator:
    def estimate_crowd_level(self, raw_crowd_level: int) -> Dict[str, str]:
        if raw_crowd_level < 10:
            crowd_level = "Low"
        elif 10 <= raw_crowd_level < 30:
            crowd_level = "Medium"
        else:
            crowd_level = "High"
        
        return {"crowd_level": crowd_level}