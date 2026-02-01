#!/usr/bin/env python3
"""
Clean up Markdown files for VitePress migration.
Usage: python3 cleanup.py <source-directory> <output-directory> [options]
Options:
  --fix-headings     Fix multiple H1 and skipped levels
  --convert-links    Convert wiki links [[...]] to standard links
  --convert-images   Convert embedded images ![[...]] to standard images
  --normalize-names  Normalize filenames (spaces to dashes, etc.)
  --all             Apply all fixes
"""

import sys
import os
import re
import shutil
from pathlib import Path


class MarkdownCleaner:
    def __init__(self, source_dir, output_dir):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.changes = []

    def clean(self, fix_headings=False, convert_links=False, convert_images=False, normalize_names=False):
        """Clean Markdown files and copy to output directory."""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)

        for md_file in self.source_dir.rglob('*.md'):
            relative_path = md_file.relative_to(self.source_dir)
            output_file = self.output_dir / relative_path
            output_file.parent.mkdir(parents=True, exist_ok=True)

            content = md_file.read_text(encoding='utf-8')
            original_content = content

            if convert_links:
                content = self._convert_wiki_links(content)

            if convert_images:
                content = self._convert_embedded_images(content)

            if fix_headings:
                content = self._fix_headings(content)

            if content != original_content:
                self.changes.append(str(relative_path))

            output_file.write_text(content, encoding='utf-8')

        if normalize_names:
            self._normalize_filenames()

        return self.changes

    def _convert_wiki_links(self, content):
        """Convert [[Wiki Link]] or [[Wiki Link|Text]] to [Text](/wiki-link)."""
        def replace_link(match):
            full = match.group(1)
            if '|' in full:
                link, text = full.split('|', 1)
            else:
                link = text = full
            # Convert to slug
            slug = link.lower().replace(' ', '-').replace('_', '-')
            return f'[{text}](/{slug})'

        return re.sub(r'\[\[([^\]]+)\]\]', replace_link, content)

    def _convert_embedded_images(self, content):
        """Convert ![[image.png]] to ![image](./image.png)."""
        def replace_image(match):
            path = match.group(1)
            alt = Path(path).stem
            return f'![{alt}](./{path})'

        return re.sub(r'!\[\[([^\]]+)\]\]', replace_image, content)

    def _fix_headings(self, content):
        """Fix multiple H1s and skipped heading levels."""
        lines = content.split('\n')
        result = []
        h1_found = False
        prev_level = 0

        for line in lines:
            # Check if it's a heading
            match = re.match(r'^(#{1,6})\s+(.*)$', line)
            if match:
                hashes, text = match.groups()
                level = len(hashes)

                # Handle multiple H1s
                if level == 1:
                    if h1_found:
                        # Convert subsequent H1 to H2
                        line = f'## {text}'
                        level = 2
                    else:
                        h1_found = True

                # Handle skipped levels
                if level > prev_level + 1 and prev_level > 0:
                    level = prev_level + 1
                    line = f'{"#" * level} {text}'

                prev_level = level

            result.append(line)

        return '\n'.join(result)

    def _normalize_filenames(self):
        """Normalize filenames: spaces to dashes, remove special chars."""
        for filepath in list(self.output_dir.rglob('*')):
            if filepath.is_file():
                new_name = self._normalize_name(filepath.name)
                if new_name != filepath.name:
                    new_path = filepath.parent / new_name
                    filepath.rename(new_path)

    def _normalize_name(self, name):
        """Normalize a single filename."""
        # Replace spaces with dashes
        name = name.replace(' ', '-')
        # Remove special characters except dash, underscore, dot
        name = re.sub(r'[^\w\-.]', '', name)
        # Remove leading numbers with dots
        name = re.sub(r'^\d+\.', '', name)
        return name.lower()


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    source_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isdir(source_dir):
        print(f"Error: '{source_dir}' is not a valid directory")
        sys.exit(1)

    options = sys.argv[3:]
    fix_all = '--all' in options

    cleaner = MarkdownCleaner(source_dir, output_dir)
    changes = cleaner.clean(
        fix_headings=fix_all or '--fix-headings' in options,
        convert_links=fix_all or '--convert-links' in options,
        convert_images=fix_all or '--convert-images' in options,
        normalize_names=fix_all or '--normalize-names' in options
    )

    print(f"Cleaned Markdown files copied to: {output_dir}")
    print(f"Files modified: {len(changes)}")
    if changes:
        print("\nModified files:")
        for f in changes:
            print(f"  - {f}")


if __name__ == '__main__':
    main()
