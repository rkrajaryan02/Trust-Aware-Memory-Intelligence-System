from storage.memory_manager import load_memory
from agents.explainer import explain

memory = load_memory()

print(explain(memory[0]))