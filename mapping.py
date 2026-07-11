"""
Mapping layer: translates a profitable price event into a predefined operational action.
"""

from dataclasses import dataclass
from typing import Callable

from signal import PriceEvent


@dataclass
class Action:
    name: str
    package: str
    description: str
    handler: Callable[["Action", PriceEvent], None]

    def execute(self, event: PriceEvent) -> None:
        self.handler(self, event)


class ActionMapper:
    """Maps price conditions to registered operational actions."""

    def __init__(self) -> None:
        self._rules: list[tuple[Callable[[PriceEvent], bool], Action]] = []

    def register(
        self, condition: Callable[[PriceEvent], bool], action: Action
    ) -> None:
        """Register an *action* to fire when *condition* returns True."""
        self._rules.append((condition, action))

    def resolve(self, event: PriceEvent) -> Action | None:
        """Return the first action whose condition matches *event*, or None."""
        for condition, action in self._rules:
            if condition(event):
                return action
        return None


# ---------------------------------------------------------------------------
# Default rule set
# ---------------------------------------------------------------------------

def _log_action(action: Action, event: PriceEvent) -> None:
    print(
        f"  [action] '{action.name}' triggered by {event.asset}@{event.price:.2f} "
        f"(package: {action.package})"
    )


def build_default_mapper(profit_threshold: float = 110.0) -> ActionMapper:
    """Return an ActionMapper pre-loaded with the default rule set."""
    mapper = ActionMapper()

    mapper.register(
        condition=lambda e: e.price >= profit_threshold * 1.2,
        action=Action(
            name="high-profit-deploy",
            package="greed-premium-toolkit-1.0.pkg",
            description="Deploy premium toolkit to entire fleet on peak profit signal.",
            handler=_log_action,
        ),
    )

    mapper.register(
        condition=lambda e: e.price >= profit_threshold,
        action=Action(
            name="standard-profit-deploy",
            package="greed-standard-toolkit-1.0.pkg",
            description="Deploy standard toolkit when profit threshold is crossed.",
            handler=_log_action,
        ),
    )

    return mapper
