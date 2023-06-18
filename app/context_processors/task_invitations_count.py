from django.contrib.auth.models import AnonymousUser


def task_invitations_count(request):
    return {
        "task_invitations_count": len(request.user.pending_tasks.all())
        if request.user == AnonymousUser
        else 0,
    }
