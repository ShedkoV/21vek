import logging

from app.storages.tables import Content

logger = logging.getLogger('app.api')


def log_result(func):
    """Декоратор для логирования результата функций."""
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        if result is None:
            logging.info(f'Function: {func.__name__}, Result: None value')
            return result

        if isinstance(result, list):
            log_list = [item.as_dict() for item in result]
            log_info = f'Function: {func.__name__}, Result: {log_list}'
        elif isinstance(result, Content):
            log_info = f'Function: {func.__name__}, Result: {result.as_dict()}'
        else:
            log_info = f'Function: {func.__name__}, value deleted'

        logging.info(log_info)
        return result

    return wrapper
