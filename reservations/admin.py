from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'guests')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('date',)


from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import EventBooking


@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ("name", "event_type", "event_date", "status")
    list_filter = ("status",)

    actions = ["approve_events", "reject_events"]

    def approve_events(self, request, queryset):
        for obj in queryset:
            obj.status = "approved"
            obj.save()

            # Email to user
            send_mail(
                "Your Event Request Approved 🎉",
                f"""
Hi {obj.name},

Your event request has been APPROVED.

Event: {obj.event_type}
Date: {obj.event_date}
Time: {obj.event_time}

We look forward to serving you!

Thanks,
Joe's Italian Grill
                """,
                settings.EMAIL_HOST_USER,
                [obj.email],
            )

        self.message_user(request, "Selected events approved")

    def reject_events(self, request, queryset):
        for obj in queryset:
            obj.status = "rejected"
            obj.save()

            # Email to user
            send_mail(
                "Your Event Request Update",
                f"""
Hi {obj.name},

We regret to inform you that your event request has been REJECTED.

Please contact us for more details.

Thanks,
Joe's Italian Grill
                """,
                settings.EMAIL_HOST_USER,
                [obj.email],
            )

        self.message_user(request, "Selected events rejected")