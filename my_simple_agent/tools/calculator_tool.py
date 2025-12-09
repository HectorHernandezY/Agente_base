"""
Herramienta de Calculadora Simple
"""

from google.adk.tools import FunctionTool


def calculate(operation: str, num1: float, num2: float) -> dict:
    """
    Realiza operaciones matemáticas básicas.
    
    Args:
        operation: La operación a realizar (suma, resta, multiplicacion, division).
        num1: Primer número.
        num2: Segundo número.
        
    Returns:
        Un diccionario con el resultado de la operación.
    """
    operations = {
        "suma": lambda a, b: a + b,
        "resta": lambda a, b: a - b,
        "multiplicacion": lambda a, b: a * b,
        "division": lambda a, b: a / b if b != 0 else "Error: División por cero",
    }
    
    op_lower = operation.lower()
    
    if op_lower in operations:
        result = operations[op_lower](num1, num2)
        return {
            "operation": operation,
            "num1": num1,
            "num2": num2,
            "result": result,
            "status": "success"
        }
    else:
        return {
            "status": "error",
            "message": f"Operación '{operation}' no reconocida. Usa: suma, resta, multiplicacion, division"
        }


# Crear la herramienta
calculator_tool = FunctionTool(func=calculate)
