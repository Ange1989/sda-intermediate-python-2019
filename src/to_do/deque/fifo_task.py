from dataclasses import dataclass
from datetime import datetime

from src.to_do.deque import Fifo


@dataclass
class FifoTask(Fifo):

    name: str
    description: str
    status: int



