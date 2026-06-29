from functools import wraps

def require_role(role: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # placeholder check
            return func(*args, **kwargs)
        return wrapper
    return decorator

def require_permission(permission: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # placeholder check
            return func(*args, **kwargs)
        return wrapper
    return decorator
