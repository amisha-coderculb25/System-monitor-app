from django.shortcuts import render
import subprocess

def htop_view(request):
    try:
        process = subprocess.Popen(['htop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(timeout=10)  # Add a timeout
        output = stdout.decode('utf-8')
    except FileNotFoundError:
        output = "htop command not found."
    except subprocess.TimeoutExpired:
        process.kill()
        output = "htop command timed out."
    except Exception as e:
        output = f"Error running htop: {e}"
    return render(request, 'monitor/htop.html', {'output': output})