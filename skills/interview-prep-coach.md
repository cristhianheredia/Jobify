# Interview Prep Coach

## Purpose
Prepare for design interviews by generating STAR stories, anticipating questions, practicing portfolio walkthroughs, and developing strategic responses that highlight your strengths while addressing potential concerns.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Key Companies**: Kushki (fintech, scaled team), Fincast (B2B SaaS, first designer), Koombea
- **Leadership Style**: Coaching, facilitative, evidence-based
- **Unique Strengths**: First design hire experience, B2B complexity, team building, strategic ambiguity navigation
- **Past Success**: Thoughtworks interview (4 STAR stories prepared: people development/Andreina, strategic ambiguity/Fincast pivot, business outcomes/formula module, upward influence)

## Input
- Company name and role
- Interview stage (screening, behavioral, portfolio review, panel, etc.)
- Known interview format (if available)
- Specific competencies being evaluated (from JD or recruiter)
- Your concerns or "yellow flags" to address

## Output
- Tailored STAR stories for key competencies
- Anticipated questions with strategic answers
- Portfolio walkthrough script
- Questions to ask the interviewer
- Saved to database for continuous improvement

---

## INTERVIEW PREP DATABASE MANAGEMENT

### Database Structure
**File**: `/data/interview-prep.json`

**Schema**:
```json
{
  "interviews": [
    {
      "id": "int_001",
      "company": "Thoughtworks",
      "role": "Senior Design Lead",
      "stage": "leadership-interview",
      "date": "2025-04-15",
      "stories_prepared": [
        {
          "competency": "people-development",
          "story": "Mentoring Andreina at Kushki",
          "outcome": "well-received"
        },
        {
          "competency": "strategic-ambiguity",
          "story": "Fincast product pivot",
          "outcome": "well-received"
        },
        {
          "competency": "business-outcomes",
          "story": "Formula module redesign",
          "outcome": "well-received"
        },
        {
          "competency": "upward-influence",
          "story": "Design system advocacy at Kushki",
          "outcome": "well-received"
        }
      ],
      "questions_asked": [
        "Tell me about your leadership style",
        "How do you handle disagreement with stakeholders?"
      ],
      "outcome": "advanced",
      "learnings": [
        "STAR format with concrete examples worked well",
        "Showing vulnerability (challenges) built trust",
        "Tying stories to business impact resonated"
      ]
    }
  ],
  "story_bank": [
    {
      "name": "Mentoring Andreina",
      "company": "Kushki",
      "competencies": ["people-development", "coaching", "leadership"],
      "situation": "Junior designer struggling with strategic thinking",
      "task": "Level her up for complex projects",
      "action": "1:1 coaching, STAR framework, shadowing, feedback loops",
      "result": "Promoted to mid-level, led 2 major features independently",
      "usage_count": 3,
      "success_rate": "100%"
    }
  ]
}
```

### Workflow Instructions for Claude Code

#### BEFORE interview:
1. **Load company context** from company-research-brief
2. **Match competencies** from JD to story bank
3. **Generate STAR stories** tailored to company/role
4. **Prepare questions** to ask interviewer
5. **Flag yellow flags** to address proactively

#### AFTER interview:
1. **Save prep materials** with what was actually asked
2. **Track story performance** (which ones landed well)
3. **Capture learnings** for future interviews
4. **Update story bank** with new examples

---

## Interview Types & Preparation Strategy

### TYPE 1: Phone/Video Screening (30-45 min)
**Who**: Recruiter or Junior Designer
**Focus**: Culture fit, basic qualifications, logistics

**What They Ask**:
- "Walk me through your background"
- "Why are you interested in [Company]?"
- "What are you looking for in your next role?"
- "Tell me about your design process"
- "What's your experience with [tool/method]?"

**Preparation Strategy**:
```
1. 2-minute background pitch (elevator version)
2. Company-specific "why here" (from company research)
3. Clear "what I'm looking for" statement
4. High-level process overview (not too detailed)
5. 2-3 questions about role/company
```

**Goal**: Pass to next stage, don't over-complicate

---

### TYPE 2: Portfolio Review (45-60 min)
**Who**: Hiring Manager or Senior Designer
**Focus**: Design work, process, thinking

**What They Ask**:
- "Walk me through your portfolio"
- "Tell me about [specific project]"
- "How did you approach [challenge]?"
- "What would you do differently now?"
- "What's your proudest design work?"

**Preparation Strategy**:
```
1. Select 2-3 case studies (tailored to company type)
2. 5-minute walkthrough per project
3. Anticipate questions per project
4. Practice transitions between projects
5. Have "what I'd do differently" ready
```

**Portfolio Walkthrough Script Structure**:
```
For each project (5 min):
- Context (30 sec): Company, role, timeline
- Problem (1 min): What made this hard
- Process (2 min): How you approached it
- Outcome (1 min): Impact with metrics
- Learning (30 sec): What you took away
```

---

### TYPE 3: Behavioral Interview (60 min)
**Who**: Hiring Manager, Design Lead, or Panel
**Focus**: Competencies, past behavior, culture fit

**What They Ask**:
- "Tell me about a time when..."
- "Describe a situation where..."
- "Give me an example of..."
- "How do you handle..."

**Preparation Strategy**:
```
1. Map competencies from JD
2. Prepare 6-8 STAR stories covering key competencies
3. Practice concise delivery (2-3 min per story)
4. Have variation stories ready (same competency, different examples)
5. Prepare follow-up question responses
```

**Common Competencies for Senior/Lead Designers**:
- Collaboration (cross-functional)
- Leadership (formal or informal)
- Strategic thinking
- Handling ambiguity
- Influence without authority
- Conflict resolution
- Prioritization
- User advocacy
- Business thinking
- Resilience/handling failure

---

### TYPE 4: Technical/Craft Deep-Dive (60-90 min)
**Who**: Senior Designers, Design Leads
**Focus**: Design craft, systems thinking, expertise

**What They Ask**:
- "How do you approach [specific design problem]?"
- "Walk me through your design systems experience"
- "How do you ensure accessibility?"
- "What's your QA process with developers?"
- "How do you make design decisions?"

**Preparation Strategy**:
```
1. Review their product thoroughly (use it)
2. Prepare specific examples of craft excellence
3. Know your tools/methods deeply
4. Have design principles ready
5. Be ready to critique their product constructively
```

---

### TYPE 5: Stakeholder/Leadership Interview (45-60 min)
**Who**: VP Product, CTO, CEO, Head of Design
**Focus**: Strategic thinking, business acumen, leadership potential

**What They Ask**:
- "How do you influence without authority?"
- "Tell me about leading through change"
- "How do you prioritize competing requests?"
- "What's your approach to building a design team?"
- "How do you measure design success?"

**Preparation Strategy**:
```
1. Understand business context (from company research)
2. Prepare executive-level STAR stories (business outcomes)
3. Have questions about company strategy ready
4. Show business acumen, not just design craft
5. Demonstrate leadership mindset
```

---

### TYPE 6: Panel Interview (60-90 min)
**Who**: 3-6 people from different functions
**Focus**: Fit across multiple dimensions

**What They Ask**:
- Varied questions from each person's perspective
- Engineer: "How do you work with technical constraints?"
- PM: "How do you balance user needs vs. business goals?"
- Designer: "Walk me through your process"
- Leader: "How do you handle ambiguity?"

**Preparation Strategy**:
```
1. Research each panelist (LinkedIn)
2. Prepare stories that work for multiple audiences
3. Practice pivoting tone (technical vs. strategic)
4. Have 1-2 questions per panelist
5. Make eye contact with everyone, not just questioner
```

---

## STAR Story Framework (Adapted for Design)

### Structure: STAR
**S**ituation - **T**ask - **A**ction - **R**esult

### Story Length Guidelines
- **Screening**: 1-2 minutes (brief)
- **Behavioral**: 2-3 minutes (detailed)
- **Follow-up**: Add 30-60 seconds if asked

---

### SITUATION (Context)
**What to Include**:
- Company and product
- Your role
- Team structure
- Timeline/constraints
- Why it mattered

**Keep Brief**: 2-3 sentences

**Example**:
```
"At Kushki, a fintech payment platform, I was the lead designer 
supporting three product squads. We were growing rapidly, but design 
was becoming a bottleneck - engineers were shipping features without 
design input, creating UX debt."
```

---

### TASK (The Challenge)
**What to Include**:
- The specific problem you needed to solve
- What made it difficult
- What was at stake

**Key**: Make it clear this wasn't trivial

**Example**:
```
"My challenge was to scale design's impact without immediately adding 
headcount. I needed to enable engineers to maintain quality while I 
focused on strategic work, but we had no design system or standards."
```

---

### ACTION (What YOU Did)
**What to Include**:
- Your specific actions (use "I", not "we")
- Your decision-making process
- How you collaborated (if relevant)
- Steps you took

**This is the longest section**: 50% of story time

**Structure Options**:

**OPTION A: Chronological**:
```
"First, I... Then, I... Finally, I..."
```

**OPTION B: Framework-Based**:
```
"I approached this in three ways:
1. [Action category 1]
2. [Action category 2]
3. [Action category 3]"
```

**Example**:
```
"I took a three-pronged approach:

First, I conducted a UI audit to identify inconsistencies and 
created a business case for a design system, showing how it would 
3x designer efficiency.

Second, I partnered with the most design-conscious engineer to 
co-create the foundational components, building buy-in through 
collaboration rather than dictating from design.

Third, I established a weekly design critique where engineers could 
share work-in-progress and get async feedback, reducing the 
bottleneck without requiring my presence in every meeting."
```

**Critical**: Use "I" not "we" - interviewers need to know YOUR contribution

---

### RESULT (Impact)
**What to Include**:
- Quantified outcomes (metrics)
- Qualitative wins
- Business impact
- What you learned

**Metrics > Feelings**

**Example**:
```
"Results:
- Design system adoption went from 0% to 95% of components in 6 months
- Designer efficiency: I went from supporting 1 squad to enabling 
  design across 3 squads
- Handoff time dropped from 3 days to same-day
- Cross-functional NPS with design increased from 6.2 to 8.7

More importantly, this positioned design as a strategic function, 
leading to approval for two additional design hires. I learned that 
showing ROI in business terms - not just craft - unlocks resources."
```

---

## Story Bank (Your Pre-Built Stories)

### STORY 1: Mentoring Andreina (People Development)
**Competencies**: People development, coaching, leadership, patience, growth mindset

**Situation**:
"At Kushki, I was mentoring Andreina, a junior designer who was talented 
but struggling with strategic thinking and articulating her design decisions."

**Task**:
"My goal was to level her up so she could independently lead complex 
projects and eventually take on mid-level responsibilities."

**Action**:
"I structured our mentorship around three pillars:

First, weekly 1:1s where we used the STAR framework to build her case 
study storytelling, helping her connect design work to business outcomes.

Second, shadowing and co-design sessions on strategic projects, where 
I'd narrate my thinking process out loud, then gradually hand her more 
decision-making ownership.

Third, creating a safe feedback loop where she could share work early 
and often, building her confidence through iteration rather than 
perfection."

**Result**:
"Over 12 months, Andreina was promoted to mid-level designer and 
independently led two major features end-to-end. More importantly, 
she developed the confidence to push back on stakeholders with 
evidence-based rationale. This experience taught me that the best 
mentorship is about building thinking frameworks, not just teaching tools."

**Usage**: Leadership roles, people development questions, coaching culture

---

### STORY 2: Fincast Product Pivot (Strategic Ambiguity)
**Competencies**: Strategic thinking, ambiguity navigation, adaptability, resilience

**Situation**:
"At Fincast, I was the first and only designer. Midway through the year, 
leadership decided to pivot from SMB to enterprise customers - a complete 
rethink of our product assumptions while keeping the existing product running."

**Task**:
"I needed to validate this new direction quickly, re-architect the UX for 
enterprise needs, and keep the team aligned despite massive uncertainty 
about what we were building."

**Action**:
"I treated this like a discovery sprint:

First, I conducted rapid validation interviews with 8 enterprise prospects 
to understand if our core value prop held, identifying three critical gaps 
in our assumptions.

Second, I created multiple conceptual prototypes at different fidelity 
levels - from sketches to clickable demos - allowing leadership to 
pressure-test strategic direction without committing engineering resources.

Third, I established a weekly 'strategy sync' with the CEO where I'd 
present findings and prototypes, using design as a tool to clarify thinking, 
not just execute on already-decided features."

**Result**:
"While we didn't ship the exact designs (the pivot continued evolving), 
the research informed our entire roadmap for the next year. The CEO later 
told me that design became the strategic anchor during uncertainty. I learned 
that in ambiguous environments, design's value is often in asking the right 
questions, not having all the answers."

**Usage**: Startup roles, ambiguity questions, strategic thinking

---

### STORY 3: Formula Module Redesign (Business Outcomes)
**Competencies**: Business thinking, user research, impact focus, problem-solving

**Situation**:
"At Fincast, our formula builder was powerful but intimidating. Users spent 
3+ weeks in onboarding, and 40% of trial users never completed their first 
formula - directly impacting our trial-to-paid conversion."

**Task**:
"I needed to reduce onboarding time and increase trial conversion, but we 
had limited engineering resources and couldn't rebuild the entire system."

**Action**:
"I started with a UX audit and 8 user interviews to understand the root cause. 
I discovered users weren't intimidated by complexity - they were frustrated 
by unpredictability. They wanted real-time feedback, not trial-and-error.

I then created three conceptual approaches and tested them with 5 customers. 
Progressive disclosure with live preview won.

Working with the lead engineer, I phased the implementation across 3 sprints, 
shipping incremental improvements while gathering feedback, rather than a 
big-bang release."

**Result**:
"Onboarding time dropped from 3 weeks to 4 days (87% reduction), trial-to-paid 
conversion increased by 11 points, and formula-related support tickets decreased 
65%. The redesign became a sales differentiator mentioned in 70% of customer 
win stories. This taught me that connecting design improvements to specific 
business metrics unlocks executive buy-in and resources."

**Usage**: Business-focused companies, IC senior roles, impact questions

---

### STORY 4: Design System Advocacy (Upward Influence)
**Competencies**: Influence without authority, business case building, strategic communication

**Situation**:
"At Kushki, I recognized we needed a design system, but leadership was 
hesitant to allocate engineering resources to 'non-feature work' during a 
growth phase."

**Task**:
"I needed to build a compelling business case and secure buy-in from 
leadership without formal authority to dictate priorities."

**Action**:
"First, I quantified the cost of inconsistency: I tracked time spent on 
redundant design work and calculated we were losing 15-20 hours per week 
across design and engineering.

Second, I created a lightweight MVP with the most design-conscious engineer, 
proving the concept without asking for dedicated resources upfront. This 
pilot showed we could reduce handoff time by 60%.

Third, I framed the ask in business terms: 'This 3-week investment will 
3x designer efficiency and reduce QA cycles by 40%,' connecting to metrics 
leadership cared about."

**Result**:
"Leadership approved a dedicated sprint for design system foundation. Within 
6 months, 95% of new components used the system, designer-to-engineer handoff 
went from 3 days to same-day, and we reduced visual QA cycles by 40%. I learned 
that influence requires translating design value into the language stakeholders 
already speak - usually time and money."

**Usage**: Leadership roles, influence questions, stakeholder management

---

### STORY 5: Cross-Functional Collaboration (Collaboration)
**Competencies**: Collaboration, facilitation, conflict resolution

**Situation**:
"At Kushki, Product and Engineering had competing priorities for a merchant 
dashboard redesign. PM wanted feature parity with competitors; Engineering 
wanted to reduce technical debt."

**Task**:
"I needed to align both teams on a shared approach that addressed both 
concerns without compromising UX quality."

**Action**:
"I facilitated a design sprint where I brought both teams into the room:

First, I had each side present their constraints and goals, surfacing a 
shared pain point: our current architecture made ANY change slow.

Second, I proposed a phased approach: Phase 1 would tackle tech debt in 
the most-used flows (giving eng what they needed), Phase 2 would add 
competitive features (giving PM what they wanted), with design ensuring 
visual consistency across both phases.

Third, I created shared success metrics that both teams could rally around: 
load time + feature adoption + user satisfaction."

**Result**:
"Both teams bought into the plan. We shipped Phase 1 in half the time 
Engineering initially estimated, and PM got their competitive features by 
quarter-end. More importantly, this established a collaborative precedent 
where design facilitated alignment, not just took orders. I learned that 
good facilitation often means finding the third option no one saw initially."

**Usage**: Collaboration questions, conflict resolution, cross-functional roles

---

### STORY 6: Handling Failure/Resilience
**Competencies**: Resilience, learning mindset, vulnerability, growth

**Situation**:
"At [Company], I pushed for a redesign of [feature] based on user feedback, 
convinced it would improve engagement."

**Task**:
"After launch, engagement actually dropped 15%, and I had to own the failure 
and course-correct quickly."

**Action**:
"First, I acknowledged the outcome openly with the team and leadership - 
no excuses, just facts.

Second, I dug into the data to understand why: turned out power users felt 
the new design was 'dumbed down' and less efficient for their workflows. 
We'd over-optimized for new users.

Third, I advocated for a rapid iteration that reintroduced power-user 
shortcuts while keeping the simplified new-user flow, essentially creating 
two modes."

**Result**:
"Within 3 weeks, we shipped the iteration and engagement recovered to 
baseline + 8%. The experience taught me to segment users more carefully 
and never assume one solution fits all use cases. More importantly, it 
built trust with leadership that I could own mistakes and fix them quickly."

**Usage**: Failure questions, resilience, learning mindset

---

## Question Bank by Competency

### COLLABORATION
**Likely Questions**:
- "Tell me about a time you disagreed with a PM/Engineer"
- "How do you handle feedback you don't agree with?"
- "Describe working with a difficult stakeholder"
- "Tell me about a cross-functional project"

**Your Best Stories**: Cross-functional collaboration, Design system advocacy

**Answer Framework**:
- Acknowledge multiple perspectives
- Show facilitation, not dictation
- Emphasize shared goals
- Demonstrate listening + influence

---

### LEADERSHIP (for Lead/Principal roles)
**Likely Questions**:
- "Tell me about your leadership style"
- "How do you mentor junior designers?"
- "Describe building or scaling a design team"
- "How do you establish design culture?"

**Your Best Stories**: Mentoring Andreina, Design team scaling at Kushki

**Answer Framework**:
- Coaching, not commanding
- Empowering others
- Building systems, not just doing work
- Measuring team success, not just your output

---

### STRATEGIC THINKING
**Likely Questions**:
- "How do you prioritize design work?"
- "Tell me about navigating ambiguity"
- "How do you connect design to business goals?"
- "Describe a time you influenced product strategy"

**Your Best Stories**: Fincast pivot, Formula module redesign, Design system advocacy

**Answer Framework**:
- Business context first
- Design as strategic tool
- Data-informed decisions
- Outcomes over outputs

---

### PROBLEM SOLVING
**Likely Questions**:
- "Tell me about a complex design problem you solved"
- "How do you approach a new design challenge?"
- "Describe a time you had to work with constraints"
- "What's the hardest design problem you've solved?"

**Your Best Stories**: Formula module redesign, Design system with limited resources

**Answer Framework**:
- Define problem clearly (don't jump to solution)
- Show research/discovery
- Explain decision rationale
- Measure success

---

### RESILIENCE / FAILURE
**Likely Questions**:
- "Tell me about a time you failed"
- "Describe a project that didn't go as planned"
- "How do you handle criticism?"
- "What would you do differently looking back?"

**Your Best Stories**: Handling failure story, Pivot stories

**Answer Framework**:
- Own it (no blame)
- What you learned
- How you applied learning
- Show growth mindset

---

### USER ADVOCACY
**Likely Questions**:
- "How do you balance user needs vs. business goals?"
- "Tell me about championing users against pushback"
- "How do you validate design decisions?"
- "Describe your research process"

**Your Best Stories**: Formula module (research-driven), Any project with clear user outcomes

**Answer Framework**:
- User research process
- Data + qualitative insights
- Making the business case for user needs
- Measuring user satisfaction

---

## Portfolio Walkthrough Script

### INTRODUCTION (30 seconds)
```
"Thanks for the opportunity to share my work. I've selected three 
projects that I think are relevant to [Company]'s challenges:

1. [Project 1] - which shows [relevant skill]
2. [Project 2] - which demonstrates [relevant skill]
3. [Project 3] - which highlights [relevant skill]

I'll keep each to about 5 minutes and would love your questions 
along the way. Should I dive in?"
```

### PER PROJECT (5 minutes each)

**Minute 1: Context**
```
"This project was at [Company], where I was [role]. The challenge 
was [problem] for [users]. This mattered because [business impact]."
```

**Minutes 2-3: Process & Insights**
```
"My approach started with [research]. Through [method], I discovered 
[key insight]. This led me to [strategic decision], because [rationale].

The core design challenge was [challenge], and I addressed it by 
[solution approach]."
```

**Minute 4: Solution (show designs)**
```
"Here's the key flow... [walk through 2-3 screens]

A few design decisions worth highlighting:
- [Decision 1 with rationale]
- [Decision 2 with rationale]"
```

**Minute 5: Outcome & Learning**
```
"Results: [Metric 1], [Metric 2], [Qualitative outcome].

If I were to do this again, I'd [reflection]. What I took away is 
[learning that applies to future work]."
```

### CLOSING (30 seconds)
```
"Those are the three projects I wanted to highlight. I have others 
I can share if relevant, but wanted to see if you have questions 
on any of these first?"
```

---

## Questions to Ask the Interviewer

### FOR HIRING MANAGER (Design Lead, Head of Design)

**About the Role**:
- "What does success look like in this role in the first 6 months?"
- "What are the biggest design challenges the team is facing right now?"
- "How do you see this role evolving over the next year?"

**About the Team**:
- "Can you tell me about the design team structure and how it's embedded?"
- "What's the design maturity like - do you have a design system, research practice, etc.?"
- "How does the team collaborate across functions?"

**About Them**:
- "What excites you most about design at [Company] right now?"
- "What's been your biggest challenge in building/leading design here?"

---

### FOR PRODUCT MANAGER

**About Collaboration**:
- "How do Product and Design typically collaborate here?"
- "Can you walk me through a recent feature from idea to launch?"
- "How are design trade-offs typically resolved?"

**About Strategy**:
- "How much does design influence product strategy vs. execute on it?"
- "What's the balance between discovery work and delivery?"

---

### FOR ENGINEER

**About Process**:
- "What's the handoff process like from design to engineering?"
- "How early does design involve engineering in the process?"
- "What's been your best experience working with a designer here?"

**About Constraints**:
- "What technical constraints should design be aware of?"
- "How do you typically handle design requests that are technically complex?"

---

### FOR EXECUTIVE (VP, CEO, CTO)

**About Business**:
- "What role do you see design playing in achieving [Company]'s goals?"
- "How do you measure design's impact on the business?"
- "What's the vision for design at [Company] in 2-3 years?"

**About Company**:
- "What's the biggest challenge [Company] is facing right now?"
- "What differentiates [Company] in the market?"

---

## Yellow Flags & How to Address

### YELLOW FLAG: Limited Leadership Experience
**How They Might Probe**:
- "Tell me about managing a team"
- "How do you handle performance issues?"

**How to Address**:
- Reframe to "informal leadership"
- Use mentoring stories (Andreina)
- Show leadership mindset even as IC
- "While I haven't had formal reports, I've led through influence..."

---

### YELLOW FLAG: Limited [Specific Industry] Experience
**How They Might Probe**:
- "What's your experience in [their industry]?"
- "How would you approach [industry-specific challenge]?"

**How to Address**:
- Emphasize transferable skills
- Show you've researched their space
- Draw parallels to your experience
- "While I haven't worked in [industry] specifically, my experience with [similar complexity] translates because..."

---

### YELLOW FLAG: Gap in Employment
**How They Might Probe**:
- "I see a gap in your timeline, what were you doing?"

**How to Address**:
- Be honest and brief
- Frame positively (learning, growth, agency work)
- Redirect to what you're looking for now
- "I was running my agency (Poltergeist) and consulting, which gave me [skill/insight], but I'm now seeking [what you want]"

---

### YELLOW FLAG: Frequent Job Changes
**How They Might Probe**:
- "I notice you've moved companies a few times, why?"

**How to Address**:
- Show intentional career progression
- Connect each move to growth/learning
- Emphasize what you're looking for now (stability)
- "Each move was strategic: [Company 1] taught me [X], [Company 2] taught me [Y], now I'm looking for [Z] which I see at [Their Company]"

---

## Common Tricky Questions & How to Handle

### "What's your biggest weakness?"

**Bad Answer**: "I'm a perfectionist" (cliché)

**Good Answer**: 
"I sometimes dive too deep into details before stepping back to see the big 
picture. I've learned to set timers during design work - after 2 hours of 
detailed work, I force myself to zoom out and ask 'is this solving the right 
problem?' It's helped me balance craft with strategic thinking."

**Framework**: Real weakness + what you're doing about it + growth shown

---

### "Why are you leaving your current role?"

**Bad Answer**: Complaints about current company

**Good Answer**:
"I'm looking for [positive thing about target company] which aligns with 
where I want to grow. At my current role, I've accomplished [achievement], 
and I'm ready for [next challenge] which I see at [Company]."

**Framework**: Pull toward new opportunity, not push away from old

---

### "Where do you see yourself in 5 years?"

**Bad Answer**: "I want your job" or "I don't know"

**Good Answer**:
"In the next few years, I see myself deepening my impact in [specific area - 
systems, strategy, team building] while growing into formal design leadership. 
I'm excited about [Company] because [how this role fits that trajectory]."

**Framework**: Show ambition + alignment with company's growth

---

### "What's your salary expectation?"

**Bad Answer**: Giving exact number too early

**Good Answer**:
"I'm looking for compensation in line with senior design roles at [stage] 
companies, which I understand ranges from [broad range]. I'm open to 
discussing once I better understand the full scope of the role and total 
package including equity. What's the budget range for this role?"

**Framework**: Deflect politely, ask for their range

---

### "Do you have any questions for us?"

**Bad Answer**: "No" or only asking about perks

**Good Answer**: Ask 2-3 questions from categories above

**Framework**: 
- 1 about the role/team (shows you're thinking about the work)
- 1 about the company/strategy (shows you're thinking bigger picture)
- 1 personal to the interviewer (builds connection)

---

## Interview Day Logistics

### BEFORE THE INTERVIEW

**24 Hours Before**:
- [ ] Review company research brief
- [ ] Review your prepared STAR stories
- [ ] Review your portfolio (practice walkthrough)
- [ ] Prepare 5-7 questions to ask
- [ ] Check tech setup (video, audio, internet)
- [ ] Prepare environment (quiet space, good lighting)

**1 Hour Before**:
- [ ] Review company website and your application
- [ ] Skim recent company news
- [ ] Do vocal warm-ups (speak out loud)
- [ ] Have water nearby
- [ ] Close all other tabs/apps
- [ ] Join 5-10 minutes early

---

### DURING THE INTERVIEW

**First 2 Minutes**:
- Smile (they can hear it)
- Thank them for their time
- Small talk warmly but briefly
- Match their energy level

**During Questions**:
- Pause before answering (shows thoughtfulness)
- Use STAR structure for behavioral
- Ask clarifying questions if needed
- Use specific examples, not generalities
- Watch for time (2-3 min per story)

**During Portfolio Review**:
- Be concise (5 min per project)
- Focus on thinking, not just pixels
- Invite questions throughout
- Show enthusiasm for your work
- Be honest about challenges/learnings

**Last 5 Minutes**:
- Ask your prepared questions
- Thank them for their time
- Ask about next steps/timeline
- Reiterate your interest
- Send follow-up note address

---

### AFTER THE INTERVIEW

**Within 24 Hours**:
- [ ] Send thank-you email (personalized, brief)
- [ ] Update database with questions asked
- [ ] Note which stories landed well
- [ ] Capture any red flags or concerns
- [ ] Record your self-assessment

**Thank-You Email Template**:
```
Subject: Thank you - [Your Name] - [Role] Interview

Hi [Name],

Thank you for taking the time to speak with me today about the 
[Role] position. I enjoyed learning about [specific thing they 
mentioned] and discussing [specific topic from conversation].

Our conversation reinforced my interest in [Company], particularly 
[specific aspect of role or company that excites you]. I'm excited 
about the opportunity to [specific contribution you could make based 
on conversation].

Please let me know if you need any additional information from me. 
I look forward to hearing about next steps.

Best regards,
Cristhian
```

---

## Database Commands

**View**:
- `"Show all interview prep"` - List all prep sessions
- `"Show prep for [company-type]"` - Filter by company
- `"Show successful story usage"` - What stories work best

**Create**:
- `"Prepare for interview at [Company], [Role]"` - Generate prep
- `"Create STAR story for [competency]"` - Build new story
- `"Generate questions to ask [role type]"` - Interviewer questions

**Update**:
- `"Update interview [id] outcome: [result]"` - Track results
- `"Add learning to [id]: [insight]"` - Capture lessons
- `"Mark story [name] as successful for [competency]"` - Track performance

**Analysis**:
- `"Which stories led to offers?"` - Success patterns
- `"What questions come up most often?"` - Prep priorities
- `"Show interview success rate by company type"` - Strategic insights

---

## Usage Instructions

### Basic Prep:
```
"Prepare me for interview:
Company: Remote.com
Role: Senior Product Designer
Stage: Behavioral interview (60 min)
Known focus areas: Collaboration, leadership, B2B SaaS experience"
```

### With Yellow Flags:
```
"Prepare me for [Company] interview.
My concerns: They might question my limited fintech experience.
How should I address this?"
```

### Portfolio Walkthrough:
```
"Help me build a 15-minute portfolio walkthrough for [Company].
Company type: Series A B2B SaaS
Focus on: Systems thinking, business impact"
```

### Post-Interview Learning:
```
"I just finished interview at [Company]. Here's what they asked: [list]
Which of my stories worked well? What should I improve?"
```

---

## Output Format

```
---
INTERVIEW PREP
ID: int_XXX
Company: [Company Name]
Role: [Role Title]
Stage: [Interview Type]
Date: [Date]

---

WHAT THEY'RE EVALUATING:
- [Competency 1]
- [Competency 2]
- [Competency 3]

YOUR YELLOW FLAGS TO ADDRESS:
- [Flag 1: How to handle]
- [Flag 2: How to handle]

RECOMMENDED STAR STORIES:

Story 1: [Name]
Competency: [Competency]
[Full STAR story ready to use]

Story 2: [Name]
Competency: [Competency]
[Full STAR story ready to use]

...

PORTFOLIO WALKTHROUGH SCRIPT:
[15-minute script with 3 projects]

QUESTIONS TO ASK THEM:
[5-7 strategic questions based on interviewers]

ANTICIPATED TRICKY QUESTIONS:
Question: [Likely question]
Your Answer: [Strategic response]

---

DATABASE STATUS: ✅ Saved as int_XXX

PREP CHECKLIST:
- [ ] Review STAR stories (practice out loud)
- [ ] Practice portfolio walkthrough
- [ ] Review company research
- [ ] Prepare questions to ask
- [ ] Test tech setup
---
```

---

## Quality Checklist

Before any interview:

- [ ] **STAR stories prepared** (6-8 covering key competencies)
- [ ] **Stories practiced out loud** (not just read)
- [ ] **Portfolio walkthrough timed** (5 min per project)
- [ ] **Company researched** (product, news, culture)
- [ ] **Questions prepared** (5-7 strategic questions)
- [ ] **Yellow flags addressed** (proactive strategy)
- [ ] **Tech tested** (video, audio, internet)
- [ ] **Environment prepared** (quiet, professional background)
- [ ] **Follow-up template** (ready to personalize)
- [ ] **Database updated** (capture learnings after)

---

## Notes
- Behavioral questions predict future behavior based on past
- STAR format works because it's structured and evidence-based
- Practice out loud - sounds different than reading silently
- Interviewers remember stories, not lists of skills
- Show vulnerability - perfect people aren't believable
- Ask good questions - it's a two-way evaluation
- Track what works - improve with each interview
- Thank-you notes matter - personalize, don't template
- Learn from every interview - update story bank
