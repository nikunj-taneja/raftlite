from abc import ABC, abstractmethod
from enum import Enum

class StateMachine(ABC):
    @abstractmethod
    def apply(self, command: str):
        pass


class ServerState(Enum):
    FOLLOWER: int = 1
    CANDIDATE: int = 2
    LEADER: int = 3


class LogEntry:
    def __init__(self, term: int, command: str):
        self.term: int = term
        self.command: str = command
