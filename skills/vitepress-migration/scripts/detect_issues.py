#!/usr/bin/env python3
"""
Detect issues in Markdown files before VitePress migration.
Usage: python3 detect_issues.py <source-directory>
"""

import sys
import os
import re
from pathlib import Path
from collections import defaultdict


class IssueDetector:
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir)
        self.issues = defaultdict(list)
        self.stats = {
            'total_files': 0,
            'files_with_issues': 0,
            'wiki_links': 0,
            'embedded_images': 0,
            'multiple_h1': 0,
            'skipped_levels': 0,
            'absolute_paths': 0,
            'empty_headings': 0
        }

    def scan(self):
        """Scan all Markdown files in source directory."""
        for md_file in self.source_dir.rglob('*.md'):
            self.stats['total_files'] += 1
            self._check_file(md_file)

        return self.issues, self.stats

    def _check_file(self, filepath):
        """Check a single Markdown file for issues."""
        content = filepath.read_text(encoding='utf-8')
        file_issues = []

        # Check for wiki links [[...]]
        wiki_links = re.findall(r'\[\[([^\]]+)\]\]', content)
        if wiki_links:
            self.stats['wiki_links'] += len(wiki_links)
            file_issues.append(f"Found {len(wiki_links)} wiki-style link(s): {wiki_links[:3]}")

        # Check for embedded images ![[...]]
        embedded_images = re.findall(r'!\[\[([^\]]+)\]\]', content)
        if embedded_images:
            self.stats['embedded_images'] += len(embedded_images)
            file_issues.append(f"Found {len(embedded_images)} embedded image(s): {embedded_images[:3]}")

        # Check for multiple H1 headings
        h1_count = len(re.findall(r'^# [^#]', content, re.MULTILINE))
        if h1_count > 1:
            self.stats['multiple_h1'] += 1
            file_issues.append(f"Found {h1_count} H1 headings (should be exactly 1)")

        # Check for skipped heading levels
        headings = re.findall(r'^(#{1,6}) ', content, re.MULTILINE)
        if headings:
            levels = [len(h) for h in headings]
            for i in range(1, len(levels)):
                if levels[i] > levels[i-1] + 1:
                    self.stats['skipped_levels'] += 1
                    file_issues.append(f"Skipped heading level: H{levels[i-1]} -> H{levels[i]}")
                    break

        # Check for absolute local file paths
        absolute_paths = re.findall(r'\[([^\]]+)\]\((/[a-zA-Z]:?[^)]+)\)', content)
        if absolute_paths:
            self.stats['absolute_paths'] += len(absolute_paths)
            file_issues.append(f"Found {len(absolute_paths)} absolute path(s)")

        # Check for empty headings
        empty_headings = re.findall(r'^#{1,6}\s*$', content, re.MULTILINE)
        if empty_headings:
            self.stats['empty_headings'] += len(empty_headings)
            file_issues.append(f"Found {len(empty_headings)} empty heading(s)")

        if file_issues:
            self.stats['files_with_issues'] += 1
            self.issues[str(filepath.relative_to(self.source_dir))] = file_issues

    def print_report(self):
        """Print detection report."""
        print("=" * 60)
        print("VITEPRESS MIGRATION - ISSUE DETECTION REPORT")
        print("=" * 60)
        print(f"\nSource Directory: {self.source_dir}")
        print(f"\n--- Statistics ---")
        print(f"Total Markdown Files: {self.stats['total_files']}")
        print(f"Files with Issues: {self.stats['files_with_issues']}")
        print(f"\n--- Issue Counts ---")
        print(f"Wiki-style Links [[...]]: {self.stats['wiki_links']}")
        print(f"Embedded Images ![[...]]: {self.stats['embedded_images']}")
        print(f"Multiple H1 Headings: {self.stats['multiple_h1']}")
        print(f"Skipped Heading Levels: {self.stats['skipped_levels']}")
        print(f"Absolute File Paths: {self.stats['absolute_paths']}")
        print(f"Empty Headings: {self.stats['empty_headings']}")

        if self.issues:
            print(f"\n--- Detailed Issues ---")
            for filepath, issues in sorted(self.issues.items()):
                print(f"\n📄 {filepath}")
                for issue in issues:
                    print(f"   ⚠️  {issue}")
        else:
            print("\n✅ No issues found! Ready for migration.")

        print("\n" + "=" * 60)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 detect_issues.py <source-directory>")
        sys.exit(1)

    source_dir = sys.argv[1]

    if not os.path.isdir(source_dir):
        print(f"Error: '{source_dir}' is not a valid directory")
        sys.exit(1)

    detector = IssueDetector(source_dir)
    detector.scan()
    detector.print_report()


if __name__ == '__main__':
    main()
