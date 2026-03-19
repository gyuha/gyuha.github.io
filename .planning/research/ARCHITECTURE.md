# Architecture Patterns

**Domain:** Claude Code Extensions
**Researched:** 2026-03-19

## Recommended Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Claude Code CLI                        │
├─────────────────────────────────────────────────────────────┤
│  User Input ( slash commands | conversation | files )       │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Skills Resolution Layer                  │
├─────────────────────────────────────────────────────────────┤
│  Priority: Project Skills → Plugin Skills → Personal Skills │
│  Discovery: Pattern matching on SKILL.md frontmatter        │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Model Invocation Layer                    │
├─────────────────────────────────────────────────────────────┤
│  Claude decides: "Should I use a skill for this task?"      │
│  If yes: Load SKILL.md, follow instructions                 │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Tool Execution Layer                      │
├─────────────────────────────────────────────────────────────┤
│  Allowed Tools: Read, Write, Edit, Bash, Grep, Glob, etc.   │
│  MCP Servers: External tool integrations                    │
└─────────────────────────────────────────────────────────────┘
```

### Component Boundaries

| Component | Responsibility | Communicates With |
|-----------|---------------|-------------------|
| Personal Skills | User-specific custom behaviors | Model only |
| Project Skills | Team-shared capabilities | Model, git |
| Plugin Skills | Distributed extensions | Model, plugin system |
| Commands | User-invoked slash commands | User, CLI |
| Agents | Specialized autonomous workflows | Team lead, tasks |
| Hooks | Event-driven automation | Event system |
| MCP | External tool connections | External services |

### Data Flow

```
User Prompt → Claude Code
    ↓
Skills Resolution (check Project → Plugin → Personal)
    ↓
Model Decision (should I use a skill?)
    ↓
[If Yes] Load SKILL.md instructions
    ↓
Follow skill instructions with allowed tools
    ↓
Return result to user
```

## Patterns to Follow

### Pattern 1: Basic Skill Structure
**What:** Single-file extension with YAML frontmatter
**When:** Creating reusable behaviors or workflows
**Example:**
```yaml
---
name: commit
description: Create git commits with conventional commit format
allowed-tools: Bash, Grep, Read
---

When the user asks to commit changes:
1. Check git status
2. Stage files
3. Create commit with conventional commit format
4. Show the commit result
```

### Pattern 2: Three-Tier Skill Storage
**What:** Personal → Project → Plugin priority
**When:** Managing skill lifecycle and sharing
**Example:**
```
~/.claude/skills/commit/SKILL.md           # User's personal version
.claude/skills/commit/SKILL.md             # Team's project version
plugins/commit-plugin/skills/commit/       # Plugin distributed version

Resolution: Project wins, then Plugin, then Personal
```

### Pattern 3: Plugin Bundle
**What:** Multi-component extension package
**When:** Distributing complex integrations
**Example:**
```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Metadata
├── commands/
│   └── my-command.sh        # User-invoked
├── agents/
│   └── my-agent.md          # Custom agent
├── skills/
│   └── my-skill/
│       └── SKILL.md         # Model-invoked
├── hooks/
│   └── pre-commit.sh        # Event-triggered
└── mcp-servers.json         # External tools
```

## Anti-Patterns to Avoid

### Anti-Pattern 1: Overlapping Skills
**What:** Multiple skills with similar purposes
**Why bad:** Conflicts, unpredictable behavior
**Instead:** Consolidate into one well-designed skill with clear triggers

### Anti-Pattern 2: Giant SKILL.md Files
**What:** Single skill trying to do everything
**Why bad:** Hard to maintain, model may lose focus
**Instead:** Break into focused, single-purpose skills

### Anti-Pattern 3: Hard-Coded Paths
**What:** Skills that only work in specific directories
**Why bad:** Not portable, breaks across projects
**Instead:** Use relative paths and environment-aware patterns

## Scalability Considerations

| Concern | At 10 skills | At 100 skills | At 1000 skills |
|---------|--------------|---------------|----------------|
| Skill Discovery | Manual listing | Project-level | Plugin marketplace needed |
| Naming Conflicts | Easy to avoid | Possible | Likely without namespacing |
| Performance | Negligible | Minor impact | May need lazy loading |
| Maintenance | Trivial | Manageable | Requires categorization |

## Skill Invocation Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   User      │───▶│  Claude     │───▶│   Skills    │
│  Request    │    │   Code      │    │  Resolution │
└─────────────┘    └─────────────┘    └─────────────┘
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    ▼                         ▼                         ▼
              ┌─────────────┐          ┌─────────────┐          ┌─────────────┐
              │   Project   │          │   Plugin    │          │   Personal  │
              │   Skills    │          │   Skills    │          │   Skills    │
              └─────────────┘          └─────────────┘          └─────────────┘
                    │                         │                         │
                    └─────────────────────────┼─────────────────────────┘
                                              ▼
                                      ┌─────────────┐
                                      │   Selected  │
                                      │   SKILL.md  │
                                      └─────────────┘
                                              │
                                              ▼
                                      ┌─────────────┐
                                      │   Model     │
                                      │  Execution  │
                                      └─────────────┘
```

## Sources

- https://docs.anthropic.com/en/docs/claude-code/skills
- https://docs.anthropic.com/en/docs/claude-code/plugins
- https://github.com/anthropics/claude-code/tree/main/plugins
