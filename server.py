from enum import Enum
from typing import List, Optional
from messages import LogEntry, AppendEntriesMessage, AppendEntriesResponse, RequestVoteMessage, RequestVoteResponse

class State(Enum):
    FOLLOWER = 1
    CANDIDATE = 2
    LEADER = 3


class Server:
    def __init__(self):
        # persistent state on all servers
        self.state: State = State.FOLLOWER
        self.current_term: int = 0
        self.voted_for: Optional[int] = None
        self.log: List[LogEntry] = []

        # volatile state on all servers
        self.commit_index: int = 0
        self.last_applied: int = 0

        # volatile state on leaders
        self.next_index: List[int] = []
        self.match_index: List[int] = []

    """
    Leader function to send AppendEntries RPC
    
    Args:
        msg (AppendEntriesMessage): The message to send to other servers
    """
    def append_entries(self, msg: AppendEntriesMessage):
        pass


    """
    Candidate function to gather votes
    
    Returns:
        msg (RequestVoteMessage): The message to send to other servers
    """
    def request_vote(self):
        pass
    

    """
    Follower function to respond to AppendEntries RPC

    Args:
        msg (AppendEntriesMessage): The AppendEntries message received from the leader

    Returns:
        AppendEntriesResponse: The response to the AppendEntries message
    """
    def reply_to_append_entries(self, msg: AppendEntriesMessage) -> AppendEntriesResponse:
        pass
    

    """
    Follower function to respond to RequestVote RPC

    Returns:
        RequestVoteResponse: The response to the RequestVote message
    """
    def reply_to_request_vote(self, msg: RequestVoteMessage) -> RequestVoteResponse:
        pass
    