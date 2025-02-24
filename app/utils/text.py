def truncate_text(s: str, max_chars: int) -> str:
    return s[:max_chars] + "..." if len(s) > max_chars else s
