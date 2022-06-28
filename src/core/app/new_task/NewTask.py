from dataclasses import dataclass


@dataclass
class NewTask:
    title: str
    description: str
    due_date: str
