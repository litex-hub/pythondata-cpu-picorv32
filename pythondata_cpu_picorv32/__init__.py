import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post169"
version_tuple = (1, 0, 169)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post169")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post52"
data_version_tuple = (1, 0, 52)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post52")
except ImportError:
    pass
data_git_hash = "f00a88c36eaab478b64ee27d8162e421049bcc66"
data_git_describe = "v1.0-52-gf00a88c"
data_git_msg = """\
commit f00a88c36eaab478b64ee27d8162e421049bcc66
Merge: 1d9f5b7 e8dbd9a
Author: Claire Xen <claire@clairexen.net>
Date:   Mon Jan 3 16:03:13 2022 +0100

    Merge pull request #209 from YosysHQ/micko/cleanups
    
    Cleanups

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_picorv32."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_picorv32".format(f))
    return fn
