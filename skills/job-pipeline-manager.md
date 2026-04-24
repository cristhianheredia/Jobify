# Job Pipeline Manager

## Purpose
Manage your job search pipeline efficiently - track applications, deadlines, follow-ups, and status updates in a structured way. Provide dashboard views, alerts, and analytics to optimize your search process.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer seeking next opportunity
- **Pain Points**: Broken links, expired postings, tracking where you are in multiple processes
- **Pipeline Size**: Typically 5-15 active applications at any time
- **Key Metrics**: Applications → Screening → Interview → Offer conversion rates

## Input
- New opportunity details (company, role, URL, salary range)
- Status updates (applied, rejected, interview scheduled, offer)
- Notes and follow-up actions
- Deadlines and important dates

## Output
- Current pipeline dashboard
- Next actions list
- Follow-up reminders
- Analytics and insights
- Saved to persistent database

---

## PIPELINE DATABASE STRUCTURE

### Database File
**File**: `/data/job-pipeline.json`

**Schema**:
```json
{
  "opportunities": [
    {
      "id": "opp_001",
      "company": "Remote.com",
      "role": "Senior Product Designer",
      "url": "https://remote.com/careers/...",
      "url_status": "active",
      "url_last_checked": "2025-04-24",
      "status": "interview_r2",
      "priority": "high",
      "fit_score": 9,
      "salary_range": "$3500-5000",
      "location": "Remote",
      "date_added": "2025-04-15",
      "date_applied": "2025-04-16",
      "source": "LinkedIn",
      "contact_person": "Sarah (Recruiter)",
      "contact_email": "sarah@remote.com",
      "next_action": "Prepare for 2nd interview",
      "next_action_date": "2025-04-26",
      "timeline": [
        {
          "date": "2025-04-15",
          "event": "opportunity_found",
          "notes": "Found via LinkedIn, strong fit"
        },
        {
          "date": "2025-04-16",
          "event": "applied",
          "notes": "Submitted application + cover letter"
        },
        {
          "date": "2025-04-18",
          "event": "screening",
          "notes": "30min call with Sarah, went well"
        },
        {
          "date": "2025-04-22",
          "event": "interview_r1",
          "notes": "Portfolio review with Design Lead, positive"
        }
      ],
      "notes": "Great culture fit, remote-first, B2B SaaS",
      "red_flags": [],
      "green_flags": ["remote-first", "b2b-saas", "series-b-funded"],
      "materials_submitted": ["resume", "portfolio", "cover-letter"],
      "interviews_completed": 2,
      "archived": false
    }
  ],
  "metadata": {
    "total_opportunities": 1,
    "active_count": 1,
    "archived_count": 0,
    "last_updated": "2025-04-24"
  },
  "analytics": {
    "conversion_rates": {
      "applied_to_screening": 0,
      "screening_to_interview": 0,
      "interview_to_offer": 0
    },
    "avg_time_to_response": 0,
    "sources_by_success": {}
  }
}
```

---

## Status Definitions

### PIPELINE STAGES

**Stage 1: Prospect**
- Status: `prospect`
- Description: Opportunity identified, not yet applied
- Next Action: Analyze fit, prepare application materials
- Typical Duration: 1-3 days

**Stage 2: Applied**
- Status: `applied`
- Description: Application submitted, waiting for response
- Next Action: Follow up after 7-10 days if no response
- Typical Duration: 3-14 days

**Stage 3: Screening**
- Status: `screening`
- Description: Initial recruiter/phone screen scheduled or completed
- Next Action: Prepare for/complete screening call
- Typical Duration: 1-2 weeks

**Stage 4: Interview Round 1**
- Status: `interview_r1`
- Description: First formal interview (usually hiring manager or portfolio review)
- Next Action: Prepare with interview-prep-coach.md
- Typical Duration: 1-2 weeks

**Stage 5: Interview Round 2+**
- Status: `interview_r2`, `interview_r3`, etc.
- Description: Subsequent interviews (team, panel, leadership)
- Next Action: Prepare for specific interview type
- Typical Duration: 1-2 weeks per round

**Stage 6: Design Challenge**
- Status: `design_challenge`
- Description: Take-home design assignment
- Next Action: Use design-challenge-strategist.md
- Typical Duration: 3-7 days

**Stage 7: Final Round**
- Status: `final_round`
- Description: Last interview before decision
- Next Action: Prepare for leadership/exec interview
- Typical Duration: 1 week

**Stage 8: Offer**
- Status: `offer`
- Description: Offer received, negotiating or deciding
- Next Action: Use salary-negotiation-advisor.md
- Typical Duration: 3-7 days

**Terminal States:**

**Rejected**
- Status: `rejected`
- Description: Application rejected at any stage
- Next Action: Request feedback, update learnings
- Archive: Yes

**Withdrawn**
- Status: `withdrawn`
- Description: You withdrew from process
- Next Action: Document reason
- Archive: Yes

**Accepted**
- Status: `accepted`
- Description: You accepted an offer
- Next Action: Celebrate! Archive all other applications
- Archive: No (keep as reference)

**Expired**
- Status: `expired`
- Description: Job posting removed/expired before you could apply
- Next Action: None
- Archive: Yes

**Ghosted**
- Status: `ghosted`
- Description: No response after 3+ weeks, multiple follow-ups
- Next Action: Move on, archive
- Archive: Yes

---

## Priority Levels

### HIGH PRIORITY
**Criteria**:
- Fit score 8-10
- Salary meets or exceeds target ($3,200+)
- Active interview process
- Deadline approaching

**Action**: Check daily, prioritize prep time

---

### MEDIUM PRIORITY
**Criteria**:
- Fit score 6-7
- Salary acceptable but not ideal
- Applied, waiting for response
- No immediate deadline

**Action**: Check 2x per week, standard prep

---

### LOW PRIORITY
**Criteria**:
- Fit score 5 or below
- Backup options
- Agency/consultancy without immediate project
- On-site or hybrid in Ecuador

**Action**: Check weekly, minimal prep unless they advance you

---

## Database Operations

### ADD NEW OPPORTUNITY
**Command**: `"Add opportunity: [company] - [role]"`

**Required Fields**:
- Company name
- Role title
- URL (for job posting)
- Status (usually starts as `prospect`)

**Optional Fields** (can add later):
- Fit score (from job-opportunity-analyzer.md)
- Salary range
- Contact person
- Priority level

**Auto-Generated**:
- Unique ID
- Date added
- Timeline entry (opportunity found)

**Example**:
```
Add opportunity:
Company: Crustdata
Role: Principal Product Designer
URL: https://jobs.crustdata.com/...
Fit Score: 8
Salary: $4000-5500
Priority: High
Notes: YC-backed, first design hire, API product
```

---

### UPDATE STATUS
**Command**: `"Update [company] status to [new-status]"`

**What Happens**:
1. Status field updated
2. Timeline entry added with timestamp
3. Next action suggested based on new status
4. Analytics recalculated

**Example**:
```
Update Remote.com status to interview_r2
→ Status changed
→ Timeline: "2025-04-24: Advanced to Round 2 interview"
→ Next Action: "Prepare for 2nd interview - use interview-prep-coach.md"
```

---

### CHECK URL STATUS
**Command**: `"Check URLs for expired/broken links"`

**What Happens**:
1. Iterate through all non-archived opportunities
2. Attempt to fetch each URL
3. Mark as `active`, `expired`, or `broken`
4. Flag opportunities with broken links for review

**Auto-Run**: Weekly (if Claude Code is configured for scheduled tasks)

**Manual Trigger**: When you notice broken links

---

### ADD NOTE
**Command**: `"Add note to [company]: [note text]"`

**Use Cases**:
- Interview observations ("Sarah mentioned they're hiring 2 more designers")
- Red flags discovered ("Glassdoor reviews mention poor work-life balance")
- Follow-up reminders ("Need to send thank-you email by Friday")
- Learnings ("They asked a lot about design systems - be ready for that")

---

### SET NEXT ACTION
**Command**: `"Set next action for [company]: [action] by [date]"`

**Examples**:
- "Set next action for Remote.com: Prepare portfolio walkthrough by 2025-04-26"
- "Set next action for Crustdata: Follow up with recruiter by 2025-04-30"
- "Set next action for Thoughtworks: Submit design challenge by 2025-05-01"

**Reminder**: Claude Code can surface upcoming next actions in daily/weekly summaries

---

### ARCHIVE OPPORTUNITY
**Command**: `"Archive [company]"`

**When to Archive**:
- Rejected
- Withdrawn by you
- Expired/broken link with no alternative
- Ghosted (3+ weeks, no response)
- Accepted another offer (archive all others)

**What Happens**:
- `archived: true` flag set
- Removed from active dashboard
- Kept in database for analytics
- Can be unarchived if needed

---

## Dashboard Views

### VIEW 1: Active Pipeline (Default)

```
ACTIVE PIPELINE (5 opportunities)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 HIGH PRIORITY (2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Remote.com - Senior Product Designer
  Status: Interview R2
  Fit: 9/10 | Salary: $3500-5000
  Next: Prepare for 2nd interview by Apr 26
  Notes: Remote-first, B2B SaaS, great culture fit
  
Crustdata - Principal Designer  
  Status: Applied
  Fit: 8/10 | Salary: $4000-5500
  Next: Follow up if no response by Apr 28
  Notes: YC-backed, first design hire
  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 MEDIUM PRIORITY (2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Similar format]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LOW PRIORITY (1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Similar format]
```

---

### VIEW 2: Next Actions (To-Do List)

```
NEXT ACTIONS DUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 TODAY (Apr 24)
  □ Check if Figma responded to application (Added 7 days ago)

📅 THIS WEEK (Apr 25-30)
  □ Remote.com: Prepare for 2nd interview (Due: Apr 26)
  □ Crustdata: Follow up with recruiter (Due: Apr 28)
  □ Thoughtworks: Submit design challenge (Due: Apr 30)

📅 NEXT WEEK (May 1-7)
  □ Linear: Schedule screening call (Due: May 2)

⚠️ OVERDUE
  □ Stripe: Send thank-you email after interview (Was: Apr 22)
```

---

### VIEW 3: Analytics Dashboard

```
PIPELINE ANALYTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 CONVERSION RATES
  Applied → Screening:  60% (6/10)
  Screening → Interview: 75% (3/4)
  Interview → Offer:    50% (1/2)
  Overall Success Rate:  10% (1/10 applied → offer)

⏱️ AVERAGE TIME TO RESPONSE
  After application: 5 days
  Between interview rounds: 8 days
  Offer decision time: 4 days

📈 SOURCES (by success rate)
  LinkedIn:     3 applied, 2 interviews (67%)
  WeWorkRemote: 4 applied, 1 interview (25%)
  Direct:       2 applied, 2 interviews (100%)
  Referral:     1 applied, 1 offer (100%)

🎯 FIT SCORE CORRELATION
  Fit 9-10: 80% interview rate
  Fit 7-8:  50% interview rate
  Fit 5-6:  20% interview rate

⚠️ HEALTH CHECK
  ✅ Good application velocity (3-5 per week)
  ⚠️ Low follow-up rate (2 opportunities need follow-up)
  ✅ High fit score average (7.2/10)
  ⚠️ 3 broken/expired URLs need attention
```

---

### VIEW 4: Timeline View (Gantt-style)

```
TIMELINE VIEW (Last 30 Days)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Apr 15 ▓▓░░░░░░░░░░░░░░ Remote.com (Applied → Interview R2)
Apr 18 ░░▓▓░░░░░░░░░░░░ Crustdata (Applied, waiting)
Apr 20 ░░░░▓▓░░░░░░░░░░ Thoughtworks (Challenge in progress)
Apr 22 ░░░░░░▓▓▓░░░░░░░ Figma (Applied, no response)
Apr 24 ░░░░░░░░░▓░░░░░░ Linear (Prospect, researching)

Legend: ▓ Active stages | ░ Waiting/No activity
```

---

## Alerts & Reminders

### DAILY DIGEST
**Trigger**: Every morning (if Claude Code scheduled)

**Contents**:
```
Good morning, Cristhian!

📬 ACTIONS DUE TODAY:
  • Remote.com: Prepare for 2nd interview (tomorrow)

⏰ FOLLOW-UPS NEEDED:
  • Figma: No response in 7 days - follow up today?

🆕 NEW OPPORTUNITIES:
  • 3 new Senior Designer roles match your criteria (check pipeline)

📊 PIPELINE HEALTH:
  • 5 active opportunities
  • 2 interviews this week
  • 1 design challenge due Friday
```

---

### WEEKLY SUMMARY
**Trigger**: Every Monday morning

**Contents**:
```
Weekly Job Search Summary (Week of Apr 21-27)

📈 ACTIVITY:
  • 2 new applications submitted
  • 3 interviews completed
  • 1 offer received (Remote.com! 🎉)

📊 PIPELINE STATUS:
  • 5 active opportunities
  • 2 in final rounds
  • 3 awaiting response

🎯 NEXT WEEK PRIORITIES:
  • Negotiate Remote.com offer
  • Complete Thoughtworks design challenge
  • Schedule Crustdata screening

⚠️ NEEDS ATTENTION:
  • 2 broken links - check if postings still active
  • 1 overdue follow-up
```

---

### BROKEN LINK ALERT
**Trigger**: When URL check detects broken/expired link

**Contents**:
```
⚠️ BROKEN LINK DETECTED

Company: Figma
Role: Senior Product Designer
Original URL: [broken link]

Actions:
1. Search company careers page for reposted role
2. Contact recruiter if you have their info
3. Archive if truly expired

Would you like me to search for alternative posting?
```

---

### FOLLOW-UP REMINDER
**Trigger**: 7 days after application with no response

**Contents**:
```
⏰ FOLLOW-UP REMINDER

It's been 7 days since you applied to:
  Company: Crustdata
  Role: Principal Designer
  Applied: Apr 18

Suggested action: Send polite follow-up email

Would you like me to draft a follow-up email?
```

---

## Analytics & Insights

### CONVERSION FUNNEL ANALYSIS

**Track These Metrics**:
```
Total Prospects:        20
↓ Applied:             15 (75% of prospects)
↓ Screening:           9  (60% of applied)
↓ Interview R1:        6  (67% of screening)
↓ Interview R2+:       3  (50% of R1)
↓ Offer:              1  (33% of R2+)

Overall Success Rate: 1/15 applied = 6.7%
```

**Insights**:
- Strong conversion from screening → interview (67%)
- Weakness: Applied → screening (60%, industry avg: 70%)
- Action: Improve application materials (cover letter, resume)

---

### SOURCE EFFECTIVENESS

**Track Where Opportunities Come From**:
```
Source          Applied  Interview  Offer  Success Rate
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Referral        2        2          1      50% ⭐⭐⭐
LinkedIn        8        5          0      0%
Direct          3        3          0      0%
WeWorkRemote    2        0          0      0%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Insight**: Referrals have 50% success rate vs. 0% for cold applications
**Action**: Prioritize networking and referrals

---

### FIT SCORE VALIDATION

**Does Your Fit Score Predict Success?**
```
Fit Score   Applied  Interview  Offer  Interview Rate
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9-10        4        3          1      75% ⭐⭐⭐
7-8         6        3          0      50%
5-6         5        0          0      0%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Insight**: Fit score 9-10 correlates with 75% interview rate
**Action**: Be more selective, focus on fit 8+ opportunities

---

### TIME-TO-RESPONSE TRENDS

**How Long Before Companies Respond?**
```
After Application:
  25th percentile: 2 days
  50th percentile: 5 days (median)
  75th percentile: 10 days
  90th percentile: 14 days

Between Interview Rounds:
  Median: 8 days
  Range: 3-21 days
```

**Insight**: If no response after 10 days, 75% unlikely to respond
**Action**: Follow up at 7-10 day mark

---

## Database Commands

### View Commands
```
"Show active pipeline"
"Show next actions"
"Show analytics"
"Show opportunities by priority: high"
"Show opportunities by status: interview"
"Show opportunities from source: LinkedIn"
"Show archived opportunities"
```

### Add/Update Commands
```
"Add opportunity: [company] - [role]"
"Update [company] status to [status]"
"Add note to [company]: [note]"
"Set next action for [company]: [action] by [date]"
"Set priority for [company]: high/medium/low"
"Mark [company] as rejected"
"Archive [company]"
```

### Utility Commands
```
"Check all URLs for broken links"
"Generate weekly summary"
"Export pipeline to CSV"
"Search opportunities by keyword: [keyword]"
"Show opportunities needing follow-up"
```

### Analytics Commands
```
"Calculate conversion rates"
"Show source effectiveness"
"Validate fit score predictions"
"Show time-to-response trends"
"Identify pipeline bottlenecks"
```

---

## Export Formats

### CSV EXPORT
**Use Case**: Backup, analysis in Google Sheets, sharing with career coach

**Format**:
```
Company,Role,Status,Priority,Fit,Salary,Applied,Source,URL,Notes
Remote.com,Senior Product Designer,interview_r2,high,9,$3500-5000,2025-04-16,LinkedIn,https://...,Remote-first culture
```

### MARKDOWN SUMMARY
**Use Case**: Weekly review, sharing progress with accountability partner

**Format**:
```
# Job Search Pipeline - Week of Apr 21

## Active Opportunities (5)

### High Priority
- **Remote.com** - Senior Product Designer
  - Status: Interview Round 2
  - Fit: 9/10 | $3500-5000
  - Next: Prepare for interview on Apr 26
  
[...]
```

---

## Integration with Other Skills

### WITH job-opportunity-analyzer.md
**Flow**:
1. Analyze opportunity → Get fit score
2. Add to pipeline with fit score
3. Priority set automatically based on score

**Example**:
```
User: "Analyze this job: [URL]"
→ job-opportunity-analyzer runs
→ Returns fit score: 8/10
→ "Should I add this to your pipeline?"
→ User: "Yes"
→ Added with priority: High (based on fit score 8)
```

---

### WITH application-form-writer.md
**Flow**:
1. Check pipeline for opportunity
2. Pull company research from notes
3. Generate tailored application
4. Update pipeline: status → "applied"

---

### WITH interview-prep-coach.md
**Flow**:
1. Check pipeline for upcoming interviews
2. Pull company context and notes
3. Generate prep materials
4. After interview: update status, add notes

---

### WITH salary-negotiation-advisor.md
**Flow**:
1. Opportunity moves to "offer" status
2. Pull salary range from pipeline
3. Generate negotiation strategy
4. Update pipeline with negotiation notes

---

## Best Practices

### DO:
✅ **Update immediately after events** (applied, interview, rejection)
✅ **Add notes while fresh** (right after calls/interviews)
✅ **Check pipeline daily** (5 min review)
✅ **Follow up systematically** (7-10 day rule)
✅ **Archive promptly** (keep pipeline clean)
✅ **Track learnings** (what worked, what didn't)

### DON'T:
❌ Let pipeline get stale (outdated statuses)
❌ Skip URL checks (broken links waste time)
❌ Ignore next actions (they compound)
❌ Over-apply (quality > quantity)
❌ Forget to archive (cluttered view)

---

## Usage Instructions

### Initial Setup:
```
"Initialize job pipeline for me.
Current active applications:
1. Remote.com - Senior Designer (Interview R2)
2. Crustdata - Principal Designer (Applied)
3. Thoughtworks - Design Lead (Challenge in progress)"
```

### Daily Usage:
```
"Show my active pipeline"
→ View current status

"What are my next actions?"
→ See to-do list

"Update Remote.com to offer"
→ Status change

"Add note to Crustdata: Recruiter mentioned hiring 2 designers total"
→ Context capture
```

### Weekly Review:
```
"Generate weekly summary"
→ See progress, analytics, next week priorities

"Check URLs for broken links"
→ Pipeline health check
```

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JOB PIPELINE DASHBOARD
Last Updated: [Timestamp]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 QUICK STATS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Active Opportunities: 5
High Priority: 2 | Medium: 2 | Low: 1
Interviews This Week: 2
Next Actions Due: 3

🔥 HIGH PRIORITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Opportunities listed]

📋 MEDIUM PRIORITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Opportunities listed]

📌 LOW PRIORITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Opportunities listed]

⏰ NEXT ACTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Actions due listed by date]

⚠️ ALERTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Any broken links, overdue follow-ups, etc.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Notes
- Keep pipeline lean (5-15 active max for sanity)
- Archive promptly (clean data = better analytics)
- Update immediately (don't rely on memory)
- Check URLs weekly (broken links are common)
- Use next actions (don't let things slip)
- Review analytics monthly (optimize your approach)
- This is your single source of truth for job search
