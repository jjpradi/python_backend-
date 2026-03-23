from django.shortcuts import render

# Create your views here.






import os 
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model=genai.Generativemodel("gemini-2.5-flash")

@csrf_exempt


def chat_view(request):
    if request.method=="POST":
        try:
            body:json.loads(request.body)
                        user_message = body.get("message", "")
prompt=f"""
You are a shopping assistant for NxtTrendz.

Use the below data to answer:

{user_message}
"""

response=model.generate_content(prompt)
return jsonResponse({

    "reply":response.reply
})

except Exception as e:
return jsonResponse({

    "reply":"Error: "+str(e)
})
    return JsonResponse({"error": "Only POST allowed"})

