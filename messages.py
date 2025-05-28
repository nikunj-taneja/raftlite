import json
from typing import List

class AppendEntriesMessage():
    def __init__(self, term: int, leader_id: int, prev_log_index: int, prev_log_term: int, entries: List[LogEntry], leader_commit: int):
        self.term = term
        self.leader_id = leader_id
        self.prev_log_index = prev_log_index
        self.prev_log_term = prev_log_term
        self.entries = entries
        self.leader_commit = leader_commit
    
    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str: str):
        return AppendEntriesMessage(**json.loads(json_str))

class AppendEntriesResponse():
    def __init__(self, term: int, success: bool, last_log_index: int):
        self.term = term
        self.success = success
        self.last_log_index = last_log_index
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def from_json(json_str: str):
        return AppendEntriesResponse(**json.loads(json_str))


class RequestVoteMessage():
    def __init__(self, term: int, candidate_id: int, last_log_index: int, last_log_term: int):
        self.term = term
        self.candidate_id = candidate_id
        self.last_log_index = last_log_index
        self.last_log_term = last_log_term
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def from_json(json_str: str):
        return RequestVoteMessage(**json.loads(json_str))

class RequestVoteResponse():
    def __init__(self, term: int, vote_granted: bool):
        self.term = term
        self.vote_granted = vote_granted
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def from_json(json_str: str):
        return RequestVoteResponse(**json.loads(json_str))
