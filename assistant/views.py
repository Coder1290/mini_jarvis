from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

from core.executor import execute_command

EXIT_WORDS = ["bye", "goodbye", "good bye", "exit", "quit", "stop"]

@csrf_exempt
def command_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            cmd = data.get("command", "").lower().strip()
        except Exception:
            return JsonResponse({"response": "Invalid request"}, status=400)

        if not cmd:
            response = "Please say that again."
        elif any(x in cmd for x in EXIT_WORDS):
            response = "Goodbye Sir! Have a great day!"
        else:
            response = execute_command(cmd)

        return JsonResponse({"response": response})

    return JsonResponse({"response": "Only POST allowed"}, status=405)


def index(request):
    """Serve the frontend page."""
    return render(request, "assistant/home.html")