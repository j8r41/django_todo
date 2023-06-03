import datetime


def current_year(request):
    return {
        "current_year": datetime.date.today().year,
        "current_time": datetime.datetime.now()
    }
