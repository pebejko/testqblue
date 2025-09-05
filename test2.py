import qibo
from qibo import Circuit, gates
from collections import Counter

# Configurar backend
qibo.set_backend("qibojit")  # o "qibojit", platform="numba"

# Construir el circuito
circuit = Circuit(2)
circuit.add(gates.X(0))
circuit.add(gates.H(1))
circuit.add(gates.M(0, 1))

# Ejecutar el circuito
result = circuit(nshots=10000)

# Obtener frecuencias
counts = Counter(result.frequencies())
print(counts)