import csv
from django.shortcuts import render

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
        # Do something with the CSV data
        return render(request, 'csvuploader/success.html')
    else:
        return render(request, 'csvuploader/upload.html')
