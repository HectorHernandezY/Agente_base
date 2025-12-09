from google.adk import Agent
from .tools import calculator_tool


root_agent = Agent(
    name="calculator_agent",
    model="gemini-2.5-flash",
    description="Un agente que realiza cálculos matemáticos.",
    instruction="""Eres un asistente de cálculos. Tu trabajo es:
    
1. Ayudar a realizar operaciones matemáticas básicas.
2. Usar la herramienta calculate para hacer sumas, restas, multiplicaciones y divisiones.
3. Presentar los resultados de manera clara.

Siempre responde en español.""",
    tools=[calculator_tool],
)
