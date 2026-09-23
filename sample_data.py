import data_generator as dg
import random
from classes import *

default_id = 1 # global variable to assign unique session IDs

def getScenarioData(scenario):
    global default_id
    profile, observations = dg.generate_fitness_data(
            participant_id="P123",
            scenario=scenario,
            seed=random.randint(1, 10000),
            number_of_windows=12,
        )
    participant = Participant(
        participant_id=profile["participant_id"],
        ref_heart_rate=profile["baseline_heart_rate"],
        ref_skin_response=profile["baseline_skin_response"],
        ref_temperature=profile["baseline_temperature"],
        ref_activity_level=profile.get("baseline_activity_level", 0.2),
    )
    session = Session(session_id=f"S-{default_id}", participant=participant, start_time=0, end_time=0)
    default_id += 1
    for obs in observations:
        try:
            session.addObservation(Observation(**obs))
        except ValueError:
            pass
    return participant, session

if __name__ == "__main__":
    print("Error: sample_data.py is not meant to be run directly. Please run main.py or tests.py instead.")