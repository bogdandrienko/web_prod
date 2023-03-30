import time

from rest_framework.request import Request


def logging(log_response=True):
    def wrapper1(controller: callable):
        def wrapper2(*args, **kwargs):
            start = time.perf_counter()

            request: Request = args[0]

            result = controller(*args, **kwargs)

            elapsed = round(time.perf_counter() - start, 3)
            with open("log.txt", 'a') as file:
                file.write(
                    f"[{elapsed}] {request.path} {request.method} "
                    f"{request.user if request.user.username else '-'} "
                    f"{result if log_response else '-'}"
                )

            return result

        return wrapper2

    return wrapper1
