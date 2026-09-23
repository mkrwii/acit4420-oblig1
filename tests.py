import data_generator as dg
import sample_data as sd
from classes import *

scenarios = dg.available_scenarios()


SCENARIO_TO_EXPECTED_CLASSIFICATION = {
    #maps the data generators scenarios to the expected classification results
    "resting": "RESTING",
    "moderate_activity": "MEDIUM",
    "high_activity": "HIGH",
    "recovery": "RECOVERY",
    "poor_quality": "INSUFFICIENT",
}

def test():
    for scenario, expected in SCENARIO_TO_EXPECTED_CLASSIFICATION.items():
        participant, session = sd.getScenarioData(scenario)
        result = SessionClassifier(session).getResult()
        assert result["classification"] == expected, f"{scenario}: expected {expected}, got {result['classification']}"
        print(f"PASS: {scenario} -> {result['classification']}")

if __name__ == "__main__":
    print("--- Runnning tests with random seeds for all five scenarios: ---")
    test()