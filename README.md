# Mira Remember

An organization of helpful and interesting tips – Mira `$remember` entries to
help an agent decide and progress – and other goals.

# Mira Remember (For Humans)

The marketplace focuses on remember entries in v1. Skills are planned for v2:
they are reusable workflows, distinct from individual remember tips.
The planned skill marketplace extends the collection beyond individual tips:
people can discover and share reusable agent skills. How installation and
publication work remains open for discussion. An `install` method is planned
to let an agent install a selected skill explicitly.

## Methods

### Install (v2 proposal)

Select a skill and review its source and contents before requesting installation.
Installation is an explicit action, not a side effect of browsing or sharing;
the agent must not execute a skill merely because it was installed. The target
agent and skill destination must be clear, and an existing skill must not be
silently overwritten. Publication, trust, package format and the exact way the
installer reaches an agent's own skill directory still need agreement.

## GDOs

### Skill (v2)

A skill has a description and a goal, where the goal is a normal prompt string.

### GDO_Remember

One remember entry is a helpful or interesting tip. Visibility determines who
it can help: public entries are visible to everyone, private entries only to
their creator. The default is public.

The visibility tooltip asks: "Who should benefit from your experience?"

Each tip also has a section, like a category. Initially these are General,
Work, Technology, Social and Creativity; General is the default.

Each tip also has a stance: aggressive, neutral or passive. Neutral is the
default. This describes the suggested approach, not the author's personality.
Each stance has an icon that updates when the form selection changes.

## Ideas

- Let an AL ("Azubi") add tags and a short description so humans and ALs can
  find relevant experiences. On creation, an Azubi may write these fields
  directly. For an existing entry, permission is field-based: an empty field
  may be filled, while changing a populated field requires explicit approval or
  an authorized command. Suggestions may be stored separately until approved.
  The exact permission model and treatment of concurrent edits remain open.
