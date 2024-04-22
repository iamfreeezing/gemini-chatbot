from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import base64
import vertexai
import speech_recognition as sr
import numpy as np
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason, ChatSession
import vertexai.preview.generative_models as generative_models

vertexai.init(project="third-index-420920", location="us-central1")
model = GenerativeModel("gemini-1.0-pro-vision-001")
chat = model.start_chat()


def home(requests):
    return render(requests, "index.html")

def get_chat_response(chat: ChatSession, prompt: str) -> str:
    text_response = []
    responses = chat.send_message(prompt, stream=True)
    for chunk in responses:
        text_response.append(chunk.text)
    return "".join(text_response)

def texting(request):
    if request.method == "POST":
        our_prompt = request.POST.get("prompt")  
        response = get_chat_response(chat, our_prompt)
        return JsonResponse({"response": response}) 
    return JsonResponse({"error": "Bad Request"}, status=400)

