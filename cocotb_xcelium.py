import os
import argparse
from cocotb_tools.runner import Xcelium

script_dir = os.path.dirname(os.path.abspath(__file__))

def get_args():
    parser = argparse.ArgumentParser(
        description="Run alu cocotb test with optional waveform dump."
    )
    parser.add_argument(
        "-w", "--waves",
        action="store_true",
        help="Enable waveform dumping"
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Open SimVision GUI automatically (if waves enabled)"
    )
    parser.add_argument(
        "-l", "--log-level",
        default="INFO",
        type=str
    )
    return parser.parse_args()

def xcelium_simulate(args):
    sim = Xcelium()

    sim.build(
        sources=["rtl/alu_interface.sv", "rtl/alu.sv", "rtl/top.sv"],
        hdl_toplevel="top",
        always=True
    )

    sim.env["LOG_LEVEL"] = args.log_level.upper()

    sim.test(
        hdl_toplevel="top",
        test_module=f"tb.alu_test",
        waves=args.waves
    )

    if args.waves and args.gui:
        waves_path = os.path.join(script_dir,
                                  "sim_build",
                                  "cocotb_waves.shm",
                                  "cocotb_waves.trn")
        if os.path.exists(waves_path):
            print(f"[INFO] Opening waves: {waves_path}")
            os.system(f"simvision {waves_path} &")
        else:
            print(f"[WARN] Wave file not found at: {waves_path}")

def main():
    args = get_args()
    xcelium_simulate(args)

if __name__ == "__main__":
    main()

