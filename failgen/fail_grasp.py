from enum import Enum
from typing import List

from .fail_instance import IFailure

class State(Enum):
    IDLE = 0
    FAIL = 1


class FailGrasp(IFailure):
    def __init__(self, name: str, stage_indices: List[int]):
        super().__init__(name, stage_indices)
        self._state = State.IDLE

    def on_stage_completed(self, stage_id: int) -> None:
        pass

    def on_gripper_start_close(self, stage_id: int) -> None:
        pass

    def on_gripper_start_open(self, stage_id: int) -> None:
        pass
