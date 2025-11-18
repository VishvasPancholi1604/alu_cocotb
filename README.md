# alu

Project skeleton created by create_cocotb_project.py.

Structure:
```
alu/
  setup_cocotb.csh
  cocotb_xcelium.py
  rtl/
  tb/
```

Usage:
1. Source the setup script (csh/tcsh):
   ```
   source setup_cocotb.csh
   ```

2. Run the simulator script (examples):
   ```
   python3 cocotb_xcelium.py          # run without waves
   python3 cocotb_xcelium.py -w --gui # run with waves and open SimVision
   ```

Place your RTL in `rtl/` (e.g. `rtl/adder.sv`) and tests in `tb/` (e.g. `tb/test_adder.py`).
