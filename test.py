#!/usr/bin/env python3
import os

from litex.data.cpu import picorv32

print("Found picorv32 @ version", picorv32.version_str, "("+picorv32.git_hash+")")
print("Data is in", picorv32.data_location)
assert os.path.exists(picorv32.data_location)
print("It contains:\n -", end=" ")
print("\n - ".join(os.listdir(picorv32.data_location)))