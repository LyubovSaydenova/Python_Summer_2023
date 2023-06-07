def deco(func):
    def wrapper(text):
        res = func(text)
        return res.title()
    return wrapper
@deco
def hello(text):
    return text
print(hello("какой-то текст для ДЕКО"))