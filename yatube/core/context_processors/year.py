import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    current_year = datetime.datetime.today()
    return {
        'year': current_year.year,
    }
