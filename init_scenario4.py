import cocotb
from lib.common.program_class import program
from lib.scenario4_class import scenario4

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario4()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
