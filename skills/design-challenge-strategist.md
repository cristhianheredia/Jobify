# Design Challenge Strategist

## Purpose
Analyze design challenges, develop winning strategies, manage time effectively, and deliver high-quality outputs that demonstrate your design thinking - not just execution skills.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Strengths**: B2B SaaS, complex workflows, systems thinking, strategic design
- **Experience**: First design hire scenarios, cross-functional collaboration, data-heavy products
- **Past Challenge**: Thoughtworks "Roomies" app (roommate matching) - addressed research, accessibility, collaboration

## Input
- Design challenge brief (problem statement, requirements, constraints)
- Time limit (typical: 3-7 days)
- Deliverables expected (deck, prototype, documentation)
- Company context (if known - from company-research-brief)
- Role level (mid, senior, lead, principal)

## Output
- Challenge analysis (what they're REALLY evaluating)
- Strategic approach recommendation
- Time management plan
- Deliverable structure
- Key decisions framework
- Saved to database for learning

---

## DESIGN CHALLENGE DATABASE MANAGEMENT

### Database Structure
**File**: `/data/design-challenges.json`

**Schema**:
```json
{
  "challenges": [
    {
      "id": "dc_001",
      "company": "Thoughtworks",
      "role": "Senior Designer",
      "challenge_type": "product-design",
      "brief": "Roommate matching app",
      "time_limit": "5 days",
      "deliverables": ["presentation", "prototype"],
      "approach": "research-heavy-accessibility-focus",
      "date_completed": "2025-04-01",
      "outcome": "interview",
      "learnings": [
        "Strong research process impressed them",
        "Accessibility considerations were differentiator",
        "Showing collaboration approach worked well"
      ],
      "yellow_flags_addressed": ["research", "accessibility", "collaboration"]
    }
  ],
  "patterns": {
    "successful_approaches": ["show-research-process", "address-constraints-explicitly"],
    "time_allocations": {
      "research": "20%",
      "ideation": "15%",
      "design": "35%",
      "documentation": "30%"
    }
  }
}
```

### Workflow Instructions for Claude Code

#### BEFORE starting challenge:
1. **Analyze the brief** - decode what they're really evaluating
2. **Check database** for similar challenges at similar companies
3. **Show past approaches** that led to success
4. **Recommend strategy** based on role level and company type

#### DURING challenge:
1. **Time tracking** - remind about milestones
2. **Decision logging** - capture key choices and rationale
3. **Progress checks** - validate approach at 25%, 50%, 75%

#### AFTER challenge:
1. **Save to database** with approach and outcome
2. **Capture learnings** once outcome is known
3. **Update patterns** based on success/failure

---

## Challenge Types & What They Evaluate

### TYPE 1: Product Design Challenge
**Format**: "Design [feature/product] for [user group]"
**Example**: "Design a roommate matching app"

**What They're REALLY Evaluating**:
- ✅ **Problem definition** - Can you identify the REAL problem?
- ✅ **User research mindset** - Do you ask questions vs. assume?
- ✅ **Strategic thinking** - Do you solve the right problem?
- ✅ **Craft execution** - Can you design well?
- ✅ **Communication** - Can you articulate decisions?

**NOT Evaluating** (usually):
- ❌ Pixel-perfect polish
- ❌ Comprehensive feature set
- ❌ Production-ready designs

**Success Formula**:
```
30% Problem framing + research approach
40% Strategic design decisions with rationale
30% Craft execution and presentation
```

---

### TYPE 2: Redesign Challenge
**Format**: "Improve [existing product/feature]"
**Example**: "Redesign the checkout experience for [e-commerce site]"

**What They're REALLY Evaluating**:
- ✅ **Critical analysis** - Can you identify real issues?
- ✅ **Prioritization** - Do you tackle the right problems?
- ✅ **Constraint awareness** - Do you consider tech/business limits?
- ✅ **Measurement thinking** - How would you measure success?
- ✅ **Incremental vs. radical** - Do you understand trade-offs?

**Success Formula**:
```
40% UX audit and problem prioritization
35% Solution with clear rationale
25% Implementation considerations
```

---

### TYPE 3: Whiteboard/Live Challenge
**Format**: In-person or video call design exercise
**Example**: "Design a feature for [scenario] in 45 minutes"

**What They're REALLY Evaluating**:
- ✅ **Thinking process** - How you approach problems
- ✅ **Communication** - Can you think out loud?
- ✅ **Collaboration** - Do you ask questions vs. dictate?
- ✅ **Flexibility** - Can you pivot based on feedback?
- ✅ **Speed** - Can you work under pressure?

**Success Formula**:
```
50% Process and thinking out loud
30% Asking clarifying questions
20% Sketching and articulation
```

---

### TYPE 4: Systems Thinking Challenge
**Format**: "Design a design system component" or "Scale [X]"
**Example**: "Create a table component for our design system"

**What They're REALLY Evaluating**:
- ✅ **Systems thinking** - Do you think beyond one instance?
- ✅ **Edge cases** - Do you consider variants and states?
- ✅ **Documentation** - Can you enable others to use it?
- ✅ **Flexibility** - Is it robust yet extensible?
- ✅ **Standards** - Do you know best practices?

**Success Formula**:
```
25% Requirements gathering (use cases)
40% Component design (variants, states, responsiveness)
35% Documentation and guidelines
```

---

### TYPE 5: Strategy/Critique Challenge
**Format**: "Critique this product" or "What would you do differently?"
**Example**: "Analyze [competitor product] and suggest improvements"

**What They're REALLY Evaluating**:
- ✅ **Analytical thinking** - Can you dissect systematically?
- ✅ **Balanced perspective** - Do you see strengths AND weaknesses?
- ✅ **Business understanding** - Do you connect UX to business?
- ✅ **Constructive critique** - Are you thoughtful, not just critical?
- ✅ **Prioritization** - What would you fix first and why?

**Success Formula**:
```
30% Structured analysis framework
40% Insights and opportunities
30% Prioritized recommendations
```

---

## Strategic Analysis Framework

### STEP 1: Decode the Brief
**Ask These Questions:**

**About the Problem**:
- What's the STATED problem?
- What's the REAL problem? (often different)
- Who benefits if this is solved?
- What constraints are mentioned? (time, tech, users)
- What constraints are IMPLIED but not stated?

**About the Company**:
- What stage are they? (startup/growth/enterprise)
- What's their product complexity?
- What's their design maturity?
- What role level is this for?

**About the Evaluation**:
- What skills does this role need? (from JD)
- What gaps might they be testing for?
- What "yellow flags" from your background might they be probing?

**Example - Thoughtworks Roomies Challenge**:
```
STATED: Design a roommate matching app
REAL: Can you do user research, handle accessibility, show collaboration?
YELLOW FLAGS: Research process, accessibility, collaboration approach
CONCLUSION: Over-index on research, explicitly address accessibility, 
show cross-functional thinking
```

---

### STEP 2: Choose Your Strategic Approach

**APPROACH A: Research-Heavy** (when they doubt your research skills)
```
Time Split:
- 25% Research and insights
- 15% Ideation
- 30% Design
- 30% Documentation

Deliverables Emphasis:
- Show research process explicitly
- Include user quotes/insights
- Document assumptions vs. validated
- Show how research informed decisions
```

**APPROACH B: Systems-Thinking** (for senior/lead roles)
```
Time Split:
- 15% Problem framing
- 20% Systems mapping
- 35% Scalable solution
- 30% Documentation

Deliverables Emphasis:
- Think beyond single feature
- Consider edge cases and scale
- Show component thinking
- Document patterns and principles
```

**APPROACH C: Business-Impact** (for business-focused companies)
```
Time Split:
- 20% Business context
- 15% User needs
- 35% Solution
- 30% Metrics and impact

Deliverables Emphasis:
- Connect to business goals
- Define success metrics
- Show ROI thinking
- Prioritize by impact
```

**APPROACH D: Craft-Excellence** (for design-forward companies)
```
Time Split:
- 10% Research
- 20% Exploration
- 45% High-fidelity design
- 25% Documentation

Deliverables Emphasis:
- Pixel-perfect execution
- Thoughtful micro-interactions
- Design system consistency
- Visual polish
```

**APPROACH E: Speed-to-Value** (for startups/early-stage)
```
Time Split:
- 15% Problem validation
- 20% Quick ideation
- 35% MVP solution
- 30% Implementation considerations

Deliverables Emphasis:
- Scrappy but strategic
- Ship-able solutions
- Phased approach
- Technical feasibility
```

---

## Time Management Templates

### 3-DAY CHALLENGE
**Research-Heavy Approach**:
```
Day 1 (8 hours):
- 2h: Brief analysis + research plan
- 3h: User research (interviews, competitive analysis)
- 2h: Synthesis and insights
- 1h: Problem reframing and opportunity areas

Day 2 (8 hours):
- 2h: Ideation and concept exploration
- 4h: Design (wireframes → mid-fi)
- 2h: Iteration based on self-critique

Day 3 (8 hours):
- 3h: Finalize designs
- 4h: Presentation deck creation
- 1h: Practice presentation
```

**Craft-Excellence Approach**:
```
Day 1:
- 2h: Brief analysis + quick research
- 3h: Concept sketches and wireframes
- 3h: Begin high-fidelity design

Day 2:
- 6h: High-fidelity design execution
- 2h: Micro-interactions and polish

Day 3:
- 2h: Final polish
- 4h: Presentation creation
- 2h: Practice and refinement
```

---

### 5-DAY CHALLENGE
**Balanced Approach**:
```
Day 1: Research & Problem Definition
- Brief analysis (1h)
- Research plan (1h)
- User research (4h)
- Synthesis (2h)

Day 2: Strategy & Ideation
- Insights presentation (2h)
- Opportunity framing (2h)
- Ideation (3h)
- Concept selection (1h)

Day 3: Design Execution
- Wireframes (3h)
- User flow mapping (2h)
- Mid-fidelity design (3h)

Day 4: Refinement & Documentation
- High-fidelity design (4h)
- Iteration (2h)
- Begin presentation (2h)

Day 5: Presentation & Polish
- Finish presentation (4h)
- Practice (2h)
- Buffer for last-minute tweaks (2h)
```

---

### 7-DAY CHALLENGE
**Comprehensive Approach**:
```
Days 1-2: Research
- Deep user research
- Competitive analysis
- Stakeholder interviews (if allowed)
- Market research

Days 3-4: Strategy & Ideation
- Insights synthesis
- Problem reframing
- Multiple concept exploration
- Concept validation

Days 5-6: Design
- Detailed user flows
- High-fidelity design
- Micro-interactions
- Responsive considerations

Day 7: Presentation
- Deck creation
- Storytelling refinement
- Practice
- Polish
```

---

## Deliverable Structures

### PRESENTATION DECK STRUCTURE

**OPENING (1-2 slides)**:
```
Slide 1: Title
- Challenge name
- Your name
- Date
- (Optional: One-line hook about your approach)

Slide 2: Agenda/Executive Summary
- Problem
- Approach
- Solution
- Impact
```

**PROBLEM FRAMING (3-5 slides)**:
```
Slide 3: Understanding the Brief
- Problem statement
- Key constraints
- Success criteria

Slide 4: Research Approach
- Methods used
- Participants/sources
- Timeline

Slide 5: Key Insights
- 3-5 main findings
- User quotes or data
- Implications
```

**SOLUTION (8-12 slides)**:
```
Slide 6: Design Principles
- 3-4 principles guiding the solution
- Why these matter for this problem

Slide 7: User Journey/Flow
- Before (current state)
- After (proposed solution)
- Key improvements

Slides 8-12: Solution Walkthrough
- Key screens/flows
- Annotations explaining decisions
- One concept per slide
- Progressive disclosure of complexity
```

**RATIONALE (3-5 slides)**:
```
Slide 13: Key Design Decisions
- Decision 1: What + Why
- Decision 2: What + Why
- Decision 3: What + Why
- Trade-offs considered

Slide 14: Measuring Success
- Metrics to track
- Expected outcomes
- How you'd validate

Slide 15: Next Steps
- What you'd do with more time
- Open questions to explore
- Implementation considerations
```

**CLOSING (1 slide)**:
```
Slide 16: Thank You
- Contact info
- (Optional: One reflection or learning)
```

**Total: 12-16 slides** (sweet spot for 20-30 min presentation)

---

### PROTOTYPE STRUCTURE

**If High-Fidelity Prototype**:
```
Flows to Include:
1. Happy path (primary user journey)
2. One key edge case
3. Error/empty states

States to Show:
- Default
- Hover (if interactive)
- Active/selected
- Error
- Loading
- Empty
- Success

Annotations:
- Interaction notes
- Transitions
- Constraints or limitations
```

**If Low/Mid-Fidelity**:
```
Focus:
- User flow clarity
- Information architecture
- Interaction patterns
- Key decisions

Skip:
- Visual polish
- Micro-interactions
- Pixel perfection
- Multiple color themes
```

---

### DOCUMENTATION STRUCTURE

**Design Rationale Doc**:
```
1. Problem Statement
2. Research Summary
3. User Needs Identified
4. Design Principles
5. Key Decisions & Trade-offs
6. Assumptions Made
7. Open Questions
8. Next Steps
```

**If Showing Process**:
```
Include:
- Research plan
- Synthesis artifacts (affinity map, personas)
- Sketches and explorations
- Iteration notes
- Decision log
```

---

## Key Decisions Framework

**For Every Major Decision, Document**:

```
DECISION: [What you decided]

WHY: [Rationale - user needs, business goals, constraints]

ALTERNATIVES CONSIDERED: [What else you explored]

TRADE-OFFS: [What you sacrificed, what you gained]

VALIDATION: [How you would test this]
```

**Example**:
```
DECISION: Progressive disclosure for advanced filters

WHY: 
- 80% of users only need basic filters (research finding)
- Power users need advanced options (business requirement)
- Limited screen real estate (constraint)

ALTERNATIVES CONSIDERED:
- Show all filters upfront (too overwhelming)
- Hide advanced filters completely (power users frustrated)
- Separate "advanced mode" (added unnecessary complexity)

TRADE-OFFS:
- Sacrificed: Immediate access to all options
- Gained: Cleaner interface, faster completion for majority

VALIDATION: 
- A/B test task completion time
- Track advanced filter usage rate
- User satisfaction scores
```

---

## Common Pitfalls & How to Avoid

### PITFALL 1: Designing Without Research
**Symptom**: Jumping straight to solutions
**Why It Fails**: Shows you make assumptions
**Fix**: Even with 3 days, spend 4-6 hours on research
**Minimum**: Competitive analysis + assumptions documentation

---

### PITFALL 2: Over-Scoping
**Symptom**: Trying to design entire product in limited time
**Why It Fails**: Deliverables are rushed and shallow
**Fix**: Ruthlessly scope to 1-2 key flows
**Framework**: "If I only had time for ONE thing, what would matter most?"

---

### PITFALL 3: No Clear Point of View
**Symptom**: Designs are safe and generic
**Why It Fails**: Doesn't show strategic thinking
**Fix**: Have a clear thesis about the REAL problem
**Example**: "The problem isn't matching roommates, it's building trust between strangers"

---

### PITFALL 4: Ignoring Constraints
**Symptom**: Solutions that are unrealistic
**Why It Fails**: Shows lack of pragmatism
**Fix**: Explicitly address constraints in rationale
**Include**: Technical limitations, timeline, resources, user capabilities

---

### PITFALL 5: Poor Presentation
**Symptom**: Great design, terrible storytelling
**Why It Fails**: They can't see your thinking
**Fix**: Spend 25-30% of time on presentation
**Structure**: Problem → Insights → Solution → Impact

---

### PITFALL 6: Pixel-Pushing Instead of Problem-Solving
**Symptom**: Beautiful designs with weak rationale
**Why It Fails**: Senior roles need strategic thinking
**Fix**: Articulate WHY for every design decision
**Ratio**: For every hour of design, 30 min of documentation

---

### PITFALL 7: Not Addressing Your "Yellow Flags"
**Symptom**: Avoiding areas where you're weaker
**Why It Fails**: They're testing for those specifically
**Fix**: Over-index on your known gaps
**Example**: Weak on research? Make research VERY visible

---

## Evaluation Criteria (How They Score You)

### SENIOR IC DESIGNER
**What They're Scoring**:
- Problem definition (20%)
- Design craft (30%)
- Strategic thinking (25%)
- Communication (15%)
- Attention to detail (10%)

**To Excel**: Show deep craft + clear thinking + good communication

---

### LEAD/PRINCIPAL DESIGNER
**What They're Scoring**:
- Strategic thinking (35%)
- Systems thinking (25%)
- Communication (20%)
- Design craft (15%)
- Leadership indicators (5%)

**To Excel**: Think beyond the feature, show how you'd scale it, demonstrate influence

---

### FIRST DESIGN HIRE
**What They're Scoring**:
- Scrappiness (25%)
- Breadth (25%)
- Business thinking (25%)
- Speed (15%)
- Collaboration signals (10%)

**To Excel**: Show you can wear multiple hats, move fast, think about business

---

## Presentation Tips

### STRUCTURE YOUR STORY
**Not**: "Here's what I designed"
**But**: "Here's the problem I uncovered, why it matters, and how I solved it"

**Arc**:
```
1. Hook (interesting problem insight)
2. Problem depth (show your thinking)
3. Solution reveal (with rationale)
4. Impact (how you'd measure success)
5. Reflection (what you learned)
```

---

### SHOW YOUR THINKING, NOT JUST DESIGNS
**Not**: 10 slides of polished screens
**But**: Research → Insights → Decisions → Designs → Impact

**Ratio**: 
- 30% Problem/Research
- 40% Solution
- 30% Rationale/Impact

---

### HANDLE QUESTIONS WELL
**When Challenged**:
- Don't get defensive
- Acknowledge the question
- Explain your rationale
- Be open to other approaches

**Example**:
```
Them: "Why didn't you consider [X]?"
You: "That's a great point. I prioritized [Y] because [reason], 
but I'd definitely want to test [X] in the next iteration. 
How do you see the trade-offs there?"
```

---

### PRACTICE OUT LOUD
- Time yourself (stick to limit)
- Record and watch yourself
- Practice transitions between slides
- Prepare for likely questions

---

## Database Commands

**View**:
- `"Show all design challenges"` - List completed challenges
- `"Show challenges for [company-type]"` - Filter by company
- `"Show successful challenge approaches"` - What worked

**Create**:
- `"Analyze this design challenge: [brief]"` - Get strategy
- `"Create time plan for [X]-day challenge"` - Get schedule

**Update**:
- `"Update challenge [id] outcome: [result]"` - Track results
- `"Add learning to [id]: [insight]"` - Capture lessons

**Analysis**:
- `"What challenge approaches led to interviews?"` - Patterns
- `"What time allocations work best?"` - Optimize planning

---

## Usage Instructions

### Basic Usage:
```
"Analyze this design challenge:

Brief: [Paste challenge brief]
Time: [Days available]
Company: [Company name]
Role: [Role level]

Help me develop a strategy."
```

### With Context:
```
"I have a 5-day design challenge for [Company].
Challenge: [Brief]
My yellow flags for this company: [List concerns]
What strategy should I use?"
```

### During Challenge:
```
"I'm on Day 2 of my challenge. Here's my progress: [Update]
Am I on track? What should I prioritize for remaining time?"
```

---

## Output Format

```
---
CHALLENGE ANALYSIS
ID: dc_XXX
Company: [Company Name]
Role: [Role Level]
Time: [Days]

---

WHAT THEY'RE REALLY EVALUATING:
- [Evaluation criterion 1]
- [Evaluation criterion 2]
- [Evaluation criterion 3]

YOUR YELLOW FLAGS TO ADDRESS:
- [Flag 1 and how to address it]
- [Flag 2 and how to address it]

RECOMMENDED APPROACH: [Approach name]

TIME ALLOCATION:
Day 1: [Schedule]
Day 2: [Schedule]
...

DELIVERABLE STRUCTURE:
- [Component 1]
- [Component 2]
- [Component 3]

KEY DECISIONS TO MAKE:
1. [Decision area 1]
2. [Decision area 2]
3. [Decision area 3]

SUCCESS CRITERIA:
- [What good looks like]
- [What great looks like]

RED FLAGS TO AVOID:
- [Pitfall 1]
- [Pitfall 2]

---

DATABASE STATUS: ✅ Saved as dc_XXX
---
```

---

## Quality Checklist

Before submitting any design challenge:

- [ ] **Clear problem definition** (not just restating brief)
- [ ] **Research shown** (even if limited time)
- [ ] **Strategic rationale** (WHY for key decisions)
- [ ] **Constraints addressed** (technical, time, user)
- [ ] **Metrics defined** (how you'd measure success)
- [ ] **Trade-offs acknowledged** (what you sacrificed/gained)
- [ ] **Presentation tells story** (not just screen gallery)
- [ ] **Appropriate scope** (focused, not trying to solve everything)
- [ ] **Proofread** (no typos, company name correct)
- [ ] **Practiced** (presentation flows smoothly)
- [ ] **Yellow flags addressed** (over-indexed on weak areas)
- [ ] **Next steps included** (what you'd do with more time)

---

## Notes
- Design challenges test THINKING more than EXECUTION
- Show your process, not just your polish
- Address constraints explicitly - it shows pragmatism
- When in doubt, over-communicate your rationale
- The presentation is as important as the design
- Learn from each challenge - track what works
- Senior roles care more about strategy than pixels
- Always show how you'd measure success
