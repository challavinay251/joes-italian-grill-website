from django.shortcuts import render, redirect
from datetime import date
from .models import Reservation
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import EventBooking


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


def special_events(request):
    success = False

    if request.method == "POST":
        data = request.POST

        EventBooking.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            event_date=data.get("event_date"),
            event_time=data.get("event_time"),
            event_type=data.get("event_type"),
            guests=data.get("guests"),
            need_catering=True if data.get("need_catering") == "yes" else False,
            description=data.get("description"),
        )

        # Email to ADMIN
        send_mail(
            "New Event Booking Request",
            f"""
New event request received:

Name: {data.get("name")}
Email: {data.get("email")}
Phone: {data.get("phone")}

Event: {data.get("event_type")}
Date: {data.get("event_date")}
Time: {data.get("event_time")}

Guests: {data.get("guests")}
Catering: {data.get("need_catering")}

Description:
{data.get("description")}
            """,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )

        success = True

    return render(request, "reservations/special_events.html", {"success": success})