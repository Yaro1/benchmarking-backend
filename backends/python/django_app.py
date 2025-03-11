from django.http import JsonResponse
from django.conf import settings
from django.urls import path
import json
import os
import sys
import logging

# Ensure the correct path for function imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../functions/python")))

from logic import average, compute, multiply

# Configure Django settings
settings.configure(
    SECRET_KEY=os.environ.get("DJANGO_SECRET_KEY", "default-secret-key"),
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_to_numbers(data):
    """Convert input data to a list of numbers."""
    try:
        return [float(item) for item in data if isinstance(item, (int, float, str)) and str(item).replace('.', '', 1).isdigit()]
    except Exception as e:
        raise ValueError(f"Invalid input for number conversion: {e}")

# Handlers for each function with unique numbering

def average_handler(request):
    if request.method == "POST":
        try:
            # Parse and convert JSON input to a list of numbers
            data = json.loads(request.body.decode("utf-8"))
            numbers = convert_to_numbers(data.get("numbers", []))

            # Dynamically call the function with the processed numbers
            result = average(numbers=numbers)

            return JsonResponse({"status": "success", "data": result})

        except ValueError as e:
            logging.error(f"ValueError for average: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        except TypeError as e:
            logging.error(f"TypeError for average: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        except Exception as e:
            logging.error(f"Unexpected error for average: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

def compute_handler(request):
    if request.method == "POST":
        try:
            # Parse and convert JSON input to a list of numbers
            data = json.loads(request.body.decode("utf-8"))
            numbers = convert_to_numbers(data.get("numbers", []))

            # Dynamically call the function with the processed numbers
            result = compute(numbers=numbers)

            return JsonResponse({"status": "success", "data": result})

        except ValueError as e:
            logging.error(f"ValueError for compute: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        except TypeError as e:
            logging.error(f"TypeError for compute: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        except Exception as e:
            logging.error(f"Unexpected error for compute: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

def multiply_handler(request):
    if request.method == "POST":
        try:
            # Parse and convert JSON input to a list of numbers
            data = json.loads(request.body.decode("utf-8"))
            numbers = convert_to_numbers(data.get("numbers", []))

            # Dynamically call the function with the processed numbers
            result = multiply(numbers=numbers)

            return JsonResponse({"status": "success", "data": result})

        except ValueError as e:
            logging.error(f"ValueError for multiply: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        except TypeError as e:
            logging.error(f"TypeError for multiply: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        except Exception as e:
            logging.error(f"Unexpected error for multiply: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)


urlpatterns = [

    path("average", average_handler),

    path("compute", compute_handler),

    path("multiply", multiply_handler),

]

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    import sys
    execute_from_command_line([sys.argv[0], "runserver", "0.0.0.0:8000"])