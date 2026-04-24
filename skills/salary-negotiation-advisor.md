# Salary Negotiation Advisor

## Purpose
Navigate salary negotiations strategically - from initial salary discussions to offer evaluation to counter-offer crafting. Maximize compensation while maintaining positive relationships and understanding your market value.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Location**: Ecuador (remote work)
- **Salary Range**: Minimum $2,000 USD (dealbreaker), Target $3,200-5,000 USD
- **Negotiation Style**: Professional, data-driven, collaborative (not adversarial)
- **Leverage Points**: B2B SaaS expertise, first design hire experience, team scaling, remote work effectiveness

## Input
- Offer details (base salary, equity, benefits, etc.)
- Company context (stage, funding, location)
- Your priorities (cash vs. equity, title, flexibility)
- Market data (if available)
- Your walk-away point

## Output
- Offer evaluation and analysis
- Market benchmarking
- Negotiation strategy
- Counter-offer scripts
- Decision framework
- Saved to database for learning

---

## NEGOTIATION DATABASE MANAGEMENT

### Database Structure
**File**: `/data/salary-negotiations.json`

**Schema**:
```json
{
  "negotiations": [
    {
      "id": "neg_001",
      "company": "Remote.com",
      "role": "Senior Product Designer",
      "date_received": "2025-04-24",
      "initial_offer": {
        "base_salary": 4500,
        "currency": "USD",
        "equity": "0.05%",
        "equity_type": "stock_options",
        "bonus": "10% target",
        "benefits": ["health_insurance", "unlimited_pto", "home_office_stipend"],
        "other": "Annual learning budget $2000"
      },
      "counter_offer": {
        "base_salary": 5000,
        "equity": "0.08%",
        "signing_bonus": 5000,
        "rationale": "Market rate for senior B2B SaaS designers with leadership experience"
      },
      "final_offer": {
        "base_salary": 4800,
        "equity": "0.06%",
        "signing_bonus": 3000,
        "additional": "Guaranteed 6-month review with equity refresh"
      },
      "outcome": "accepted",
      "learnings": [
        "They moved on equity but not much on base",
        "Signing bonus was easier to negotiate than base",
        "6-month review commitment was valuable"
      ],
      "total_comp_initial": 4950,
      "total_comp_final": 5200
    }
  ],
  "market_data": {
    "role": "Senior Product Designer",
    "location": "Remote (Global)",
    "experience": "10+ years",
    "specialization": "B2B SaaS",
    "data_points": [
      {
        "source": "Levels.fyi",
        "p25": 3500,
        "p50": 4200,
        "p75": 5500
      }
    ]
  }
}
```

### Workflow Instructions for Claude Code

#### WHEN offer received:
1. **Capture all offer details** - base, equity, benefits, timeline
2. **Research market rates** - use available data sources
3. **Calculate total comp** - apples-to-apples comparison
4. **Generate negotiation strategy** - based on leverage and priorities
5. **Save to database** for learning

#### AFTER negotiation:
1. **Record outcome** - accepted, declined, countered
2. **Capture learnings** - what worked, what didn't
3. **Update market data** - your data point added
4. **Review patterns** - build negotiation playbook

---

## Offer Evaluation Framework

### STEP 1: Capture All Components

**Base Salary**:
- Annual amount
- Currency
- Payment frequency (monthly, bi-weekly)

**Equity**:
- Type (stock options, RSUs, phantom stock)
- Percentage or number of shares
- Vesting schedule (typical: 4 years, 1-year cliff)
- Strike price (for options)
- Current valuation (for equity value calculation)

**Bonus**:
- Target percentage
- Performance-based or guaranteed
- Payment schedule

**Benefits**:
- Health insurance (employee only or family)
- Retirement/401k matching
- PTO/vacation days
- Sick leave
- Parental leave
- Professional development budget
- Home office stipend
- Equipment provided
- Coworking space allowance

**Other**:
- Signing bonus
- Relocation assistance
- Visa sponsorship
- Flexible schedule
- Remote work policy
- Performance review schedule

---

### STEP 2: Calculate Total Compensation

**Formula**:
```
Total Comp = Base + Bonus (expected) + Equity (annual value) + Benefits (cash value)
```

**Example Calculation**:
```
Base Salary:              $4,500/month × 12 = $54,000
Target Bonus:             10% of base        = $5,400
Equity (annual):          0.05% / 4 years    = ~$2,000 (conservative)
Benefits (cash value):    Health insurance   = $6,000
                          Learning budget    = $2,000
                          Home office        = $1,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Compensation:                           $70,400/year
Effective Monthly:                            $5,867
```

**Equity Valuation Note**:
- Early-stage (Seed/Series A): Value equity at $0 (high risk)
- Growth-stage (Series B/C): Use 25-50% of paper value
- Late-stage/Pre-IPO: Use 50-75% of paper value
- Public company: Use current market value

---

### STEP 3: Benchmark Against Market

**Data Sources**:
1. **Levels.fyi**: Tech compensation data (most reliable)
2. **Glassdoor**: Salary reports (directional)
3. **LinkedIn Salary**: Industry averages
4. **Blind**: Anonymous tech worker discussions
5. **Design community**: Designer Hangout, ADPList discussions
6. **Your network**: Ask peers (in confidence)

**Your Market Positioning**:
```
Role: Senior Product Designer
Experience: 10+ years
Specialization: B2B SaaS, Design Systems, Team Scaling
Location: Remote (global companies)
Company Stage: Series A-C preferred

Market Ranges (USD, remote):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
25th percentile:  $3,500/month ($42,000/year)
50th percentile:  $4,200/month ($50,400/year)
75th percentile:  $5,500/month ($66,000/year)
90th percentile:  $7,000/month ($84,000/year)

Your Target Range: $3,200-5,000/month
Your Minimum: $2,000/month (dealbreaker)
```

**Evaluation**:
- Below 25th percentile → Definitely negotiate
- 25th-50th percentile → Negotiate if possible
- 50th-75th percentile → Negotiate for top of band
- Above 75th percentile → May not need to negotiate base (focus on equity/benefits)

---

### STEP 4: Assess Non-Salary Factors

**Factors That Increase Offer Value**:
✅ Full remote flexibility (no required office days)
✅ Async-first culture (timezone flexibility)
✅ Generous PTO (20+ days + holidays)
✅ Learning & development budget ($1,500+ annually)
✅ Equity with clear exit potential
✅ Strong leadership/mentorship opportunities
✅ Impact/scope (Lead role vs. IC)
✅ Company mission alignment

**Factors That Decrease Offer Value**:
❌ Hybrid requirement (especially in Ecuador)
❌ Limited PTO (<15 days)
❌ No professional development budget
❌ Equity in early-stage with unclear path
❌ Limited growth opportunity
❌ Poor company culture signals

**Your Priorities** (Ranked):
1. Base salary (must meet $3,200+ for comfort)
2. Remote flexibility (100% remote, async-friendly)
3. Growth opportunity (Lead/Principal path)
4. Equity (if Series A+)
5. Learning budget
6. Title (Senior+ for career progression)

---

## Negotiation Strategy

### WHEN TO NEGOTIATE

**Always Negotiate When**:
✅ Offer is below market (25th-50th percentile)
✅ Offer is below your target range
✅ You have competing offers
✅ You have unique leverage (rare skills, proven track record)
✅ Initial offer leaves room (first offer is rarely final)

**Consider NOT Negotiating When**:
⚠️ Offer is at/above 75th percentile and meets all priorities
⚠️ You're already at top of their stated band
⚠️ You have zero leverage (no other options, desperate)
⚠️ Company is transparent startup with fixed bands

**Still Express Enthusiasm Even If Not Negotiating**:
"I'm excited about this opportunity. The offer is strong and meets my expectations. I'd like to accept."

---

### NEGOTIATION LEVERAGE POINTS

**Your Leverage**:
1. **Specialized expertise**: B2B SaaS, fintech, complex products
2. **Leadership experience**: First design hire, team scaling
3. **Track record**: Measurable outcomes (87% onboarding reduction, etc.)
4. **Multiple offers**: If you have them (be honest)
5. **Unique value**: Remote work effectiveness, bilingual, timezone flexibility
6. **Scarcity**: Senior designers with your profile are in demand

**Company's Leverage**:
1. **Budget constraints**: Early-stage startups have fixed budgets
2. **Equity compensation**: Can offer more equity than cash
3. **Band limits**: HR-defined salary bands
4. **Timeline pressure**: If they need to fill quickly

**How to Increase Your Leverage**:
- Have multiple offers (or at least multiple active conversations)
- Demonstrate unique value during interview process
- Show you're not desperate (professional, not pushy)
- Research their funding/financial health

---

### NEGOTIATION TIMELINE

**Day 0: Offer Received**
- Thank them enthusiastically
- Ask for offer in writing
- Request 3-5 business days to review
- DO NOT accept or counter immediately

**Day 1-2: Evaluation**
- Calculate total comp
- Benchmark against market
- Identify gaps vs. your target
- Consult with trusted advisors (not publicly)

**Day 3-4: Prepare Counter**
- Decide what to ask for (base, equity, benefits)
- Prepare rationale (data-driven, not emotional)
- Script your counter-offer
- Practice delivery

**Day 5: Deliver Counter**
- Schedule call (better than email for nuance)
- Express enthusiasm first
- Present counter with rationale
- Give them time to consider

**Day 6-10: Await Response**
- They may come back with:
  - Full acceptance (rare)
  - Partial movement (common)
  - No movement (possible)
- Be prepared to accept, counter again, or walk away

---

### WHAT TO NEGOTIATE (Priority Order)

**Tier 1: Easiest to Negotiate**

1. **Signing Bonus**
   - One-time, doesn't affect ongoing budget
   - Easier for companies than base salary increase
   - Ask: $3,000-10,000 depending on level

2. **Start Date**
   - Delay 2-4 weeks if needed
   - Gives you transition time

3. **Title**
   - Sometimes free for company
   - "Senior" vs. "Lead" can matter for career

4. **Professional Development Budget**
   - Ask: $1,500-3,000 annually
   - Conferences, courses, books

5. **Equipment/Home Office Stipend**
   - Ask: $1,500-3,000 one-time or $500/year ongoing

**Tier 2: Moderate Difficulty**

6. **Equity**
   - Easier to negotiate at startups
   - Can often get 20-30% more
   - Focus on percentage, not dollar value

7. **Bonus Structure**
   - Target percentage (10% → 15%)
   - Guaranteed first year

8. **PTO/Vacation**
   - Add 5 days if below 20
   - Or unlimited (if they offer it)

9. **Review Schedule**
   - Ask for 6-month review (with potential increase)
   - Especially if taking lower offer

**Tier 3: Hardest to Negotiate**

10. **Base Salary**
    - Often in fixed bands
    - Requires strong justification
    - Ask for 10-20% increase (if below market)

11. **Remote Work Policy**
    - Usually company-wide policy
    - Hard to change for one person
    - But worth asking if hybrid → full remote

**Negotiation Bundle Strategy**:
Don't ask for everything. Pick 2-3 items that matter most.

**Example**:
"I'm excited about this role. Based on market research and my experience, I'd like to propose:
1. Base salary of $5,000/month (up from $4,500)
2. Equity of 0.08% (up from 0.05%)
3. $3,000 signing bonus to help with transition

Would this be possible?"

---

## Counter-Offer Scripts

### SCRIPT 1: Counter with Data (Base Salary)

```
"Thank you so much for the offer - I'm genuinely excited about joining 
[Company] and contributing to [specific aspect of role/mission].

I've done some market research for Senior Product Designers with my 
background in B2B SaaS and design leadership. Based on data from 
Levels.fyi and conversations with peers, the market range for this 
role is $4,500-6,000/month for remote positions.

Given my 10+ years of experience, track record scaling design teams, 
and expertise in complex B2B products, I'd like to propose a base 
salary of $5,000/month, which puts me at the mid-market range.

I'm confident I can deliver significant value quickly - for example, 
at Fincast I reduced onboarding time by 87%, directly impacting 
conversion. I'm eager to bring that impact to [Company].

Does this adjustment work within your budget?"
```

**Why This Works**:
- Enthusiasm first (not leading with demands)
- Data-driven (market research, not feelings)
- Value proposition (what they get for the increase)
- Collaborative tone ("does this work" vs. "I demand")

---

### SCRIPT 2: Counter with Competing Offer

```
"I really appreciate the offer and I'm excited about the opportunity 
to work with the team at [Company].

I want to be transparent with you: I'm also in late-stage conversations 
with another company, and their offer is slightly higher at $5,200/month 
base. However, I'm more excited about [Company]'s mission and the 
opportunity to [specific opportunity that excites you].

Is there any flexibility to match or get closer to that number? If we 
can land at $5,000/month, I'd love to accept and focus 100% on [Company].

What do you think?"
```

**Why This Works**:
- Honesty (transparency builds trust)
- Preference signaling (you WANT to work here)
- Specific ask (clear number)
- Collaborative close

**⚠️ Warning**: Only use if you ACTUALLY have a competing offer. Don't bluff.

---

### SCRIPT 3: Counter with Equity Focus

```
"Thank you for the offer - I'm really excited about [Company]'s growth 
trajectory and the role I can play in scaling design.

The base salary of $4,500 works for me. I'd like to discuss the equity 
component. Given that I'd be [first design hire / early design team 
member] and will be instrumental in establishing design culture and 
systems, I'd like to propose 0.10% equity (up from 0.05%).

This reflects the strategic nature of the role and my commitment to 
[Company]'s long-term success. I'm planning to be here for the long 
haul and want my compensation to reflect that partnership.

Is this something you can accommodate?"
```

**Why This Works**:
- Accepts base (shows flexibility)
- Justifies equity ask (strategic impact)
- Long-term commitment signal (not here for quick cash)

---

### SCRIPT 4: Counter with Benefits Bundle

```
"I really appreciate the offer. The base salary of $4,500 is in my 
range. I'd like to discuss a few additional components to make this 
work great for both of us:

1. A $5,000 signing bonus to help with transition costs
2. Increase equity to 0.08% (recognizing my leadership experience)
3. An annual learning budget of $2,000 (conferences, courses)

These adjustments would make the package very compelling and ensure 
I can hit the ground running. The total impact on your budget is 
relatively small, but it significantly increases the offer's 
competitiveness.

Can we make this work?"
```

**Why This Works**:
- Bundled ask (easier to say yes to package)
- Justification for each item
- Acknowledges budget impact (shows business thinking)

---

### SCRIPT 5: Accept with Future Review

```
"Thank you for the offer. I'm excited to join [Company]!

The offer is strong. I'd like to accept with one request: Can we 
schedule a compensation review at the 6-month mark? 

By then, I'll have delivered tangible results and we can reassess 
based on my impact. This gives both of us a clear checkpoint.

If you're open to that, I'm ready to accept and get started!"
```

**Why This Works**:
- Shows confidence (you'll deliver value)
- Low-risk ask (deferred, performance-based)
- Closes deal (acceptance contingent on this)

**When to Use**: When offer is close but not quite there, and you want to accept

---

## Handling Common Responses

### RESPONSE 1: "This is our best offer"

**Your Reply**:
```
"I appreciate the transparency. Can you help me understand the 
constraints? Is it budget, equity pool, or salary band?

If base salary is fixed, would there be flexibility on equity, 
signing bonus, or benefits? I'm trying to find a way to make 
this work because I'm genuinely excited about the role."
```

**Why This Works**:
- Accepts their constraint
- Seeks to understand (not push back)
- Proposes alternatives (creative problem-solving)

---

### RESPONSE 2: "We need to know by tomorrow"

**Your Reply**:
```
"I understand the urgency, and I'm equally eager to move forward. 
To make a well-informed decision on an important commitment like 
this, I'd appreciate until [day after tomorrow]. Would that work?

If there's a specific reason for the tight timeline, I'm happy to 
discuss - I want to be respectful of your process."
```

**Why This Works**:
- Pushes back gently (you need time)
- Offers compromise (day after tomorrow vs. end of week)
- Professional (not letting them rush you, but collaborative)

**⚠️ Note**: 24-hour deadlines are often a pressure tactic. Push back politely.

---

### RESPONSE 3: "We can't move on salary, but can do more equity"

**Your Reply**:
```
"I appreciate the flexibility on equity. Can you help me understand 
the equity value?

- What's the current valuation?
- What's the vesting schedule?
- How much is in the option pool?

If we're moving from 0.05% to 0.08%, I want to make sure I understand 
the real value. Also, would you be open to a signing bonus as an 
alternative to base increase?"
```

**Why This Works**:
- Informed decision-making (not taking equity blindly)
- Proposes alternative (signing bonus)
- Still collaborative

---

### RESPONSE 4: "You're already at the top of our band"

**Your Reply**:
```
"Thank you for sharing that context. I understand band constraints.

Given that I'm at the top of the band, would it be possible to:
1. Review for a band change at 6 months (if I deliver X, Y, Z)
2. Or increase equity to reflect the salary constraint
3. Or provide a signing bonus as a one-time adjustment

I want to find a creative solution that works within your structure."
```

**Why This Works**:
- Acknowledges their constraint
- Offers band-compliant alternatives
- Creative problem-solving

---

## Red Flags During Negotiation

### 🚩 RED FLAG: Rescinding Offer When You Negotiate
**What It Means**: Toxic culture, poor leadership, not respectful of candidates
**Action**: Walk away. You dodged a bullet.

### 🚩 RED FLAG: Pressuring You to Decide Immediately
**What It Means**: Lack of respect for your decision-making process
**Action**: Push back firmly. If they won't give 3-5 days, reconsider.

### 🚩 RED FLAG: Lowballing with "We hire for potential"
**What It Means**: Undervaluing your experience
**Action**: Counter strongly or walk. You're not junior.

### 🚩 RED FLAG: Refusing to Put Offer in Writing
**What It Means**: Not serious, or hiding something
**Action**: Don't accept verbal offers. Get it in writing.

### 🚩 RED FLAG: Equity with Vague Details
**What It Means**: May not be worth much
**Action**: Ask for specifics (valuation, strike price, exit timeline)

---

## Green Flags During Negotiation

### ✅ GREEN FLAG: Transparent About Bands and Budget
**What It Means**: Honest company culture
**Interpretation**: They respect you enough to be direct

### ✅ GREEN FLAG: Open to Creative Solutions
**What It Means**: Collaborative, flexible
**Interpretation**: Good sign for working relationship

### ✅ GREEN FLAG: Willing to Put Everything in Writing
**What It Means**: Trustworthy, professional
**Interpretation**: What they say = what you'll get

### ✅ GREEN FLAG: Encouraging You to Take Time
**What It Means**: Respectful, want you to make informed decision
**Interpretation**: Not desperate, confident in their offer

### ✅ GREEN FLAG: Explaining Constraints Clearly
**What It Means**: Transparent communication
**Interpretation**: Sets tone for future working relationship

---

## Decision Framework

### ACCEPT IF:
✅ Offer meets or exceeds your target ($3,200-5,000 range)
✅ Total comp is at/above market 50th percentile
✅ Company/role aligns with career goals
✅ No major red flags
✅ You've negotiated and got reasonable movement

### COUNTER IF:
⚠️ Offer is below target but close
⚠️ Strong interest but gap on 1-2 components
⚠️ You have leverage (competing offers, unique skills)
⚠️ Market data supports higher comp

### WALK AWAY IF:
❌ Offer below minimum ($2,000 dealbreaker)
❌ Major red flags in negotiation process
❌ Significant misalignment on role/expectations
❌ Better offer elsewhere (and this can't match)
❌ Company culture concerns

---

## Post-Negotiation

### IF YOU ACCEPT:
1. **Get it in writing** (offer letter with all agreed terms)
2. **Review carefully** (all verbal agreements captured?)
3. **Sign and return** (don't delay once decided)
4. **Update pipeline** (mark all other opps as withdrawn)
5. **Thank everyone** (recruiter, hiring manager)
6. **Prepare for onboarding** (logistics, paperwork)

### IF YOU DECLINE:
1. **Be gracious** ("Thank you for the opportunity...")
2. **Be brief** ("I've decided to pursue another direction")
3. **Don't burn bridges** (industry is small)
4. **Optional: Share reason** (if helpful feedback: "salary gap was too large")
5. **Stay connected** (LinkedIn, future opportunities)

### IF NEGOTIATION CONTINUES:
1. **Stay patient** (don't rush)
2. **Stay professional** (emotions low)
3. **Document everything** (all offers in writing)
4. **Know your walk-away point** (don't negotiate forever)

---

## Database Commands

**View**:
- `"Show all negotiations"` - List all past negotiations
- `"Show negotiation for [company]"` - Specific company details
- `"Show successful negotiations"` - What worked

**Create**:
- `"Analyze offer from [company]"` - Evaluate new offer
- `"Generate counter-offer for [company]"` - Create counter script
- `"Compare offers: [company1] vs [company2]"` - Decision support

**Update**:
- `"Update [company] negotiation: final offer [details]"` - Record outcome
- `"Add learning to [company] negotiation: [insight]"` - Capture lessons

**Analysis**:
- `"What negotiation tactics worked best?"` - Learn from history
- `"Show market data for [role]"` - Benchmark offers
- `"Calculate total comp for [offer details]"` - Apples-to-apples

---

## Usage Instructions

### Offer Evaluation:
```
"Evaluate this offer:
Company: Remote.com
Role: Senior Product Designer
Base: $4,500/month
Equity: 0.05% (4-year vest, 1-year cliff)
Bonus: 10% target
Benefits: Health insurance, unlimited PTO, $2k learning budget

Should I negotiate? What should I ask for?"
```

### Counter-Offer Generation:
```
"Generate counter-offer for Remote.com.
Current offer: $4,500 base, 0.05% equity
My target: $5,000 base, 0.08% equity
Leverage: 10+ years experience, B2B SaaS expertise, competing offer at $5,200"
```

### Offer Comparison:
```
"Compare these offers:

Offer A (Remote.com): $4,500 base, 0.05% equity, Series B
Offer B (Crustdata): $5,200 base, 0.10% equity, Seed stage

Which is better total comp? Which should I accept?"
```

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OFFER EVALUATION
Company: [Company Name]
Role: [Role Title]
Date: [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 OFFER DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Base Salary:      $X,XXX/month ($XX,XXX/year)
Equity:           X.XX% (vesting: X years)
Bonus:            X% target
Benefits:         [List]
Other:            [List]

💰 TOTAL COMPENSATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Base:             $XX,XXX
Bonus (expected): $X,XXX
Equity (annual):  $X,XXX (conservative estimate)
Benefits (value): $X,XXX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL:            $XX,XXX/year ($X,XXX/month effective)

📊 MARKET COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your Offer:       $X,XXX (XX percentile)
Market 25th:      $X,XXX
Market 50th:      $X,XXX
Market 75th:      $X,XXX
Your Target:      $X,XXX - $X,XXX

Assessment: [Above/At/Below market]

✅ STRENGTHS OF OFFER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Strength 1]
- [Strength 2]

⚠️ GAPS VS. YOUR TARGET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Gap 1]
- [Gap 2]

🎯 NEGOTIATION STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recommendation: [Negotiate / Accept / Walk Away]

If Negotiating, Ask For:
1. [Item 1]: $X,XXX (rationale: [why])
2. [Item 2]: X% (rationale: [why])
3. [Item 3]: [detail] (rationale: [why])

Leverage Points:
- [Your leverage 1]
- [Your leverage 2]

📝 COUNTER-OFFER SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Generated script based on strategy]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Quality Checklist

Before negotiating any offer:

- [ ] **All offer components captured** (base, equity, benefits, etc.)
- [ ] **Total comp calculated** (apples-to-apples comparison)
- [ ] **Market research completed** (know your percentile)
- [ ] **Priorities clear** (what matters most to you)
- [ ] **Leverage identified** (what makes you valuable)
- [ ] **Counter-offer prepared** (specific asks with rationale)
- [ ] **Scripts practiced** (conversational, not robotic)
- [ ] **Walk-away point known** (minimum acceptable)
- [ ] **Timeline understood** (when they need decision)
- [ ] **Everything in writing** (no verbal-only agreements)

---

## Notes
- Never accept first offer without at least exploring negotiation
- Enthusiasm + data = successful negotiation (not demands)
- Everything is negotiable except when it's not (know the difference)
- Signing bonuses are often easier than base increases
- Equity value is uncertain - discount appropriately
- Get EVERYTHING in writing before accepting
- Companies expect you to negotiate (don't feel guilty)
- Walk away if offer is below your minimum (protect your value)
- Maintain relationships even if you decline (industry is small)
- Learn from each negotiation (update database, refine approach)
