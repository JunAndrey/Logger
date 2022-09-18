import logging
import logging.config
import os
from config import FOLDER_LOG


def decorator(path):
    if not os.path.exists(path):
        os.mkdir(path)

    def decorator_1(some_function):
        def new_function(*args, **kwargs):
            logging.basicConfig(filename=os.path.join(path, 'My_log.log'), filemode='w',
                                format='%(asctime)s %(name)s %(levelname)s: %(message)s',
                                datefmt='%Y/%m/%d %H:%M:%S', level=logging.INFO)

            logger = logging.getLogger(__name__)
            logger.info(f'I call a function < {some_function.__name__} >')
            logger.info(f'with arguments {args} {kwargs}')
            result = some_function(*args, **kwargs)
            logger.info('Finished')
            return result

        return new_function

    return decorator_1



nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


@decorator(FOLDER_LOG)
def final_list(list_1):
    for item in list_1:
        if isinstance(item, list):
            yield from final_list(item)
        else:
            yield item


if __name__ == "__main__":
    decorator(FOLDER_LOG)
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
final_list(nested_list)