from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from .models import Reservation


def reserve(request):

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        res_date = request.POST.get('date')
        res_time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')

        # Validation
        if res_date and str(res_date) < str(date.today()):
            return render(request, 'reservations/reserve.html', {
                'error': "Past date not allowed",
                'today': date.today()
            })

        if not guests or int(guests) <= 0:
            return render(request, 'reservations/reserve.html', {
                'error': "Guests must be at least 1",
                'today': date.today()
            })

        # Save
        Reservation.objects.create(
            name=name,
            phone=phone,
            email=email,
            date=res_date,
            time=res_time,
            guests=guests,
            message=message,
        )

        # Email (safe)
        try:
            send_mail(
                "Reservation Confirmed 🍽",
                f"Hi {name}, your table is booked on {res_date} at {res_time}.",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )

            send_mail(
                "New Reservation",
                f"{name} booked for {guests} people on {res_date} at {res_time}.",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
        except:
            pass

        # ✅ REDIRECT (IMPORTANT FIX)
        return redirect('/reserve/?success=1')

    # GET request
    success = request.GET.get('success')

    return render(request, 'reservations/reserve.html', {
        'success': success,
        'today': date.today()
    })