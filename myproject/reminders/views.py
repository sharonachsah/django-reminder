# Import necessary modules
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reminder
from datetime import datetime

@csrf_exempt
def create_reminder(request):
    if request.method == 'POST':
        # Extract data from request
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        # Parse date and time strings to datetime object
        datetime_str = f"{date} {time}"
        reminder_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

        # Create reminder object and save to database
        reminder = Reminder(datetime=reminder_datetime, message=message)
        reminder.save()

        # Return success response
        return JsonResponse({'status': 'Reminder saved successfully'})
    else:
        # Return error response for unsupported methods
        return JsonResponse({'error': 'Unsupported method'}, status=405)
    
def reminder_view(request):
    if request.method == 'GET':
        # Extract reminder ID from request
        reminder_id = request.GET.get('id')

        # Retrieve reminder from database
        reminder = Reminder.objects.get(id=reminder_id)

        # Return reminder details
        return JsonResponse({
            'id': reminder.id,
            'datetime': reminder.datetime,
            'message': reminder.message
        })
    else:
        # Return error response for unsupported methods
        return JsonResponse({'error': 'Unsupported method'}, status=405)
    
def reminders_view(request):
    if request.method == 'GET':
        # Retrieve all reminders from database
        reminders = Reminder.objects.all()

        # Return reminders details
        return JsonResponse({
            'reminders': [
                {
                    'id': reminder.id,
                    'datetime': reminder.datetime,
                    'message': reminder.message
                }
                for reminder in reminders
            ]
        })
    else:
        # Return error response for unsupported methods
        return JsonResponse({'error': 'Unsupported method'}, status=405)
