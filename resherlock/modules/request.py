import httpx
from httpcore import ConnectError, ReadTimeout
from httpx._exceptions import InvalidURL


def normal(url):
    try:
        response = httpx.get(url)
        if "codechef" in url:
            if "The username specified does not exist in our database" in str(response.content):
                return 404
        return response.status_code
    except ConnectError:
        return 404
    except ReadTimeout:
        return 404
    except InvalidURL:
        return 404
