import data_generator as dg
from classes import *

scenarios = dg.available_scenarios()

def test():
    for scenario in scenarios:
        run_scenario(scenario)

def run_scenario(scenario):
    print(f"Running scenario: {scenario}")
    profile, observations = dg.generate_fitness_data(
        participant_id="P123",
        scenario=scenario,
        seed=2123,
        number_of_windows=12,
    )

    print("\n=== Participant Profile ===")
    for key, value in profile.items():
        print(f"{key}: {value}")

        clean_observations = []

    for obs in observations:
        try:
            obs = Observation(**obs)   # map dict → object
            clean_observations.append(obs)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    test()
    print("Hello from tests.py!")