def format_string(s: str) -> str:
    """Форматує рядок до заглавних букв."""
    return s.upper()

def process_data(data: list) -> list:
    """Обробляє дані, видаляючи дублікати."""
    return list(set(data))
