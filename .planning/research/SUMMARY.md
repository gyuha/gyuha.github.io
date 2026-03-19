# Research Summary: Superpowers for Claude Code

**Domain:** Claude Code Extensions
**Researched:** 2026-03-19
**Overall confidence:** HIGH

## Executive Summary

**Critical Finding:** "Superpowers" does NOT exist as a Claude Code plugin, marketplace, or feature. Extensive web searches, GitHub repository searches, and documentation reviews found no connection between "Superpowers" and Claude Code.

The GitHub organization "superpowers" (https://github.com/superpowers) hosts an HTML5 2D+3D game maker project that is completely unrelated to Anthropic's Claude Code CLI tool.

However, Claude Code DOES have a robust extension ecosystem that may be what was intended:
- **Agent Skills**: Model-invoked capabilities for autonomous task execution
- **Plugins**: Extension bundles with custom commands, agents, hooks, Skills, and MCP servers
- **Plugin Marketplaces**: Catalogs for plugin distribution (official documentation had network errors during research)

## Key Findings

**Stack:** Claude Code CLI with Skills and Plugins extension systems
**Architecture:** Personal Skills (~/.claude/skills/), Project Skills (.claude/skills/), Plugin Skills (bundled)
**Critical finding:** "Superpowers" plugin does not exist; confusion may stem from the unrelated GitHub game project

## Implications for Roadmap

Since "Superpowers" does not exist as a Claude Code feature, this research documents the ACTUAL extension capabilities:

1. **Agent Skills** - Model-invoked capabilities
   - Addresses: Extending Claude's autonomous behavior
   - Three types: Personal, Project, Plugin-based

2. **Plugins** - Full extension bundles
   - Addresses: Custom commands, agents, hooks, Skills, MCP servers
   - Official plugins available (agent-sdk-dev, code-review, feature-dev, etc.)

3. **Plugin Marketplaces** - Distribution catalogs
   - Addresses: Sharing and discovering plugins
   - Documentation had network errors; may need phase-specific research

**Phase ordering rationale:**
- Understand Skills first (simpler, single-file)
- Then Plugins (more complex, multi-component)
- Finally Marketplace distribution

**Research flags for phases:**
- Phase 1 (Skills): Standard patterns, official docs available
- Phase 2 (Plugins): Official examples in GitHub, well-documented
- Phase 3 (Marketplaces): Documentation had network errors, needs deeper research

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack (Skills/Plugins exist) | HIGH | Official documentation verified |
| Features (what they do) | HIGH | Comprehensive docs available |
| "Superpowers" existence | HIGH | Confirmed DOES NOT exist via multiple sources |
| Pitfalls | MEDIUM | Limited by marketplace documentation network errors |

## Gaps to Address

- Plugin Marketplace documentation had network errors (500 error)
- Marketplace features and usage patterns need phase-specific research
- Clarification needed: Was "Superpowers" a hypothetical feature or confusion with the game project?
