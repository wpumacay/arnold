import os
from logging import Logger
from typing import Tuple, Optional

import numpy as np
from omegaconf import DictConfig, OmegaConf

import omni
from omni.isaac.franka import Franka
from omni.isaac.franka.controllers import RMPFlowController

CURRENT_DIR = os.path.basename(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(CURRENT_DIR, "configs")


class FailManager:
    def __init__(self, task_name: str):
        # Load config from same location as this script
        cfg_filepath = os.path.join(CONFIGS_DIR, f"{task_name}.yaml")
        fail_cfg = OmegaConf.load(cfg_filepath)

        self._robot: Optional[Franka] = None
        self._logger: Optional[Logger] = None
        self._controller: Optional[RMPFlowController] = None

    def set_robot(self, robot: Franka) -> None:
        self._robot = robot

    def set_logger(self, logger: Logger) -> None:
        self._logger = logger

    def set_controller(self, controller: RMPFlowController) -> None:
        self._controller = controller

    def on_stage_completed(self, stage_id: int) -> None:
        if self._logger:
            self._logger.info(f"Completed stage: {stage_id}")
        # TODO(wilbert): link here to specific failure objects

    def on_gripper_start_close(self, stage_id: int) -> None:
        if self._logger:
            self._logger.info(f"Start gripper close: {stage_id}")

    def on_gripper_start_open(self, stage_id: int) -> None:
        if self._logger:
            self._logger.info(f"Start gripper open: {stage_id}")

    def on_update_target(
        self, target: Tuple[np.ndarray, np.ndarray, bool]
    ) -> Tuple[np.ndarray, np.ndarray, bool]:
        # TODO(wilbert): check if using translation failure
        return (
            target[0] + np.random.rand(*target[0].shape),
            target[1] + np.random.rand(*target[1].shape),
            target[2],
        )
