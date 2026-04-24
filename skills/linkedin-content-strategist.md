# LinkedIn Content Strategist

## Purpose
Generate thought leadership content for LinkedIn that demonstrates your expertise, builds your professional brand, and attracts opportunities passively - without coming across as self-promotional or salesy.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Expertise Areas**: B2B SaaS design, complex data products, design systems, team scaling, first design hire experience
- **Thought Leadership Angles**: Design-business alignment, strategic design thinking, B2B UX patterns, design team building
- **Target Audience**: Hiring managers, design leaders, fellow designers, product people at B2B companies
- **Tone**: Professional but approachable, evidence-based, helpful not preachy

## Input
- Content theme or topic idea
- Target audience (recruiters, design leaders, peers, etc.)
- Post type (insight, story, how-to, hot take, case study)
- Length preference (short: 100-200 words, medium: 200-400 words, long: 400-600 words)
- Frequency goal (1x/week, 2x/week, etc.)

## Output
- Complete LinkedIn post ready to publish
- Variations if needed (different angles on same topic)
- Content calendar suggestions
- Saved to database for performance tracking

---

## LINKEDIN CONTENT DATABASE MANAGEMENT

### Database Structure
**File**: `/data/linkedin-content.json`

**Schema**:
```json
{
  "posts": [
    {
      "id": "lnk_001",
      "date_published": "2025-04-24",
      "theme": "b2b-ux-complexity",
      "post_type": "insight",
      "word_count": 287,
      "hook": "B2B designers don't design for delight...",
      "key_topics": ["b2b-saas", "user-efficiency", "power-users"],
      "engagement": {
        "views": 0,
        "likes": 0,
        "comments": 0,
        "shares": 0
      },
      "outcome": "pending",
      "learnings": []
    }
  ],
  "content_calendar": {
    "frequency": "1x-per-week",
    "themes_rotation": ["b2b-design", "design-leadership", "design-systems", "career-advice"],
    "next_planned": "2025-05-01"
  },
  "performance_insights": {
    "best_performing_themes": [],
    "best_performing_hooks": [],
    "optimal_post_length": null
  }
}
```

### Workflow Instructions for Claude Code

#### BEFORE creating content:
1. **Check content calendar** - what theme is next in rotation
2. **Review past performance** - what topics/formats resonated
3. **Avoid repetition** - don't write similar posts too close together
4. **Match to current job search stage** - adjust positioning

#### AFTER publishing:
1. **Save post to database** with metadata
2. **Track engagement** (manually update after 48-72 hours)
3. **Capture learnings** (what worked, what didn't)
4. **Update performance insights** to improve future content

#### Weekly Review:
1. **Analyze engagement patterns** - which themes perform best
2. **Refine content calendar** based on what works
3. **Generate next week's post ideas**

---

## LinkedIn Content Strategy

### GOALS (Priority Order)
1. **Demonstrate expertise** - Show you know B2B design deeply
2. **Build trust** - Share real experiences, not theories
3. **Stay visible** - Consistent presence in hiring managers' feeds
4. **Attract opportunities** - Make people think "we should talk to this person"
5. **Help others** - Provide genuine value, not just self-promotion

### NON-GOALS
- ❌ Going viral (not the point)
- ❌ Daily posting (quality over quantity)
- ❌ Being controversial for engagement
- ❌ Copying LinkedIn influencer templates
- ❌ Selling anything

---

## Post Types & When to Use

### TYPE 1: Insight Post
**What It Is**: Short observation or framework from your experience

**When to Use**: You have a clear point of view on a design topic

**Structure**:
```
Hook (surprising statement or question)
↓
Context (why this matters)
↓
Insight (your perspective)
↓
Implication (what to do with this)
```

**Example Topic Ideas**:
- "B2B users don't want beautiful - they want efficient"
- "The best design systems are boring"
- "First design hire? Here's what NOT to build first"
- "Why 'user delight' fails in B2B products"

**Length**: 150-300 words

---

### TYPE 2: Story Post
**What It Is**: Narrative from your experience with a lesson

**When to Use**: You have a compelling story that teaches something

**Structure**:
```
Situation (set the scene)
↓
Challenge (what went wrong or was hard)
↓
Resolution (what you learned/did)
↓
Takeaway (lesson for readers)
```

**Example Topic Ideas**:
- "The onboarding redesign that decreased conversion (and what I learned)"
- "How I scaled design impact from 1 squad to 3 without new headcount"
- "The design system pitch that finally got leadership buy-in"
- "Mentoring a junior designer from overwhelmed to promoted"

**Length**: 300-500 words

---

### TYPE 3: How-To / Framework Post
**What It Is**: Tactical advice or framework others can apply

**When to Use**: You have a repeatable process worth sharing

**Structure**:
```
Problem (what people struggle with)
↓
Framework/Steps (your approach)
↓
Example (how you've used it)
↓
Invitation (try it yourself)
```

**Example Topic Ideas**:
- "My 3-question framework for prioritizing design work"
- "How to build a business case for design resources"
- "5 questions I ask before any B2B redesign"
- "The STAR framework for design case studies (with template)"

**Length**: 250-400 words

---

### TYPE 4: Hot Take Post
**What It Is**: Contrarian or provocative perspective

**When to Use**: Sparingly, when you genuinely disagree with common wisdom

**Structure**:
```
Bold claim (contrarian)
↓
Why conventional wisdom is wrong
↓
Your alternative perspective
↓
Nuance (acknowledge other views)
```

**Example Topic Ideas**:
- "Stop hiring for 'culture fit' in design teams"
- "Your design process is probably too heavy for your company stage"
- "Design systems can kill innovation (here's when)"
- "Most 'design thinking' workshops are theater"

**Length**: 200-350 words

**⚠️ Warning**: Use sparingly, always add nuance, avoid pure negativity

---

### TYPE 5: Mini Case Study Post
**What It Is**: Condensed project story with metrics

**When to Use**: You want to showcase specific work

**Structure**:
```
Problem (business + user)
↓
Approach (your key decisions)
↓
Result (metrics)
↓
Learning (what you'd share)
```

**Example Topic Ideas**:
- "How we reduced onboarding from 3 weeks to 4 days"
- "Building Kushki's design team from 1 to X"
- "The formula module redesign: 87% time reduction"

**Length**: 200-400 words

**Include**: 1-2 images/screenshots if possible

---

### TYPE 6: Career Reflection Post
**What It Is**: Lessons from your career journey

**When to Use**: Monthly, to show your growth trajectory

**Structure**:
```
Then vs. Now (contrast)
↓
What changed (your learning)
↓
Advice (what you'd tell past self)
```

**Example Topic Ideas**:
- "What I wish I knew as a first design hire"
- "From solo designer to design team builder: 3 lessons"
- "The skill that matters most for senior designers (it's not Figma)"

**Length**: 250-400 words

---

## Content Themes (Rotation)

### THEME 1: B2B SaaS Design Expertise
**Your Authority**: 10+ years in B2B, fintech, complex products

**Topic Ideas**:
- Designing for efficiency over delight
- Complex workflow optimization
- Data-heavy interfaces
- Power user vs. new user balance
- B2B research approaches
- Enterprise UX patterns

**Why This Works**: Positions you for B2B roles, shows deep expertise

**Frequency**: 40% of content

---

### THEME 2: Design Leadership & Team Building
**Your Authority**: Mentoring, scaling teams, first design hire experience

**Topic Ideas**:
- Mentoring junior designers
- Building design culture
- Design team scaling
- First design hire priorities
- Cross-functional leadership
- Stakeholder management

**Why This Works**: Positions you for lead/senior roles, shows growth trajectory

**Frequency**: 30% of content

---

### THEME 3: Design Systems & Operations
**Your Authority**: Built design systems, scaled efficiency

**Topic Ideas**:
- When to build a design system
- Design system ROI
- Component thinking
- Design-eng collaboration
- Documentation that actually works
- Scaling design without headcount

**Why This Works**: Shows systems thinking, operational maturity

**Frequency**: 20% of content

---

### THEME 4: Career & Professional Growth
**Your Authority**: 10+ year career progression, job search experience

**Topic Ideas**:
- Portfolio advice
- Interview preparation
- Career transitions
- Navigating ambiguity
- Learning new domains
- Remote work as international designer

**Why This Works**: Helpful to community, shows thought leadership

**Frequency**: 10% of content

---

## Writing Guidelines

### THE HOOK (First 1-2 Lines)
**Purpose**: Stop the scroll, make them want to read more

**Good Hooks**:
- **Contrarian**: "B2B users don't want beautiful interfaces."
- **Surprising stat**: "87% time reduction. One redesign. Here's how."
- **Question**: "Why do design systems fail at most companies?"
- **Bold claim**: "Your design process is probably wrong for your company stage."
- **Story opening**: "I once shipped a redesign that decreased conversion by 15%."

**Bad Hooks**:
- Generic: "Design is important."
- Vague: "Here are some thoughts on UX."
- Humble-brag: "I'm humbled to share..."
- Clickbait: "You won't believe what happened next..."

**Test**: Would you keep reading if this was in your feed?

---

### THE BODY (Middle Section)
**Purpose**: Deliver on the hook's promise

**Best Practices**:
- **Short paragraphs** (1-3 sentences max)
- **White space** (use line breaks generously)
- **Concrete examples** (names, numbers, specifics)
- **Avoid jargon** (unless your audience uses it)
- **One idea per post** (don't try to teach everything)

**Example - Good**:
```
At Fincast, we had a problem.

Users spent 3 weeks learning our formula builder. 40% never finished setup.

We assumed they needed simpler features. We were wrong.

Through interviews, we discovered they didn't want simple - they wanted predictable. Real-time feedback, not trial-and-error.

One redesign later: 4-day onboarding. 11-point conversion increase.

The lesson: Sometimes complexity isn't the problem. Uncertainty is.
```

**Example - Bad**:
```
In my experience working on various products across different companies, I've 
observed that users often struggle with complex features, which can lead to 
frustration and abandonment. It's important to conduct user research to understand 
their needs and iterate on solutions that balance simplicity with power.
```

**Why Bad Example Fails**: Vague, wordy, no specifics, sounds like everyone else

---

### THE CLOSE (Last 1-2 Lines)
**Purpose**: Leave them with something memorable, invite engagement

**Good Closes**:
- **Takeaway**: "The best design systems are boring. And that's the point."
- **Question**: "What's your experience with [topic]?"
- **Invitation**: "Try this framework next time you're prioritizing design work."
- **Reflection**: "10 years ago, I thought craft was everything. Now I know influence matters more."

**Bad Closes**:
- Call to action: "Follow me for more tips!" (desperate)
- Self-promotion: "Hire me!" (pushy)
- Generic: "What do you think?" (lazy)
- Hashtag spam: "#design #ux #product #ui" (spammy)

---

### FORMATTING RULES

**Do**:
- ✅ Line breaks between paragraphs
- ✅ Bold for emphasis (sparingly)
- ✅ Bullet points for lists (but not every post)
- ✅ Emojis (1-2 max, only if natural)
- ✅ Tag relevant people/companies (when appropriate)

**Don't**:
- ❌ ALL CAPS (except acronyms)
- ❌ Wall of text (no breaks)
- ❌ Excessive emojis
- ❌ Clickbait formatting ("This changed everything ⬇️")
- ❌ Hashtag stuffing (3-5 relevant max)

---

## Your Voice & Tone

### VOICE CHARACTERISTICS
- **Confident but humble**: Share expertise without arrogance
- **Specific**: Use names, numbers, examples
- **Honest**: Admit failures and learnings
- **Helpful**: Focus on teaching, not showing off
- **Professional**: Approachable, not casual
- **Direct**: Get to the point quickly

### TONE CALIBRATION

**For B2B Design Topics**: Analytical, evidence-based
```
"B2B users prioritize efficiency over aesthetics. At Kushki, we tested a 
'beautiful' dashboard vs. a 'dense' one. Power users chose dense 3:1. 
They wanted information, not white space."
```

**For Leadership Topics**: Reflective, coaching
```
"The hardest part of mentoring isn't teaching design - it's teaching confidence. 
Andreina had the skills. She needed permission to trust her judgment."
```

**For Career Topics**: Encouraging, practical
```
"Your portfolio doesn't need 10 case studies. It needs 2-3 that show how you 
think, not just what you shipped."
```

**For System/Ops Topics**: Systems-thinking, pragmatic
```
"Design systems fail when they're built for ideal state, not current reality. 
Start with the 5 components you use most. Perfect comes later."
```

---

## Content Calendar Strategy

### POSTING FREQUENCY
**Recommended**: 1 post per week (consistency over quantity)

**Rationale**:
- Sustainable long-term
- Enough to stay visible
- Time to make each post good
- Doesn't feel spammy

**Alternative**: 2 posts per week if in active job search mode

---

### 4-WEEK ROTATION EXAMPLE

**Week 1: B2B Insight**
- Theme: B2B SaaS design
- Type: Insight post
- Example: "Why B2B users want density, not delight"

**Week 2: Leadership Story**
- Theme: Team building
- Type: Story post
- Example: "How I mentored a junior designer to promotion"

**Week 3: How-To Framework**
- Theme: Design operations
- Type: How-to post
- Example: "My 3-question framework for design prioritization"

**Week 4: Career Reflection**
- Theme: Professional growth
- Type: Career post
- Example: "What I'd tell myself as a first design hire"

**Repeat with variations**

---

### CONTENT BANK (Pre-Plan Topics)

**B2B Design (10 ideas)**:
1. Efficiency over delight in B2B
2. Designing for power users
3. Data-heavy interface patterns
4. Workflow complexity management
5. B2B research on a budget
6. Enterprise vs. SMB design differences
7. Balancing feature requests vs. simplicity
8. Technical user empathy
9. When to add vs. remove features
10. B2B onboarding approaches

**Leadership (10 ideas)**:
1. Mentoring junior to mid-level
2. Scaling design without headcount
3. Building design critique culture
4. Cross-functional influence
5. First design hire priorities
6. Design system advocacy
7. Handling design feedback
8. Stakeholder management
9. When to say no to requests
10. Design team rituals that work

**Design Systems (8 ideas)**:
1. When NOT to build a design system
2. Design system ROI calculation
3. Component vs. pattern libraries
4. Design-eng collaboration on systems
5. Documentation that gets used
6. Scaling design systems
7. Design tokens strategy
8. Governance without bureaucracy

**Career (8 ideas)**:
1. Portfolio case study tips
2. Interview preparation strategies
3. Negotiating as a designer
4. Career transitions (IC to lead)
5. Learning new domains quickly
6. Remote work effectiveness
7. Personal brand building
8. Networking authentically

---

## Engagement Strategy

### RESPOND TO COMMENTS
**Within 24 hours**: Respond to every comment on your posts

**How to Respond**:
- Thank them for engaging
- Add to the conversation (don't just say "thanks")
- Ask follow-up questions
- Be generous with insights

**Example**:
```
Comment: "This resonates! We struggled with the same onboarding issue."
Your Response: "Thanks for sharing! Curious - did you find users wanted 
simpler features or just more feedback along the way? That insight shifted 
everything for us."
```

---

### ENGAGE WITH OTHERS' CONTENT
**Goal**: Be visible, build relationships, not just broadcast

**Strategy**:
- Comment on 3-5 posts per week from your network
- Focus on: design leaders, hiring managers at target companies, fellow designers
- Add value in comments (insights, not just "great post!")

**Good Comment Example**:
```
"This mirrors what we saw at Kushki - the design system didn't take off 
until we tied it to engineering velocity metrics. Once we showed it reduced 
handoff time by 60%, leadership bought in immediately."
```

**Bad Comment Example**:
```
"Great post! 👍"
```

---

## What NOT to Post

### ❌ AVOID THESE TOPICS
1. **Politics** (unless design-related policy)
2. **Complaints** (about employers, clients, industry)
3. **Desperation** ("Please hire me", "Looking for any role")
4. **Humble-brags** ("So honored to be asked to speak at...")
5. **Generic advice** ("Communication is important in design")
6. **Pure self-promotion** ("Check out my new portfolio!")
7. **Unfinished thoughts** ("Some interesting ideas about design...")
8. **Engagement bait** ("Tag someone who needs to hear this")

---

### ❌ AVOID THESE PATTERNS
1. **Daily posting** (quality suffers, looks desperate)
2. **Copying templates** (sounds generic)
3. **Controversy for engagement** (polarizes, doesn't help job search)
4. **Oversharing** (personal problems, company drama)
5. **Asking for likes/shares** (desperate)
6. **Hashtag spam** (15 hashtags looks unprofessional)

---

## Example Posts (Full Templates)

### EXAMPLE 1: B2B Insight Post

```
B2B users don't want beautiful interfaces.

They want fast ones.

At Kushki, we tested two dashboard designs:

Version A: Clean, minimal, lots of white space
Version B: Dense, data-heavy, less "beautiful"

Power users chose Version B 3-to-1.

Why?

Because they're not browsing - they're working. Every click to "reveal more" 
is friction. Every animation is a delay.

In B2B design, efficiency beats aesthetics.

The best B2B interfaces feel like power tools, not art galleries.

Dense doesn't mean ugly. It means respecting that your users' time is money.

#ProductDesign #B2BSaaS #UXDesign
```

**Why This Works**:
- Contrarian hook
- Concrete example with data
- Clear point of view
- Actionable insight
- Professional tone

---

### EXAMPLE 2: Leadership Story Post

```
I once told a junior designer her presentation wasn't good enough.

She spent 30 slides explaining which design tools she used, which iterations 
she made, which meetings she attended.

Zero mention of business impact. Zero user outcomes.

Instead of saying "this needs work," I asked one question:

"If leadership remembers one thing from this presentation, what should it be?"

She said: "The design quality."

I followed up: "What do you think they actually care about?"

Long pause.

Then: "Whether it worked."

We rebuilt the entire presentation. Led with the metric: 40% reduction in 
support tickets. Showed user feedback. Design process became supporting evidence, 
not the story.

The presentation landed. She got promoted six months later.

The lesson I learned:

The best feedback helps people discover the gap themselves, rather than pointing 
it out directly.

Teaching frameworks > Giving answers.

#DesignLeadership #Mentorship #ProductDesign
```

**Why This Works**:
- Story arc (situation → challenge → resolution)
- Specific details (30 slides, 40% metric)
- Vulnerability (admitted approach)
- Clear takeaway
- Shows coaching style

---

### EXAMPLE 3: How-To Framework Post

```
"How do you prioritize design work when everything is urgent?"

I use a 3-question framework:

Question 1: Impact on core metric
"Does this move our North Star metric?"

At Fincast: Onboarding time was our metric. Formula redesign got priority 
over dashboard polish.

Question 2: Enablement vs. execution
"Does this multiply our effectiveness or just add features?"

At Kushki: Design system got priority over new features. It 3x'd our velocity.

Question 3: Reversibility
"How hard is it to undo this decision?"

Low-reversibility decisions (platform changes, system architecture) get more 
research time. High-reversibility decisions (button colors, copy) ship fast 
and iterate.

When stakeholders say "everything is urgent," this framework makes trade-offs 
visible:

"We can do X (high impact, low reversibility) or Y (low impact, high reversibility). 
Which matters more this quarter?"

Prioritization isn't about doing everything - it's about doing the right things.

Try this framework next time you're overwhelmed.

#ProductDesign #Prioritization #DesignLeadership
```

**Why This Works**:
- Answers a common pain point
- Clear framework (3 questions)
- Real examples from your experience
- Actionable (reader can try it)
- Ends with invitation

---

### EXAMPLE 4: Career Reflection Post

```
What I'd tell myself as a first design hire:

Don't build the design system first.

I know. Everyone says design systems scale design. They're right.

But when you're the first designer, nobody trusts design yet.

At Fincast, I spent my first month building components. Beautiful, 
documented, perfect.

Meanwhile, engineers shipped features without me. Product made roadmap 
decisions without design input.

I was building infrastructure for a team that didn't exist yet.

What I should have done:

Ship one high-impact feature that moves a business metric.
Then use that credibility to build the system.

Design systems are important. But credibility comes first.

First design hire? Focus on:
- One quick win that shows business impact
- Building relationships with eng and product
- Making yourself essential before making yourself efficient

The system can wait 3 months. Your credibility can't.

#DesignCareer #FirstDesignHire #ProductDesign
```

**Why This Works**:
- Vulnerable (admits mistake)
- Contrarian (challenges common advice)
- Specific story
- Actionable advice
- Relevant to hiring managers (shows you understand business)

---

## Hashtag Strategy

### HASHTAG RULES
- **Use 3-5 relevant hashtags** (not 15)
- **Mix sizes**: 1-2 large, 2-3 niche
- **Place at end** of post, not throughout
- **Relevant only** (don't spam)

### YOUR HASHTAG BANK

**Large (100k+ followers)**:
- #ProductDesign
- #UXDesign
- #DesignThinking

**Medium (10k-100k)**:
- #B2BSaaS
- #DesignLeadership
- #DesignSystems

**Niche (1k-10k)**:
- #B2BDesign
- #ProductDesigner
- #DesignOps

**Location** (if relevant):
- #RemoteDesign
- #LatamDesign

### HASHTAG SELECTION BY POST TYPE

**B2B Design Posts**: #ProductDesign #B2BSaaS #UXDesign
**Leadership Posts**: #DesignLeadership #ProductDesign #Mentorship
**Systems Posts**: #DesignSystems #DesignOps #ProductDesign
**Career Posts**: #DesignCareer #ProductDesign #UXDesign

---

## Database Commands

**View**:
- `"Show all LinkedIn posts"` - List all created content
- `"Show posts by theme: [theme]"` - Filter by topic
- `"Show best performing posts"` - Sorted by engagement

**Create**:
- `"Generate LinkedIn post: [topic/theme]"` - Create new post
- `"Create content calendar for next 4 weeks"` - Plan ahead
- `"Generate 3 variations of [topic]"` - A/B test ideas

**Update**:
- `"Update post [id] engagement: [stats]"` - Track performance
- `"Add learning to post [id]: [insight]"` - Capture what worked

**Analysis**:
- `"What themes perform best?"` - Optimize content strategy
- `"What post length gets most engagement?"` - Refine format
- `"Show content gaps"` - What topics haven't been covered

---

## Usage Instructions

### Basic Usage:
```
"Generate LinkedIn post:
Theme: B2B design complexity
Type: Insight post
Length: Medium (200-300 words)
Angle: Efficiency over delight"
```

### With Context:
```
"Create LinkedIn post about my Fincast formula module project.
Format: Mini case study
Focus: Business impact (onboarding time reduction)
Keep it: 250 words"
```

### Content Calendar:
```
"Generate 4-week LinkedIn content calendar.
Mix: 2 B2B posts, 1 leadership, 1 career
Job search stage: Active (need visibility)"
```

---

## Output Format

```
---
LINKEDIN POST
ID: lnk_XXX
Theme: [Theme]
Post Type: [Type]
Word Count: XXX
Date Created: [Date]

---

[FULL POST TEXT - ready to copy/paste to LinkedIn]

---

HASHTAGS: #Hashtag1 #Hashtag2 #Hashtag3

POSTING GUIDANCE:
- Best time: [Weekday] morning (9-11am)
- Tag: [Relevant people/companies if any]
- Image: [Yes/No - what kind if yes]

ENGAGEMENT STRATEGY:
- Respond to comments within 24h
- Expected engagement: [Low/Medium/High based on theme]
- Follow-up opportunity: [Related topic for next post]

DATABASE STATUS: ✅ Saved as lnk_XXX

PERFORMANCE TRACKING:
Update engagement after 48-72 hours:
- Views: 
- Likes: 
- Comments: 
- Shares: 
---
```

---

## Quality Checklist

Before posting any LinkedIn content:

- [ ] **Hook grabs attention** (first 2 lines stop the scroll)
- [ ] **Specific examples** (names, numbers, real situations)
- [ ] **One clear idea** (not trying to say everything)
- [ ] **Short paragraphs** (1-3 sentences, white space)
- [ ] **Authentic voice** (sounds like you, not a template)
- [ ] **Actionable insight** (reader learns something useful)
- [ ] **Professional tone** (approachable but not casual)
- [ ] **No humble-brags** (sharing expertise, not showing off)
- [ ] **No desperation** (confident, not job-seeking explicitly)
- [ ] **Proofread** (no typos, reads smoothly)
- [ ] **Hashtags relevant** (3-5 max, on-topic)
- [ ] **Strong close** (memorable takeaway or invitation)

---

## Notes
- Consistency matters more than frequency
- Help others, don't just promote yourself
- Engagement is a long game (months, not weeks)
- Track what works, double down on those themes
- Your best posts will feel vulnerable - that's good
- Think "teaching" not "broadcasting"
- Quality over quantity - one great post beats seven mediocre ones
- The goal is to be remembered when roles open, not go viral
