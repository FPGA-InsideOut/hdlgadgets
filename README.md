# hdlgadgets

**a human-in-the-loop training tool for rtl-developers, microarchitects and verification engineers allowing experiments with flow control and verification techniques**

In other words, "hdlgadgets" is a python written frontend that provides enhanced visualization and interactive interface for an HDL simulator.

"hdlgadgets" contains a library of "gadgets" packed in training scenarios. A "gadget" may come in different forms but can generally be classified either as: a fixed block that the user can only observe during simulation; a black box container in where they can put a custom HDL code; or an auxiliary block.
- Examples of "fixed gadgets": FIFO, Pipeline register, Credit counter, Skidbuffer.
- Examples of content of a "black box gadget": custom rtl code for glue-logic, custom hdl code for transaction-level-model.
- Examples of "auxiliary gadgets": control dashboard, visual checker.

A "gadget" is a module that can be reused in multiple training scenarios.
Here you can see an example of a training scenario comprised of three "gadgets": two FIFOs connected back-to-back and a control dashboard helping the user interact with the design:

![hdlgdtsdmo](https://github.com/FPGA-InsideOut/hdlgadgets/assets/53142676/d82d9e4d-302c-4000-af17-8373fbe8ff2d)


## How it works

"hdlgadgets" requires HDL simulator running on the background (it was tested with Icarus Verilog open-source simulator which has support for SystemVerilog). To communicate with the simulator "hdlgadgets" needs cocotb library:

![howitworks](https://github.com/FPGA-InsideOut/hdlgadgets/assets/53142676/7d4cb68a-fb0e-4ca3-9855-99e7112fbe58)

"hdlgadgets" uses hierarchical references to communicate with the simulated design. This allows to keep HDL code clean so that code can be used as the reference material for the design as is.

## Compatibility

`hdlgadgets` has been tested with the following software:
* python v3.11
* cocotb v1.8.0
* icarus_verilog v11.0

## Installation on Linux (Debian)

Update "apt":
```bash
sudo apt update
```

Install `git`, `IcarusVerilog`, `python3` and `python3-pip` — python package installer:
```bash
sudo apt install git iverilog python3 python3-pip
```

Install "CocoTB":
```bash
pip3 install cocotb
```

Get "hdlgadgets":
```bash
cd ~
git clone https://github.com/FPGA-InsideOut/hdlgadgets.git
```

Run "start.bash" script to run the program.
```bash
cd ./hdlgadgets
./start.bash
```

## Installation on Windows 10 (WSL)

* Enable Windows Subsystem for Linux (WSL)
  - Follow instructions from https://learn.microsoft.com/en-us/windows/wsl/install
* Download Debian from Microsoft Store
  - Use the direct [download link](https://apps.microsoft.com/detail/9MSVKQC78PK6) OR
  - Use the following command: `wsl.exe install -d Debian`
* Default Windows 10 terminal does NOT support Unicode characters. Please, install the WindowsTerminal from Microsoft Store ([Installation link](https://www.microsoft.com/store/productId/9N0DX20HK701)).

Run Debian in WSL from WindowsTerminal.

Update "apt":
```bash
sudo apt update
```

Install `git`, `IcarusVerilog`, `python3` and `python3-pip` — python package installer:
```bash
sudo apt install git iverilog python3 python3-pip
```

*On some Debian versions "cocotb" refuse to install outside python virtual environment - if that is the case then a virtual environment shall be created*

Install "python3-venv" — module for managing virtual environments:
```bash
sudo apt install python3-venv
```

Create python3 virtual environment in user home directory:
```bash
cd ~
python3 -m venv myvirtenv
```

Activate virtual environment and install CocoTB inside it:
```bash
cd ~
source ./myvirtenv/bin/activate
pip3 install cocotb
```

Leave virtual environment (if you want to):
```bash
deactivate
```

Get "hdlgadgets":
```bash
cd ~
git clone https://github.com/FPGA-InsideOut/hdlgadgets.git
```

Activate virtual environment (if not active) and run "start.bash" script to run the program:
```bash
cd ~
source ./myvirtenv/bin/activate
cd ./hdlgadgets
./start.bash
```

## Possible issues and troubleshooting

1. `hdlgadgets` uses `curses` library which may crash the program if it tries to draw outside terminal window. Although `start.bash` script checks the size of the terminal window before proceeding, it is important not to resize terminal window while `hdlgadgets` is running.

2. In case of an unexpected program crash it might not be possible to see an exact reason displayed on the screen because `curses` intercepts `stdout`.

To help troubleshoot the problem it is recommended to close current terminal window. And in new terminal window start problematic scenario redirecting `stout` to a file on disk:

Start `hdlgadgets` scenario directly using `make` command:
```bash
make -B -f ./Makefile_sc1 >> ./outfile
```

Then you can analyze `outfile` for a possible error that caused program crash.

3. For Linux, standard Linux terminal can be used as it has full unicode support. On Windows10 please use WindowsTerminal and run WSL with Linux.
