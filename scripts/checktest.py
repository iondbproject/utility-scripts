#!/usr/bin/python

import argparse
import re
import os

test_files = []
for root, dirnames, filenames in os.walk("src"):
    for filename in filenames:
        if re.search(r"test_.*\.c(?:pp)?", filename):
           test_files.append(os.path.join(root, filename))

for filename in test_files:
    with open(filename, "r") as f:
        contents = f.read()

        test_defns = re.findall(r"void\n(.*)\(\n\s*planck_unit_test_t \*.*?\n\)", contents)
        if not test_defns:
            print("Note: {} didn't have any valid test defns".format(filename))
            continue
        
        suite_adds = re.findall(r"PLANCK_UNIT_ADD_TO_SUITE\(.*?, (.*?)\);", contents)
        if not suite_adds:
            print("Note: {} didn't have any valid suite defns".format(filename))
            continue

        defn_set = set(test_defns)
        suite_set = set(suite_adds)
        missing_set = defn_set - suite_set

        print("[{}]".format(filename))
        for missing in missing_set:
            print("\t{}".format(missing))
