from cocotb_test.simulator import run
import pytest
import os

from telemetry import telemetryMark
pytestmark = telemetryMark()


def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)

@pytest.mark.telemetry_files(source('gray.vhd'))
def test_gray():
    run(vhdl_sources=[source("gray.vhd")], toplevel="gray", module="av2_cocotb" , testcase='tb_gray', toplevel_lang="vhdl")

@pytest.mark.telemetry_files(source('fullsub.vhd'))
def test_fullsub():
    run(vhdl_sources=[source("fullsub.vhd")], toplevel="fullsub", module="av2_cocotb" , testcase='tb_fullsub', toplevel_lang="vhdl")

if __name__ == "__main__":
    test_gray()
    test_fullsub()
