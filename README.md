
# stunning-rotary-phone

Greed defines an automated operational architecture in which a live profitability signal
can trigger coordinated software changes across a managed device fleet.

## Closed-loop architecture

The repository models a three-stage loop:

1. **Signal: most profitable trending price**
   - A live market or pricing feed acts as the input layer.
   - An agent watches the feed continuously for a target profit condition instead of
     waiting for a human operator to notice it.

2. **Logic: system mapping**
   - A mapping layer translates the live price event into a predefined operational action.
   - The mapping determines which software package, configuration, or local workflow must
     be activated when the target trend is reached.

3. **Execution: Jamf Now deployment**
   - The selected package is delivered through Jamf Now.
   - Blueprints push the change across managed Mac devices so the fleet aligns with the
     active market opportunity without manual IT intervention.

## Intended perspective

This architecture should be understood primarily as an **enterprise operational loop**,
not as a direct automated asset-trading engine.

The trending price is the external trigger, but the action taken here is fleet-wide
software orchestration: detecting a profitable condition, mapping it to an approved
system response, and deploying the required tools or updates to end-user machines.

## Operational boundaries

- Market data may trigger action, but deployment rules should remain explicitly mapped and
  controlled.
- Jamf Now is the action layer for managed-device execution, not the decision-making layer.
- The value of the system comes from compressing the path from signal detection to approved
  infrastructure response.

## Implementation

| Module | Role |
|---|---|
| `signal.py` | Simulates a live price feed and detects profitable trending peaks |
| `mapping.py` | Translates price events to predefined operational actions |
| `deployment.py` | Simulates Jamf Now Blueprint deployment across managed devices |
| `greed.py` | Entry point that wires the three stages into a closed loop |

### Quick start

```bash
python greed.py
```

### Options

```
--asset          Asset name (default: GREED)
--base-price     Starting price (default: 100.0)
--threshold      Profit trigger price (default: 110.0)
--volatility     Price swing per tick (default: 6.0)
--fleet-size     Number of managed devices (default: 10)
--ticks          Simulated price ticks before stopping (default: 50)
--tick-interval  Seconds between ticks (default: 0.1)
```
World
