# American Retirement Account System (ARAS)
## A Framework for Transitioning Social Security Retirement to Privately Owned Accounts

**Status:** Rough draft. Design choices specified. Actuarial modeling needed to calibrate key numbers. Backtesting can be done with available tools to test design resilience.

**Purpose:** To transition the retirement portion of Social Security from a pay-as-you-go system to a system of mandatory, privately owned, inheritable personal accounts, while preserving disability and survivors benefits as a pooled program and providing a minimum floor for those who outlive their accounts or whose accounts are insufficient.

**Scope:** This framework addresses the retirement portion of Social Security only. Supplemental Security Income (SSI) and Medicare are outside its scope and shall continue under existing law.

---

## Section 0: Preamble

The original purpose of Social Security was to prevent poverty in old age. When President Roosevelt signed the Social Security Act in 1935, the nation was in the midst of the Great Depression. The program was designed to provide a baseline of protection against "the loss of a job and against poverty-ridden old age." It was not designed to make anyone wealthy. It was designed to ensure that no American who worked their entire life would spend their final years in destitution.

The current system has drifted from that purpose. It pays benefits to millionaires. It imposes the same tax rate on a worker earning $50,000 and a worker earning $50 million. It has accumulated an estimated $29.3 trillion in unfunded obligations over 75 years, and $71.9 trillion over the infinite horizon, according to the 2026 Social Security Trustees Report. If nothing changes, benefits are estimated to be cut by roughly 22% when the combined trust funds are depleted in 2034, and the very people the system was designed to protect - low-income retirees - will be the hardest hit.

This framework returns Social Security to its original purpose. It creates a system where every worker owns an account that grows over their lifetime. It provides a floor that ensures no one falls into destitution. It asks those with the greatest capacity to contribute more during the transition. And it eliminates the unfunded liability that threatens the entire system.

The goal is not to make everyone equal. The goal is not to make everyone wealthy. The goal is to ensure that no American who works their entire life retires into poverty. That was the promise of 1935. This framework keeps it.

---

## Section 1: Cohort Transition Schedule

**Effective Date:** January 1, 2028 (or January 1 of the year following enactment).

**Age Rule:** For all purposes under this framework, age is determined as of January 1 of each calendar year. Anyone whose birthday falls during that year is treated as having reached that age on January 1.

**Cohort Schedule:**

| Age on Jan 1, 2028 | Birth Year | Old System Contribution | Private Account Contribution |
|---|---|---|---|
| 51+ | 1976 or earlier | 100% | 0% |
| 46-50 | 1977-1981 | 90% | 10% |
| 41-45 | 1982-1986 | 80% | 20% |
| 36-40 | 1987-1991 | 60% | 40% |
| 31-35 | 1992-1996 | 40% | 60% |
| 26-30 | 1997-2001 | 20% | 80% |
| 21-25 | 2002-2006 | 10% | 90% |
| 20 or younger | 2007 or later | 0% | 100% |

**Principle:** No one currently receiving benefits or near retirement is affected. Transition is based on age at effective date. Rules are knowable from day one. The old system winds down gradually as cohorts age out.

**Transition principle:** The transition is a gradual weaning, not a switch. The younger the worker, the less they contribute to the old system and the less legacy benefit they receive. The trade-off is that they contribute more to their private account and have more time for compounding. The older the worker, the more they stay in the old system and the more legacy benefit they receive. The trade-off is that they have less time to build a private account. The cohort schedule is designed so that every cohort receives a fair combination of legacy benefit and private account, proportional to their remaining working years.

---

## Section 2: Contribution Split

**Total payroll contribution:** 12.4% (6.2% employee, 6.2% employer). No change in what either party pays. Only the destination changes.

**Scaled contribution table (Total Base Tax: 12.4%):**

| Annual Wages | Private Account | S&D Pool | Floor Reserve | Public Safety Total |
|---|---|---|---|---|
| Up to $300,000 | 10.4% | 2.0% | 0.0% | 2.0% |
| $300,000 - $1,000,000 | 7.4% | 3.0% | 2.0% | 5.0% |
| $1,000,000 - $5,000,000 | 4.4% | 4.5% | 3.5% | 8.0% |
| Over $5,000,000 | 2.4% | 5.0% | 5.0% | 10.0% |

**Principle:** Everyone pays the same total rate. As wages rise, a smaller share goes into the personal account and a larger share goes into the pooled programs. This prevents the system from becoming an unlimited tax-advantaged wealth transfer vehicle for high earners while preserving the full contribution rate for low and middle earners.

**$5 Million Lifetime Balance Cap:**

During the accumulation phase, if an individual's private ARAS account balance reaches a lifetime value of $5,000,000 (indexed annually for inflation), the account is considered Fully Capitalized. Once that cap is triggered, the worker's private account contribution rate drops instantly to 0%. Their entire 12.4% payroll contribution (along with the temporary surcharge, if applicable) is diverted entirely to the S&D Pool and the Floor Reserve Pool, split according to the board's current allocation. The cap applies only during the accumulation phase, before the account holder begins drawing from the account at age 62. After retirement, the account is governed by the withdrawal formula in Section 6 and is not subject to the cap.

The board shall track each account balance and shall automatically trigger the Fully Capitalized status when an account balance reaches $5,000,000 (indexed) during the accumulation phase. Upon triggering, the board shall notify the centralized clearinghouse, which shall instruct the employer to redirect the private account contribution to the S&D Pool and Floor Reserve Pool in accordance with the scaled contribution table. The board shall publish an annual report on the number of accounts that have reached Fully Capitalized status and the total contributions diverted to the pools.

**Definition of Total Compensation:**

For purposes of this framework, "wages" or "total compensation" means all remuneration and direct or indirect economic benefits derived from employment or self-employment, including but not limited to:

(1) Standard wages, salary, bonuses, commissions, and tips;

(2) Vested stock options and restricted stock units (RSUs) valued at vesting;

(3) Non-qualified deferred compensation valued in the year earned;

(4) Pass-through distributions to an active owner representing payment for services;

(5) Deemed Earned Income via Corporate Perquisites: Any expense paid by a business entity that provides personal life comfort, lifestyle maintenance, or personal consumption for an individual outside the ordinary course of basic business operations. This strictly encompasses:

- Personal security services, bodyguards, and residential security systems provided for the individual or their immediate family.
- Personal travel and transit, including corporate jet usage for non-business travel, personal luxury vehicles, and travel stipends.
- Personal housing, corporate-owned luxury apartments, residential utilities, personal chefs, or domestic staff paid via the corporate ledger.

This definition applies to all workers. However, the board shall focus enforcement and audit resources on individuals with total compensation exceeding $300,000, as low and middle earners have no incentive to reclassify income. The board shall have authority to issue regulations defining and interpreting this section and to prevent reclassification of compensation as non-wage income for the purpose of avoiding ARAS contributions.

**Section 2.4: Minimum Alternative Contribution (MAC) Evasion Penalty Surcharge:**

The Minimum Alternative Contribution (MAC) functions as a punitive enforcement penalty to deter the artificial under-reporting or deceptive non-reporting of Total Compensation. The framework maintains no objection to the provision of corporate perquisites, life-comfort services, or executive security programs, provided such benefits are valued at fair market value under existing IRS fringe benefit valuation rules and documented transparently as earned compensation from the date of inception.

**The Deceptive Trigger:** The MAC Penalty Surcharge shall automatically trigger if an individual's aggregated Total Compensation (inclusive of all base wages, equity, and corporate perquisites) exceeds the $300,000 threshold (as indexed) for the taxable year, but any portion of those compensatory life-comfort expenses or fringe benefits was hidden, un-reported, or left off the primary W-2 filing.

**The Punitive Levy:** For individuals who report their Total Compensation transparently, contributions shall be processed under the standard, non-penalized progressive schedule in Section 2. For individuals who engage in deceptive non-reporting, their right to build private wealth on the hidden portion of their compensation is suspended for that taxable year. The un-reported Total Compensation shall be subjected to the baseline 12.4 percent ARAS contribution rate plus an additional 8 percent MAC Penalty Surcharge, enforcing a combined 20.4 percent penalty rate from the very first dollar of deception. All revenues generated by this penalty shall bypass private accounts entirely and be deposited 100 percent into the Floor Reserve Pool to secure the 28% NAWI safety floor.

**Temporary Legacy Backfill Surcharge (Years 1-25 at full strength):**

| Annual Wages | Total Contribution | Surcharge to Old System |
|---|---|---|
| Up to $400,000 | 12.4% | 0% |
| $400,000 - $600,000 | 13.4% | +1.0% |
| $600,000 - $1M | 14.4% | +2.0% |
| $1M - $2M | 15.4% | +3.0% |
| $2M - $10M | 16.4% | +4.0% |
| Over $10M | 17.4% | +5.0% |

The surcharge is a temporary, transparent tax increase on high earners to fund the transition. It applies at full strength for the first 25 years. Beginning in year 26, each surcharge bracket shall phase down linearly by 1/25th of its original value per year, reaching zero in year 50.

The surcharge shall be deposited into the old system's annual cash flow and used first to pay benefits to current and transition beneficiaries. Any surplus in a given year shall be deposited into the OASI Trust Fund and invested in special-issue Treasury obligations under existing law. The surcharge shall not be deposited into the new system's pools or the private accounts.

**Tax Treatment:** Contributions are made with after-tax dollars and do not reduce taxable income. Withdrawals are not taxed as ordinary income. The account is exempt from estate taxes.

---

## Section 3: Governance and Administration

**Model:** Federal Thrift Savings Plan (TSP) structure, expanded to universal coverage.

**Key features:**

- Independent fiduciary board, legally bound to act solely in participants' interest
- Asset management contracts awarded through full and open competition
- Mandatory rebidding every 2 years
- No single manager may exceed a statutory cap of total system assets (cap to be determined; needs modeling)
- Centralized clearinghouse for employer contributions
- Administrative costs paid by participants, not taxpayers
- Annual public audits and cost disclosure

**Board authority:**

| Element | Set By | Adjustable By |
|---|---|---|
| Total contribution rate (12.4%) | Statute | Congress only |
| Scaled contribution table | Statute | Congress only |
| Surcharge schedule | Statute | Congress only |
| Individual account glide path | Statute | Congress only |
| Pool split (S&D vs. Floor) | Board, within guardrails | Board |
| Pool investment allocation | Board, within guardrails | Board |
| Withdrawal formula | Board, reviewed annually | Board |
| Total compensation definition | Statute | Board regulations |
| MAC trigger and rate | Statute | Congress only |

**Pool guardrails:**

- S&D pool: 2.0% - 7.0% of payroll
- Floor Reserve: 0.0% - 7.0% of payroll
- Combined total: not less than 2.0%, not more than 12.4% of payroll
- Minimum S&D: 2.0%
- Minimum Floor: 0.0%

For workers who have reached the $5 million lifetime balance cap, the full 12.4% contribution shall be split between the S&D pool and the Floor Reserve according to the board's current allocation.

**Administrative costs:** Paid by participants from account assets. Board may charge a fee not to exceed 0.10% of assets annually. If a higher fee is necessary, the board reports to Congress and justifies the increase. No administrative costs paid from general revenue. Voting system costs included in the administrative cost ratio and published separately.

**Asset manager concentration:** No single asset manager may manage more than a statutory cap of total system assets. The cap is to be determined by modeling. Contracts rebid every 2 years.

---

## Section 4: Investment Menu

**Core funds (five, passive index):**

| Fund | Tracks | Asset Class |
|---|---|---|
| G Fund | Government securities | Bonds |
| F Fund | Bloomberg US Aggregate | Bonds |
| C Fund | S&P 500 | Large-cap US stocks |
| S Fund | Dow Jones US Completion TSM | Small/mid-cap US stocks |
| I Fund | MSCI EAFE | International stocks |
| L Funds | Automatically balanced between the above five funds based on age | Composite |

**Mandatory glide path for individual accounts (statutory, firm floor, not ceiling, stepped not linear):**

| Age | Minimum % in G/F Funds | Maximum % in Stocks |
|---|---|---|
| 50 | 20% | 80% |
| 55 | 30% | 70% |
| 60 | 40% | 60% |
| 65 | 50% | 50% |
| 70+ | 60% | 40% |

**Principle:** The bond floor steps up by 10 percentage points every 5 years from age 50 to age 70, then caps at 60% for all ages above 70. This keeps 40% in stocks throughout retirement for inflation protection while maintaining substantial protection against a market crash. Account holders may choose a more conservative allocation than the floor requires but may not choose a less conservative allocation. The L Funds automatically comply with the mandatory glide path.

**Pool investments:** The S&D pool and Floor Reserve use the same five funds. The board sets allocations within statutory guardrails (equities 40%-70% for S&D; 20%-50% for Floor). The board publishes an annual report showing current allocation, rationale for any changes, and projected solvency over 25, 50, and 75 years.

---

## Section 5: Voting and Proxy

**Rule:**

1. Participants who vote: shares voted as instructed.
2. Participants who don't vote: shares voted in same proportions as votes cast by other participants who did vote.
3. Zero participation: fiduciary board votes each share independently.
4. No minimum participation threshold.

**Voting interface:** Electronic, secure, delivered at least 30 days before the meeting. Cost included in administrative fee.

---

## Section 6: Withdrawal Design

**Principle:** Account is yours. Withdrawals designed to last to age 90. No pooling. 100% inheritability. Floor catches those who live past 90 or whose accounts are depleted.

| Feature | Design |
|---|---|
| Earliest access age | 62 (statutory, no exceptions except terminal illness) |
| Withdrawal calculation | Recalculated annually using annuity formula, designed to deplete at 90, assuming 3% nominal return |
| Annual adjustment | Recalculated each year based on actual balance |
| Required minimum distributions | None |
| Estate tax | Exempt |
| Inheritability | 100% of remaining balance passes to heirs |
| If you live past 90 | Minimum floor kicks in (subject to means test) |
| Pooling | None |
| Formula-setting | Board recalculates annually using mortality tables |

**Withdrawal formula (for scoring purposes):**

The monthly withdrawal shall be recalculated annually based on the account balance at the beginning of each year, the remaining months to age 90, and a nominal return assumption of 3% per year. The withdrawal shall be calculated using a standard annuity formula designed to deplete the account by age 90. If actual returns exceed the assumed rate, the following year's monthly withdrawal shall be adjusted upward accordingly. If actual returns fall short, the following year's monthly withdrawal shall be adjusted downward accordingly. If the recalculated withdrawal falls below the minimum floor threshold, the floor shall supplement the difference. Any remaining balance at death passes to designated beneficiaries.

**Terminal illness exception:**

Upon certification by a licensed physician that an account holder has a terminal illness with a life expectancy of less than 12 months, the account holder may withdraw any or all of their private account balance without penalty or reduction. By electing terminal illness access, the account holder acknowledges that any remaining balance, if any, shall pass to designated beneficiaries, and that if the account holder survives beyond the certification period, they shall not be eligible for the minimum floor or any other ARAS backstop. This election is irrevocable.

**Market risk acknowledgment:**

The private account is invested in the market. Markets go up and down. The account balance at retirement depends on the sequence of returns during the accumulation phase, and the monthly withdrawal depends on the sequence of returns during the drawdown phase. This is a real risk, and it cannot be fully eliminated.

The framework mitigates this risk in three ways:

(1) The mandatory glide path shifts the account toward bonds as the worker approaches retirement, reducing exposure to a market crash in the critical final years.

(2) The withdrawal formula is designed to last to age 90, providing a margin of safety for most retirees.

(3) The minimum floor catches those whose accounts are depleted or insufficient, preventing destitution.

These mitigations do not eliminate market risk. They reduce it to a level the framework's designers judged acceptable. Under the current system, the risk is different: benefits are estimated to be cut by roughly 22% when the trust fund depletes, or taxes will be increased, or the retirement age will be raised. Those are also real risks, and they are not mitigated by anything in current law. The framework trades one set of risks for another, more acceptable set of risks. It does not eliminate risk.

**Account access and allocation changes:**

Each account holder shall have secure, real-time access to their account balance, contribution history, and projected retirement income through an online portal and mobile application. Account holders may change their investment allocation once per calendar year. The mandatory glide path specified in Section 4 shall apply as a hard floor; account holders may choose a more conservative allocation than the floor requires but may not choose a less conservative allocation. Default enrollment shall be in the L Fund appropriate to the account holder's birth year. Contributions shall post to the account within 3 business days of receipt by the clearinghouse. The board shall publish an annual statement of administrative costs and fund expenses for each account.

---

## Section 7: Minimum Floor

| Feature | Design |
|---|---|
| Qualification | Account depleted OR insufficient balance at retirement, AND total retirement income below floor threshold, AND liquid assets below board-set threshold |
| Floor amount | 28% of the National Average Wage Index (NAWI), divided by 12 |
| Funding | Floor Reserve pool, backed by general revenue if depleted |
| Phase-out | Income and asset test as specified; no floor for those with substantial means |
| Purpose | Backstop against destitution, not universal supplement |

**Floor calculation:**

The minimum floor shall be calculated as 28% of the National Average Wage Index (NAWI), as published annually by the Social Security Administration, divided by 12 to determine the monthly floor amount. For 2025, using the NAWI of $72,011.81, the floor would be $1,680.28 per month. The floor shall be adjusted annually based on the NAWI. This replaces the previous SSI tie.

**Means test:**

The minimum floor shall be available to any qualifying individual who meets both of the following conditions:

(1) The individual's total retirement income, including any private account withdrawal, falls below the floor threshold; and

(2) The individual's liquid assets, excluding the primary residence, fall below a threshold to be determined by the board and adjusted annually for inflation.

For scoring purposes, the liquid asset threshold shall be assumed to be $50,000 for an individual, indexed annually by the National Average Wage Index (NAWI). The primary residence shall be excluded. The board may adjust this threshold within a range of $25,000 to $100,000, indexed, based on actuarial review.

The floor shall be available to two populations: (a) individuals whose private account balance at retirement is insufficient to generate a monthly withdrawal at or above the floor threshold, and (b) individuals whose private account is depleted after retirement. In both cases, the means test in this section shall apply.

The floor shall be calculated as the difference between the individual's actual retirement income and the floor threshold. The floor shall be adjusted annually based on the NAWI. The floor shall not be available to individuals who elected terminal illness access and survived beyond the certification period, as specified in Section 6. The floor shall not be available to individuals whose liquid assets exceed the threshold, regardless of income.

The purpose of the floor is to prevent destitution, not to supplement adequate retirement savings. No individual with substantial means shall draw from the pooled funds.

**If the Floor Reserve is depleted:**

If the board determines that the Floor Reserve is estimated to be depleted within 10 years despite adjustments within the board's authority, the board shall publish a report and recommend corrective action to Congress. Congress shall then determine whether to increase the total contribution rate, adjust the scaled contribution table, appropriate general revenue, or take other action. If Congress does not act, the full faith and credit of the United States shall back the floor obligations to the extent of available appropriations.

**Legacy Benefit Phase-Out for High-Balance Retirees:**

Transition cohort members whose monthly ARAS withdrawal exceeds the following thresholds shall have their legacy Social Security benefit reduced:

| Monthly ARAS Withdrawal | Legacy Benefit Reduction |
|---|---|
| Under $3,000 | 0% |
| $3,000 - $5,000 | 25% |
| $5,000 - $8,000 | 50% |
| $8,000 - $12,000 | 75% |
| Over $12,000 | 100% |

A worker with $3,000+/month from ARAS, plus legacy Social Security, plus a 401(k), plus other investments is not the population Social Security was designed to protect. The phase-out redirects limited old-system resources to people who actually need them.

---

## Section 8: Disability and Survivors (S&D)

| Feature | Design |
|---|---|
| Program name | Survivors and Disability (S&D) |
| Funding | S&D pool, funded by scaled contribution table |
| Structure | Separate pooled program with trust fund |
| Disability | Same eligibility as current SSDI |
| Survivors | Same structure as current Social Security survivors benefits |
| Administration | SSA determines eligibility and administers payments using current standards; S&D board sets benefit formula and eligibility standards; SSA reimbursed from S&D pool |

**Survivor/account interaction:**

Survivor benefits under the S&D program shall be calculated and paid under the same rules as current Social Security survivor benefits, including the application of the family maximum. The private account balance of a deceased worker shall be paid to the designated beneficiaries in accordance with the account's inheritance rules. Receipt of a private account balance shall not reduce, offset, or otherwise affect the calculation or payment of S&D survivor benefits.

---

## Section 9: Transition Financing

**Principle:** The transition is not free. Congress chooses the mechanism. Full funding required.

**Framework language:**

> *"The transition to personal accounts shall be implemented gradually by cohort, as specified in Section 1. The old system shall continue to receive contributions from transition cohorts at the rates specified and shall continue to pay benefits to current and transition beneficiaries. The old system's trust fund shall be drawn down as needed. Congress shall determine the specific mix of revenue measures, spending offsets, or borrowing to cover any shortfall during the transition period. The framework requires that the transition be fully funded so that the new system does not inherit the old system's unfunded liabilities."*

**Transition cost acknowledgment:**

The transition to personal accounts is not free. The old system's obligations to current retirees and transition cohorts must be paid while the new system is being funded. This is a real cost, and it will be paid by someone - through taxes, spending offsets, borrowing, or a combination. The framework does not pretend otherwise.

However, the cost of not transitioning is also real, and it is larger. The current system faces an estimated 75-year unfunded obligation of roughly $29.3 trillion and an infinite horizon unfunded obligation of roughly $71.9 trillion, according to the 2026 Social Security Trustees Report. If nothing is done, benefits are estimated to be cut automatically by roughly 22% when the combined trust funds are depleted in 2034, or Congress will be forced to raise taxes, cut spending, or borrow to cover the gap. Those costs are not hypothetical. They are already scheduled to arrive.

The transition cost is the price of moving to a system that is structurally solvent. Once the transition is complete, the new system does not have an unfunded liability. The old system's shortfall is permanent; the transition cost is temporary. The framework requires that Congress choose how to fund it, but it does not pretend the cost doesn't exist.

**Existing trust fund treatment:**

The existing Social Security trust fund shall remain with the old system. It shall be drawn down as needed to pay benefits to current retirees and transition cohorts as they age out. When the trust fund is depleted, Congress shall cover the old system's remaining obligations from general revenue, or through such other funding mechanisms as it determines. No portion of the existing trust fund shall be transferred to the new pools, the private accounts, or any other component of the new system.

**Current beneficiary funding:**

Current beneficiaries and transition cohorts shall receive benefits calculated under the existing formula using their actual earnings record, subject to the legacy benefit phase-out for high-balance retirees specified in Section 7. The old system's obligations shall be funded first from remaining payroll tax contributions from transition cohorts, then from the Temporary Legacy Backfill Surcharge, then from the existing trust fund, and finally from general revenue as needed. Congress shall appropriate such sums as are necessary to ensure that no beneficiary receives an unexpected reduction in benefits during the transition period, other than the phase-out specified in Section 7. The framework does not prescribe a specific funding mechanism for any remaining transition shortfall; Congress shall determine the mix of revenue measures, spending offsets, or borrowing on an annual basis.

**Transition cohort benefit formula:**

Transition cohort members shall have their Social Security benefit calculated under the existing benefit formula using their actual earnings record, regardless of the contribution rate applicable during the transition period. The contribution rate determines where the money goes, not what the worker earned. The private account balance shall be paid separately. The legacy benefit phase-out for high-balance retirees specified in Section 7 shall apply.

**Long-term savings:**

The current pay-as-you-go system has an estimated infinite horizon unfunded obligation of roughly $71.9 trillion and no end to its unfunded liabilities. This framework has an estimated 100-year cost of roughly $38.5 trillion, with the deficit estimated to be fully extinguished by year 50. The transition cost is temporary. The savings are permanent. Once the transition is complete, the federal government is estimated to be permanently freed from funding legacy retirement benefits, and those resources can be used for debt reduction, infrastructure, or other national priorities.

All figures in this framework are estimates based on current demographic, economic, and actuarial assumptions. Actual costs and savings will depend on future conditions and will be subject to periodic review and adjustment. The framework is intended to be scored, critiqued, and revised. The estimates are the starting point for analysis, not the conclusion.

---

## Section 10: Self-Employed Workers

Self-employed workers shall contribute to the new system at the same total rate as employee-employer pairs, calculated on net earnings from self-employment as defined under existing law. Contributions shall be split between the private account, the S&D pool, and the Floor Reserve using the same scaled contribution table applicable to wage earners. Self-employed workers shall remit contributions to the centralized clearinghouse in the same manner as employers. The existing SECA framework shall be adapted to route contributions to the new system.

---

## Section 11: Federal Workers

Federal employees shall participate in the new system on the same terms as private-sector workers. The 6.2% employee contribution and the 6.2% employer contribution shall be routed to the employee's ARAS private account, the S&D pool, and the Floor Reserve as specified in the scaled contribution table. Contributions shall be made with after-tax dollars and shall not reduce taxable income. Withdrawals shall not be taxed as ordinary income.

Federal employees shall retain their existing Thrift Savings Plan accounts and any associated matching contributions. The TSP shall continue to operate as a supplemental retirement plan. Federal employees shall have two separate accounts: the existing TSP and the new ARAS account.

---

## Section 12: SSI and Medicare

Supplemental Security Income (SSI) and Medicare are outside the scope of this framework. Both programs shall continue to operate under existing law, with existing funding mechanisms, eligibility standards, and administrative structures. Nothing in this framework shall be construed to alter, reduce, or redirect funding for SSI or Medicare. The Social Security Administration shall continue to administer SSI and Medicare enrollment as under current law.

---

## Section 13: Actuarial Assumptions and Modeling Notes

**What can be modeled with available tools:**

- Backtesting of glide path against historical crashes (2008, 2000-2002, 1929-1932)
- Withdrawal sustainability under different return sequences
- Account balance projections for different wage levels
- Cohort transition outcomes under different scenarios
- Floor take-up estimates under different assumptions

**What needs formal actuarial scoring:**

- Official SSA actuarial score
- DYNASIM or Urban Institute distributional analysis
- CBO cost estimate
- Long-term trust fund projections

**Assumptions to be specified:**

- Real market returns (equity, bond, blended)
- Mortality tables (current and projected)
- Wage growth
- Inflation (CPI-W)
- Administrative costs at scale
- Participation rates in voting

**Scoring assumptions specified in this draft:**

| Assumption | Placeholder Value |
|---|---|
| Surcharge phase-down | Linear, 1/25th of original value per year, zero at year 50 |
| Floor liquid asset threshold | $50,000 individual, indexed by NAWI, range $25K-$100K |
| Withdrawal formula | Annual recalculation, 3% nominal return, deplete at 90 |
| Glide path | Stepped, capped at 60% bonds at age 70+ |
| Floor amount | 28% of NAWI, divided by 12. For 2025: $1,680.28/month |
| Private account cap | $5,000,000 lifetime balance, indexed, accumulation phase only |
| MAC penalty rate | 8% of hidden compensation, plus 12.4% base rate, total 20.4% |

---

## Section 14: Open Questions

1. Exact cohort contribution percentages (needs transition cost modeling)
2. Asset manager concentration cap (needs antitrust and market analysis)
3. S&D adequacy at 2% base payroll (needs actuarial scoring)
4. Voting interface design (needs operational planning)
5. Employer compliance mechanism (needs administrative design)
6. Transition financing total (needs official scoring)
7. Administrative cost projections at universal scale (needs modeling)
8. Pool guardrail calibration (needs actuarial review)
9. Terminal illness certification process (needs administrative design)
10. Total compensation regulations (needs administrative design)
11. MAC enforcement mechanism (needs administrative design)

---

## Next Steps

1. Run glide path backtests against 2008, 2000-2002, 1929-1932
2. Model withdrawal sustainability under historical sequences
3. Project account balances for different wage levels and contribution histories
4. Estimate cohort transition outcomes
5. Estimate floor take-up and cost
6. Refine all placeholder numbers
7. Assemble final document for think tank scoring

---

*This draft is a work in progress. It is intended to be scored, critiqued, and revised. The numbers are estimates. The design is the starting point for analysis, not the conclusion.*
