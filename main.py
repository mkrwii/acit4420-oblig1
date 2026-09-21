from classes import *

def main():
    testparticipant = Participant(1, "Test Testesen", 10, 10, 10, 10)
    testobservation1 = Observation(1, 70, 0.5, 36.5, 1, "Good")
    testobservation2 = Observation(2, 75, 0.6, 36.7, 2, "Good")
    testobservation3 = Observation(3, 80, 0.7, 36.9, 3, "Good")
    testobservation4 = Observation(4, 85, 0.8, 37.1, 4, "Good")
    testobservations = [testobservation1, testobservation2, testobservation3, testobservation4]
    print("Hello, World!")
    print(testparticipant.name)

if __name__ == "__main__":
    main()