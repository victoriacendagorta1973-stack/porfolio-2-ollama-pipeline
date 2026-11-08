import json
from ollama import chat
from pydantic import BaseModel, Field


# 1. Esquema de datos estricto con Pydantic
class SolicitudSoporte(BaseModel):
    resumen: str = Field(
        description="Resumen conciso en una frase de la incidencia"
    )
    categoria: str = Field(
        description="Categoría principal: Pagos, Cuenta, Técnico o Envíos"
    )
    urgencia: str = Field(description="Nivel de urgencia: Alta, Media o Baja")
    escalado_humano: bool = Field(
        description="True si requiere intervención humana urgente"
    )


# 2. Texto de prueba no estructurado (simulación de caso real)
texto_entrada = """
Hola, llevo desde esta mañana intentando pagar la suscripción mensual y la pasarela 
de pago me da un error 500 constante. He probado con dos tarjetas distintas y no hay manera. 
Necesito acceso hoy mismo porque trabajo con la plataforma.
"""

print("Procesando solicitud localmente con Ollama (Llama 3.2)...")

# 3. Llamada al motor local de Ollama imponiendo el esquema Pydantic
response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": (
                "Eres un sistema automatizado de triaje de soporte. "
                "Analiza el texto y responde ÚNICAMENTE con la estructura JSON requerida."
            ),
        },
        {"role": "user", "content": texto_entrada},
    ],
    format=SolicitudSoporte.model_json_schema(),
    options={"temperature": 0},  # Máximo determinismo
)

# 4. Extracción y validación estricta del JSON recibido
datos_raw = response["message"]["content"]
solicitud_validada = SolicitudSoporte.model_validate_json(datos_raw)

# 5. Impresión de resultados en consola
print("\n--- RESULTADO PROCESADO EN LOCAL (COSTO: $0.00) ---")
print(f"Resumen: {solicitud_validada.resumen}")
print(f"Categoría: {solicitud_validada.categoria}")
print(f"Urgencia: {solicitud_validada.urgencia}")
print(f"Escalado Humano: {solicitud_validada.escalado_humano}")
print(f"\nTipo de objeto validado: {type(solicitud_validada)}")
