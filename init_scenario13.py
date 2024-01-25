import cocotb
from lib.common.program_class import program
from lib.scenario13_class import scenario13

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario13()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
