import re
from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class User:
    email: str
    role: str = 'developer'
    id: UUID = field(default_factory=uuid4)

    def validate_email(self) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, self.email) is not None

    def is_admin(self) -> bool:
        return self.role == 'admin'
