from classes import *
import data_generator as dg

def main():
    # Pick a scenario (or use "random")
    scenario = "poor_quality"

    # Generate dummy data
    profile, observations = dg.generate_fitness_data(
        participant_id="P123",
        scenario=scenario,
        seed=42,
        number_of_windows=12,
    )

    print("\n=== Participant Profile ===")
    for key, value in profile.items():
        print(f"{key}: {value}")

    print("\n=== Observations ===")
    for obs in observations:
        print(obs)

    clean_observations = []

    for obs in observations:
        try:
            obs = Observation(**obs)   # map dict → object
            clean_observations.append(obs)
            print(obs)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()