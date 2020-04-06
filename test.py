#!/usr/bin/env python3
import os

from litex.data.cpu import picorv32

print("Found picorv32 @ version", picorv32.version_str, "(with data", picorv32.data_version_str, ")")
print()
print("Data is in", picorv32.data_location)
assert os.path.exists(picorv32.data_location)
print("Data is version", picorv32.data_version_str, picorv32.data_git_hash)
print("-"*75)
print(picorv32.data_git_msg)
print("-"*75)
print()
print("It contains:")
for root, dirs, files in os.walk(picorv32.data_location):
    dirs.sort()
    for f in sorted(files):
        path = os.path.relpath(os.path.join(root, f), picorv32.data_location)
        print(" -", path)
