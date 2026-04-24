# Leadership Narrative Builder

## Purpose
Articulate your leadership philosophy, style, and experience for senior/lead/principal designer roles. Build compelling narratives that demonstrate leadership capability even without formal management titles.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Leadership Experience**: Informal leadership (mentoring, influence, team scaling), not formal people management yet
- **Leadership Style**: Coaching, facilitative, evidence-based
- **Key Leadership Moments**: Mentoring Andreina, scaling design at Kushki, first design hire at Fincast, upward influence
- **Next Step**: Transitioning to formal Lead/Principal/Head of Design roles

## Input
- Target role level (Lead, Principal, Director, Head of Design)
- Company context (startup, scale-up, enterprise)
- Specific leadership competencies being evaluated
- Interview format (behavioral, case discussion, presentation)

## Output
- Leadership philosophy statement
- Leadership style articulation
- Evidence-based leadership stories
- Vision for leading design teams
- Answers to common leadership questions
- Saved to database for refinement

---

## LEADERSHIP NARRATIVE DATABASE MANAGEMENT

### Database Structure
**File**: `/data/leadership-narratives.json`

**Schema**:
```json
{
  "narratives": [
    {
      "id": "ln_001",
      "role_level": "lead-designer",
      "company_type": "scale-up",
      "leadership_philosophy": "I lead through coaching and empowerment...",
      "key_themes": ["coaching", "systems-thinking", "influence", "culture-building"],
      "evidence_stories": [
        "Mentoring Andreina",
        "Design team scaling at Kushki",
        "Design system advocacy"
      ],
      "used_for": [
        {
          "company": "Thoughtworks",
          "outcome": "advanced"
        }
      ],
      "date_created": "2025-04-24",
      "refinements": 2
    }
  ],
  "leadership_evolution": {
    "current_stage": "senior-ic-with-informal-leadership",
    "target_stage": "formal-design-lead",
    "growth_areas": ["formal team management", "hiring", "performance management"]
  }
}
```

### Workflow Instructions for Claude Code

#### BEFORE interview/application:
1. **Match role level** to appropriate narrative version
2. **Customize for company stage** (startup vs. scale-up vs. enterprise)
3. **Select evidence stories** that demonstrate relevant leadership
4. **Prepare answers** to common leadership questions for that level

#### AFTER interview:
1. **Capture questions asked** about leadership
2. **Note what resonated** (which stories, which themes)
3. **Refine narrative** based on feedback
4. **Track evolution** toward formal leadership roles

---

## Leadership Levels & Expectations

### SENIOR IC DESIGNER (Where You Are Now)
**Leadership Expected**:
- Informal mentoring
- Project leadership
- Cross-functional influence
- Design quality standards
- Junior designer guidance

**NOT Expected**:
- Formal people management
- Hiring decisions
- Performance reviews
- Budget ownership
- Org-level strategy

**Narrative Focus**: "Leadership through craft, influence, and mentorship"

---

### LEAD DESIGNER (Your Next Step)
**Leadership Expected**:
- Formal people management (2-5 reports)
- Hiring and team growth
- Design process establishment
- Cross-functional partnership
- Strategic design direction

**NEW Responsibilities**:
- 1:1s and career development
- Performance management
- Resource allocation
- Roadmap prioritization

**Narrative Focus**: "Building and empowering design teams"

---

### PRINCIPAL DESIGNER (IC Leadership Track)
**Leadership Expected**:
- Design systems and standards
- Technical leadership across teams
- Strategic design vision
- Mentoring other seniors
- Influence at exec level

**NOT Expected**:
- People management (IC track)
- BUT: Deep technical/craft leadership

**Narrative Focus**: "Setting technical direction, elevating craft standards"

---

### DESIGN MANAGER / HEAD OF DESIGN
**Leadership Expected**:
- Team of 5-15+ designers
- Hiring strategy and team scaling
- Design culture and process
- Budget management
- Executive-level stakeholder management
- Design org structure

**Narrative Focus**: "Scaling design as a strategic function"

---

## Your Leadership Philosophy (Foundation)

### CORE STATEMENT
**Template**:
```
"I lead through [primary approach] because [core belief about people/design]. 
In practice, this means [specific behaviors]. I've seen this work when 
[evidence from experience]."
```

**Your Version**:
```
"I lead through coaching and empowerment because I believe the best design 
outcomes come from teams who own their decisions, not execute someone else's 
vision. In practice, this means I focus on building thinking frameworks - 
teaching 'how to fish' rather than providing answers. I've seen this work 
at Kushki, where mentoring Andreina from junior to mid-level created a 
designer who could independently lead strategic projects, multiplying our 
team's impact far beyond what I could achieve alone."
```

---

### YOUR LEADERSHIP STYLE: Coaching & Facilitation

**What This Means**:
- **Coaching**: Developing people through questions, not directives
- **Facilitation**: Creating conditions for good decisions, not making all decisions yourself
- **Evidence-based**: Decisions driven by data/research, not opinion or hierarchy

**Key Behaviors**:
1. **Ask questions before giving answers**
   - Example: "What user problem are we solving?" vs. "Here's the solution"
   
2. **Create frameworks, not prescriptions**
   - Example: Teaching STAR methodology to Andreina vs. writing her case studies
   
3. **Build systems, not dependencies**
   - Example: Design system to scale vs. being the bottleneck reviewer
   
4. **Show vulnerability**
   - Example: Acknowledging when you don't have the answer
   
5. **Measure impact, not activity**
   - Example: "Did conversion improve?" vs. "Did we ship the designs?"

---

### CONTRAST: What You're NOT

**NOT Command-and-Control**:
- You don't dictate solutions
- You don't need to be the smartest in the room
- You don't measure success by your personal output

**NOT Hands-Off**:
- You're not absent or uninvolved
- You don't avoid making decisions when needed
- You're not avoiding accountability

**Your Balance**:
```
"I'm hands-on when it comes to establishing frameworks and standards, but 
hands-off when it comes to letting people apply those frameworks. I'll 
co-design the first iteration to teach the approach, then step back and 
let them run with the next one."
```

---

## Evidence: Your Leadership Moments

### MOMENT 1: People Development (Andreina)
**Leadership Demonstrated**: Coaching, patience, growth mindset

**The Story** (condensed for leadership context):
```
"At Kushki, I mentored Andreina, a talented junior designer who struggled 
with strategic articulation. Rather than just giving her feedback on designs, 
I taught her the STAR framework for connecting design work to business outcomes. 
Over 12 months, she went from needing constant guidance to independently leading 
two major features. This taught me that the multiplier effect of developing 
people far exceeds what I can produce myself."
```

**What This Shows**:
- Investment in others' growth
- Long-term thinking (12 months)
- Teaching frameworks, not just tasks
- Measuring success by team growth, not personal output

**When to Use**: People development questions, coaching culture, mentorship

---

### MOMENT 2: Team Scaling (Kushki Design System)
**Leadership Demonstrated**: Systems thinking, strategic prioritization, influence

**The Story**:
```
"When I was the only designer at Kushki supporting 3 squads, I recognized 
I was the bottleneck. Rather than immediately push for more headcount, I 
invested in a design system that would 3x efficiency. I partnered with an 
engineer to co-create it, building buy-in through collaboration. Within 6 
months, I went from supporting 1 squad to enabling design across 3, and 
that efficiency case helped secure approval for 2 additional design hires."
```

**What This Shows**:
- Strategic before tactical (system before headcount)
- Building leverage (design system as force multiplier)
- Collaboration over dictation
- Business thinking (ROI case for hiring)

**When to Use**: Scaling questions, strategic thinking, design ops

---

### MOMENT 3: Influence Without Authority (Design System Advocacy)
**Leadership Demonstrated**: Upward influence, business case building, pragmatism

**The Story**:
```
"At Kushki, leadership was hesitant to allocate engineering resources to 
'non-feature work' during a growth phase. I built a business case: quantified 
the cost of inconsistency (15-20 hours/week wasted), created an MVP with one 
engineer to prove the concept, and framed the ask in business terms ('3-week 
investment to 3x designer efficiency'). Leadership approved it, and within 
6 months we had 95% design system adoption."
```

**What This Shows**:
- Influence through data, not authority
- Speaking stakeholder language (business metrics)
- Pragmatic approach (MVP to prove, then scale)
- Strategic patience (build case before asking)

**When to Use**: Stakeholder management, influence questions, resource negotiation

---

### MOMENT 4: Leading Through Ambiguity (Fincast Pivot)
**Leadership Demonstrated**: Strategic thinking, adaptability, using design to clarify thinking

**The Story**:
```
"During Fincast's pivot from SMB to enterprise, I treated design as a strategic 
tool for clarifying direction, not just executing decided features. I ran rapid 
validation interviews with enterprise prospects, created multiple conceptual 
prototypes at different fidelity levels to pressure-test strategy, and established 
weekly syncs with the CEO where design findings informed roadmap decisions. The 
CEO later told me design became the strategic anchor during uncertainty."
```

**What This Shows**:
- Design as strategy tool, not just execution
- Comfort with ambiguity
- Proactive leadership (didn't wait for clarity)
- Executive-level communication

**When to Use**: Strategic thinking, ambiguity questions, startup contexts

---

### MOMENT 5: Cross-Functional Leadership (Alignment)
**Leadership Demonstrated**: Facilitation, finding third options, shared goals

**The Story**:
```
"When Product and Engineering had competing priorities at Kushki (feature parity 
vs. technical debt), I facilitated a design sprint where I brought both teams 
into the room. By having each side present their constraints, I surfaced a shared 
pain point: our architecture made ANY change slow. I proposed a phased approach 
that tackled tech debt in high-use flows first (eng), then added competitive 
features (PM), with design ensuring consistency across both. Both teams bought 
in, and we shipped faster than either initially estimated."
```

**What This Shows**:
- Facilitation over mediation
- Finding win-win solutions
- Cross-functional empathy
- Design as connective tissue

**When to Use**: Collaboration, conflict resolution, cross-functional leadership

---

## Leadership Vision (Forward-Looking)

### FOR LEAD DESIGNER ROLES

**Your Vision**:
```
"In a Lead Designer role, I see three priorities:

First, building a high-performing team through coaching and clear growth paths. 
I'd establish regular 1:1s focused on career development, create a critique 
culture where feedback is expected and safe, and ensure every designer has a 
mentor-mentee relationship.

Second, establishing design operations that scale: design systems, documentation 
standards, design-eng collaboration rituals. The goal is to make good design 
the easy path, not the heroic effort.

Third, elevating design's strategic influence by connecting our work to business 
outcomes. I'd establish shared success metrics with Product and Engineering, 
ensure design is involved in roadmap planning early, and create visibility into 
design's impact through regular presentations to leadership."
```

**What This Shows**:
- People-first mindset
- Systems thinking
- Business acumen
- Concrete plans, not vague aspirations

---

### FOR PRINCIPAL DESIGNER ROLES (IC Track)

**Your Vision**:
```
"As a Principal Designer, I'd focus on technical design leadership:

Setting the standard for craft excellence through deep work on complex problems, 
establishing design patterns and systems that others can learn from, and being 
the go-to person for the hardest design challenges.

Mentoring senior designers to level up their strategic thinking and systems 
approach, not through formal management but through pairing, critique, and 
creating learning opportunities.

Being the bridge between design and engineering at the architectural level - 
understanding technical constraints deeply enough to design within them, and 
advocating for design-friendly technical decisions early in the process."
```

**What This Shows**:
- IC leadership clarity (not people management)
- Technical depth
- Mentorship at senior level
- Strategic technical thinking

---

### FOR HEAD OF DESIGN ROLES

**Your Vision** (aspirational, acknowledge growth needed):
```
"While I haven't led at this scale yet, my approach to Head of Design would 
center on three pillars:

Design as a strategic function, not a service organization. This means design 
involved in company strategy from the start, clear metrics connecting design 
to business outcomes, and executive-level communication about design's impact.

Team building and culture: hiring for diverse skills and perspectives, creating 
clear career ladders with multiple paths (IC and management), and establishing 
a culture where design excellence and business impact are equally valued.

Design operations and systems: the infrastructure that allows design to scale - 
tools, processes, design systems, research repositories, collaboration rituals.

I know I have growth areas here - formal people management at scale, hiring 
strategy, budget ownership - but my experience building teams informally and 
establishing design systems gives me a foundation to build on."
```

**What This Shows**:
- Vision for the role
- Honest about gaps (builds trust)
- Connects to your experience
- Growth mindset

---

## Common Leadership Questions & Your Answers

### "What's your leadership style?"

**Your Answer**:
```
"I lead through coaching and facilitation. I believe the best outcomes come 
from empowered teams who own their decisions, not teams executing someone else's 
vision. 

In practice, this means I focus on building frameworks and systems that enable 
good decision-making, rather than making every decision myself. When I mentored 
Andreina at Kushki, I didn't write her case studies - I taught her the STAR 
framework and coached her through building her own. That investment took longer 
upfront, but created a designer who could independently lead strategic work.

I'm hands-on when establishing standards and teaching approaches, but hands-off 
once people have the frameworks. I measure success by the team's growth and 
impact, not my personal output."
```

**Why This Works**:
- Clear philosophy
- Concrete example
- Shows the "why" behind the "what"
- Demonstrates results

---

### "How do you handle underperformance?"

**Your Answer**:
```
"I start by diagnosing the root cause - is it a skill gap, unclear expectations, 
or misalignment on what success looks like? 

In my experience mentoring designers, I've found that most 'underperformance' 
is actually unclear expectations or lack of framework. When Andreina struggled 
with strategic thinking at Kushki, it wasn't a capability issue - she didn't 
have a mental model for connecting design work to business outcomes. Once I 
taught her the STAR framework, she thrived.

If it's a skill gap, I create a clear development plan with milestones and 
check-ins. If it's effort or fit issues, I'd have direct conversations early 
and often - I believe in candor with kindness.

What I don't do is avoid the conversation or let it linger. Performance issues 
don't age well, and the person deserves to know where they stand."
```

**Why This Works**:
- Structured thinking (diagnose first)
- Example from your experience
- Balances empathy with accountability
- Shows you'd take action

---

### "How do you prioritize design work?"

**Your Answer**:
```
"I use a framework based on three dimensions: business impact, user impact, and 
effort. But the key is involving the team in the prioritization conversation, 
not dictating it.

At Kushki, when I was supporting multiple squads, I couldn't do everything. I 
facilitated a prioritization exercise with Product and Engineering where we 
scored projects on impact and effort, but more importantly, I made the trade-offs 
visible. 'If we do X, we can't do Y this quarter' - that transparency built trust.

I also distinguish between strategic design work (where design should lead) and 
execution work (where we support). Strategic work - like the design system at 
Kushki - gets priority even if it's not on the feature roadmap, because it 
multiplies our effectiveness.

The hardest prioritization is saying no to good ideas. I've learned to reframe 
'no' as 'not now, here's why' and document it. Sometimes good ideas become great 
ideas when timing is right."
```

**Why This Works**:
- Clear framework
- Involves others (facilitation)
- Business thinking (ROI focus)
- Real example
- Addresses the hard part (saying no)

---

### "How would you scale a design team from 1 to 5?"

**Your Answer**:
```
"I'd approach this in phases:

Phase 1 (Team of 1-2): Establish foundations before scaling. Build the design 
system, document design processes, create design-eng collaboration rituals. This 
is what I did at Kushki - the design system made it possible to scale later.

Phase 2 (Team of 3-4): Hire for diversity of skills, not just more generalists. 
One person might spike on systems thinking, another on research, another on 
visual craft. I'd also establish critique culture and mentorship pairs early.

Phase 3 (Team of 5+): Introduce structure - design leads for different product 
areas, clear decision-making frameworks, regular team syncs. At this size, you 
need lightweight process to stay aligned.

Throughout, I'd focus on hiring people who fill gaps in our capabilities, not 
clones of the first designer. And I'd establish clear career paths early - some 
people want IC growth, others want management."
```

**Why This Works**:
- Phased thinking (not "hire 5 people at once")
- Connects to your experience (Kushki)
- Strategic (systems before people)
- Considers different growth paths

---

### "Tell me about a time you had to deliver difficult feedback."

**Your Answer**:
```
"At Kushki, I was coaching Andreina on a presentation about her design work. 
Her case study focused entirely on the design process - which tools she used, 
which iterations she made - but completely missed the business impact and user 
outcomes.

I knew this would hurt her credibility with leadership, but I also knew she'd 
be defensive if I just said 'this isn't good enough.' So I started with a 
question: 'If leadership could only remember one thing from this presentation, 
what should it be?' She said 'the design quality.' I followed up: 'What do you 
think they care about more - how it looks or whether it worked?'

That Socratic approach helped her arrive at the insight herself. We then rebuilt 
the presentation together, leading with business impact and user outcomes, with 
design process in support.

The lesson I learned: difficult feedback lands better when you help people 
discover the gap themselves, rather than pointing it out directly."
```

**Why This Works**:
- Real example
- Shows your coaching approach
- Demonstrates care (didn't just criticize)
- Shares what you learned

---

### "How do you build design culture?"

**Your Answer**:
```
"Culture isn't built through mission statements - it's built through consistent 
behaviors and systems.

At Kushki, I built design culture through three mechanisms:

First, critique rituals. I established weekly design critique where we reviewed 
work-in-progress, not finished work. This normalized feedback as part of the 
process, not a judgment on the person. Over time, people started bringing 
earlier work, knowing it was safe.

Second, design visibility. I created a Slack channel where we shared design 
decisions with rationale, making design thinking visible to the whole company. 
This educated non-designers on why design matters and built respect.

Third, celebrating outcomes, not outputs. When Andreina led her first major 
feature, I made sure the team all-hands highlighted not just that we shipped, 
but that conversion improved by X%. This reinforced that design success is 
measured by impact.

Culture is what you celebrate, what you tolerate, and what you make easy or 
hard to do."
```

**Why This Works**:
- Concrete mechanisms, not vague aspirations
- Real examples from your experience
- Shows systems thinking
- Quotable closing line

---

## Leadership Red Flags to Avoid

### RED FLAG 1: "I'd do it all myself if I could"
**Why It's Bad**: Doesn't understand leadership is about multiplying through others

**Instead Say**: 
"My goal is to make myself replaceable, not indispensable. Success is when the 
team can thrive without me in every conversation."

---

### RED FLAG 2: "I don't like politics"
**Why It's Bad**: Leadership requires navigating organizational dynamics

**Instead Say**:
"I see stakeholder management as understanding different perspectives and finding 
alignment, not avoiding disagreement. It's part of the job."

---

### RED FLAG 3: "I'd just hire more designers"
**Why It's Bad**: Doesn't show strategic thinking about leverage

**Instead Say**:
"I'd first assess whether our constraint is headcount or efficiency. At Kushki, 
the design system created more leverage than immediate hiring would have."

---

### RED FLAG 4: "I'm very detail-oriented" (when asked about weaknesses)
**Why It's Bad**: Cliché, sounds like you micromanage

**Instead Say**:
"I sometimes dive deep into craft details before ensuring we're solving the right 
strategic problem. I've learned to set check-ins to zoom out."

---

### RED FLAG 5: Talking only about YOUR designs
**Why It's Bad**: Leadership is about the team's success, not yours

**Instead Say**:
"The work I'm proudest of is what the team accomplished - like when Andreina 
independently led her first feature to successful launch."

---

## Demonstrating Leadership Without Management Title

### STRATEGY 1: Reframe "Informal Leadership"

**Don't Say**: "I haven't managed anyone yet"

**Do Say**: 
"While I haven't had formal reports, I've led through influence and mentorship. 
At Kushki I mentored junior designers, at Fincast I was the design voice in 
product strategy, and I've consistently led cross-functional projects."

---

### STRATEGY 2: Show Leadership Mindset

**Example**:
"Even as an IC, I've always thought like a leader - how do we scale design beyond 
my capacity? How do we build systems that outlast individual contributors? At 
Kushki, the design system was a leadership decision, not a task I was assigned."

---

### STRATEGY 3: Demonstrate "Manager of One"

**Example**:
"I've managed my own career strategically: seeking out mentorship opportunities, 
taking on projects that build leadership skills, and documenting my work to 
teach others. This self-direction is the foundation of managing others."

---

### STRATEGY 4: Highlight Readiness to Learn

**Example**:
"I know there are aspects of formal people management I haven't done yet - 
performance reviews, hiring interviews, budget ownership. But I've prepared by 
[reading books, taking courses, seeking mentorship from design leaders]. I'm 
ready to learn on the job with support."

**Books to Mention** (if asked):
- "The Manager's Path" by Camille Fournier
- "Radical Candor" by Kim Scott
- "High Output Management" by Andy Grove

---

## Database Commands

**View**:
- `"Show all leadership narratives"` - List all versions
- `"Show narrative for [role-level]"` - Filter by role
- `"Show successful leadership answers"` - What worked in interviews

**Create**:
- `"Build leadership narrative for Lead Designer role at [company-type]"`
- `"Generate leadership philosophy statement"`
- `"Create answer to [leadership question]"`

**Update**:
- `"Refine narrative [id] based on [feedback]"`
- `"Update leadership evolution: moved to [new-stage]"`
- `"Add leadership moment: [new-story]"`

**Analysis**:
- `"What leadership themes resonate most?"`
- `"Track narrative evolution over time"`

---

## Usage Instructions

### For Interview Prep:
```
"Build leadership narrative for:
Role: Lead Product Designer
Company: Series A startup
Focus: Team building, scaling design, stakeholder management"
```

### For Specific Questions:
```
"Generate answer to: 'How would you build a design team from scratch?'
Context: Early-stage startup, first design hire"
```

### For Philosophy Refinement:
```
"Review my leadership philosophy statement.
Feedback from last interview: Too theoretical, needed more examples.
Refine it."
```

---

## Output Format

```
---
LEADERSHIP NARRATIVE
ID: ln_XXX
Role Level: [Lead/Principal/Head of Design]
Company Type: [Startup/Scale-up/Enterprise]
Date: [Date]

---

LEADERSHIP PHILOSOPHY:
[2-3 paragraph statement of your leadership approach]

LEADERSHIP STYLE:
[Coaching/Facilitative/Evidence-based - articulation]

KEY EVIDENCE STORIES:
1. [Story 1 name] - Demonstrates [competency]
2. [Story 2 name] - Demonstrates [competency]
3. [Story 3 name] - Demonstrates [competency]

LEADERSHIP VISION FOR THIS ROLE:
[What you'd focus on in first 6-12 months]

COMMON QUESTIONS & ANSWERS:

Q: "What's your leadership style?"
A: [Your tailored answer]

Q: "How do you handle underperformance?"
A: [Your tailored answer]

Q: [Other relevant questions]
A: [Your answers]

GROWTH AREAS (Address Proactively):
- [Gap 1: How you're addressing it]
- [Gap 2: How you're addressing it]

---

DATABASE STATUS: ✅ Saved as ln_XXX
---
```

---

## Quality Checklist

Before using any leadership narrative:

- [ ] **Philosophy is clear** (not jargon or buzzwords)
- [ ] **Evidence-based** (every claim backed by story)
- [ ] **Authentic voice** (sounds like you, not copied)
- [ ] **Specific examples** (names, metrics, outcomes)
- [ ] **Forward-looking** (vision for next role)
- [ ] **Acknowledges growth areas** (honest about gaps)
- [ ] **Business-minded** (connects to outcomes, not just craft)
- [ ] **People-focused** (about team growth, not your glory)
- [ ] **Practiced out loud** (conversational, not written)
- [ ] **Tailored to role** (Lead vs. Principal vs. Head)

---

## Notes
- Leadership is demonstrated through actions, not titles
- Your coaching style is a strength - own it confidently
- Informal leadership experience is real leadership
- Show readiness to learn formal management skills
- Connect every leadership claim to specific evidence
- Business thinking separates design leaders from designers
- Practice these answers out loud - they should sound natural
- Your leadership narrative will evolve - refine it with each interview
