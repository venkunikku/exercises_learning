def test_exception():
    try:
        f = open("notes.txt")
        for line in f:
            print(line)
        f.close()
    except IOError as e:
        print(e)

    try:
        f = open("nofile")
    except IOError as e:
        print('From Print', e)
        # raise IOError


def raise_raise_exception():
    try:
        test_exception()
    except Exception as e:
        print('From second erro:', e)


def multipe_excetions():
    try:
        1 / 0
    except (IOError, TypeError, NameError, Exception) as e:
        print("HERE", e)


def all_exceptions():
    try:
        1 / 0
    except:
        print('all exceptions are caught here')


def try_with_else():
    try:
        f = open('notes.txt')
    except IOError as e:
        print(e)
    else:
        print(f.readline())
        f.close()


def try_with_finally():
    try:
        f = open('notes.txt')
        print(f.readline())
        1 / 0
    except (IOError, ZeroDivisionError) as e:
        print(e)
    finally:
        print("Calling finally")
        f.close()


def user_defined_exception():
    if 1 > 0:
        raise UserDefintedException(1, "1 is not < 0 ")


def user_def_inherited():
    if 1 > 0:
        raise UserDefintedExceptionInherited("message from exception")


class UserDefintedException(Exception):
    def __init__(self, msg1, msg2):
        self.args = (msg1, msg2)
        self.msg1 = msg1
        self.msg2 = msg2


class UserDefintedExceptionInherited(UserDefintedException):
    def __init__(self, msg):
        self.args = ('new error', msg)


if __name__ == '__main__':
    test_exception()
    raise_raise_exception()
    multipe_excetions()
    all_exceptions()
    try_with_else()
    try_with_finally()
    try:
        user_defined_exception()
    except Exception as e:
        print(e)

    try:
        user_def_inherited()
    except Exception as e:
        if type(e) is UserDefintedExceptionInherited:
            print("Performa any further actions for this type of excepion")
