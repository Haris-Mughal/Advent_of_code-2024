def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    initial_values = {}
    gates = []
    reading_gates = False

    for line in lines:
        line = line.strip()
        if not line:
            reading_gates = True
            continue
        
        if not reading_gates:
            wire, value = line.split(': ')
            initial_values[wire] = int(value)
        else:
            gates.append(line)
    
    return initial_values, gates

def evaluate_gate(gate, wire_values):
    inputs, output = gate.split(' -> ')
    if ' AND ' in inputs:
        a, b = inputs.split(' AND ')
        if a in wire_values and b in wire_values:
            result = wire_values[a] & wire_values[b]
        else:
            return output, None
    elif ' OR ' in inputs:
        a, b = inputs.split(' OR ')
        if a in wire_values and b in wire_values:
            result = wire_values[a] | wire_values[b]
        else:
            return output, None
    elif ' XOR ' in inputs:
        a, b = inputs.split(' XOR ')
        if a in wire_values and b in wire_values:
            result = wire_values[a] ^ wire_values[b]
        else:
            return output, None
    else:
        raise ValueError(f"Unknown gate type in {gate}")
    
    return output, result

def simulate_system(initial_values, gates):
    wire_values = initial_values.copy()
    remaining_gates = gates[:]
    
    while remaining_gates:
        new_remaining_gates = []
        for gate in remaining_gates:
            output, result = evaluate_gate(gate, wire_values)
            if result is not None:
                wire_values[output] = result
            else:
                new_remaining_gates.append(gate)
        if len(new_remaining_gates) == len(remaining_gates):
            # No progress was made, meaning there may be a dependency issue.
            break
        remaining_gates = new_remaining_gates
    
    return wire_values

def get_output_value(wire_values):
    binary_value = ''
    index = 0
    while f'z{index:02}' in wire_values:
        binary_value = str(wire_values[f'z{index:02}']) + binary_value
        index += 1
    
    return int(binary_value, 2)

def main():
    initial_values, gates = parse_input('day_24.in')
    wire_values = simulate_system(initial_values, gates)
    output_value = get_output_value(wire_values)
    print(output_value)

if __name__ == '__main__':
    main()