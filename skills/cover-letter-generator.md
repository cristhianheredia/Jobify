# Cover Letter Generator

## Purpose
Generate compelling, personalized cover letters that connect your experience to specific company needs, demonstrate genuine interest, and position you as the ideal candidate.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Core Experience**: B2B SaaS, fintech, data-heavy products, complex systems
- **Key Companies**: Kushki (fintech, scaled design team), Fincast (B2B SaaS, sole designer), Koombea
- **Unique Positioning**: First design hire experience, team building, leadership in ambiguous environments
- **Location**: Ecuador (remote work)
- **Languages**: Spanish (native), English (fluent)

## Input
- Company name and role title
- Job description (full text or key requirements)
- Company research (from company-research-brief.md - optional but recommended)
- Specific angle/emphasis (optional - e.g., "emphasize leadership", "focus on fintech experience")
- Length preference (short: 250-350 words, standard: 350-500 words, long: 500-700 words)

## Output
- Complete cover letter ready to submit
- Multiple versions if needed (different angles)
- Saved to database for tracking and learning

---

## COVER LETTER DATABASE MANAGEMENT

### Database Structure
**File**: `/data/cover-letters.json`

**Schema**:
```json
{
  "letters": [
    {
      "id": "cl_001",
      "date": "2025-04-24",
      "company": "Remote.com",
      "role": "Senior Product Designer",
      "version": 1,
      "angle": "leadership-scaling",
      "word_count": 387,
      "key_themes": ["remote-first", "b2b-saas", "team-building"],
      "opening_hook": "first-design-hire-experience",
      "outcome": "applied",
      "notes": "Emphasized design team scaling experience"
    }
  ],
  "metadata": {
    "total_letters": 1,
    "last_updated": "2025-04-24",
    "success_rate": "0%"
  }
}
```

### Workflow Instructions for Claude Code

#### BEFORE generating new letter:
1. **Check database** for letters to same company or similar roles
2. **Show previous angles** if found:
   ```
   "Found 1 previous letter for similar role:
   - Crustdata (YC-backed, first design hire angle) - Interview secured ✅
   
   Suggested angle for this letter: [recommendation based on company research]"
   ```
3. **Identify successful patterns** from letters that led to interviews

#### AFTER generating letter:
1. **Save to database** with metadata
2. **Auto-tag** key themes and angle
3. **Assign unique ID** (cl_XXX format)
4. **Confirm**: "Cover letter saved as cl_015 for [Company]"

#### Outcome Tracking:
- `draft` - Generated but not sent
- `applied` - Submitted with application
- `no-response` - No reply from company
- `rejected` - Application rejected
- `interview` - Secured interview
- `offer` - Received offer

---

## Cover Letter Structure

### STANDARD FORMAT (3-4 Paragraphs)

#### Paragraph 1: HOOK + POSITIONING
**Purpose**: Grab attention, show you did research, position yourself

**Framework**:
```
[Specific insight about their product/company/challenge]
+ [Your unique positioning for this exact need]
+ [Why you're reaching out now]
```

**Hook Types**:
1. **Product Insight**: "I've been following [Product]'s evolution in [space], particularly [specific feature/approach]..."
2. **Mission Alignment**: "Your approach to [X] resonates with my experience at [Company] where..."
3. **Problem Recognition**: "Building [product type] for [audience] requires [specific skill] - something I've done at..."
4. **Mutual Connection**: "After speaking with [Name] about your design team's growth..." (if applicable)

**Positioning Statements** (choose based on role):
- First design hire: "Having been the first design hire at Fincast..."
- Team scaling: "I scaled the design team at Kushki from solo to [X]..."
- Complex B2B: "My experience designing data-heavy B2B tools at [companies]..."
- Leadership: "Leading design in ambiguous, high-growth environments is where I thrive..."

---

#### Paragraph 2: EXPERIENCE MATCH
**Purpose**: Connect your background to their specific needs

**Framework**:
```
[Their need #1] → [Your experience addressing it]
[Their need #2] → [Your experience addressing it]
[Their need #3] → [Your experience addressing it]
```

**Structure Options**:

**Option A - Project-Based**:
```
"At Kushki, I [specific project] which resulted in [metric/outcome]. 
This mirrors the challenges you're facing with [their product/challenge], 
where [your relevant skill] will be crucial."
```

**Option B - Skills Showcase**:
```
"The role requires [skill 1], [skill 2], and [skill 3] - 
areas where I have deep experience:

- [Skill 1]: At [Company], I [achievement]
- [Skill 2]: My work on [Project] involved [relevant work]
- [Skill 3]: I've consistently [pattern of behavior]"
```

**Option C - Story Arc**:
```
"My career has been defined by [overarching theme]. 
At Fincast, [example]. At Kushki, [example]. 
Now I'm seeking to bring this experience to [their challenge/opportunity]."
```

**Key Experiences to Draw From**:
1. **Kushki**: Fintech, scaled design team, design systems, complex B2B product
2. **Fincast**: First design hire, strategic pivot, formula module redesign (business impact)
3. **Koombea**: Early career, foundational skills
4. **Poltergeist**: Agency experience, diverse client work, embedded design services

---

#### Paragraph 3: VALUE PROPOSITION
**Purpose**: What you'll bring, why you specifically

**Framework**:
```
[Unique value #1: e.g., "cross-functional leadership"]
+ [Unique value #2: e.g., "design systems thinking"]
+ [Unique value #3: e.g., "business outcome focus"]
= [How this creates impact at their company]
```

**Value Props Based on Role Type**:

**For IC Senior Roles**:
- Deep craft expertise in [specific area]
- Systems thinking for scalable design
- Data-informed decision making
- Cross-functional collaboration strength

**For Lead/Principal Roles**:
- Design team building experience
- Strategic design thinking
- Stakeholder influence and alignment
- Process and culture establishment

**For First Design Hire**:
- 0-to-1 design foundation experience
- Wearing multiple hats (research, UI, systems)
- Establishing design culture
- Working with constraints (time, resources, buy-in)

**Differentiation Angles**:
- "Having worked in both early-stage (Fincast) and scaling (Kushki) environments..."
- "My background in fintech gives me deep understanding of [regulatory/complex workflows]..."
- "I don't just design interfaces - I focus on [business outcomes/user impact]..."
- "My facilitative leadership style means I [specific behavior]..."

---

#### Paragraph 4: CLOSING + CALL TO ACTION
**Purpose**: Reinforce interest, invite conversation

**Framework**:
```
[Enthusiasm statement]
+ [Specific next step or conversation topic]
+ [Professional close]
```

**Closing Options**:

**Standard**:
```
"I'd love to discuss how my experience scaling design at [Company] 
can help [Their Company] achieve [their goal]. I'm particularly 
excited to explore [specific aspect of role/product]."
```

**Project-Specific**:
```
"I'm excited about the opportunity to [specific contribution]. 
I'd welcome the chance to share my approach to [relevant challenge] 
and learn more about your product vision."
```

**Culture-Forward**:
```
"Your commitment to [value] aligns with how I approach design leadership. 
I'd love to discuss how we can collaborate to [shared goal]."
```

**Call to Action**:
- "I'd welcome the opportunity to discuss this further."
- "I look forward to exploring how I can contribute."
- "I'm eager to share my approach to [specific challenge]."
- "Let's talk about how my experience can support your growth."

---

## Cover Letter Angles & Themes

### ANGLE 1: First Design Hire / 0-to-1
**When to Use**: Startup, early-stage, first design role on team

**Key Points**:
- Experience being sole designer (Fincast)
- Building design foundation from scratch
- Working with constraints
- Establishing design culture
- Wearing multiple hats

**Example Opening**:
```
"As the first design hire at Fincast, I know firsthand the unique 
challenges of establishing design in a fast-moving startup. When I 
read about [Company]'s mission to [X], I immediately recognized the 
opportunity to bring that 0-to-1 experience to your team."
```

---

### ANGLE 2: Team Scaling / Leadership
**When to Use**: Lead roles, growing teams, design management

**Key Points**:
- Scaled design team at Kushki (solo → X)
- Mentorship (Andreina example)
- Process establishment
- Design systems thinking
- Cross-functional leadership

**Example Opening**:
```
"Building and scaling design teams in high-growth environments is 
where I thrive. At Kushki, I grew the design function from [X to Y], 
establishing [processes/culture/systems] that enabled the team to 
support [outcome]. I see similar opportunities at [Company]."
```

---

### ANGLE 3: Complex B2B / Data-Heavy Products
**When to Use**: B2B SaaS, fintech, analytics, enterprise tools

**Key Points**:
- B2B SaaS experience (Kushki, Fincast)
- Data visualization and complex workflows
- Technical user empathy
- Information architecture
- Designing for efficiency and power users

**Example Opening**:
```
"Designing for B2B users requires a different mindset - one focused 
on efficiency, data density, and workflow optimization rather than 
consumer delight. My work at [Companies] designing [product types] 
has given me deep expertise in this domain, which I'm excited to 
bring to [Company]'s [product]."
```

---

### ANGLE 4: Design-Business Alignment
**When to Use**: Business-focused companies, growth-stage, metrics-driven

**Key Points**:
- Formula module redesign (reduced onboarding time)
- Business impact focus
- Data-informed decisions
- ROI of design
- Strategic thinking

**Example Opening**:
```
"Great design isn't just about craft - it's about business impact. 
At Fincast, my redesign of the formula module reduced onboarding 
time by [X], directly impacting customer retention. This approach 
to connecting design decisions to business outcomes is what I'd 
bring to [Company]."
```

---

### ANGLE 5: Strategic Ambiguity / Pivots
**When to Use**: Startups in transition, product pivots, uncertain roadmaps

**Key Points**:
- Fincast product pivot experience
- Comfort with ambiguity
- Strategic design thinking
- Adaptability
- Discovery and validation

**Example Opening**:
```
"I thrive in ambiguous environments where the path isn't clear. 
During Fincast's product pivot, I led design through [challenge], 
navigating uncertainty while keeping the team aligned on user needs. 
This experience positions me well for [Company]'s current stage."
```

---

### ANGLE 6: Remote-First / Distributed Teams
**When to Use**: Remote companies, distributed teams, async culture

**Key Points**:
- Remote work experience (Ecuador-based)
- Async collaboration
- Documentation and transparency
- Distributed team dynamics
- Self-direction

**Example Opening**:
```
"As a designer based in Ecuador working with global teams, I've 
developed strong async collaboration habits and documentation 
practices. Your remote-first culture at [Company] aligns perfectly 
with how I work best."
```

---

## Tone Calibration by Company Type

### YC Startup / Early Stage
- **Energy Level**: High
- **Length**: Shorter (250-350 words)
- **Focus**: Speed, ownership, building from scratch
- **Voice**: Direct, action-oriented
- **Keywords**: "build", "ship", "iterate", "impact", "growth"

**Example Excerpt**:
```
"I'm excited to help [Company] build [X]. As the first designer at 
Fincast, I shipped [outcome] in [timeframe] while establishing the 
design foundation. Let's talk about how I can do the same for you."
```

---

### Series A/B Scale-Up
- **Energy Level**: Balanced
- **Length**: Standard (350-450 words)
- **Focus**: Scaling, process, systems
- **Voice**: Professional but personable
- **Keywords**: "scale", "establish", "optimize", "team", "growth"

**Example Excerpt**:
```
"At this stage of growth, [Company] needs design leadership that can 
scale alongside the product. My experience at Kushki - where I 
[achievement] - has prepared me to tackle these exact challenges."
```

---

### Enterprise / Established
- **Energy Level**: Professional
- **Length**: Longer (450-550 words)
- **Focus**: Strategy, stakeholders, maturity
- **Voice**: Strategic, thoughtful
- **Keywords**: "strategic", "align", "stakeholder", "optimize", "mature"

**Example Excerpt**:
```
"Effective design at enterprise scale requires not just craft 
excellence, but strategic thinking and stakeholder alignment. 
Throughout my career at [Companies], I've developed..."
```

---

### Design-Forward Culture
- **Energy Level**: Thoughtful
- **Length**: Standard (350-450 words)
- **Focus**: Craft, process, quality
- **Voice**: Considered, detail-oriented
- **Keywords**: "craft", "intentional", "thoughtful", "excellence", "experience"

**Example Excerpt**:
```
"What draws me to [Company] is your commitment to design excellence. 
The attention to detail in [Product] demonstrates the kind of craft-
focused culture where I do my best work."
```

---

## Common Pitfalls to Avoid

### ❌ DON'T:
1. **Generic openings**: "I am writing to express my interest..."
2. **Resume repetition**: Don't just restate your CV
3. **Over-flattery**: "You're the best company ever..."
4. **Vague claims**: "I'm passionate about design" without proof
5. **Negativity**: Criticizing current/past employers
6. **Typos/errors**: Company name wrong, role title wrong
7. **Too long**: > 600 words (unless specifically requested)
8. **All about you**: Focus on their needs, not just your journey
9. **Overused phrases**: "Think outside the box", "hit the ground running"
10. **Desperation**: "I need this job", "Please consider me"

### ✅ DO:
1. **Specific opening**: Reference their product, news, challenge
2. **Connect dots**: Link your experience to their exact needs
3. **Show research**: Demonstrate you understand their business
4. **Quantify impact**: Include metrics and outcomes
5. **Be authentic**: Use your voice, not corporate speak
6. **Proofread**: Company name, role, contact info all correct
7. **Be concise**: Respect their time, every word counts
8. **Focus outward**: What you'll contribute, not just what you want
9. **Fresh language**: Avoid clichés, be direct
10. **Show enthusiasm**: Genuine excitement for the opportunity

---

## Quality Checklist

Before finalizing any cover letter:

- [ ] **Company name spelled correctly** (everywhere)
- [ ] **Role title matches exactly** from job posting
- [ ] **Specific references** to their product/company (not generic)
- [ ] **Quantified achievements** (at least 1-2 metrics)
- [ ] **Clear value proposition** (why you specifically)
- [ ] **Appropriate length** (target range met)
- [ ] **No typos or grammar errors**
- [ ] **Authentic voice** (sounds like you, not AI)
- [ ] **Strong opening** (grabs attention in first 2 sentences)
- [ ] **Clear CTA** (what happens next)
- [ ] **Proofread** (read aloud to catch awkward phrasing)
- [ ] **Matches application materials** (consistent with CV, portfolio)

---

## Multi-Language Support

### English (Default)
- Professional but conversational
- Direct and clear
- Active voice
- American English spelling (unless UK company)

### Spanish (Upon Request)
**Formal (Usted)**:
- Use for: Corporate, traditional companies
- Tone: Professional and respectful
- Structure: More formal opening/closing

**Informal (Tú)**:
- Use for: Startups, tech companies, creative agencies
- Tone: Professional but friendly
- Structure: Conversational

**When to Use Spanish**:
- LATAM-based companies with Spanish job posting
- Company culture indicates Spanish preference
- Explicitly requested

**Default Rule**: If job posting is in English → respond in English (even for LATAM companies)

---

## Database Commands

**View**:
- `"Show all cover letters"` - List all saved letters
- `"Show letters for [company]"` - Filter by company
- `"Show successful letters"` - Filter by outcome: interview/offer
- `"Show letters using [angle]"` - Filter by angle (e.g., "first-design-hire")

**Update**:
- `"Update outcome for [company] letter to [outcome]"` - Track results
- `"Add note to letter [id]: [note]"` - Capture learnings

**Analysis**:
- `"What's my cover letter success rate?"` - Interviews/applications
- `"Which angles led to interviews?"` - Pattern recognition
- `"Show evolution of my opening hooks"` - Track improvements

---

## Usage Instructions

### Basic Usage:
```
"Generate cover letter for:
Company: Remote.com
Role: Senior Product Designer
JD: [paste or summarize]
Angle: Leadership/team scaling
Length: Standard"
```

### With Context:
```
"Generate cover letter using company-research-brief for Remote.com.
Emphasize: remote-first culture alignment, B2B SaaS experience
De-emphasize: agency work
Length: Short (300 words)"
```

### Quick Version:
```
"Cover letter for [Company], [Role]. Emphasize [X], keep it short."
```

---

## Output Format

```
---
COMPANY: [Company Name]
ROLE: [Role Title]
LETTER ID: cl_XXX
DATE: [Date]
ANGLE: [Primary angle used]
WORD COUNT: XXX
KEY THEMES: [Auto-generated tags]

---

COVER LETTER:

[Full letter text, ready to copy/paste]

---

DATABASE STATUS: ✅ Saved as cl_XXX

NOTES:
- Angle: [Why this angle was chosen]
- Key differentiators: [What makes this letter stand out]
- Follow-up: [Suggested next steps after applying]

SIMILAR LETTERS:
- [If any exist, show reference]
---
```

---

## Advanced Features

### A/B Testing
Generate 2 versions with different angles:
```
"Generate 2 cover letters for [Company]:
Version A: First design hire angle
Version B: B2B complexity angle"
```

### Iteration
Refine based on feedback:
```
"Revise letter cl_015:
- Shorten to 300 words
- Emphasize fintech experience more
- Soften the opening"
```

### Template Extraction
Create reusable patterns:
```
"Extract template from successful letters (interview outcomes)"
→ Identify patterns in openings, structure, closing
```

---

## Notes
- Cover letters should complement CV, not duplicate it
- Always customize - never send generic template
- Research company thoroughly before writing (use company-research-brief)
- Track outcomes to learn what works
- When in doubt, be specific over generic
- Shorter is often better (respect their time)
- Proofread multiple times (typos = rejection)
