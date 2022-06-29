from dataclasses import dataclass

from src.base.Id import Id


@dataclass
class DeleteTask:
    task_id: Id
