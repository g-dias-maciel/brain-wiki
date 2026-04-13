# LLM Wiki System - Schema

This document defines the rules, conventions, and workflows for the LLM Wiki system. As the LLM agent, you must follow these guidelines precisely in all interactions.

## Directory Structure

```
Gabriel Brain/
├── raw/                    # Source documents (immutable)
│   ├── financial/         # Bank statements, tax documents, investment records
│   ├── legal/             # Contracts, legal documents, residency papers
│   ├── business/          # Business plans, invoices, company documents
│   ├── personal/          # Journal entries, health records, personal notes
│   ├── references/        # Articles, books, research papers
│   └── assets/            # Downloaded images and attachments
├── wiki/                  # LLM-generated wiki pages
│   ├── life-domains/      # Major life areas
│   │   ├── finance/       # Financial strategy, investments, taxes
│   │   ├── legal/         # Legal status, residency, citizenship
│   │   ├── business/      # Business operations, companies, projects
│   │   ├── health/        # Health records, fitness, medical
│   │   ├── personal/      # Goals, relationships, personal development
│   │   └── admin/         # Administrative tasks, bureaucracy
│   ├── entities/          # People, organizations, institutions
│   ├── concepts/          # Strategies, frameworks, methodologies
│   ├── sources/           # Source summaries and metadata
│   ├── timelines/         # Chronological views and projections
│   ├── dashboards/        # Status overviews and metrics
│   └── outputs/           # Generated reports, analyses, plans
├── index.md              # Catalog of all wiki pages
├── log.md                # Chronological activity log
└── CLAUDE.md            # This schema file
```

## File Naming Conventions

- **Wiki pages**: Use kebab-case with descriptive names (e.g., `quantum-mechanics-basics.md`, `albert-einstein.md`)
- **Source files**: Keep original names when possible, or use descriptive names with dates (e.g., `2026-04-07-llm-wiki-pattern.md`)
- **Images**: Use descriptive names (e.g., `einstein-1905-photo.jpg`)

## Wiki Page Structure

Every wiki page must include:

```yaml
---
title: Page Title
type: [entity|concept|source|topic|comparison|output]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of source file names]
tags: [relevant tags]
aliases: [alternative names]
---
```

### Page Types

1. **Life Domain**: Major areas of life (finance, legal, business, health, personal, admin)
2. **Entity**: People, organizations, institutions, companies
3. **Concept**: Strategies, frameworks, methodologies, principles
4. **Source**: Summary and analysis of a source document
5. **Timeline**: Chronological view of events or projections
6. **Dashboard**: Status overview with key metrics and updates
7. **Output**: Generated reports, analyses, plans, checklists

## Core Operations

### Ingest Workflow
When a new source is added to `raw/`:

1. **Read & Analyze**: Read the source document thoroughly
2. **Discuss**: Present key takeaways to the user for guidance
3. **Create Source Page**: In `wiki/sources/` with comprehensive summary
4. **Update Index**: Add new page to `index.md`
5. **Update Related Pages**: Find and update all relevant entity/concept/topic pages
6. **Log Entry**: Append to `log.md` with `## [YYYY-MM-DD] ingest | Source Title`
7. **Cross-reference**: Add bidirectional links between all affected pages

### Query Workflow
When the user asks a question:

1. **Search Index**: Consult `index.md` for relevant pages
2. **Read Pages**: Load and analyze relevant wiki pages
3. **Synthesize**: Generate answer with citations to wiki pages
4. **Consider Output**: If answer is valuable, create new `output/` page
5. **Update Links**: Add links from answer to relevant wiki pages
6. **Log Entry**: Append to `log.md` with `## [YYYY-MM-DD] query | Brief description`

### Lint Workflow
Periodically or when requested:

1. **Check Consistency**: Look for contradictions between pages
2. **Find Orphans**: Identify pages with no inbound links
3. **Flag Stale Content**: Mark claims needing updates
4. **Identify Gaps**: Suggest missing pages or connections
5. **Propose Questions**: Suggest research questions to explore
6. **Log Entry**: Append to `log.md` with `## [YYYY-MM-DD] lint | Summary of findings`

## Index Structure

`index.md` should be organized by life domain:

```markdown
# Wiki Index

## Life Domains

### Finance
- [Margin Engine Strategy](wiki/life-domains/finance/margin-engine-strategy.md) - Buy, Borrow, Die investment approach
- [Tax Planning](wiki/life-domains/finance/tax-planning.md) - German and Brazilian tax optimization

### Legal
- [Residency Status](wiki/life-domains/legal/residency-status.md) - German residency, Brazilian tax exit
- [Citizenship Planning](wiki/life-domains/legal/citizenship-planning.md) - Italian passport process

### Business
- [Caju Wear GbR](wiki/life-domains/business/caju-wear-gbr.md) - Business operations and strategy
- [Banking Setup](wiki/life-domains/business/banking-setup.md) - Business account selection

### Personal
- [Goals 2026](wiki/life-domains/personal/goals-2026.md) - Annual objectives and tracking
- [Driver's License](wiki/life-domains/personal/drivers-license.md) - German license conversion

## Entities
- [Scalable Capital](wiki/entities/scalable-capital.md) - Current brokerage platform
- [Interactive Brokers](wiki/entities/interactive-brokers.md) - Target brokerage for migration

## Concepts
- [Buy Borrow Die](wiki/concepts/buy-borrow-die.md) - Lombard loan wealth strategy
- [LTV Management](wiki/concepts/ltv-management.md) - Loan-to-Value risk protocols

## Dashboards
- [Financial Dashboard](wiki/dashboards/financial-dashboard.md) - Portfolio status, LTV, cash flow
- [Project Tracker](wiki/dashboards/project-tracker.md) - Active projects and deadlines

## Timelines
- [Migration Timeline](wiki/timelines/migration-timeline.md) - Germany exit planning
- [Business Timeline](wiki/timelines/business-timeline.md) - Caju Wear development

## Outputs
- [Monthly Financial Review](wiki/outputs/monthly-financial-review-2026-04.md)
- [Tax Compliance Checklist](wiki/outputs/tax-compliance-checklist.md)
```

Each entry should include the page title as a link and a one-line description.

## Log Structure

`log.md` should use consistent entry format:

```markdown
## [2026-04-07] ingest | LLM Wiki Pattern
Added source document describing the LLM Wiki pattern. Created source page and initialized wiki structure.

## [2026-04-07] query | What is quantum mechanics?
Answered user question about quantum mechanics basics. Created output page with learning path.

## [2026-04-07] lint | Initial consistency check
Performed first lint of wiki. No contradictions found. Suggested adding pages for key physicists.
```

## Linking Conventions

- Use Obsidian-style links: `[[page-name]]` for internal links
- Always add reciprocal links when creating connections
- When mentioning an entity/concept that doesn't have a page yet, create a TODO note: `[[TODO: page-name]]`

## Image Handling

- Store images in `raw/assets/`
- Reference in markdown: `![Description](raw/assets/image-name.jpg)`
- When processing sources with images, download them locally first

## Git Integration

- Commit changes after significant updates
- Use descriptive commit messages
- The wiki is version-controlled by default

## Quality Standards

1. **Accuracy**: Verify facts before adding to wiki
2. **Completeness**: Each page should be a comprehensive treatment of its subject
3. **Consistency**: Maintain consistent formatting and style
4. **Currency**: Update pages when new information arrives
5. **Clarity**: Write in clear, accessible language

## User Interaction Protocol

1. Always confirm before making significant changes
2. Present summaries of proposed updates for user review
3. Ask for guidance on emphasis and interpretation
4. Report progress at each step of workflows
5. Suggest next steps and research directions

---

*This schema evolves with the wiki. Update this document when new conventions or workflows are established.*