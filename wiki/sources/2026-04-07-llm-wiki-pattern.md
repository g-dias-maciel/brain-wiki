---
title: LLM Wiki Pattern Document
type: source
created: 2026-04-07
updated: 2026-04-07
sources: [2026-04-07-llm-wiki-pattern.md]
tags: [llm, wiki, knowledge-management, system-design]
aliases: [llm-wiki-blueprint, knowledge-base-pattern]
---

# LLM Wiki Pattern Document

*Source: `raw/articles/2026-04-07-llm-wiki-pattern.md`*
*Ingested: 2026-04-07*

## Summary

This document describes the LLM Wiki pattern - a system for building persistent, compounding knowledge bases maintained by LLMs rather than using traditional RAG (Retrieval-Augmented Generation) approaches. The core innovation is having the LLM incrementally build and maintain a structured wiki that compounds knowledge over time.

## Core Idea

### Problem with Traditional RAG
- LLMs rediscover knowledge from scratch on every query
- No accumulation or synthesis across multiple documents
- Fragmented understanding requiring reassembly each time

### LLM Wiki Solution
- LLM builds and maintains a persistent wiki structure
- Knowledge is compiled once and kept current
- Cross-references, contradictions, and synthesis are pre-computed
- Wiki grows richer with each new source and query

### Human-LLM Division of Labor
- **Human**: Curates sources, directs analysis, asks questions, thinks strategically
- **LLM**: Summarizes, cross-references, files, maintains consistency, handles bookkeeping

## Architecture

### Three Layers
1. **Raw Sources**: Immutable source documents (articles, papers, notes)
2. **Wiki**: LLM-generated markdown files (summaries, entity pages, concepts)
3. **Schema**: Rules and workflows (CLAUDE.md) that guide the LLM

### Key Files
- **index.md**: Catalog of all wiki pages organized by category
- **log.md**: Chronological record of wiki operations
- **CLAUDE.md**: Schema defining conventions and workflows

## Operations

### 1. Ingest Workflow
When adding a new source:
1. Read and analyze the source
2. Discuss key takeaways with human
3. Create source summary page
4. Update relevant entity/concept pages
5. Update index.md
6. Append to log.md
7. Add cross-references

### 2. Query Workflow
When answering questions:
1. Search index.md for relevant pages
2. Read and synthesize from wiki pages
3. Generate answer with citations
4. Optionally create new output page if valuable
5. Update links and log

### 3. Lint Workflow
Periodic health checks:
1. Find contradictions between pages
2. Identify orphan pages (no inbound links)
3. Flag stale content needing updates
4. Suggest missing pages or connections
5. Propose research questions

## Applications

1. **Personal**: Goals, health, psychology, self-improvement tracking
2. **Research**: Deep topic exploration over months/years
3. **Reading**: Building companion wikis for books
4. **Business**: Internal wikis from meetings, documents, calls
5. **Various**: Competitive analysis, due diligence, trip planning, course notes

## Historical Context

Related to Vannevar Bush's **Memex (1945)** concept:
- Personal, curated knowledge store
- Associative trails between documents
- Private and actively curated
- Bush's unsolved problem: maintenance burden
- LLM solves the maintenance problem

## Why This Works

- **Maintenance Burden**: Humans abandon wikis due to bookkeeping overhead
- **LLM Advantage**: No boredom, forgetfulness; can update 15+ files in one pass
- **Near-Zero Cost**: Maintenance cost approaches zero with LLMs
- **Compounding Value**: Wiki improves with each interaction

## Implementation in This Vault

This Gabriel Brain vault implements the LLM Wiki pattern with customization for personal life organization:

### Customizations
- **Life Domains**: Finance, legal, business, health, personal, admin
- **Dashboard Pages**: Status overviews with key metrics
- **Timeline Pages**: Chronological views and projections
- **Integration**: Financial strategy, business operations, personal goals

### Current Status
- Schema defined in CLAUDE.md
- Directory structure created
- First sources ingested (this document + financial strategy)
- Initial wiki pages generated
- Index and log maintained

## Related Pages
- [[CLAUDE.md]] - The schema guiding this implementation
- [[Financial Dashboard]] - Example of applied pattern
- [[Margin Engine Strategy]] - Domain-specific knowledge organization

## Questions for Exploration
1. How to scale beyond hundreds of pages?
2. What search tools integrate best (qmd, etc.)?
3. How to handle conflicting information from sources?
4. What visualization tools complement the wiki (Obsidian graph, etc.)?
5. How to version and collaborate on the wiki?