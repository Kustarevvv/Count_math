class Function:
    approx_left = ""
    approx_right = ""

    def __init__(self, exe, present):
        self.exe = exe
        self.present = present


class Response:
    error_vector = {}
    root = None
    fun_in_root = None
    i_count = 0
    message = ""
    code = 0


class Single_request:

    def __init__(self, function, method, term_left, term_right, accuracy):
        self.function = function
        self.method = method
        self.term_left = term_left
        self.term_right = term_right
        self.accuracy = accuracy


class Sys_request:

    def __init__(self, functions, method, term_left, term_right, accuracy):
        self.functions = functions
        self.method = method
        self.term_left = term_left
        self.term_right = term_right
        self.accuracy = accuracy
