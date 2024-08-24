import os
from logging import Logger
from typing import List, Optional, Tuple

import numpy as np
from omegaconf import DictConfig, OmegaConf

import omni
from omni.isaac.franka import Franka
from omni.isaac.franka.controllers import RMPFlowController

from .fail_instance import IFailure

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(CURRENT_DIR, "configs")


class FailManager:
    def __init__(self, task_name: str):
        # Load config from same location as this script
        cfg_filepath = os.path.join(CONFIGS_DIR, f"{task_name}.yaml")
        self.config = OmegaConf.load(cfg_filepath)

        # Create the failure objects according to the config
        self._fails: List[IFailure] = []
        for fail_cfg in self.config.failures:
            ...

        self._logger: Optional[Logger] = None
        self._robot: Optional[Franka] = None
        self._controller: Optional[RMPFlowController] = None

    def set_logger(self, logger: Logger) -> None:
        self._logger = logger

    def set_robot(self, robot: Franka) -> None:
        self._robot = robot
        for fail in self._fails:
            fail.set_robot(robot)

    def set_controller(self, controller: RMPFlowController) -> None:
        self._controller = controller
        for fail in self._fails:
            fail.set_controller(controller)

    def on_stage_completed(self, stage_id: int) -> None:
        if self._logger:
            self._logger.info(f"Completed stage: {stage_id}")

        for fail in self._fails:
            fail.on_stage_completed(stage_id)

    def on_gripper_start_close(self, stage_id: int) -> None:
        if self._logger:
            self._logger.info(f"Start gripper close: {stage_id}")

        for fail in self._fails:
            fail.on_gripper_start_close(stage_id)

    def on_gripper_start_open(self, stage_id: int) -> None:
        if self._logger:
            self._logger.info(f"Start gripper open: {stage_id}")

        for fail in self._fails:
            fail.on_gripper_start_open(stage_id)
