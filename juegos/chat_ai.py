from typing import List
import google.generativeai as genai
from django.conf import settings
import os
from dotenv import load_dotenv

load_dotenv()

# Configurar la API de Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))


def get_game_context(juegos, categorias):
    """Genera el contexto del catálogo de juegos"""
    context = "Este es un catálogo de videojuegos con la siguiente información:\n\n"

    # Información de categorías
    context += "Categorías disponibles:\n"
    for categoria in categorias:
        context += f"- {categoria.nombre}: {categoria.descripcion}\n"

    # Información de juegos
    context += "\nJuegos disponibles:\n"
    for juego in juegos:
        context += f"""
                    - {juego.titulo}:
                    Desarrollador: {juego.desarrollador}
                    Precio: ${juego.precio}
                    Categorías: {
            ', '.join([cat.nombre for cat in juego.categorias.all()])}
                    Descripción: {juego.descripcion}
                    """

    return context


def get_chat_response(prompt: str, conversation_history: List[dict], context: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-pro')

        system_prompt = f"""Eres un asistente experto en videojuegos que trabaja con nuestro catálogo.
        Usa esta información sobre nuestro catálogo para responder:

        {context}

        Instrucciones de formato:
        - Usa **texto** para títulos y elementos importantes
        - Organiza las listas con viñetas claras
        - Separa los párrafos con líneas en blanco
        - Usa categorías claramente marcadas
        - Mantén un formato consistente y legible

        Ejemplo de formato:
        **Categoría Principal**
        • Elemento importante: descripción
        • Otro elemento: detalles

        **Otra Categoría**
        Texto descriptivo bien organizado.

        Responde en español y sé amable y profesional."""

        chat = model.start_chat(history=[])
        chat.send_message(system_prompt)

        for message in conversation_history:
            chat.send_message(message['content'])

        response = chat.send_message(prompt)

        return response.text

    except Exception as e:
        return f"Lo siento, hubo un error al procesar tu pregunta: {str(e)}"
