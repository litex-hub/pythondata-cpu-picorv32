import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"
git_hash = "e308982e18fc952a8d446ddb7ea8b70433a998c2"
git_describe = "v1.0-23-ge308982"
version_str = "1.0.post23"
version_tuple = (1, 0)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post23")
except ImportError:
    pass
