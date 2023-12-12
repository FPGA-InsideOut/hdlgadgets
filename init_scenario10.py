import cocotb
from lib.common.program_class import program
from lib.scenario10_class import scenario10

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario10()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
