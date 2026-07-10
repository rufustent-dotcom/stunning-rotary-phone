"""
Greed – closed-loop orchestration entry point.

Runs the three-stage pipeline:
  1. Signal  – detect the most profitable trending price
  2. Logic   – map the price event to an operational action
  3. Execute – deploy the action via the Jamf Now fleet layer
"""

import argparse
import sys

from deployment import JamfNowDeployer
from mapping import build_default_mapper
from signal import PriceFeed, detect_trending_peak


def run(
    asset: str = "GREED",
    base_price: float = 100.0,
    profit_threshold: float = 110.0,
    volatility: float = 6.0,
    fleet_size: int = 10,
    ticks: int = 50,
    tick_interval: float = 0.1,
) -> None:
    print("=== Greed: closed-loop orchestration started ===")
    print(
        f"Asset={asset}  base={base_price}  threshold={profit_threshold}  "
        f"fleet={fleet_size}  ticks={ticks}\n"
    )

    feed = PriceFeed(
        asset=asset,
        base_price=base_price,
        volatility=volatility,
        profit_threshold=profit_threshold,
        tick_interval=tick_interval,
    )
    mapper = build_default_mapper(profit_threshold=profit_threshold)
    deployer = JamfNowDeployer(fleet_size=fleet_size)

    deployments = 0
    for event in detect_trending_peak(feed, window=5):
        print(f"[signal] Profitable peak detected: {event.asset}@{event.price:.2f}")

        action = mapper.resolve(event)
        if action is None:
            print("  [mapping] No matching action for this event – skipping.")
            continue

        deployer.deploy(action, event)
        deployments += 1

        # Stop after the configured number of ticks have been consumed.
        # detect_trending_peak itself drives the feed; we count deployments here.
        if deployments >= max(1, ticks // 10):
            break

    deployer.summary()
    print("\n=== Greed: session complete ===")


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Greed – signal-to-fleet orchestration loop"
    )
    parser.add_argument("--asset", default="GREED")
    parser.add_argument("--base-price", type=float, default=100.0)
    parser.add_argument("--threshold", type=float, default=110.0)
    parser.add_argument("--volatility", type=float, default=6.0)
    parser.add_argument("--fleet-size", type=int, default=10)
    parser.add_argument("--ticks", type=int, default=50,
                        help="Number of price ticks to simulate before stopping")
    parser.add_argument("--tick-interval", type=float, default=0.1,
                        help="Seconds between simulated ticks")
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = _parse_args(sys.argv[1:])
    run(
        asset=args.asset,
        base_price=args.base_price,
        profit_threshold=args.threshold,
        volatility=args.volatility,
        fleet_size=args.fleet_size,
        ticks=args.ticks,
        tick_interval=args.tick_interval,
    )
