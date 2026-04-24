# Personal Brand Amplifier

## Purpose
Identify strategic opportunities to make your expertise visible beyond LinkedIn - through articles, talks, case studies, community contributions, and other channels that position you as a thought leader and attract opportunities passively.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Expertise**: B2B SaaS, complex products, design systems, team building, first design hire
- **Unique Positioning**: Ecuador-based designer with US/global company experience, Spanish/English bilingual
- **Target Visibility**: Design leaders, hiring managers at B2B companies, design community
- **Time Investment**: Sustainable (not full-time content creation)

## Input
- Current visibility level (low, medium, high)
- Time available per month (5 hours, 10 hours, 20 hours)
- Comfort level with public speaking (low, medium, high)
- Career goals (IC senior, Lead, Principal)
- Geographic/industry focus (remote global, LATAM, fintech, etc.)

## Output
- Prioritized visibility opportunities
- Content/talk topic ideas tailored to your expertise
- Step-by-step execution plan
- Templates and frameworks
- Saved to database for tracking

---

## BRAND AMPLIFICATION DATABASE MANAGEMENT

### Database Structure
**File**: `/data/brand-amplification.json`

**Schema**:
```json
{
  "initiatives": [
    {
      "id": "ba_001",
      "type": "article",
      "platform": "medium",
      "title": "Why B2B Users Want Density, Not Delight",
      "status": "published",
      "date_published": "2025-04-24",
      "reach": {
        "views": 0,
        "engagement": 0
      },
      "opportunities_generated": [],
      "time_invested": "4 hours",
      "roi": "pending"
    }
  ],
  "visibility_channels": {
    "active": ["linkedin", "medium"],
    "planned": ["conference-speaking", "podcast-guest"],
    "paused": []
  },
  "brand_metrics": {
    "linkedin_followers": 0,
    "article_views_total": 0,
    "speaking_engagements": 0,
    "inbound_opportunities": 0
  }
}
```

### Workflow Instructions for Claude Code

#### BEFORE starting initiative:
1. **Assess time available** - be realistic
2. **Check existing content** - can you repurpose LinkedIn posts?
3. **Evaluate ROI** - which channel reaches your target audience?
4. **Plan execution** - break into manageable steps

#### DURING initiative:
1. **Track time invested** - understand actual cost
2. **Document learnings** - what's working, what's not
3. **Leverage cross-platform** - one article → LinkedIn post → talk outline

#### AFTER completion:
1. **Measure reach** - views, engagement, opportunities
2. **Calculate ROI** - was it worth the time?
3. **Decide next steps** - double down or try something else

---

## Visibility Channels (Prioritized by ROI)

### TIER 1: HIGH ROI, LOW TIME (Start Here)

#### 1. LinkedIn Consistency
**Time**: 2-3 hours/week
**ROI**: High (direct reach to hiring managers)
**Status**: Already covered in linkedin-content-strategist.md
**Action**: Continue 1 post/week

---

#### 2. Long-Form Articles (Medium, Substack, Dev.to)
**Time**: 4-6 hours per article, 1 article/month
**ROI**: High (evergreen, shows depth, SEO)

**Platforms**:
- **Medium**: Largest design audience
- **Substack**: Own your audience (email list)
- **Dev.to**: Tech-focused audience
- **Your own blog**: Full control (but needs traffic strategy)

**Article Topics from Your Expertise**:
1. "The First Design Hire Playbook: What to Build (and Skip) in Your First 90 Days"
2. "Why B2B SaaS Design Requires Different Thinking Than Consumer Products"
3. "How I Scaled Design Impact 3x Without Adding Headcount"
4. "Building a Design System Business Case That Actually Gets Approved"
5. "The STAR Framework for Design Case Studies (with Template)"

**Article Structure** (2,000-3,000 words):
```
- Hook paragraph (problem/insight)
- Your credibility (why you're qualified to write this)
- Framework/approach (the meat)
- Real examples from your experience
- Actionable takeaways
- Invitation to connect
```

**Execution Plan**:
```
Week 1: Outline + research (1-2h)
Week 2: First draft (2-3h)
Week 3: Edit + visuals (1-2h)
Week 4: Publish + promote on LinkedIn (30min)
```

**Leverage**:
- Turn article into 3-4 LinkedIn posts
- Repurpose sections for talks
- Update portfolio with "Published Writer" section

---

#### 3. Design Community Engagement
**Time**: 1-2 hours/week
**ROI**: Medium-High (relationship building, visibility)

**Platforms**:
- **Designer Hangout** (Slack): Active design community
- **ADPList**: Mentoring platform (give sessions, build reputation)
- **Design Buddies**: Community for designers
- **Reddit** (r/userexperience, r/designcareers): Thoughtful answers to questions

**How to Engage**:
- Answer 2-3 questions/week with detailed, helpful responses
- Share your articles/insights
- Offer mentoring sessions (1-2 per month)
- Participate in discussions (not lurking)

**What to Share**:
- Your frameworks (STAR, prioritization, etc.)
- Real experiences (Fincast pivot, Kushki scaling)
- Career advice (first design hire, remote work)

**ROI Signal**: When people start DMing you for advice

---

### TIER 2: MEDIUM ROI, MEDIUM TIME (Once Tier 1 is Consistent)

#### 4. Conference/Meetup Speaking
**Time**: 10-20 hours per talk (prep + practice)
**ROI**: Medium (credibility boost, network expansion)

**Speaking Opportunities**:
- **Local Meetups**: Lower stakes, good practice (Quito design meetups)
- **Virtual Conferences**: Wider reach, no travel (Design Matters, Awwwards)
- **Company Webinars**: Easier to get accepted (host company lunch-and-learns)
- **Podcast Guest**: Medium time, high reach (Design Better, Lenny's Podcast for product/design)

**Talk Topics from Your Experience**:
1. "From Solo to Team: Scaling Design Without Losing Quality"
2. "B2B Design Patterns That Actually Work"
3. "Building Your First Design System: A Business Case Approach"
4. "Career Growth for Remote Designers in Emerging Markets"
5. "The First Design Hire Survival Guide"

**Talk Structure** (20-30 min):
```
- Hook: Surprising insight or problem (2 min)
- Your Story: Context and credibility (3 min)
- Framework: Your approach (10-12 min)
- Real Example: Case study from your work (5-7 min)
- Takeaways: 3-5 actionable points (3 min)
- Q&A (10 min)
```

**How to Get Speaking Gigs**:
1. Start local (Quito meetups, Ecuador tech groups)
2. Submit to CFPs (Call for Proposals) - Config, Awwwards, local events
3. Leverage your network (ask connections to introduce you)
4. Offer lunch-and-learns at companies (lower barrier)
5. Guest on podcasts (easier entry than conference stage)

**Leverage**:
- Record talk → YouTube video
- Slides → SlideShare → LinkedIn post
- Transcript → Medium article
- Add to portfolio: "Speaker" section

---

#### 5. Portfolio Case Studies (Public)
**Time**: 8-12 hours per case study
**ROI**: Medium (showcases work, but passive discovery)

**Where to Publish**:
- **Behance**: Design community, good for discovery
- **Medium**: Long-form storytelling
- **Your portfolio site**: Own the traffic
- **Case Study Club**: Curated case studies

**Case Studies to Write**:
1. "Reducing Onboarding Time by 87%: The Fincast Formula Redesign"
2. "Scaling Design at Kushki: From 1 to X Without Losing Quality"
3. "Building a Design System That Actually Gets Used"

**Structure** (already covered in portfolio-case-study-builder.md):
- Use SCIAR framework
- Focus on business outcomes
- Include metrics
- Show process

**Leverage**:
- Link from LinkedIn
- Submit to design galleries (Awwwards, CSS Design Awards)
- Share in design communities
- Use in job applications

---

#### 6. YouTube/Video Content
**Time**: High (5-10 hours per video)
**ROI**: Medium (slow build, but evergreen)

**Video Ideas**:
1. "Portfolio Teardown: What Hiring Managers Actually Look For"
2. "Live Design Critique: B2B Dashboard Redesign"
3. "First Design Hire Mistakes (And How to Avoid Them)"
4. "My Design Process: From Research to Handoff"

**Format Options**:
- **Loom walkthroughs**: Low production, high value
- **Screen recordings**: Design process, tool tips
- **Talking head**: Career advice, frameworks
- **Hybrid**: Mix of slides + screen share

**Start Small**:
- 1 video every 2 months (not weekly)
- Repurpose existing content (turn article into video)
- Share on LinkedIn for distribution

---

### TIER 3: LOW ROI, HIGH TIME (Skip Unless Passionate)

#### 7. Design Newsletter
**Time**: Very High (4-8 hours/week)
**ROI**: Low initially (slow subscriber growth)
**Recommendation**: Skip unless you LOVE writing weekly

#### 8. Twitter/X Engagement
**Time**: Medium-High (daily engagement)
**ROI**: Low for job search (unless you go viral)
**Recommendation**: Skip, focus on LinkedIn instead

#### 9. Instagram/TikTok Design Content
**Time**: High (video editing)
**ROI**: Low for senior B2B roles
**Recommendation**: Skip, not your audience

---

## Strategic Positioning Angles

### ANGLE 1: "The First Design Hire Expert"
**Your Authority**: Been there at Fincast, mentored others into this role

**Content Ideas**:
- "First Design Hire Mistakes (I Made Them So You Don't Have To)"
- "What to Build First as a Solo Designer"
- "How to Build Design Credibility at a Startup"
- "Establishing Design Culture When You're the Only Designer"

**Why This Works**: Niche expertise, clear audience (hiring managers + designers)

**Channels**: Articles, talks, mentoring on ADPList

---

### ANGLE 2: "B2B SaaS Design Specialist"
**Your Authority**: 10+ years in B2B, fintech, complex products

**Content Ideas**:
- "Why B2B Design is Different (And Harder)"
- "Designing for Power Users vs. Beginners"
- "B2B UX Patterns That Scale"
- "Data-Heavy Interface Design Principles"

**Why This Works**: Underserved niche, high-value companies

**Channels**: Articles, conference talks, design community answers

---

### ANGLE 3: "Design Team Builder"
**Your Authority**: Scaled Kushki design team, mentored designers

**Content Ideas**:
- "Scaling Design: From 1 to Team of X"
- "Building Design Critique Culture"
- "Mentoring Junior Designers Effectively"
- "Design Hiring for Startups"

**Why This Works**: Relevant for Lead/Head roles you're targeting

**Channels**: Talks, LinkedIn, mentoring

---

### ANGLE 4: "Remote Design Leader from Emerging Markets"
**Your Authority**: Ecuador-based, worked with US/global companies

**Content Ideas**:
- "Thriving as a Remote Designer in LATAM"
- "Building a Design Career from Ecuador"
- "Async Collaboration for Distributed Teams"
- "Global Companies, Local Designers: Making It Work"

**Why This Works**: Unique perspective, growing audience

**Channels**: Talks (LATAM conferences), articles, community

---

## Content Repurposing Matrix

### ONE ARTICLE → MULTIPLE ASSETS

**Example: "The First Design Hire Playbook" Article**

**From 1 Article, Create**:
1. **LinkedIn Post Series** (4 posts)
   - Post 1: Hook + Problem
   - Post 2: Framework overview
   - Post 3: Biggest mistake
   - Post 4: Takeaway + link to article

2. **Conference Talk** (30 min)
   - Use article as outline
   - Add slides with visuals
   - Include case study from article

3. **Twitter/X Thread** (10 tweets)
   - Break down key points
   - One insight per tweet

4. **Newsletter** (if you start one)
   - Repurpose with fresh intro

5. **Podcast Talking Points**
   - Use as interview prep
   - Discuss on design podcasts

6. **Portfolio Addition**
   - "Published Writing" section
   - Link to article

**Time Breakdown**:
- Write article: 6 hours
- Repurpose to all formats: 2-3 hours
- **Total**: 8-9 hours for 6+ assets

---

## Execution Roadmap

### MONTH 1-2: Foundation
**Goal**: Establish consistent LinkedIn presence

**Actions**:
- ✅ Already doing: 1 LinkedIn post/week (linkedin-content-strategist.md)
- Set up Medium account
- Join 2-3 design communities (Designer Hangout, ADPList)
- Outline 3 article ideas

**Time**: 3-4 hours/week

---

### MONTH 3-4: First Expansion
**Goal**: Publish first long-form article

**Actions**:
- Write and publish 1 Medium article (choose from topics above)
- Repurpose into LinkedIn series
- Answer 5-10 questions in design communities
- Offer 2 mentoring sessions on ADPList

**Time**: 6-8 hours/week (article month)

---

### MONTH 5-6: Speaking Preparation
**Goal**: Get first speaking opportunity

**Actions**:
- Submit to 3-5 conference CFPs or local meetups
- Create talk outline based on published article
- Practice talk (record yourself)
- Publish second article

**Time**: 8-10 hours/week (talk prep)

---

### MONTH 7-12: Consistency & Optimization
**Goal**: Maintain cadence, track ROI

**Actions**:
- 1 article every 6-8 weeks
- 1 LinkedIn post/week (ongoing)
- 1 talk per quarter (if booked)
- Active in 2-3 communities
- Track inbound opportunities

**Time**: 4-6 hours/week average

---

## Templates & Frameworks

### ARTICLE PITCH TEMPLATE (for publications)

```
Subject: Article Pitch: [Title]

Hi [Editor Name],

I'm Cristhian, a Senior Product Designer with 10+ years designing B2B SaaS 
products at companies like Kushki (fintech) and Fincast.

I'd like to pitch an article for [Publication]:

**Title**: [Your Title]

**Angle**: [What makes this unique/valuable]

**Outline**:
1. [Section 1]
2. [Section 2]
3. [Section 3]

**Why I'm qualified**: [Your relevant experience]

**Why this matters to your readers**: [Audience benefit]

The article would be approximately [word count] words and include [X] 
original examples from my work.

Available to write and submit within [timeline].

Looking forward to your thoughts!

Best,
Cristhian
[LinkedIn URL]
[Portfolio URL]
```

---

### CONFERENCE CFP (Call for Proposals) TEMPLATE

```
**Talk Title**: [Compelling, specific title]

**Format**: [Talk length - 20min, 45min, workshop]

**Abstract** (100-150 words):
[Hook - What problem does this solve?]
[Approach - Your unique framework/perspective]
[Takeaway - What attendees will learn]
[Credibility - Why you're qualified]

**Outline**:
1. [Section 1 - Time]
2. [Section 2 - Time]
3. [Section 3 - Time]

**Target Audience**: [Who should attend]

**Key Takeaways**:
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

**Speaker Bio** (50 words):
Cristhian is a Senior Product Designer with 10+ years designing B2B SaaS 
products. He's scaled design teams at Kushki, led product design at Fincast, 
and mentored designers from junior to mid-level. Based in Ecuador, he works 
with global remote teams.

**Previous Speaking Experience**: [If any, or "First-time speaker"]

**Sample Materials**: [Link to article, portfolio, LinkedIn]
```

---

### PODCAST PITCH TEMPLATE

```
Subject: Guest Idea for [Podcast Name]

Hi [Host Name],

I've been listening to [Podcast Name] for [time period] and loved your 
recent episode on [specific episode]. [Specific compliment or insight].

I'd love to be a guest to discuss [topic].

**Potential Topics**:
1. [Topic 1]: [One-line description]
2. [Topic 2]: [One-line description]
3. [Topic 3]: [One-line description]

**My Background**:
I'm a Senior Product Designer who's [unique experience - first design hire, 
team scaling, B2B specialist, etc.]. I've worked at [companies] and have 
[specific credibility points].

**Why this would resonate with your audience**:
[Connection to podcast's themes and listener interests]

**Sample Content**:
[Link to article, LinkedIn post, or video showing your speaking/writing]

Happy to work around your schedule. Let me know if this could be a fit!

Best,
Cristhian
[Contact info]
```

---

## Measuring Success

### METRICS TO TRACK

**Visibility Metrics**:
- LinkedIn followers growth
- Article views (Medium stats)
- Speaking engagements booked
- Community reputation (upvotes, mentions)

**Opportunity Metrics** (What Actually Matters):
- Inbound messages from hiring managers
- Interview requests
- Consulting/freelance inquiries
- Speaking invitations
- Collaboration opportunities

**Efficiency Metrics**:
- Time invested per initiative
- ROI per channel (opportunities / hours)
- Content repurposing ratio (1 article → X assets)

---

### MONTHLY REVIEW TEMPLATE

```
MONTH: [Month Year]

ACTIVITIES COMPLETED:
- [Activity 1]: [Time invested]
- [Activity 2]: [Time invested]

REACH:
- LinkedIn post views: [Total]
- Article views: [Total]
- Community engagement: [Comments/DMs]

OPPORTUNITIES GENERATED:
- Inbound messages: [Count]
- Interview requests: [Count]
- Speaking invites: [Count]
- Other: [Describe]

LEARNINGS:
- What worked: [Insight]
- What didn't: [Insight]
- Adjust for next month: [Action]

ROI ASSESSMENT:
- Time invested: [Total hours]
- Value generated: [High/Medium/Low]
- Continue/Adjust/Stop: [Decision]
```

---

## What NOT to Do

### ❌ DON'T: Spread Too Thin
**Why**: Better to own one channel than be mediocre on five

**Instead**: Master LinkedIn + one other channel (articles or speaking)

---

### ❌ DON'T: Chase Vanity Metrics
**Why**: 10k followers doesn't matter if none are hiring managers

**Instead**: Track inbound opportunities, not follower counts

---

### ❌ DON'T: Create Content Daily
**Why**: Unsustainable, quality suffers, looks desperate

**Instead**: Consistent weekly (LinkedIn) + monthly (articles)

---

### ❌ DON'T: Copy "Influencer" Tactics
**Why**: You're building professional credibility, not entertainment brand

**Instead**: Focus on teaching, not performing

---

### ❌ DON'T: Ignore Your Audience
**Why**: Content for other designers ≠ content for hiring managers

**Instead**: Write for decision-makers (but help peers too)

---

### ❌ DON'T: Wait for Perfection
**Why**: "I'll publish when it's perfect" = never publishing

**Instead**: Ship at 80%, iterate based on feedback

---

## Database Commands

**View**:
- `"Show all brand initiatives"` - List all activities
- `"Show initiatives by channel: [channel]"` - Filter by platform
- `"Show ROI by channel"` - Compare effectiveness

**Create**:
- `"Plan article: [topic]"` - Generate article outline
- `"Create talk proposal for: [topic]"` - CFP template
- `"Build 3-month visibility roadmap"` - Strategic plan

**Update**:
- `"Update initiative [id] reach: [metrics]"` - Track performance
- `"Add opportunity generated from [id]: [description]"` - Track ROI
- `"Mark channel [name] as paused/active"` - Adjust strategy

**Analysis**:
- `"Calculate ROI by channel"` - Time vs. opportunities
- `"What initiatives generated most opportunities?"` - Double down
- `"Show visibility trends over time"` - Growth tracking

---

## Usage Instructions

### Initial Strategy:
```
"Build personal brand amplification strategy:
Time available: 5-8 hours/week
Comfort with public speaking: Medium
Career target: Lead Designer roles
Geographic focus: Remote global, LATAM secondary"
```

### Content Planning:
```
"Generate 3 article ideas based on my expertise:
- First design hire experience
- B2B SaaS design
- Design team scaling

Format: 2,500 word articles for Medium"
```

### Speaking Opportunities:
```
"Create conference talk proposal:
Topic: Scaling design without headcount
Target: Mid-level design conferences
Length: 30 minutes"
```

---

## Output Format

```
---
BRAND AMPLIFICATION PLAN
ID: ba_XXX
Type: [Article/Talk/Community/Video]
Channel: [Platform]
Status: [Planned/In-Progress/Published]
Date: [Date]

---

INITIATIVE DETAILS:
Title: [Title]
Topic: [Theme]
Target Audience: [Who this reaches]
Time Estimate: [Hours]

EXECUTION PLAN:
Week 1: [Tasks]
Week 2: [Tasks]
Week 3: [Tasks]
Week 4: [Tasks]

LEVERAGE OPPORTUNITIES:
- [How to repurpose into other formats]
- [Cross-promotion strategy]
- [Long-term value]

SUCCESS METRICS:
- Primary: [Key metric to track]
- Secondary: [Supporting metrics]
- ROI Signal: [What indicates this worked]

---

DATABASE STATUS: ✅ Saved as ba_XXX

NEXT ACTIONS:
1. [Immediate next step]
2. [Follow-up action]
3. [Promotion plan]
---
```

---

## Quality Checklist

Before launching any brand initiative:

- [ ] **Clear goal** (what success looks like)
- [ ] **Realistic time estimate** (can you sustain this?)
- [ ] **Target audience defined** (who needs to see this?)
- [ ] **Repurposing plan** (how to maximize this effort)
- [ ] **Unique angle** (what makes this different/valuable)
- [ ] **Authentic to you** (sounds like your voice)
- [ ] **Actionable value** (reader/viewer learns something)
- [ ] **Promotion strategy** (how will people find it?)
- [ ] **Success metrics** (how will you measure ROI)
- [ ] **Sustainable cadence** (can you do this long-term?)

---

## Notes
- Personal brand is a marathon, not a sprint
- Consistency beats intensity (1/week for 12 months > 10/week for 1 month)
- Focus on teaching, not promoting
- Track opportunities generated, not vanity metrics
- Repurpose ruthlessly (1 article → 6 assets)
- Start with one channel, expand when consistent
- Your unique angle: First design hire + B2B + LATAM remote
- Quality > Quantity always
- The goal is to be remembered when roles open, not to be famous
