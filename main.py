from classes import *
import data_generator as dg

def main():
    # Pick a scenario (or use "random")
    scenario = "random"

    # Generate dummy data
    profile, observations = dg.generate_fitness_data(
        participant_id="P123",
        scenario=scenario,
        seed=2123,
        number_of_windows=12,
    )

    #print("\n=== Participant Profile ===")
    #for key, value in profile.items():
    #    print(f"{key}: {value}")

    #print("\n=== Observations ===")
    #for obs in observations:
    #    print(obs)

    clean_observations = []

    for obs in observations:
        try:
            obs = Observation(**obs)   # map dict → object
            clean_observations.append(obs)
            #print(obs)
        except ValueError as e:
            print(e)

    # --- Build the Participant ---
    # NOTE: check these key names against what your generator's profile dict
    # actually uses — this assumes it matches the earlier printed profile.
    participant = Participant(
        participant_id=profile["participant_id"],
        name=profile.get("name", profile["participant_id"]),  # fallback if no name field
        ref_heart_rate=profile["baseline_heart_rate"],
        ref_skin_response=profile["baseline_skin_response"],
        ref_temperature=profile["baseline_temperature"],
        ref_activity_level=profile.get("baseline_activity_level", 0.2),  # adjust/remove if your generator provides this
    )

    # --- Build the Session and attach observations ---
    session = Session(
        session_id="S001",
        participant=participant,
        start_time=0,
        end_time=len(clean_observations),
    )
    for obs in clean_observations:
        session.addObservation(obs)

    # --- Classify and report ---
    classifier = SessionClassifier(session)
    result = classifier.getResult()

    print("\n=== Classification Result ===")
    for key, value in result.items():
        print(f"{key}: {value}")

        # --- Readable report ---
    printSessionReport(session, participant, result)

if __name__ == "__main__":
    main()