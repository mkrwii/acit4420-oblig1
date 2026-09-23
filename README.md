ACIT4420 - assignment 1
Project title: WIP
Chosen alternative: A
Student: Magnus K Wiik
Student no: 374992
Description: WIP

Class design and responsibilities:
All classes contained in classes.py
Participant: Plain class representing the participant and their reference values
Observation: Represents a single observation. Responsible for validating data integrity, will dismiss impossible values
Session: Represents a group of Observations, connected to a single Participant. Responsible for storing these observations securely
SessionClassifier: Stores the logic for classifying a Session.
Relations between classes: Observations constitute a Session, where one Participant participates, and one SessionClassifier classifies.

Where composition, encapsulation, inheritance and overriding are represented:
The core of this assignment is to group together observations into sessions. This lends itself particularly well to composition: Observations constitute a Session, where one Participant participates, and one SessionClassifier classifies. Therefore, there are no examples of inheritance and overriding in this assignment. Encapsulation is done with the __observations attribute in Session. Observations that are already validated should not be changed, and the Session class only provides methods to add observations and retrieve observations and the number of observations in a Session.

Assumptions and classification rules:
The primary assumption is that heart rate is the primary indicator for how hard a session is. Testing of the solution with the provided synthetic data has confirmed this. We rate a session as hard if it has an increase of at least 40% from the participants' reference value. A medium session requires more than 15% increase in the heart rate. Anything below this is seen as a Resting session. A session is rejected as insufficient if it either contains fewer than 3 valid observations, or if the signal quality is at less than 65%. In addition, a session is classified as recovering if the heart rate is at least 20% lower in the second half than in the first half. These percentages can be changed, see below.

Exact installation and running instructions:
install: `git clone github.com/mkrwii/acit4420-oblig1`
running: from the root folder, run `python3 tests.py` for the five prescribed scenarios. Certain of the rules for classification can be altered by changing the constant variables in the SessionClassifier class.

Example output: WIP
Known limitations: WIP
