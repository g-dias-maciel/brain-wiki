---
title: Margin Engine Strategy
type: life-domain
created: 2026-04-07
updated: 2026-04-07
sources: [2026-04-07-financial-strategic-advisor-initialization.md]
tags: [finance, investment, leverage, strategy]
aliases: [buy-borrow-die, lombard-strategy]
---

# Margin Engine Strategy

**Life Domain**: Finance  
**Status**: Active Implementation  
**Risk Level**: High (concentrated, leveraged)  
**Time Horizon**: Long-term (10+ years)

## Overview

The Margin Engine is a "Buy, Borrow, Die" strategy using Lombard loans against a concentrated tech ETF portfolio to build wealth while avoiding capital gains taxes.

## Core Components

### 1. Investment Thesis
- **Asset**: 100% QDVE (iShares S&P 500 Information Technology Sector UCITS ETF)
- **Rationale**: Tech sector historical growth (~15-16% p.a.) vs. margin cost (~4% p.a.)
- **Structure**: Irish-domiciled UCITS ETF, USD accumulating
- **ISIN**: IE00B3WJKG14

### 2. Brokerage Setup
- **Current**: Scalable Capital (PRIME+ Tier, Baader Bank)
- **Margin Rate**: 3.00%-4.24% p.a.
- **Target Migration**: Interactive Brokers (IBKR) at €150k-200k portfolio value
- **Migration Reason**: Lower rates, higher credit limits (>€100k)

### 3. Operational Rules

#### Buying Phase (Predator Mode)
```yaml
Normal Operation:
  - Invest: 100% of monthly salary surplus into QDVE
  - LTV Limit: 35% maximum

Market Dip Response:
  - Dip 10%: Start using margin
  - Dip 15%: Aggressive margin buying
  - Dip 20%: Maximum margin utilization
  - Stop: At 35% LTV
```

#### Borrowing Phase
- **Purpose**: Fund large expenses, lifestyle inflation
- **Rule**: Never sell shares for expenses
- **Method**: Draw from margin line as needed

#### Payback Phase (ATH Rule)
- **Trigger**: QDVE at or within 3% of All-Time High
- **Action**: Redirect salary surplus to pay down margin principal
- **Goal**: Reload credit line for next market dip

### 4. Risk Management Framework

| LTV Level | Action | Survival Crash |
|-----------|--------|----------------|
| ≤35% | Normal operation | ~53% |
| >45% | Interest Freeze: Pay interest in cash only | ~40% |
| >55% | Cash Shield: Inject €1,500 emergency buffer | ~30% |
| >60% | Nuclear Option: Sell 10% preemptively | ~25% |
| 70-75% | Bank Liquidation (AVOID) | 0% |

### 5. Tax Optimization

#### German Considerations
- **Exit Tax (Wegzugsbesteuerung)**: €500,000 unrealized gains threshold
- **Strategy**: Diversify before hitting €400,000 in QDVE
- **Alternative ETFs**: Xtrackers Tech, NASDAQ 100 UCITS

#### International Considerations
- **QDVE Advantage**: Irish UCITS avoids 40% US Estate Tax
- **Global Portability**: Can transfer between brokers internationally

## Current Status
- **Implementation Phase**: Active
- **Portfolio Concentration**: 100% QDVE
- **LTV Target**: 35% maximum
- **Cash Buffer**: €1,000-1,500

## Related Strategies
- [[LTV Management]] - Detailed risk protocols
- [[Tax Planning]] - Cross-border tax optimization
- [[Global Migration Timeline]] - Exit strategy from Germany
- [[2026-04-07 Sovereign Predator Strategy]] - Career transition integration
- [[Career Transition Strategy]] - B2B contracting implementation

## Monitoring Metrics
1. **Monthly**: Portfolio value, LTV ratio, margin interest
2. **Quarterly**: Performance vs. benchmarks, tax threshold proximity
3. **Annually**: Strategy review, broker comparison

## Open Questions
1. Diversification timing and ETF selection
2. Interest rate sensitivity analysis
3. Currency hedge requirements (EUR salary → USD ETF)
4. Contingency plans for prolonged bear markets

## Sources
- [[2026-04-07 Financial & Strategic Advisor Initialization]] - Primary strategy document
- [[Comprehensive Context Summary April 2026]] - Additional context