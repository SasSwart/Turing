"""
    Syntax:
        [x, y, x], where:
            x = opcode
            y = address
            z = flag

        opcodes:
            0 => HALT
                Halts execution and returns specified status code
            1 => GOTO
                Sets memory index as specified
            2 => PRINT
                Prints specified value to Console
            3 => SET
                Sets Clipboard value to specified address
            4 => LOAD
                Loads specified value to clipboard
            5 => ADD
                Adds specified value to clipboard
            6 => IF
                If the clipboard value = 0, goto specified address, else continue as normal

        flags:
            0 => Absolute
            1 => Relative
            2 => Clipboard
            3 => Value

        Examples:
        [3, y, 2] => Set clipboard value to current index
        [4, 5, 3] => Load value 5 to clipboard
        [2, -3, 1] => Print value at memory address 3 left of current
        [0, 10, 0] => Halt, returning value at address 10 as status code
"""


class Machine:
    def __init__(self, memory_size=1024):
        self.memory = []
        self.address = 0
        self.clipboard = 0
        for i in range(0, memory_size):
            self.memory.append(0)

    def run(self, address=0):
        self.address == address
        while "True":
            opcode = self.memory[self.address]
            if opcode == 0:  # HALT
                if self.memory[self.address + 2] == 0:
                    return self.memory[self.memory[self.address + 1]]
                elif self.memory[self.address + 2] == 1:
                    return self.memory[self.address + self.memory[self.address + 1]]
                elif self.memory[self.address + 2] == 2:
                    return self.clipboard
                else:
                    return self.memory[self.address + 1]
            elif opcode == 1:  # GOTO
                if self.memory[self.address + 2] == 0:
                    self.address = self.memory[self.memory[self.address + 1]]
                elif self.memory[self.address + 2] == 1:
                    self.address = self.memory[self.address + self.memory[self.address + 1]]
                elif self.memory[self.address + 2] == 2:
                    self.address = self.clipboard
                else:
                    self.address = self.memory[self.address + 1]
                continue
            elif opcode == 2:  # PRINT
                if self.memory[self.address + 2] == 0:
                    print(self.memory[self.memory[self.address + 1]])
                elif self.memory[self.address + 2] == 1:
                    print(self.memory[self.address + self.memory[self.address + 1]])
                elif self.memory[self.address + 2] == 2:
                    print(self.clipboard)
                else:
                    print(self.memory[self.address + 1])
            elif opcode == 3:  # SET
                if self.memory[self.address + 2] == 0:
                    self.memory[self.memory[self.address + 1]] = self.clipboard
                elif self.memory[self.address + 2] == 1:
                    self.memory[self.address + self.memory[self.address + 1]] = self.clipboard
                elif self.memory[self.address + 2] == 2:
                    self.memory[self.clipboard] = self.clipboard
                else:
                    self.memory[self.address] = self.clipboard
            elif opcode == 4:  # LOAD
                if self.memory[self.address + 2] == 0:
                    self.clipboard = self.memory[self.memory[self.address + 1]]
                elif self.memory[self.address + 2] == 1:
                    self.clipboard = self.memory[self.address + self.memory[self.address + 1]]
                elif self.memory[self.address + 2] == 2:
                    self.clipboard = self.clipboard
                else:
                    self.clipboard = self.memory[self.address + 1]
            elif opcode == 5:  # ADD
                if self.memory[self.address + 2] == 0:
                    self.clipboard += self.memory[self.memory[self.address + 1]]
                elif self.memory[self.address + 2] == 1:
                    self.clipboard += self.memory[self.address + self.memory[self.address + 1]]
                elif self.memory[self.address + 2] == 2:
                    self.clipboard += self.clipboard
                else:
                    self.clipboard += self.memory[self.address + 1]
            elif opcode == 6:  # IF
                if self.clipboard == 0:
                    if self.memory[self.address + 2] == 0:
                        self.address = self.memory[self.memory[self.address + 1]]
                    elif self.memory[self.address + 2] == 1:
                        self.address = self.memory[self.address + self.memory[self.address + 1]]
                    elif self.memory[self.address + 2] == 2:
                        self.address = self.clipboard
                    else:
                        self.address = self.memory[self.address + 1]
                    continue
            else:
                return -1
            self.address += 3

    def load(self, start=0, stack=[0]):
        for address in range(start, start + len(stack)):
            self.memory[address] = stack[address - start]

"""
#Uncomment this block for a simple example of how to program the machine.
#The following code counts from 0 to 10 in an infinite loop.
machine = Machine()
machine.load(0, [
    4, 1, 3,
    3, 101, 0,
    4, 100, 0,
    5, 101, 0,
    3, 100, 0,
    2, 100, 0,
    6, 39, 3,
    5, -10, 3,
    6, 30, 3,
    1, 6, 3,
    4, -1, 3,
    3, 101, 0,
    1, 6, 3,
    4, 1, 3,
    3, 101, 0,
    1, 27, 3])
print(machine.run())
"""