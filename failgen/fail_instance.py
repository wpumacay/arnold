import abc
from typing import List, Optional

import numpy as np
from omegaconf import DictConfig

import omni
from omni.isaac.franka import Franka

from tasks.base_task import BaseTask


class IFailure(abc.ABC):
    def __init__(self, name: str, stage_indices: List[int]):
        self._name = name
        self._enabled = True
        self._stage_indices = stage_indices.copy()

        self._robot: Optional[Franka] = None

    def set_robot(self, robot: Franka) -> None:
        self._robot = robot

    @abc.abstractmethod
    def on_stage_completed(self, stage_id: int) -> None:
        ...

    @abc.abstractmethod
    def on_gripper_start_close(self, stage_id: int) -> None:
        ...

    @abc.abstractmethod
    def on_gripper_start_open(self, stage_id: int) -> None:
        ...
