import os
import argparse
from cocotb_tools.runner import get_runner

def get_args():
    parser = argparse.ArgumentParser(
        description="Run alu cocotb test with Icarus Verilog."
    )
    parser.add_argument(
        "-w", "--waves",
        action="store_true",
        help="Enable waveform dumping"
    )
    return parser.parse_args()

def run_simulation(args):
    sim = get_runner("icarus")
    
    sources = [
        os.path.join("rtl", "alu_interface.sv"),
        os.path.join("rtl", "alu.sv"),
        os.path.join("rtl", "top.sv")
    ]
    
    sim.build(
        sources=sources,
        hdl_toplevel="top",
        always=True,
        defines={"COCOTB_SIM": 1}
    )

    sim.test(
        hdl_toplevel="top",
        test_module="tb.alu_test",
        waves=args.waves
    )

    if args.waves:
        # Common wave file names for Icarus
        wave_files = [
            os.path.join("sim_build", "sim.fst"),
            os.path.join("sim_build", "sim.vcd"),
            os.path.join("sim_build", "dump.vcd"),
            os.path.join("sim_build", "dump.fst"),
        ]
        
        found_wave = None
        for wf in wave_files:
            if os.path.exists(wf):
                found_wave = wf
                break
        
        if found_wave:
            print(f"[INFO] Opening waves: {found_wave}")
            # Use Popen to open in background so it doesn't block script
            import subprocess
            subprocess.Popen(["gtkwave", found_wave])
        else:
            print("[WARN] Wave file not found. Check if simulation generated one.")

if __name__ == "__main__":
    args = get_args()
    run_simulation(args)
