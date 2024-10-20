import os
import time


def publish_interceptor(plt):
    """
    发布拦截器
    :param plt: 平台
    :return:
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print(f"{plt} 开始执行")
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{plt} 执行完毕，耗时{round(end_time - start_time, 1)}秒")
            return result

        return wrapper

    return decorator


def append_footer(content: str):
    return f"{content}\n> 本文使用[MdSync](https://github.com/tanhh326/MdSync)工具发布！"


class MdFile:
    def __init__(self):
        self.name = None
        self.content = None
        self.abs_path = None

    def parse(self, path):
        try:
            self.name = os.path.splitext(os.path.basename(path))[0]
            self.abs_path = os.path.abspath(path)
            with open(path, 'r', encoding='utf-8') as file:
                self.content = append_footer(file.read())
        except FileNotFoundError:
            print("没找到md文档")
        except Exception as e:
            print(e)
        return self


def configureChromiumPage():
    from DrissionPage.common import Settings
    Settings.raise_when_ele_not_found = True
