# Feature Landscape

**Domain:** Claude Code Extensions
**Researched:** 2026-03-19

## Table Stakes

Features users expect from an extension system. Missing = system feels incomplete.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Model-invoked Skills | Autonomous behavior without user prompts | Low | Core differentiator of Claude Code |
| User-invoked Commands | Explicit slash command triggering | Low | Standard CLI pattern |
| Personal Skills | User-specific customizations | Low | Stored in `~/.claude/skills/` |
| Project Skills | Team-shared skills via git | Medium | Stored in `.claude/skills/` |
| Plugin Skills | Bundled extensions | Medium | Distributed with plugins |
| MCP Integration | External tool connections | High | Protocol for tool integrations |

## Differentiators

Features that set Claude Code apart. Not expected, but valued.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Model-Invoked Skills | Claude decides when to use capabilities autonomously | Low | Unlike traditional CLI tools |
| Three-tier Skill Storage | Personal, Project, Plugin levels | Medium | Flexible scoping and sharing |
| Plugin Bundles | Commands + agents + hooks + Skills + MCP in one package | High | Comprehensive extension model |
| Event Hooks | Trigger actions on specific events | Medium | Automate workflows |
| Agent SDK | Build custom specialized agents | High | For advanced use cases |

## Anti-Features

Features to explicitly NOT build.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| "Superpowers" plugin | Does not exist; name conflicts with unrelated game project | Use Skills/Plugins that actually exist |
| Central marketplace only | Not yet fully documented | Use GitHub for distribution |
| Complex dependency systems | Skills should be self-contained | Keep SKILL.md files independent |

## Feature Dependencies

```
Personal Skills → Project Skills (team sharing requires git)
Skills → Plugins (plugins can bundle skills)
MCP → Plugins (MCP configs typically in plugins)
Commands → Plugins (slash commands are plugin components)
```

## MVP Recommendation

Prioritize:
1. **Personal Skills** - Start with `~/.claude/skills/` for immediate value
2. **Project Skills** - Move to `.claude/skills/` for team collaboration
3. **Basic Plugin** - Create a simple plugin with one skill

Defer:
- **Complex MCP integrations**: Require more research
- **Custom agents**: Advanced use case, learn Skills first
- **Event hooks**: Understand core system before automating

## Skill Types Comparison

| Type | Scope | Storage | Version Control | Discovery |
|------|-------|---------|-----------------|------------|
| Personal | User-only | `~/.claude/skills/` | No (local) | Manual |
| Project | Project-specific | `.claude/skills/` | Yes (git) | Git-based |
| Plugin | Distributed | In plugin bundle | Yes (plugin repo) | Plugin catalog |

## Plugin Component Capabilities

| Component | Model-Invoked | User-Invoked | Purpose |
|-----------|---------------|--------------|---------|
| commands/ | No | Yes | Slash commands |
| agents/ | No | No (team lead) | Custom agents |
| skills/ | Yes | No | Agent Skills |
| hooks/ | No | Event-triggered | Automation |
| MCP | Yes | No | External tools |

## Sources

- https://docs.anthropic.com/en/docs/claude-code/skills
- https://docs.anthropic.com/en/docs/claude-code/plugins
- https://github.com/anthropics/claude-code/tree/main/plugins
