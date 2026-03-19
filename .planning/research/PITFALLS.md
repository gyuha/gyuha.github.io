# Domain Pitfalls

**Domain:** Claude Code Extensions
**Researched:** 2026-03-19

## Critical Pitfalls

Mistakes that cause rewrites or major issues.

### Pitfall 1: Assuming "Superpowers" Exists
**What goes wrong:** Searching for or attempting to install a "Superpowers" plugin
**Why it happens:** Confusion with the unrelated HTML5 game maker project (github.com/superpowers)
**Consequences:** Wasted time, dead-end searches, frustration
**Prevention:** Focus on the actual Skills and Plugins systems that exist
**Detection:** Web searches returning unrelated game development results

### Pitfall 2: Skill Priority Confusion
**What goes wrong:** Expecting Personal Skills to override Project Skills
**Why it happens:** Intuition that "my settings" should win
**Consequences:** Unexpected behavior, skill not triggering as expected
**Prevention:** Remember priority: Project → Plugin → Personal (Personal is lowest)
**Detection:** "Why isn't my skill running?" when project has same-named skill

### Pitfall 3: Missing Frontmatter
**What goes wrong:** SKILL.md files without YAML frontmatter
**Why it happens:** Creating markdown files without proper structure
**Consequences:** Skill not discovered by Claude
**Prevention:** Always include `---` delimited YAML with name and description
**Detection:** Skill doesn't appear in available skills list

## Moderate Pitfalls

### Pitfall 1: Overly Broad Skills
**What goes wrong:** Skills with vague descriptions like "help with coding"
**Why it happens:** Wanting a catch-all assistant
**Consequences:** Model invokes skill inappropriately, confusing results
**Prevention:** Use specific descriptions: "create conventional commit format git commits"
**Detection:** Skill triggers when it shouldn't

### Pitfall 2: Not Using allowed-tools
**What goes wrong:** Missing `allowed-tools` in frontmatter
**Why it happens:** Not reading documentation, copying incomplete examples
**Consequences:** Model may not have access to needed tools
**Prevention:** Explicitly list tools: `allowed-tools: Read, Write, Bash`
**Detection:** "I can't do that" errors during skill execution

### Pitfall 3: Confusing Commands vs Skills
**What goes wrong:** Creating user-invoked slash commands when model-invoked skills are needed
**Why it happens:** Not understanding the distinction
**Consequences:** User has to manually trigger; loses autonomous benefit
**Prevention:** Commands = user-invoked (`/command`), Skills = model-invoked (autonomous)
**Detection:** Having to manually run something that should be automatic

## Minor Pitfalls

### Pitfall 1: Skill File Naming
**What goes wrong:** Poor directory naming for skills
**Why it happens:** No clear convention documented
**Consequences:** Harder to identify skills, maintenance issues
**Prevention:** Use descriptive kebab-case: `~/.claude/skills/commit-message/SKILL.md`
**Detection:** Can't tell what a skill does from directory name

### Pitfall 2: Missing Documentation in Skills
**What goes wrong:** SKILL.md with only code, no explanation
**Why it happens:** Focusing on implementation over usability
**Consequences:** Hard to modify later, unclear purpose
**Prevention:** Include usage examples and explanation in skill body
**Detection:** Opening a skill you wrote and not remembering what it does

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Skills Development | Overlapping skill triggers | Clear, specific descriptions |
| Plugin Creation | Incorrect plugin.json format | Use official examples as template |
| MCP Integration | Assuming all tools work via MCP | Verify MCP server compatibility first |
| Distribution | Manual file sharing only | Use git for project skills, plugins for wider dist |
| Marketplace | Network errors on marketplace docs | Fall back to GitHub for distribution |

## Naming Conflict Prevention

```
Problem: Same skill name in multiple scopes

Resolution Priority:
1. Project Skills (.claude/skills/) ← Highest priority
2. Plugin Skills (plugins/)           ← Medium priority
3. Personal Skills (~/.claude/skills/) ← Lowest priority

Best Practice:
- Use project-specific prefixes for project skills
- Use plugin-specific prefixes for plugin skills
- Reserve personal skills for truly personal customizations
```

## Skill Discovery Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Missing frontmatter | Add YAML `---` block |
| Skill not found | Wrong directory | Verify `~/.claude/skills/` or `.claude/skills/` |
| Skill not found | Not named `SKILL.md` | Rename to exact filename |
| Wrong skill used | Priority confusion | Move to higher-priority scope |
| Skill outdated | Git not updated | Pull latest for project skills |

## Sources

- https://docs.anthropic.com/en/docs/claude-code/skills
- https://docs.anthropic.com/en/docs/claude-code/plugins
- https://github.com/anthropics/claude-code/tree/main/plugins
- https://github.com/superpowers (unrelated game project - source of confusion)
