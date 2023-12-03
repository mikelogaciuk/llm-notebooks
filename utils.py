from timeit import default_timer as timer
from functools import wraps
import string
import random
import cv2
import os


def chronometer(func):
    """
    Decorator that processes task computation time and returns its function name.

    :param func: A func that has to be wrapped
    :return: Computation time with a task name.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        starting_time = timer()
        task_name: str = str(func.__name__).replace('_', ' ').capitalize()
        result = func(*args, **kwargs)
        ending_time = timer()

        print(f"Task: '{task_name}', has been processed in: {(ending_time - starting_time): 0.4f} seconds.")

        return result

    return wrapper


def generate_random_string(size: int = 12):
    """Generate a random string of fixed length

    :param size:  of string
    :return: random string
    """
    random_string: str = ""

    for i in range(size):
        random_string += random.choice(string.ascii_letters)
        for key in range(1):
            random_string += str(random.randint(0, size))

    return random_string


def scale(scaler,
          model,
          factor,
          source
          ):
    """
    Scale image

    :param scaler:
    :param model:
    :param factor:
    :param source:
    :return:
    """

    if not os.path.exists("./temp"):
        os.mkdir("./temp")

    if not os.path.exists(f"./images/{model}"):
        os.mkdir(f"./images/{model}")

    file_name = generate_random_string()
    temp_path = f"temp/{file_name}.png"

    target_path = f"images/{model}/{file_name}.png" \
        if not os.path.exists(f"images/{model}/{file_name}.png") \
        else f"images/{model}/{file_name}_{generate_random_string()}.png"

    if scaler.lower() not in ["espcn", "fsrcnn", "lapsrn"]:
        raise Exception("Model not available")

    scaler = scaler.upper()
    scaler_path = f"scalers/{scaler}_x{factor}.pb"

    source.save(temp_path)

    image = cv2.imread(temp_path)

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(scaler_path)
    sr.setModel(scaler.lower(), factor)

    result = sr.upsample(image)

    cv2.imwrite(target_path, result)

    os.remove(temp_path)

    print(f"Image saved at {target_path}")
