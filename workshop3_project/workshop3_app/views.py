from django.http import JsonResponse
from .serial_sum import serial_sum


def calculate_serial_sum(request, n, m=None):
    if m is None:
        result = serial_sum(int(n))
    else:
        result = serial_sum(int(n), int(m))

    return JsonResponse({'result': result})
