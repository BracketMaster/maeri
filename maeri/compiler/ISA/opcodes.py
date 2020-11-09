from enum import IntEnum, unique

@unique
class Opcodes(IntEnum):
    configure_states = 1
    configure_weights = 2
    load_features = 3
    store_features = 4
    run = 5

class ConfigureStates():
    op = Opcodes.configure_states

    def __init___(self, address):
        self.address = address

class ConfigureWeights():
    op = Opcodes.configure_weights

    def __init___(self, address):
        self.address = address

class LoadFeatures():
    op = Opcodes.load_features

    def __init___(self, port_buffer_address, num_lines, address):
        self.port_buffer_address = port_buffer_address
        self.num_lines = num_lines
        self.address = address

class StoreFeatures():
    op = Opcodes.store_features

    def __init___(self, port_buffer_address, num_lines, address):
        self.port_buffer_address = port_buffer_address
        self.num_lines = num_lines
        self.address = address

class Run():
    op = Opcodes.run

    def __init__(self, length):
        self.length = length