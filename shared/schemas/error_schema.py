from datetime import datetime


def erro_padrao(error: str, message: str, path: str, details=None):
    return {
        "error": error,
        "message": message,
        "details": details or [],
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "path": path,
    }
