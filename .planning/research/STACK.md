# Technology Stack

**Project:** Claude Code Extension Ecosystem (Skills & Plugins)
**Researched:** 2026-03-19

## Recommended Stack

### Core Framework
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| Claude Code CLI | Latest | Terminal-based agentic coding tool | Official Anthropic tool for AI-assisted development |
| Agent Skills | Built-in | Model-invoked capabilities | Extend Claude's autonomous behavior without user prompts |
| Plugins | Built-in | Extension bundles | Full extensibility with commands, agents, hooks, Skills, MCP |

### Skill Structure
| Component | Format | Purpose | Location |
|-----------|--------|---------|----------|
| SKILL.md | YAML + Markdown | Skill definition and instructions | `~/.claude/skills/` (Personal), `.claude/skills/` (Project), plugins (Plugin) |
| Frontmatter | YAML | Metadata (name, description, allowed-tools) | Required in every SKILL.md |
| Body | Markdown | Instructions for the model | Free-form instructions |

### Plugin Structure
| Component | Purpose | Location |
|-----------|---------|----------|
| `.claude-plugin/plugin.json` | Plugin metadata | Required |
| `commands/` | Custom slash commands | User-invoked |
| `agents/` | Custom agents | Specialized behaviors |
| `skills/` | Agent Skills | Model-invoked |
| `hooks/` | Event handlers | Triggered by events |
| `mcp-servers.json` | MCP server configs | External tool integrations |

### File System Locations
| Type | Path | Scope | Git Status |
|------|------|-------|------------|
| Personal Skills | `~/.claude/skills/*/SKILL.md` | User-only | Not tracked |
| Project Skills | `.claude/skills/*/SKILL.md` | Project-specific | Tracked in git |
| Plugin Skills | `plugins/*/.claude-plugin/` | Plugin-installed | Tracked in plugin repo |

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Extension Method | Agent Skills | Custom prompts only | Skills are reusable, discoverable, and can be shared |
| Skill Storage | Project Skills | Personal Skills only | Project skills enable team collaboration via git |
| Distribution | Plugins | Manual copy-paste | Plugins bundle multiple extensions together |

## Official Plugins Available

Source: https://github.com/anthropics/claude-code/tree/main/plugins

| Plugin | Purpose |
|--------|---------|
| agent-sdk-dev | Agent SDK development |
| claude-opus-4-5-migration | Migration from Opus 4.5 |
| code-review | Code review assistance |
| commit-commands | Git commit workflows |
| feature-dev | Feature development |
| frontend-design | Frontend design assistance |
| hookify | Hook creation |
| learning-output-style | Style learning |
| plugin-dev | Plugin development |
| pr-review-toolkit | PR review workflows |
| ralph-wiggum | Character-based assistant |
| security-guidance | Security best practices |

## Installation

```bash
# No installation required for Skills - they're built into Claude Code
# Simply create SKILL.md files in the appropriate directory

# Plugin installation (example - official plugin location)
git clone https://github.com/anthropics/claude-code.git
# Plugins are in the plugins/ subdirectory
```

## Sources

- https://docs.anthropic.com/en/docs/claude-code/overview
- https://docs.anthropic.com/en/docs/claude-code/skills
- https://docs.anthropic.com/en/docs/claude-code/plugins
- https://github.com/anthropics/claude-code/tree/main/plugins
