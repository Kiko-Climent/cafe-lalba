from django.contrib import admin
from django.core.mail import send_mail
from .models import ContactMessage


# Customizing the admin view for ContactMessage
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'subject', 'email', 'responded']
    list_filter = ['responded']
    readonly_fields = ['timestamp', 'email']
    # Define fieldsets for the admin panel
    fieldsets = (
        (None, {
            'fields': ('timestamp', 'subject', 'email', 'responded', 'notes')
        }),
        ('Admin Response', {
            'fields': ('admin_response',),
            'classes': ('wide', 'extrapretty'),
        }),
    )

    def save_model(self, request, obj, form, change):
        print("Saving model...")
        if not change:
            print("Responded:", obj.responded)
            print("Admin response:", obj.admin_response)

            if obj.responded and obj.admin_response.strip():
                response = obj.admin_response.strip()
                send_mail('Answered: ' + obj.subject, response, 'climent.kiko@gmail.com', [obj.email], fail_silently=False)
                print("Email send to:", obj.email)

        super().save_model(request, obj, form, change)


admin.site.register(ContactMessage, ContactMessageAdmin)
