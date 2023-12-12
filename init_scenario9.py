import cocotb
from lib.common.program_class import program
from lib.scenario9_class import scenario9

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario9()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
