#!/usr/bin/env python3
"""
Helper script to apply batch translations to LaTeX files.
Reads a translation map file and applies replacements to a target file.
"""
import sys
import re

def apply_translations(source_file, trans_file, output_file):
    """Apply translations from trans_file to source_file, write to output_file."""
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    with open(trans_file, 'r', encoding='utf-8') as f:
        trans_content = f.read()

    # Parse translation pairs separated by ===SEPARATOR===
    pairs = trans_content.split('===SEPARATOR===')

    for pair in pairs:
        pair = pair.strip()
        if not pair or '===TRANSLATION===' not in pair:
            continue
        parts = pair.split('===TRANSLATION===')
        if len(parts) != 2:
            continue
        old_text = parts[0].strip()
        new_text = parts[1].strip()
        if old_text and new_text and old_text in content:
            content = content.replace(old_text, new_text, 1)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <source> <translations> <output>")
        sys.exit(1)
    apply_translations(sys.argv[1], sys.argv[2], sys.argv[3])
