import abc
from typing import List, Optional

import numpy as np
from omegaconf import DictConfig

import omni
from omni.isaac.franka import Franka
from omni.isaac.franka.controllers import RMPFlowController

from tasks.base_task import BaseTask


class IFailure(abc.ABC):
    def __init__(self, name: str, stage_indices: List[int]):
        self._name = name
        self._enabled = True
        self._stage_indices = stage_indices.copy()

        self._robot: Optional[Franka] = None
        self._controller: Optional[RMPFlowController] = None

    def set_robot(self, robot: Franka) -> None:
        self._robot = robot

    def set_controller(self, controller: RMPFlowController) -> None:
        self._controller = controller

    @abc.abstractmethod
    def on_stage_completed(self, stage_id: int) -> None:
        ...

    @abc.abstractmethod
    def on_gripper_start_close(self, stage_id: int) -> None:
        ...

    @abc.abstractmethod
    def on_gripper_start_open(self, stage_id: int) -> None:
        ...
