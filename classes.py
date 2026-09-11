class Observation:
    def __init__(self, timestamp, heart_rate, skin_response, temperature, activity_level, signal_quality):
        self.timestamp = timestamp
        self.heart_rate = heart_rate
        self.skin_response = skin_response
        self.temperature = temperature
        self.activity_level = activity_level
        self.signal_quality = signal_quality
        
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
