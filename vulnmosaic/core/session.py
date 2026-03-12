"""Session management: run IDs, target scope, timestamps, artifact paths."""

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class Target:
    """Defines the scope of a scan."""
    hosts: list[str]
    ports: list[str] = field(default_factory=lambda: ["80", "443"])
    exclude: list[str] = field(default_factory=list)

    def validate(self) -> None:
        if not self.hosts:
            raise ValueError("at least one host is required in target scope")


@dataclass
class Session:
    """A single VulnMosaic run."""
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    target: Target | None = None
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    artifacts_dir: Path = field(default_factory=lambda: Path("artifacts"))
    permission_confirmed: bool = False

    def __post_init__(self) -> None:
        self.artifacts_dir = self.artifacts_dir / self.id
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)

    def require_permission(self) -> None:
        """Hard gate: no scanning without explicit permission."""
        if not self.permission_confirmed:
            raise PermissionError(
                "explicit --i-own-this or --have-permission flag required. "
                "vulnmosaic does not scan targets without authorization."
            )
