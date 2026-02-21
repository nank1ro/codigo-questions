#!/usr/bin/env python3
"""
Exercise Translation Script for Codigo Questions

Translates all exercises from English to multiple locales using Claude API.
Handles all exercise types (1-4), data.json files, and templates.
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Optional
from anthropic import Anthropic

# Configuration
REPO_ROOT = Path(__file__).parent
SOURCE_DIR = REPO_ROOT / "en"
TARGET_LOCALES = ["de", "es", "fr", "pl", "pt", "ru"]

# Language names for translation context
LANGUAGE_NAMES = {
    "de": "German",
    "es": "Spanish",
    "fr": "French",
    "pl": "Polish",
    "pt": "Portuguese",
    "ru": "Russian",
}

# Section tags that must be preserved
SECTION_TAGS = [
    "# --description--",
    "# --instructions--",
    "# --seed--",
    "# --before-seed--",
    "# --solutions--",
    "# --before-asserts--",
    "# --asserts--",
    "# --after-asserts--",
    "# --output--",
    "# --answers--",
]

# Regex patterns for content extraction
FRONTMATTER_PATTERN = re.compile(r"^---$(.*?)^---$", re.MULTILINE | re.DOTALL)
SECTION_PATTERN = re.compile(r"^# --([a-z-]+--)$", re.MULTILINE)
CODE_BLOCK_PATTERN = re.compile(r"^```(\w*)\n(.*?)^```$", re.MULTILINE | re.DOTALL)


class ExerciseTranslator:
    """Translates exercises from English to target locales."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize translator with Anthropic API key."""
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable must be set or passed as argument"
            )
        self.client = Anthropic(api_key=self.api_key)

    def translate_text(
        self, text: str, target_locale: str, context: str = ""
    ) -> str:
        """
        Translate text to target locale using Claude API.

        Args:
            text: Text to translate
            target_locale: Target locale code (e.g., 'es', 'de')
            context: Additional context for translation

        Returns:
            Translated text
        """
        if not text or not text.strip():
            return text

        language_name = LANGUAGE_NAMES[target_locale]

        prompt = f"""Translate the following content to {language_name} ({target_locale}).

Context: {context}

Important rules:
1. Translate ALL user-facing text including descriptions, instructions, and comments
2. Translate variable names in code examples (e.g., 'sum' → German 'summe', 'count' → Spanish 'conteo')
3. DO NOT translate: programming keywords (if, else, for, while, def, function, etc.), function/class declarations, error tags like '--err-t1--', section tags like '# --description--'
4. Preserve ALL code structure and syntax exactly
5. Keep code formatting and indentation identical
6. For data.json files: only translate 'title' and 'description' field values, not keys

Content to translate:
{text}

Return ONLY the translated content without any explanation."""

        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=8192,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text.strip()
        except Exception as e:
            print(f"Error translating text: {e}", file=sys.stderr)
            return text

    def translate_exercise_file(self, source_file: Path, target_file: Path) -> bool:
        """
        Translate a single exercise file.

        Args:
            source_file: Source exercise file path
            target_file: Target exercise file path

        Returns:
            True if successful, False otherwise
        """
        # Read source content
        content = source_file.read_text(encoding="utf-8")
        target_locale = target_file.parent.parent.parent.name

        # Extract frontmatter
        frontmatter_match = FRONTMATTER_PATTERN.search(content)
        if not frontmatter_match:
            print(f"Warning: No frontmatter found in {source_file}", file=sys.stderr)
            return False

        frontmatter = frontmatter_match.group(0)
        remaining_content = content[frontmatter_match.end() :]

        # Build translated content
        translated_parts = [frontmatter]
        current_section = None
        current_content = []
        in_code_block = False
        code_block_lang = None

        for line in remaining_content.splitlines(keepends=True):
            stripped = line.strip()

            # Check for section tags
            if stripped in SECTION_TAGS:
                # Save previous section
                if current_section:
                    section_text = "".join(current_content).strip()
                    if section_text:
                        translated = self._translate_section(
                            section_text, current_section, target_locale
                        )
                        translated_parts.append(translated)
                    current_content = []

                current_section = stripped
                translated_parts.append(line)
                in_code_block = False
                continue

            # Track code blocks
            if stripped.startswith("```"):
                if not in_code_block:
                    in_code_block = True
                    code_block_lang = stripped[3:].strip()
                else:
                    in_code_block = False
                    code_block_lang = None
                current_content.append(line)
                continue

            current_content.append(line)

        # Don't forget the last section
        if current_section and current_content:
            section_text = "".join(current_content).strip()
            if section_text:
                translated = self._translate_section(
                    section_text, current_section, target_locale
                )
                translated_parts.append(translated)

        # Ensure target directory exists
        target_file.parent.mkdir(parents=True, exist_ok=True)

        # Write translated content
        target_file.write_text("".join(translated_parts), encoding="utf-8")
        return True

    def _translate_section(self, text: str, section: str, locale: str) -> str:
        """Translate a section based on its type."""
        section_name = section.replace("# --", "").replace("--", "")

        # Sections that don't need translation
        if section_name in ["before-seed", "before-asserts", "after-asserts"]:
            # Check if it contains test framework boilerplate
            if any(
                keyword in text.lower()
                for keyword in [
                    "unittest",
                    "xctestcase",
                    "do not edit",
                    "codigo tests",
                    "test case",
                ]
            ):
                return text

        # Code sections get special handling
        if section_name in ["seed", "solutions", "asserts"]:
            return self._translate_code_section(text, locale, section_name)

        # Text sections get full translation
        if section_name in ["description", "instructions", "output"]:
            return self.translate_text(text, locale, f"Exercise {section_name}")

        # Answer sections
        if section_name == "answers":
            return self._translate_answers(text, locale)

        return text

    def _translate_code_section(self, code: str, locale: str, section_type: str) -> str:
        """Translate code comments and variable names."""
        # Split into lines for processing
        lines = code.splitlines()
        translated_lines = []

        for line in lines:
            translated_lines.append(self._translate_code_line(line, locale))

        # Translate the whole block context-aware
        full_code = "\n".join(translated_lines)
        return self.translate_text(
            full_code, locale, f"Code section ({section_type}) - translate variables and comments"
        )

    def _translate_code_line(self, line: str, locale: str) -> str:
        """Translate a single line of code."""
        # Preserve indentation
        indent = len(line) - len(line.lstrip())
        stripped = line.lstrip()

        # Skip empty lines
        if not stripped:
            return line

        # Detect and translate comments
        if stripped.startswith("#"):
            comment_content = stripped[1:].strip()
            translated = self.translate_text(comment_content, locale, "Code comment")
            return " " * indent + f"# {translated}"

        return line

    def _translate_answers(self, answers: str, locale: str) -> str:
        """Translate answer options."""
        return self.translate_text(answers, locale, "Answer options")

    def translate_data_json(self, source_file: Path, target_file: Path) -> bool:
        """Translate a data.json file."""
        data = json.loads(source_file.read_text(encoding="utf-8"))
        locale = target_file.parent.parent.parent.name

        translated_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                translated_data[key] = {
                    "order": value.get("order"),
                    "title": self.translate_text(
                        value.get("title", ""), locale, "Argument title"
                    ),
                    "description": self.translate_text(
                        value.get("description", ""), locale, "Argument description"
                    ),
                }
            else:
                translated_data[key] = value

        target_file.parent.mkdir(parents=True, exist_ok=True)
        with target_file.open("w", encoding="utf-8") as f:
            json.dump(translated_data, f, ensure_ascii=False, indent=2)
        return True

    def translate_template(self, source_file: Path, target_file: Path) -> bool:
        """Translate a template file."""
        content = source_file.read_text(encoding="utf-8")
        locale = target_file.parent.parent.parent.name

        # Extract sections and translate
        translated = self.translate_text(content, locale, "Exercise template")

        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(translated, encoding="utf-8")
        return True

    def translate_locale(
        self, locale: str, programming_language: Optional[str] = None
    ) -> None:
        """
        Translate all content for a specific locale.

        Args:
            locale: Target locale code (e.g., 'es', 'de')
            programming_language: Specific programming language to translate, or None for all
        """
        print(f"\n{'='*60}")
        print(f"Translating to {LANGUAGE_NAMES[locale]} ({locale})...")
        print(f"{'='*60}\n")

        source_base = SOURCE_DIR
        target_base = REPO_ROOT / locale

        # Determine which programming languages to process
        if programming_language:
            prog_langs = [programming_language]
        else:
            prog_langs = [
                d.name for d in source_base.iterdir() if d.is_dir() and not d.name.startswith("_")
            ]

        for prog_lang in prog_langs:
            print(f"\n  Processing {prog_lang}...")
            source_lang_dir = source_base / prog_lang
            target_lang_dir = target_base / prog_lang

            if not source_lang_dir.exists():
                print(f"    Warning: {source_lang_dir} does not exist, skipping")
                continue

            # Translate data.json at language level
            data_json = source_lang_dir / "data.json"
            if data_json.exists():
                print(f"    Translating data.json...")
                self.translate_data_json(data_json, target_lang_dir / "data.json")

            # Process each argument directory
            for item in source_lang_dir.iterdir():
                if not item.is_dir():
                    continue

                if item.name == "challenges":
                    # Handle challenges separately
                    self._translate_challenges(
                        item, target_lang_dir / "challenges", locale
                    )
                    continue

                # Regular argument directory
                print(f"    Translating {item.name}...")
                target_arg_dir = target_lang_dir / item.name

                # Translate data.json in argument
                arg_data_json = item / "data.json"
                if arg_data_json.exists():
                    self.translate_data_json(
                        arg_data_json, target_arg_dir / "data.json"
                    )

                # Translate exercise files
                for exercise_file in sorted(item.glob("*.md")):
                    if exercise_file.name.startswith("_"):
                        continue  # Skip _theory.md (auto-generated)

                    target_exercise = target_arg_dir / exercise_file.name
                    print(f"      {exercise_file.name}...", end=" ", flush=True)
                    success = self.translate_exercise_file(exercise_file, target_exercise)
                    print("✓" if success else "✗")

    def _translate_challenges(
        self, source_dir: Path, target_dir: Path, locale: str
    ) -> None:
        """Translate all challenges."""
        print(f"    Translating challenges...")

        # Translate challenges data.json
        challenges_data = source_dir / "data.json"
        if challenges_data.exists():
            self.translate_data_json(challenges_data, target_dir / "data.json")

        # Translate each challenge file
        target_dir.mkdir(parents=True, exist_ok=True)
        for challenge_file in sorted(source_dir.glob("*.md")):
            target_challenge = target_dir / challenge_file.name
            print(f"      {challenge_file.name}...", end=" ", flush=True)
            success = self.translate_exercise_file(challenge_file, target_challenge)
            print("✓" if success else "✗")

    def translate_templates(self, locale: str) -> None:
        """Translate all template files for a locale."""
        print(f"\n  Translating templates for {locale}...")

        source_templates = REPO_ROOT / "translations" / "en" / "templates"
        target_templates = REPO_ROOT / "translations" / locale / "templates"

        target_templates.mkdir(parents=True, exist_ok=True)

        for template_file in sorted(source_templates.glob("*.md")):
            target_template = target_templates / template_file.name
            print(f"    {template_file.name}...", end=" ", flush=True)
            success = self.translate_template(template_file, target_template)
            print("✓" if success else "✗")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Translate Codigo exercises to multiple locales"
    )
    parser.add_argument(
        "--locale",
        choices=TARGET_LOCALES,
        help="Specific locale to translate (default: all)",
    )
    parser.add_argument(
        "--language",
        help="Specific programming language to translate (e.g., 'python')",
    )
    parser.add_argument(
        "--templates-only",
        action="store_true",
        help="Only translate templates, not exercises",
    )
    parser.add_argument(
        "--api-key",
        help="Anthropic API key (default: from ANTHROPIC_API_KEY env var)",
    )

    args = parser.parse_args()

    # Determine which locales to process
    locales = [args.locale] if args.locale else TARGET_LOCALES

    # Initialize translator
    translator = ExerciseTranslator(api_key=args.api_key)

    # Process each locale
    for locale in locales:
        if args.templates_only:
            translator.translate_templates(locale)
        else:
            # Translate templates first
            translator.translate_templates(locale)
            # Then translate exercises
            translator.translate_locale(locale, args.language)

    print(f"\n{'='*60}")
    print("Translation complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
