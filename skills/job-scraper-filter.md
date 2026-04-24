# Job Scraper Filter

## Purpose
Automatically filter raw scraped job opportunities from SQLite database, eliminate dealbreakers, calculate pre-scores, and populate a clean filtered table for manual review - saving you from reviewing 100+ irrelevant opportunities.

## Profile Context
- **Name**: Cristhian
- **Role**: Senior Product Designer (10+ years)
- **Location**: Ecuador (remote work)
- **Dealbreakers**: On-site only, Salary < $2,000 USD, No remote option
- **Preferences**: B2B SaaS, Senior+ level, Series A+, Remote-first
- **Processing Goal**: 100 raw jobs → 15-20 filtered → 5-10 deep analysis → 3-5 applications

## Database Architecture

### INPUT: raw_jobs Table
**Purpose**: Stores all scraped opportunities (unprocessed)

**Schema**:
```sql
CREATE TABLE IF NOT EXISTS raw_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    role TEXT,
    url TEXT UNIQUE,
    description TEXT,
    location TEXT,
    salary TEXT,
    posted_date TEXT,
    source TEXT,
    status TEXT DEFAULT 'unprocessed',
    rejection_reason TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Status Values**:
- `unprocessed` - Fresh from scraper, not yet filtered
- `filtered_pass` - Passed automatic filters
- `filtered_reject` - Rejected by dealbreaker criteria

---

### OUTPUT: filtered_jobs Table
**Purpose**: Clean, pre-qualified opportunities for manual review

**Schema**:
```sql
CREATE TABLE IF NOT EXISTS filtered_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_job_id INTEGER UNIQUE,
    company TEXT,
    role TEXT,
    url TEXT,
    description TEXT,
    location TEXT,
    salary TEXT,
    pre_score INTEGER,
    priority TEXT,
    keywords_matched TEXT,
    green_flags TEXT,
    yellow_flags TEXT,
    red_flags TEXT,
    status TEXT DEFAULT 'pending_review',
    filtered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (raw_job_id) REFERENCES raw_jobs(id)
);
```

**Status Values**:
- `pending_review` - Waiting for your manual review
- `selected_for_analysis` - You chose to analyze deeply
- `skipped` - You decided not to pursue
- `analyzed` - Passed through job-opportunity-analyzer.md

**Priority Values**:
- `high` - Pre-score 8-10, review immediately
- `medium` - Pre-score 6-7, review this week
- `low` - Pre-score 5, review if time permits

---

## Filter Criteria

### DEALBREAKERS (Auto-Reject)

These criteria automatically reject opportunities without further analysis.

#### 1. Location Requirements
**Reject if**:
- Description contains: "on-site", "onsite", "in-office", "office-based"
- Location field = specific city WITHOUT "remote" mentioned
- No mention of "remote", "distributed", "work from home", "WFH"

**Exception**: 
- "Hybrid" in Ecuador (Quito, Guayaquil) → Don't auto-reject, but flag (score penalty -1)

**Keywords to detect**:
- **Reject**: "must be based in", "office required", "relocation required"
- **Pass**: "remote", "fully remote", "distributed", "work from anywhere", "remote-first"

---

#### 2. Seniority Level
**Reject if**:
- Role title contains: "Junior", "Associate", "Entry-level", "Intern"
- Role title = "Product Designer" (without Senior/Lead/Principal) AND description mentions "1-3 years"

**Pass if**:
- Role contains: "Senior", "Lead", "Principal", "Staff", "Head of"
- Role = "Product Designer" AND description mentions "5+ years" or "experienced"

**Exception**:
- Mid-level roles (no "Senior" but "3-5 years") → Don't auto-reject IF fully remote AND B2B SaaS
- Score penalty: -2 points

---

#### 3. Disclosed Salary Below Minimum
**Reject if**:
- Salary field contains amount < $2,000 USD/month (or equivalent: < $24,000/year)
- Clear salary disclosed AND below threshold

**Pass if**:
- No salary disclosed (can't reject what's unknown)
- Salary ≥ $2,000 USD/month
- Salary = "Competitive" or "DOE" (Depends on Experience)

**Conversion rates** (if needed):
- Annual to monthly: divide by 12
- EUR to USD: multiply by 1.1 (approximate)

---

#### 4. Agency/Consultancy Without Project
**Reject if**:
- Company name contains: "Agency", "Studio", "Consultancy", "Consulting"
- Description mentions: "join our talent pool", "register with us", "future opportunities"
- No specific project/client mentioned

**Pass if**:
- Agency BUT mentions: "embedded role with [Client]", "dedicated project", "specific engagement"

---

#### 5. Non-Product Design Roles
**Reject if**:
- Role is: "Graphic Designer", "Motion Designer", "Illustrator", "Brand Designer" (unless hybrid)
- Role focus is marketing/advertising without product component

**Pass if**:
- Role is: "Product Designer", "UX Designer", "UI/UX Designer", "Design Lead", "Experience Designer"

---

### SCORING SYSTEM (1-10)

For opportunities that pass dealbreakers, calculate pre-score:

**Base Score**: 5 (neutral starting point)

**Add Points (+)**:

**+2 points** - Keywords Match (B2B/SaaS/Fintech)
- Description contains: "B2B", "SaaS", "enterprise", "fintech", "financial", "payment"
- Description contains: "complex products", "data-heavy", "workflow"

**+2 points** - Seniority Match
- Role title contains: "Senior", "Lead", "Principal", "Staff"

**+2 points** - Remote-First Signals
- Description mentions: "remote-first", "distributed team", "fully remote", "async culture"
- NOT just "remote ok" or "remote possible"

**+1 point** - Company Stage (Series A+)
- Description mentions: "Series A", "Series B", "Series C", "well-funded", "backed by [VC]"

**+1 point** - Salary Transparency
- Salary range clearly disclosed (shows transparency)

**+1 point** - Design Systems/Leadership Opportunity
- Description mentions: "design system", "scale design team", "first design hire", "build design culture"

**+1 point** - Equity Mentioned
- Description includes equity/stock options

**Subtract Points (-)**:

**-1 point** - Hybrid (Ecuador)
- Hybrid model in Quito/Guayaquil (not dealbreaker but not ideal)

**-2 points** - Mid-Level Seniority
- No "Senior" in title but passes other criteria

**-2 points** - Agency/Consultancy (with project)
- Passed dealbreaker but still agency model

**-1 point** - B2C Focus
- Description emphasizes consumer products (less experience here)

**-1 point** - No Funding Info
- No mention of funding stage (might be bootstrapped early-stage)

**-3 points** - Red Flag Keywords
- "Fast-paced environment" (without other context - often means chaos)
- "Wear many hats" (can mean unfocused role)
- "Startup mentality" (can mean overwork)
- "Move fast and break things" (can mean no process)

**Score Ranges**:
- **9-10**: Exceptional fit (rare, apply immediately)
- **8**: Strong fit (high priority)
- **7**: Good fit (medium-high priority)
- **6**: Decent fit (medium priority)
- **5**: Neutral (low priority, review if time)
- **<5**: Don't filter in (re-reject or keep in raw with status)

---

## Keywords Detection

### GREEN FLAG KEYWORDS (Boost Score)

**B2B/SaaS Indicators**:
- "B2B", "SaaS", "enterprise software", "business software"
- "platform", "API", "developer tools", "workflow automation"
- "dashboard", "analytics", "data visualization"

**Fintech Indicators**:
- "fintech", "financial services", "payments", "banking"
- "lending", "investment", "trading", "cryptocurrency"

**Complexity Indicators**:
- "complex", "data-heavy", "enterprise", "technical users"
- "power users", "advanced features", "customization"

**Design Maturity**:
- "design system", "component library", "design ops"
- "design team", "scale design", "first design hire"
- "user research", "design thinking", "data-driven design"

**Remote Culture**:
- "remote-first", "distributed", "asynchronous", "async"
- "global team", "work from anywhere", "timezone flexible"

**Leadership/Growth**:
- "lead", "principal", "staff", "head of design"
- "build team", "scale", "mentor", "grow designers"

---

### YELLOW FLAG KEYWORDS (Caution, Note But Don't Reject)

**Ambiguous Terms**:
- "fast-paced" (context matters: startup chaos vs. high-growth company)
- "wear many hats" (first hire realism vs. unfocused role)
- "startup mentality" (scrappy vs. unprofessional)
- "move fast" (iterate quickly vs. no process)

**These require human judgment - flag but don't auto-reject**

---

### RED FLAG KEYWORDS (Score Penalty)

**Overwork Signals**:
- "long hours", "nights and weekends", "hustle"
- "whatever it takes", "all-hands-on-deck"

**Unclear Role**:
- "generalist" (without context - can mean unfocused)
- "do-it-all" (red flag unless first design hire context)

**Poor Culture Signals**:
- "rockstar", "ninja", "guru" (cringeworthy language)
- "thick skin" (toxic environment hint)

---

## Processing Workflow

### STEP 1: Query Unprocessed Jobs

```sql
SELECT * FROM raw_jobs 
WHERE status = 'unprocessed' 
ORDER BY scraped_at DESC;
```

**Expected volume**: 50-200 jobs per week (depending on scraper frequency)

---

### STEP 2: Apply Dealbreaker Filters

For each job in unprocessed:

```python
def check_dealbreakers(job):
    reasons = []
    
    # Check location
    if is_onsite_only(job.description, job.location):
        reasons.append("On-site only")
    
    # Check seniority
    if is_junior_mid_level(job.role, job.description):
        reasons.append("Junior/Mid level")
    
    # Check salary
    if is_salary_below_minimum(job.salary):
        reasons.append("Salary < $2,000")
    
    # Check agency without project
    if is_agency_without_project(job.company, job.description):
        reasons.append("Agency without immediate project")
    
    # Check role type
    if is_non_product_role(job.role):
        reasons.append("Non-product design role")
    
    return reasons
```

**If dealbreakers found**:
```sql
UPDATE raw_jobs 
SET status = 'filtered_reject', 
    rejection_reason = '[reasons]'
WHERE id = [job_id];
```

**If no dealbreakers**: Proceed to Step 3

---

### STEP 3: Calculate Pre-Score

```python
def calculate_pre_score(job):
    score = 5  # Base score
    
    keywords_matched = []
    green_flags = []
    yellow_flags = []
    red_flags = []
    
    # Check keywords and adjust score
    if has_b2b_saas_keywords(job.description):
        score += 2
        keywords_matched.append("B2B/SaaS")
    
    if is_senior_role(job.role):
        score += 2
        green_flags.append("Senior level")
    
    if is_remote_first(job.description):
        score += 2
        green_flags.append("Remote-first")
    
    # ... (continue for all scoring criteria)
    
    # Cap score at 10
    score = min(score, 10)
    
    return {
        'score': score,
        'keywords': keywords_matched,
        'green_flags': green_flags,
        'yellow_flags': yellow_flags,
        'red_flags': red_flags
    }
```

---

### STEP 4: Determine Priority

```python
def assign_priority(score):
    if score >= 8:
        return 'high'
    elif score >= 6:
        return 'medium'
    else:
        return 'low'
```

---

### STEP 5: Insert into filtered_jobs

```sql
INSERT INTO filtered_jobs (
    raw_job_id,
    company,
    role,
    url,
    description,
    location,
    salary,
    pre_score,
    priority,
    keywords_matched,
    green_flags,
    yellow_flags,
    red_flags,
    status
) VALUES (
    [job.id],
    [job.company],
    [job.role],
    [job.url],
    [job.description],
    [job.location],
    [job.salary],
    [calculated_score],
    [priority],
    [keywords_joined],
    [green_flags_joined],
    [yellow_flags_joined],
    [red_flags_joined],
    'pending_review'
);
```

---

### STEP 6: Update raw_jobs Status

```sql
UPDATE raw_jobs 
SET status = 'filtered_pass'
WHERE id = [job_id];
```

---

### STEP 7: Generate Summary Report

After processing all unprocessed jobs:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JOB FILTER PROCESSING SUMMARY
Run Date: 2025-04-24 14:30
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 PROCESSING STATS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Unprocessed:     127 jobs
Passed Filter:         23 jobs (18%)
Rejected:              104 jobs (82%)

✅ FILTERED OPPORTUNITIES (23)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 High Priority (8-10): 6 jobs
📋 Medium Priority (6-7): 11 jobs
📌 Low Priority (5): 6 jobs

❌ REJECTION BREAKDOWN (104)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
On-site only:          58 jobs (56%)
Junior/Mid level:      22 jobs (21%)
Agency no project:     14 jobs (13%)
Salary < $2,000:       7 jobs (7%)
Non-product role:      3 jobs (3%)

🎯 TOP OPPORTUNITIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Remote.com - Senior Product Designer (Score: 9)
   ✅ B2B SaaS, Remote-first, Series B
   
2. Crustdata - Principal Designer (Score: 8)
   ✅ First design hire, YC-backed, API product
   
3. Linear - Lead Product Designer (Score: 8)
   ✅ Remote-first, Design systems, Well-funded

[... top 5-6 listed]

⚡ NEXT ACTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Review 6 high-priority opportunities
2. Use job-opportunity-analyzer.md for deep analysis
3. Next filter run: When new jobs scraped

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Database Queries (Helper Functions)

### View Filtered Jobs (Your Review Queue)

```sql
-- All pending review, ordered by priority and score
SELECT 
    id,
    company,
    role,
    pre_score,
    priority,
    keywords_matched,
    url
FROM filtered_jobs
WHERE status = 'pending_review'
ORDER BY 
    CASE priority 
        WHEN 'high' THEN 1 
        WHEN 'medium' THEN 2 
        WHEN 'low' THEN 3 
    END,
    pre_score DESC;
```

---

### View Rejection Reasons (Analytics)

```sql
-- Breakdown of why jobs were rejected
SELECT 
    rejection_reason,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM raw_jobs WHERE status = 'filtered_reject'), 1) as percentage
FROM raw_jobs
WHERE status = 'filtered_reject'
GROUP BY rejection_reason
ORDER BY count DESC;
```

---

### Find Duplicates (URL Check)

```sql
-- Check for duplicate URLs before inserting
SELECT url, COUNT(*) as count
FROM raw_jobs
GROUP BY url
HAVING count > 1;
```

---

### Mark Job for Deep Analysis

```sql
-- When you decide to analyze a filtered job deeply
UPDATE filtered_jobs
SET status = 'selected_for_analysis'
WHERE id = [job_id];
```

---

### Skip a Filtered Job

```sql
-- When you review and decide not to pursue
UPDATE filtered_jobs
SET status = 'skipped',
    notes = 'Reason for skipping'
WHERE id = [job_id];
```

---

## Integration with Other Skills

### WITH job-opportunity-analyzer.md

**Flow**:
```
1. You review filtered_jobs (pending_review, high priority)
2. You select 5-10 to analyze deeply
3. For each selected:
   - UPDATE filtered_jobs SET status = 'selected_for_analysis'
   - Run job-opportunity-analyzer.md (full analysis)
   - Get detailed fit score (1-10)
   - UPDATE filtered_jobs SET status = 'analyzed'
   - If fit score ≥ 6 → Add to job-pipeline.json
```

---

### WITH job-pipeline-manager.md

**Flow**:
```
1. After deep analysis (fit score ≥ 6)
2. Add to job-pipeline.json as "prospect"
3. Include pre_score from filter for reference
4. Link back to filtered_jobs.id for traceability
```

---

## Automation Strategy

### Daily Run (If Scraper Runs Daily)

```bash
# Pseudo-code for Claude Code scheduled task
# Run every morning at 9am

1. Check for new raw_jobs (status = 'unprocessed')
2. If count > 0:
   - Run filter process
   - Generate summary report
   - Notify: "X new opportunities filtered, Y high priority"
3. If count = 0:
   - No action needed
```

---

### Weekly Summary

```bash
# Run every Monday morning

1. Count filtered_jobs added this week
2. Count by priority (high/medium/low)
3. Count analyzed vs. pending
4. Generate weekly digest:
   - "This week: 23 new opportunities filtered"
   - "High priority: 6 (review ASAP)"
   - "You analyzed: 8, Applied to: 3"
```

---

## Configuration (Tunable Parameters)

These can be adjusted based on your job market experience:

```python
CONFIG = {
    # Scoring weights
    'b2b_saas_points': 2,
    'seniority_points': 2,
    'remote_first_points': 2,
    'company_stage_points': 1,
    
    # Thresholds
    'minimum_salary_usd': 2000,
    'high_priority_score': 8,
    'medium_priority_score': 6,
    
    # Red flag penalties
    'agency_penalty': -2,
    'mid_level_penalty': -2,
    'red_flag_keyword_penalty': -1,
    
    # Keyword lists (editable)
    'b2b_keywords': ['b2b', 'saas', 'enterprise', 'business software'],
    'remote_keywords': ['remote-first', 'distributed', 'fully remote'],
    'red_flag_keywords': ['long hours', 'nights and weekends', 'rockstar'],
}
```

---

## Maintenance & Improvement

### Monthly Review

**Review rejection accuracy**:
```sql
-- Jobs you manually skipped after filtering
SELECT 
    pre_score,
    priority,
    rejection_reason,
    COUNT(*) 
FROM filtered_jobs 
WHERE status = 'skipped'
GROUP BY pre_score, priority;
```

**Analysis**: If many high-priority jobs are skipped, scoring criteria may need tuning.

---

### A/B Test Scoring

**Track conversion**:
```sql
-- What pre-scores lead to applications?
SELECT 
    f.pre_score,
    COUNT(*) as filtered_count,
    SUM(CASE WHEN f.status = 'analyzed' THEN 1 ELSE 0 END) as analyzed_count
FROM filtered_jobs f
GROUP BY f.pre_score
ORDER BY f.pre_score DESC;
```

**Insight**: If score 7 jobs never get analyzed, maybe threshold is too high.

---

### Keyword Tuning

**Track which keywords correlate with good opportunities**:
```sql
-- Most common keywords in analyzed jobs
SELECT 
    keywords_matched,
    COUNT(*) as count
FROM filtered_jobs
WHERE status IN ('analyzed', 'selected_for_analysis')
GROUP BY keywords_matched
ORDER BY count DESC;
```

**Action**: Add high-performing keywords, remove low-signal ones.

---

## Commands (For Claude Code)

### Run Filter
```
"Run job filter on unprocessed opportunities"
→ Processes all unprocessed raw_jobs
→ Populates filtered_jobs
→ Generates summary report
```

### View Queue
```
"Show my filtered job queue"
→ Lists pending_review jobs by priority
```

### Update After Review
```
"Mark filtered job [id] as selected for analysis"
"Mark filtered job [id] as skipped - reason: [X]"
```

### Analytics
```
"Show filter performance this week"
"Show rejection breakdown"
"Show scoring accuracy"
```

### Tune Parameters
```
"Adjust minimum salary to $2,500"
"Add keyword to B2B list: 'workflow automation'"
"Increase remote-first points to 3"
```

---

## Usage Instructions

### Initial Setup:
```
"Initialize filter tables in SQLite database.
Show me the CREATE TABLE statements."
```

### Daily Usage:
```
"Run filter on new scraped jobs.
Generate summary report."
```

### Weekly Review:
```
"Show my high-priority filtered jobs from this week.
List top 10 by score."
```

### After Manual Review:
```
"I reviewed filtered jobs #45, #47, #52.
Mark #45 and #47 for deep analysis.
Mark #52 as skipped - agency role."
```

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JOB SCRAPER FILTER - PROCESSING REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Run: 2025-04-24 14:30:00
Database: /data/jobs.db

📊 SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Unprocessed Jobs:    127
✅ Passed Filter:     23 (18%)
❌ Rejected:          104 (82%)

🔥 HIGH PRIORITY (Score 8-10) - 6 jobs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ID: 45 | Score: 9 | Remote.com - Senior Product Designer
  ✅ B2B SaaS, Remote-first, Series B, Design systems
  URL: https://remote.com/careers/...

ID: 47 | Score: 8 | Crustdata - Principal Designer  
  ✅ First design hire, YC-backed, API product
  URL: https://jobs.crustdata.com/...

[... continue for all high priority]

📋 MEDIUM PRIORITY (Score 6-7) - 11 jobs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Listed with less detail]

📌 LOW PRIORITY (Score 5) - 6 jobs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Listed with minimal detail]

❌ REJECTION BREAKDOWN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
On-site only:        58 (56%)
Junior/Mid level:    22 (21%)
Agency no project:   14 (13%)
Salary < $2,000:     7 (7%)
Non-product role:    3 (3%)

⚡ NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Review 6 high-priority opportunities manually
2. Select 3-5 for deep analysis (job-opportunity-analyzer.md)
3. Update filtered_jobs.status after review

DATABASE STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ raw_jobs: 127 processed → 0 unprocessed remaining
✅ filtered_jobs: 23 new entries (pending_review)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Notes
- Run filter AFTER scraper adds new jobs to raw_jobs
- Filter is aggressive (18% pass rate) to save your time
- Pre-score is directional, not final - deep analysis comes later
- Tune scoring weights based on your market experience
- Review high-priority jobs within 24-48 hours (before links expire)
- Update status after manual review to keep data clean
- Monthly: review filter accuracy and adjust criteria
- The goal: 100 raw → 20 filtered → 5 analyzed → 3 applied
