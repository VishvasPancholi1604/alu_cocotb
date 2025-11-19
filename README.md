# ALU Cocotb Testbench

This project contains a Cocotb testbench for an ALU design. It supports running tests with both **Icarus Verilog** (Open Source) and **Cadence Xcelium** (Commercial).

## Structure

```
alu/
  setup_cocotb.csh       # Setup script for environment variables (if needed)
  cocotb_runner.py       # Runner for Icarus Verilog (Windows/Linux)
  cocotb_xcelium.py      # Runner for Cadence Xcelium (Linux)
  rtl/                   # SystemVerilog source files
    alu.sv
    alu_interface.sv
    top.sv
    cocotb_timescale.sv  # Timescale for Icarus/Cocotb
  tb/                    # Cocotb test files
    alu_test.py
    alu_driver.py
    alu_monitor.py
    alu_seq_item.py
```

## Running Tests

### 1. Icarus Verilog (Recommended for Windows/Linux)
Uses `cocotb_runner.py`. Requires `iverilog` installed and in your PATH.

**Basic Run:**
```bash
python cocotb_runner.py
```

**Run with Waveforms (GTKWave):**
Runs the test, generates `dump.vcd`, and automatically opens it in GTKWave.
```bash
python cocotb_runner.py --waves
# or
python cocotb_runner.py -w
```

### 2. Cadence Xcelium (Linux Only)
Uses `cocotb_xcelium.py`. Requires Xcelium environment setup.

**Basic Run:**
```bash
python3 cocotb_xcelium.py
```

**Run with Waveforms (SimVision):**
Runs the test, generates waveforms, and opens SimVision.
```bash
python3 cocotb_xcelium.py --waves --gui
# or
python3 cocotb_xcelium.py -w --gui
```

## Waveforms
- **Icarus Verilog**: Generates `dump.vcd`. Use `--waves` to open in GTKWave.
- **Xcelium**: Generates SHM database. Use `--waves --gui` to open in SimVision.

## Notes
- **Timescale**: `rtl/cocotb_timescale.sv` is used for Icarus Verilog to ensure correct simulation precision (1ns/1ps) without modifying `rtl/top.sv`, preventing conflicts with Xcelium.
- **Waveform Dumping**: Waveform dumping in `rtl/top.sv` is guarded by `` `ifdef COCOTB_SIM `` to ensure it only executes when running with `cocotb_runner.py`.
