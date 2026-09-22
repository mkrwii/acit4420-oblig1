class Observation:
    def __init__(self, timestamp, heart_rate, skin_response, temperature, activity_level, signal_quality):
        if isinstance(timestamp, int) and timestamp >= 0:
            self.timestamp = timestamp
        else:
            raise ValueError(f"Observation failed! {timestamp} is not a valid timestamp.")
        if isinstance(heart_rate, (int,float)) and 35 <= heart_rate <= 205:
            self.heart_rate = heart_rate
        else:
            raise ValueError(f"Observation failed! {heart_rate} is not a valid heart rate.")
        if isinstance(skin_response, (int,float)) and 0 <= skin_response:
            self.skin_response = skin_response
        else:
            raise ValueError(f"Observation failed! {skin_response} is not a valid skin response.")
        if isinstance(temperature, (int,float)) and 25 <= temperature <= 42:
            self.temperature = temperature
        else:
            raise ValueError(f"Observation failed! {temperature} is not a valid temperature.")
        if isinstance(activity_level, (int,float)) and 0 <= activity_level <= 1:
            self.activity_level = activity_level
        else:
            raise ValueError(f"Observation failed! {activity_level} is not a valid activity level.")
        if isinstance(signal_quality, (int,float)) and 0 <= signal_quality <= 1:
            self.signal_quality = signal_quality
        else:
            raise ValueError(f"Observation failed! {signal_quality} is not a valid activity level.")


class Participant:
    def __init__(self, participant_id, name, ref_heart_rate, ref_skin_response, ref_temperature, ref_activity_level):
        print("Creating Participant object with ID:", participant_id)
        self.participant_id = participant_id
        self.name = name
        self.ref_heart_rate = ref_heart_rate
        self.ref_skin_response = ref_skin_response
        self.ref_temperature = ref_temperature
        self.ref_activity_level = ref_activity_level


class Session:
    def __init__(self, session_id, participant, start_time, end_time):
        self.session = session_id
        self.participant = participant
        self.start_time = start_time
        self.end_time = end_time
        self.__observations = []
    def addObservation(self, observation):
        self.__observations.append(observation)
    def getObservations(self):
        return list(self.__observations)
    def getAverageHeartRate(self):
        if not self.__observations:
            return None
        values = [o.heart_rate for o in self.__observations]
        return sum(values) / len(values)
    def getNumberOfObservations(self):
        return len(self.__observations)


class SessionClassifier:
    MIN_OBSERVATIONS_VALID = 3 # The minimum amount of observations required to classify a session
    RECOVERY_MARGIN = 0.20 # The decline in heart rate that triggers a recovery classification
    HIGH_HEART_RATE = 0.40 # The percentage of the baseline heart rate that is the lower bounds of high heart rate
    MEDIUM_HEART_RATE = 0.15 # Similarly, the lower bounds of what is medium heart rate

    def __init__(self, session):
        self._session = session
        self._participant = session.participant
        self.category = self.classify()

    def classify(self):
        if self._session.getNumberOfObservations() < self.MIN_OBSERVATIONS_VALID:
            self.reason = "FEW OBSERVATIONS"
            return "INSUFFICIENT"
        elif self._isRecovering():
            self.reason = "DECLINING HEART RATE"
            return "RECOVERY"
        elif self._isAboveBaseline(self._session.getAverageHeartRate(), self._participant.ref_heart_rate, self.HIGH_HEART_RATE):
            self.reason = "HIGH HEART RATE"
            return "HIGH"
        elif self._isAboveBaseline(self._session.getAverageHeartRate(), self._participant.ref_heart_rate, self.MEDIUM_HEART_RATE):
            self.reason = "MEDIUM HEART RATE"
            return "MEDIUM"
        else:
            self.reason = "LOW HEARTRATE"
            return "RESTING"
        
    def getResult(self):
        return{
            "classification": self.category,
            "reason": self.reason,
            "usable_observations": self._session.getNumberOfObservations(),
            "avg_heart_rate": self._session.getAverageHeartRate()
        }
    
    @staticmethod
    def _isAboveBaseline(value, baseline, margin):
        return value > baseline * (1 + margin)
    
    def _isRecovering(self):
        observations = self._session.getObservations()
        if len(observations) < self.MIN_OBSERVATIONS_VALID:
            return False
        mid = len(observations) // 2
        first_half = observations[:mid]
        second_half = observations[mid:]
        first_avg = sum(o.heart_rate for o in first_half) /len(first_half)
        second_avg = sum(o.heart_rate for o in second_half) /len(second_half)
        decline = (first_avg - second_avg) / first_avg
        return decline >= self.RECOVERY_MARGIN


    