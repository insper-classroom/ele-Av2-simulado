# Adapted from https://github.com/cocotb/cocotb/blob/master/examples/doc_examples/quickstart/test_my_design.py

import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def tb_gray(dut):

    inB =   [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
    outG =  [0b000, 0b001, 0b011, 0b010, 0b110, 0b111, 0b101, 0b100]


    for i in range(len(inB)):
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.g.value == outG[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:03b}".format(outG[i]) + " Obtained value: " + str(dut.g.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")
        
        
@cocotb.test()
async def tb_fullsub(dut):

    inA = [0, 0, 0, 0, 1, 1, 1, 1]
    inB = [0, 0, 1, 1, 0, 0, 1, 1]
    inC = [0, 1, 0, 1, 0, 1, 0, 1]
    outR =[0, 1, 1, 0, 1, 0, 0, 1]
    outV =[0, 1, 1, 1, 0, 0, 0, 1]
    
    for i in range(len(inA)):
        dut.A.value = inA[i]
        dut.B.value = inB[i]
        dut.C.value = inC[i]

        await Timer(1, units="ns")
        condition = (dut.resultado.value == outR[i] and dut.vemum.value == outV[i])
        if not condition:
            if not dut.resultado.value == outR[i]:
                dut._log.error("Expected value: " + "{0:1b}".format(outR[i]) + " Obtained value: " + str(dut.resultado.value) )
            if not dut.vemum.value == outV[i]:
                dut._log.error("Expected value: " + "{0:1b}".format(outV[i]) + " Obtained value: " + str(dut.vemum.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


