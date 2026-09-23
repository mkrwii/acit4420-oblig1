from classes import *
import data_generator as dg
import sample_data as sd

scenarios = dg.available_scenarios()

def main():
    for scenario in scenarios:
        participant, session = sd.getScenarioData(scenario)
        result = SessionClassifier(session).getResult()
        printParticipantData(participant)
        printSessionReport(session, participant, result)


if __name__ == "__main__":
    main()