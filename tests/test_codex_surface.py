"""Validate the ChatGPT/Codex skill surface shipped with the repository."""

from __future__ import annotations

from conftest import ROOT, parse_frontmatter

CODEX_SKILLS = ROOT / ".agents" / "skills"
ASSAY_SKILL = CODEX_SKILLS / "source-command-assay" / "SKILL.md"


def test_codex_assay_skill_is_shipped():
    assert ASSAY_SKILL.is_file(), "ChatGPT/Codex assay skill is missing"
    frontmatter = parse_frontmatter(ASSAY_SKILL.read_text())
    assert frontmatter == {
        "name": "source-command-assay",
        "description": "Migrated source command `assay`",
    }
    assert "# /assay — Master Orchestrator" in ASSAY_SKILL.read_text()


def test_codex_supporting_skills_have_frontmatter():
    skill_files = sorted(CODEX_SKILLS.glob("*/SKILL.md"))
    assert skill_files, "ChatGPT/Codex supporting skills are missing"
    for skill_file in skill_files:
        frontmatter = parse_frontmatter(skill_file.read_text())
        assert frontmatter and frontmatter.get("name"), f"missing frontmatter: {skill_file}"
        assert frontmatter.get("description"), f"missing description: {skill_file}"
