from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
        "end_date",
        "status",
        "user",
        "is_deadline_notification_sent",
    )
    list_filter = ("status", "user", "created_at", "end_date")
    search_fields = ("title", "description")
    date_hierarchy = "created_at"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "description",
                    "files",
                )
            },
        ),
        (
            "Additional information",
            {
                "fields": (
                    "end_date",
                    "status",
                    "user",
                    "is_deadline_notification_sent",
                ),
            },
        ),
    )


admin.site.register(Task, TaskAdmin)
