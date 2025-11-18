import os
import sys

# current directory path
current_directory_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory_path)

from global_methods import (get_bit_field, set_bit_field, log)


class ALUTransaction:
    _txn_counter = 0   # class-level counter for txn_id

    def __init__(self, a=0, b=0, op=0, result=0, zero=0, carry=0, error=0, width=8):
        ALUTransaction._txn_counter += 1
        self.txn_id = ALUTransaction._txn_counter

        self.width = width
        self.a = get_bit_field(a, width-1, 0)
        self.b = get_bit_field(b, width-1, 0)
        self.op = get_bit_field(op, 2, 0)
        self.result = get_bit_field(result, width-1, 0)
        self.zero = zero
        self.carry = carry
        self.error = error
        log.debug(f'transaction created:\n{self.print()}')


    def print(self):
        output = ''
        box_width = 25  # bigger box to fit extra fields
        def line():
            return f"{'-' * box_width}\n"
        def center(text):
            return text.center(box_width) + '\n'

        output += line()
        output += center(f"txn_id  #{self.txn_id}")
        output += line()

        # dynamic aligned rows
        key_width = 12
        fields = {
            "width": self.width,
            "a": self.a,
            "b": self.b,
            "op": self.op,
            "result": self.result,
            "zero": self.zero,
            "carry": self.carry,
            "error": self.error
        }

        for k, v in fields.items():
            output += f"{k.rjust(key_width)} : {str(v).ljust(box_width - key_width - 3)}\n"
        output += line()
        return output
