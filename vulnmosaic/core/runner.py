"""Task runner with concurrency controls and timeout handling."""

import asyncio
import structlog
from dataclasses import dataclass

log = structlog.get_logger()


@dataclass
class TaskResult:
    tool: str
    success: bool
    output: str
    duration_ms: float
    evidence_path: str | None = None


async def run_tool(cmd: list[str], timeout: float = 120.0) -> TaskResult:
    """Run an external tool with timeout and capture output."""
    import time
    tool_name = cmd[0] if cmd else "unknown"
    start = time.monotonic()

    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(), timeout=timeout
        )
        elapsed = (time.monotonic() - start) * 1000

        return TaskResult(
            tool=tool_name,
            success=proc.returncode == 0,
            output=stdout.decode(errors="replace"),
            duration_ms=elapsed,
        )

    except asyncio.TimeoutError:
        elapsed = (time.monotonic() - start) * 1000
        log.warning("tool_timeout", tool=tool_name, timeout=timeout)
        return TaskResult(
            tool=tool_name,
            success=False,
            output=f"timeout after {timeout}s",
            duration_ms=elapsed,
        )
