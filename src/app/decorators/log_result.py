import logging

logger = logging.getLogger('app.api')


def log_result(func):
    """Декоратор для логирования результата функций."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            logging.info(f'Function: {func.__name__}, Result: None value')
            return result

        if isinstance(result, list):
            log_info = f'Function: {func.__name__}, Result: {[item.as_dict() for item in result]}'
        else:
            log_info = f'Function: {func.__name__}, Result: {result.as_dict()}'

        logging.info(log_info)
        return result

    return wrapper
