#!/usr/bin/env python3
"""
Delete every netid headshot from img/. Nothing else is touched.

A file is treated as a headshot only if its name (minus extension) matches a
netid that has appeared in the `netid` column of some version of some file
under _data/ at any point in this repo's git history. That means:

  - graduated members' photos are caught, even though they are long gone
    from the current CSVs
  - files that merely LOOK like netids (ein24.jpg, eid24.jpg) are kept,
    because they were never published as one
  - galleries, event graphics, logos and textures are kept regardless of
    whether any page currently references them

Run from the repo root.

    python3 purge_headshots.py          # dry run, deletes nothing
    python3 purge_headshots.py --apply  # delete

Restore before committing with:  git checkout HEAD -- img/
"""

import csv
import io
import os
import subprocess
import sys

IMG_DIR = "img"
DATA_DIR = "_data/"


def git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, errors="ignore"
    ).stdout


def historical_netids():
    """Every netid published in any revision of any file under _data/."""
    revisions = {}
    sha = None
    for line in git("log", "--all", "--format=%H", "--name-only", "--", DATA_DIR).splitlines():
        line = line.strip()
        if len(line) == 40 and all(c in "0123456789abcdef" for c in line):
            sha = line
        elif line.endswith(".csv") and sha:
            revisions.setdefault(line, set()).add(sha)

    netids, scanned = set(), 0
    for path, shas in revisions.items():
        for sha in shas:
            blob = git("show", f"{sha}:{path}")
            if not blob.strip():
                continue
            scanned += 1
            try:
                rows = list(csv.DictReader(io.StringIO(blob.lstrip("\ufeff"))))
            except csv.Error:
                continue
            for row in rows:
                for key, val in row.items():
                    if key and key.strip().lower() == "netid" and val and val.strip():
                        netids.add(val.strip().lower())
    return netids, scanned, len(revisions)


def main():
    apply = "--apply" in sys.argv

    if not os.path.isdir(IMG_DIR) or not os.path.isdir(".git"):
        sys.exit("error: run this from the repo root (needs img/ and .git/).")

    netids, scanned, nfiles = historical_netids()
    print(f"scanned {scanned} historical revisions of {nfiles} data files")
    print(f"-> {len(netids)} distinct netids ever published\n")

    if not netids:
        sys.exit("error: no netids found. Aborting rather than guessing.")

    delete, keep = [], []
    for entry in sorted(os.listdir(IMG_DIR)):
        full = os.path.join(IMG_DIR, entry)
        if not os.path.isfile(full):
            continue  # subdirectories left alone
        stem = os.path.splitext(entry)[0].lower()
        (delete if stem in netids else keep).append(entry)

    mb = lambda names: sum(os.path.getsize(os.path.join(IMG_DIR, n)) for n in names) / 1e6

    print(f"DELETE — netid headshots: {len(delete)} files, {mb(delete):.1f} MB")
    for n in delete:
        print(f"    {n}")

    print(f"\nKEEP — everything else: {len(keep)} files, {mb(keep):.1f} MB")
    for n in keep:
        print(f"    {n}")

    if not apply:
        print("\nDry run. Nothing deleted. Re-run with --apply to delete.")
        return

    for n in delete:
        os.remove(os.path.join(IMG_DIR, n))
    print(f"\nDeleted {len(delete)} files.")
    print("Undo before committing with:  git checkout HEAD -- img/")


if __name__ == "__main__":
    main()
