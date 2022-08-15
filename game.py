class TurnHistory(object):
    def __init__(self):
        self._iteration = 0
        self._value = []
        self._result = []

    def write_history(self, value, result):
        self._iteration += 1
        self._value.append(value)
        self._result.append(result)

    def get_history(self):
        return self._iteration, self._value, self._result


class Player(object):
    def __init__(self, user):
        self._user = user
        self._value = None
        self._game_history = TurnHistory()

    def set_value(self, number):
        self._value = number


class Session(object):
    def __init__(self):
        self._p1 = None
        self._p2 = None
        self._end_game = False

    def add_player(self, user):
        if self._p1 is None:
            self._p1 = Player(user)


def is_correct_number(value):
    try:
        # Check basic exceptions
        if not value.isnumeric() or len(value) != 4 or list(value)[0] == "0":
            return False
    except Exception as e:
        return False
    # Check multiply digits
    used_digits = []
    for digit in list(value):
        if digit in used_digits:
            return False
        else:
            used_digits.append(digit)
    return True


def get_hint(value, true_value):
    guessed_numbers = 0
    matching_numbers = 0
    for digit in list(value):
        if digit in list(true_value):
            guessed_numbers += 1
            if list(value).index(digit) == list(true_value).index(digit):
                matching_numbers += 1
    return guessed_numbers, matching_numbers


def get_expectation(req_text):
    expectation = input(req_text+": ")
    if is_correct_number(expectation):
        print("Value accepted")
        return expectation
    else:
        print("Value incorrect")
        get_expectation(req_text)
