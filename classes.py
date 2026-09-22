class Observation:
    def __init__(self, timestamp, heart_rate, skin_response, temperature, activity_level, signal_quality):
        if isinstance(timestamp, int) and timestamp > 0:
            self.timestamp = timestamp
        else:
            raise ValueError(f"Observation failed! {timestamp} is not a valid timestamp.")
        if isinstance(heart_rate, (int,float)) and 35 < heart_rate < 205:
            self.heart_rate = heart_rate
        else:
            raise ValueError(f"Observation failed! {heart_rate} is not a valid heart rate.")
        if isinstance(skin_response, (int,float)) and 0 < skin_response:
            self.skin_response = skin_response
        else:
            raise ValueError(f"Observation failed! {skin_response} is not a valid skin response.")
        if isinstance(temperature, (int,float)) and 25 < temperature < 42:
            self.temperature = temperature
        else:
            raise ValueError(f"Observation failed! {temperature} is not a valid temperature.")
        if isinstance(activity_level, (int,float)) and 0 < activity_level < 1:
            self.activity_level = activity_level
        else:
            raise ValueError(f"Observation failed! {activity_level} is not a valid activity level.")
        if isinstance(signal_quality, (int,float)) and 0 < signal_quality < 1:
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
    def __init__(self, session_id, participant_id, start_time, end_time):
        self.session_id = session_id
        self.participant_id = participant_id
        self.start_time = start_time
        self.end_time = end_time
        self.__observations = []
    def addObservation(self, observation):
        self.__observations.append(observation)
