from django.shortcuts import render
import os 
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as genai

load_dotenv()

genai.configure(api_key="AIzaSyDftBZEbnGsSBBH17iBzMjW5VsWkP4Dv0w")




model = genai.GenerativeModel("gemini-2.5-flash")


@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)

            user_message = body.get("message", "")

            prompt = f"""
You are a shopping assistant for NxtTrendz.

User message:
{user_message}
"""

            response = model.generate_content(prompt)

            return JsonResponse({
                "reply": response.text
            })

        except Exception as e:
            return JsonResponse({
                "reply": "Error: " + str(e)
            })

    return JsonResponse({"error": "Only POST allowed"})