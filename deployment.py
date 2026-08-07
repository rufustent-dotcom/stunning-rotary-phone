"""
Deployment layer: simulates Jamf Now fleet deployment of a selected package.
"""

import random
import time
from dataclasses import dataclass, field

from mapping import Action
from signal import PriceEvent


@dataclass
class DeploymentRecord:
    action: Action
    event: PriceEvent
    device_count: int
    success: bool
    timestamp: float = field(default_factory=lambda: time.time())

    def __str__(self) -> str:
        status = "OK" if self.success else "FAILED"
        return (
            f"[{status}] {self.action.package} → {self.device_count} device(s) "
            f"@ {self.event.asset}={self.event.price:.2f}"
        )


class JamfNowDeployer:
    """Simulates the Jamf Now Blueprint deployment pipeline.

    In a real implementation this class would call the Jamf Now REST API to:
      1. Upload the .pkg file to the distribution point.
      2. Attach it to a Blueprint.
      3. Push the Blueprint to all managed devices.
    """

    def __init__(
        self,
        fleet_size: int = 10,
        simulate_failure_rate: float = 0.05,
    ) -> None:
        self.fleet_size = fleet_size
        self.simulate_failure_rate = simulate_failure_rate
        self.history: list[DeploymentRecord] = []

    def deploy(self, action: Action, event: PriceEvent) -> DeploymentRecord:
        """Push *action.package* to the entire managed fleet.

        Returns a DeploymentRecord describing the outcome.
        """
        print(f"  [deploy] Pushing '{action.package}' to {self.fleet_size} device(s) …")

        # Simulate network/API latency.
        time.sleep(0.1)

        success = random.random() > self.simulate_failure_rate
        record = DeploymentRecord(
            action=action,
            event=event,
            device_count=self.fleet_size,
            success=success,
        )
        self.history.append(record)
        print(f"  [deploy] {record}")
        return record

    def summary(self) -> None:
        """Print a summary of all deployments made in this session."""
        total = len(self.history)
        succeeded = sum(1 for r in self.history if r.success)
        print(f"\n=== Deployment summary: {succeeded}/{total} succeeded ===")
        for record in self.history:
            print(f"  {record}")
