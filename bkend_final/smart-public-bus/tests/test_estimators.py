from fastapi import HTTPException
from app.services.crowd_estimator import CrowdEstimator
from app.services.eta_estimator import ETAEstimator

def test_crowd_estimator():
    estimator = CrowdEstimator()
    assert estimator.estimate_crowd_level(5) == "Low"
    assert estimator.estimate_crowd_level(15) == "Medium"
    assert estimator.estimate_crowd_level(25) == "High"

def test_eta_estimator():
    estimator = ETAEstimator()
    assert estimator.estimate_eta((10, 10), (20, 20)) == 15  # Example values
    assert estimator.estimate_eta((0, 0), (0, 0)) == 0  # Same location
    assert estimator.estimate_eta((5, 5), (10, 10)) == 10  # Example values