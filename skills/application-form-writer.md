# Application Form Writer

## Purpose
Generate optimized, authentic responses for job application forms that are specific to each company/role, consistent with your profile, and tracked for continuous improvement.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Core Experience**: B2B SaaS, fintech, data-heavy products, first design hire, team scaling
- **Key Companies**: Kushki (fintech, scaled design team), Fincast (B2B SaaS, sole designer), Koombea
- **Leadership Style**: Coaching, facilitative, evidence-based
- **Location**: Ecuador (remote work)
- **Languages**: Spanish (native), English (fluent)

## Input
- Application form questions (copy/paste or list)
- Company name and role title
- Character/word limits (if specified)
- Context from company-research-brief (optional but recommended)

## Output
- Ready-to-use responses for each question
- Adapted to company tone and culture
- Multiple length versions if needed (short/medium/long)
- Stored in response database for future reference

---

## RESPONSE DATABASE MANAGEMENT

### Database Structure
**File**: `/data/application-responses.json`

**Schema**:
```json
{
  "responses": [
    {
      "id": "resp_001",
      "date": "2025-04-24",
      "company": "Remote.com",
      "role": "Senior Product Designer",
      "question_type": "why-company",
      "question": "Why do you want to work here?",
      "response": "Full response text...",
      "char_limit": 500,
      "word_count": 95,
      "version": 1,
      "tags": ["why-company", "remote.com", "mission-driven", "b2b-saas"],
      "outcome": "applied",
      "notes": "Emphasized remote-first culture alignment"
    }
  ],
  "metadata": {
    "total_responses": 1,
    "last_updated": "2025-04-24",
    "companies_applied": ["Remote.com"]
  }
}
```

### Workflow Instructions for Claude Code

#### BEFORE generating new response:
1. **Search database** for similar questions (same question_type or company)
2. **Show previous responses** if found:
   ```
   "Found 2 previous responses to 'Why this company?' questions:
   - Remote.com (applied, no response yet)
   - Crustdata (interview secured) ✅
   
   Would you like to:
   A) Adapt existing response
   B) Create new response
   C) View previous responses for inspiration"
   ```
3. **Identify successful patterns** from responses marked with positive outcomes

#### AFTER generating new response:
1. **Save to database** with all metadata
2. **Auto-tag** based on question type and content
3. **Assign unique ID** (resp_XXX format)
4. **Confirm saved**: "Response saved as resp_015 for [Company]"

#### Response Outcome Tracking:
- `applied` - Default when response is generated
- `not-used` - Generated but not submitted
- `no-response` - Applied but no reply from company
- `rejected` - Application rejected
- `interview` - Moved to interview stage
- `offer` - Received offer

### Database Commands

**View Commands:**
- `"Show all responses"` - List all saved responses
- `"Show responses for [company]"` - Filter by company
- `"Show [question-type] responses"` - Filter by type (why-company, challenging-project, etc.)
- `"Show successful responses"` - Filter by outcome: interview or offer
- `"Show responses from last 30 days"` - Date range filter

**Update Commands:**
- `"Update outcome for [company] to [outcome]"` - Update status
- `"Add note to response [id]: [note]"` - Add context/learnings
- `"Mark response [id] as template"` - Flag best responses

**Analysis Commands:**
- `"What's my success rate?"` - Applications → interviews conversion
- `"Which responses led to interviews?"` - Identify patterns
- `"Show response evolution for 'why-company' questions"` - Track improvements

---

## Question Types & Response Frameworks

### 1. WHY THIS COMPANY?
**Question Type Tag**: `why-company`

**Framework**:
- **Hook**: Specific insight about their product/mission (shows you did research)
- **Connection**: Your experience that aligns with their needs
- **Vision**: What excites you about contributing to their future

**Example Structure**:
```
[Specific observation about their product/approach]
+ [How your background makes you uniquely valuable]
+ [What you're excited to build/contribute]
```

**Length Variants**:
- **Short (150-250 chars)**: Hook + Connection
- **Medium (250-500 chars)**: Hook + Connection + Vision
- **Long (500+ chars)**: Full framework + specific examples

---

### 2. WHY THIS ROLE?
**Question Type Tag**: `why-role`

**Framework**:
- **Stage alignment**: Why this role fits your career trajectory
- **Challenge match**: Specific aspects of the role that excite you
- **Value prop**: What you'll bring to the role

**Connect to**:
- Your experience level (10+ years, ready for senior/lead)
- Type of work you excel at (complex B2B, data-heavy, systems thinking)
- Environment you thrive in (startups, ambiguity, cross-functional)

---

### 3. CHALLENGING PROJECT (STAR Format)
**Question Type Tag**: `challenging-project`

**Framework**:
- **Situation**: Context (company, product, team size)
- **Task**: The challenge/goal
- **Action**: Your specific approach (3-4 key actions)
- **Result**: Impact (metrics, outcomes, learnings)

**Bank of Stories** (reference from your experience):
1. **Kushki - Scaling Design Team**: Solo → team of X, establishing processes
2. **Fincast - Product Pivot**: Navigating strategic ambiguity, first design hire
3. **Formula Module Redesign**: Reducing onboarding time, business impact
4. **Kushki - Mentoring Andreina**: People development, coaching approach

**Adaptation Rule**: Pick story that maps to company's stage/challenges
- Early stage → "First design hire" stories
- Scaling → "Building team/process" stories
- Enterprise → "Complex product" stories

---

### 4. DESIGN PROCESS
**Question Type Tag**: `design-process`

**Framework**:
- **Discovery**: How you understand problems (research, stakeholder input)
- **Exploration**: How you generate solutions (ideation, prototyping)
- **Validation**: How you test assumptions (user testing, metrics)
- **Iteration**: How you refine based on feedback
- **Collaboration**: How you work with eng/PM/stakeholders

**Adapt to**:
- Company maturity (scrappy vs. established)
- Product type (B2B vs. B2C, data-heavy vs. simple)
- Team structure (solo vs. collaborative)

---

### 5. COLLABORATION EXAMPLE
**Question Type Tag**: `collaboration`

**Framework**:
- **Context**: Cross-functional project setup
- **Challenge**: Alignment issue or constraint
- **Approach**: How you facilitated/influenced
- **Outcome**: Successful collaboration result

**Emphasize**:
- Your facilitative leadership style
- Evidence-based decision making
- Stakeholder management
- Design influence on business outcomes

---

### 6. TOOL/METHOD EXPERIENCE
**Question Type Tag**: `tool-experience`

**Format**:
```
- [Tool/Method]: [Years] of experience
- Context: [Where you used it]
- Proficiency: [Your level]
- Example: [Brief use case]
```

**Your Tool Stack** (reference):
- Figma (primary)
- Design systems
- User research methods
- Prototyping tools
- Collaboration tools (Miro, FigJam, etc.)

---

### 7. SALARY EXPECTATIONS
**Question Type Tag**: `salary`

**Your Range**: $3,200 - $5,000 USD
**Minimum**: $2,000 USD (dealbreaker below this)

**Response Options**:

**If they ask for specific number**:
```
"My target range is $3,200 - $5,000 USD depending on the full compensation package, equity, and growth opportunities. I'm open to discussing what makes sense based on the role scope and company stage."
```

**If they ask "negotiable?"**:
```
"Yes, I'm open to negotiation based on the complete package."
```

**If early stage/equity heavy**:
```
"I value equity and growth potential, so I'm flexible on cash compensation if there's meaningful equity and a clear path to impact."
```

---

### 8. WHY LEAVING CURRENT ROLE?
**Question Type Tag**: `why-leaving`

**Framework** (stay positive):
- **Growth**: Seeking new challenges/scale
- **Alignment**: Looking for better fit with [specific aspect]
- **Opportunity**: Excited about [type of company/product]

**Your Context**:
- Active job search (not currently employed full-time)
- Running agency (Poltergeist) while seeking full-time role
- Open about wanting stability + growth in product design

**Example**:
```
"I'm currently running a web design agency while actively seeking a full-time product design role where I can focus on complex B2B products and contribute to scaling design. I'm particularly drawn to [company type] because [specific reason]."
```

---

### 9. 5-YEAR VISION
**Question Type Tag**: `career-vision`

**Your Trajectory**:
- **Now**: Senior IC / Senior Lead hybrid
- **Next 2-3 years**: Design leadership (Lead/Principal), team building
- **5 years**: Head of Design or VP Design at growth-stage company

**Framework**:
```
"In the next few years, I see myself deepening my impact in [specific area - systems, strategy, leadership] while growing into formal design leadership. I'm excited about building and scaling design teams, establishing design culture, and connecting design to business outcomes - skills I've started developing at Kushki and want to expand."
```

**Adapt to**:
- IC-focused role: Emphasize craft mastery, systems thinking
- Lead role: Emphasize team building, strategy, influence
- Startup: Emphasize adaptability, ownership, broad impact

---

## Response Quality Checklist

Before saving any response, verify:

- [ ] **Specific**: Names actual companies, projects, or examples
- [ ] **Authentic**: Sounds like you, not AI-generated
- [ ] **Connected**: Links to THIS company's needs/context
- [ ] **Concrete**: Includes metrics, outcomes, or specifics
- [ ] **Appropriate Length**: Fits character/word limits
- [ ] **Structured**: Easy to scan (for longer responses)
- [ ] **Positive Tone**: Even when discussing challenges
- [ ] **Proofread**: No typos, grammar issues
- [ ] **Consistent**: Aligns with other application materials (CV, portfolio)

---

## Tone Adaptation Guidelines

### Startup/High-Growth (YC, Series A-B)
- **Tone**: Energetic, action-oriented, ownership mindset
- **Emphasize**: Speed, adaptability, building from scratch, first design hire experience
- **Language**: "Build", "ship", "iterate", "impact", "growth"

### Enterprise/Established (Series C+, Public)
- **Tone**: Professional, strategic, systems-oriented
- **Emphasize**: Process, scalability, stakeholder management, design maturity
- **Language**: "Scale", "optimize", "collaborate", "strategic", "alignment"

### Design-Forward Companies
- **Tone**: Craft-focused, thoughtful, detail-oriented
- **Emphasize**: Design systems, user research, design thinking, quality
- **Language**: "Craft", "experience", "delight", "intentional", "coherent"

### Engineering-Heavy Companies
- **Tone**: Analytical, metrics-driven, technical
- **Emphasize**: Data-informed design, technical collaboration, feasibility
- **Language**: "Data", "metrics", "technical constraints", "pragmatic", "validation"

---

## Multi-Language Support

### English (Default)
- Professional but conversational
- Clear and direct
- Active voice

### Spanish (Upon Request)
- Professional tone ("usted" for formal contexts, "tú" for startups)
- Adapt idioms appropriately
- Maintain authenticity

**Translation Note**: Some companies may prefer English even if they're LATAM-based. Check job posting language.

---

## Usage Instructions

### Basic Workflow:
1. **Provide**:
   - Company name + role
   - Application questions (copy/paste)
   - Character limits if any
   
2. **Receive**:
   - Tailored responses for each question
   - Database check for similar past responses
   - Confirmation of save to database

3. **Review & Edit**:
   - Personalize if needed
   - Adjust length
   - Mark as used/not-used

4. **Track Outcomes**:
   - Update status as application progresses
   - Build learning database

### Advanced Usage:
```
"I'm applying to [Company] for [Role]. Questions:
1. Why do you want to work here? (500 chars)
2. Tell us about a challenging project (1000 chars)
3. What's your design process?

Context: Series A, B2B SaaS, first design hire"
```

### Database Management:
```
"Show me all 'why-company' responses that led to interviews"
→ Analyze patterns
→ Adapt successful frameworks
```

---

## Output Format

For each question, provide:

```
---
QUESTION: [Original question]
CHAR LIMIT: [If specified]
RESPONSE ID: resp_XXX
TAGS: [Auto-generated tags]

RESPONSE:
[Response text, ready to copy/paste]

WORD COUNT: XX | CHAR COUNT: XXX

DATABASE STATUS: ✅ Saved

SIMILAR PAST RESPONSES:
- [If any exist, show brief reference]
---
```

## Notes
- Always save responses to database for continuous improvement
- Flag responses that lead to interviews for pattern analysis
- Adapt tone to company culture (research from company-research-brief)
- Keep responses honest - never fabricate experience
- When in doubt, err on side of specificity over generality
