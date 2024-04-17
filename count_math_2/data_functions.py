import math
import numpy as np

from data_classes import Function

functions = {
    1: Function(
        lambda x: x ** 3 + 2.84 * x ** 2 - 5.606 * x - 14.766,
        "y = x^3+2.84*x^2-5.606*x-14.766"
    ),
    2: Function(
        lambda x: x ** 3 - 20 * np.sin(x),
        "x^3-20*sin(x)"
    ),
    3: Function(
        lambda x: (x + 1) ** (1 / 2) - 1 / x,
        "(x+1)^(1/2)-1/x"
    ),
    4: Function(
        lambda x: 3 * x ** 4 - 8 * x ** 3 - 18 * x ** 2 + 2,
        "3*x^4-8*x^3-18*x^2+2"
    )
}

systems = {
    1: {
        "first": Function(
            lambda x, y: x + 0.1 * x ** 2 + 0.2 * y ** 2 - 0.3,
            "x+0.1*x^2+0.2*y^2-0.3"
        ),
        "second": Function(
            lambda x, y: y + 0.2 * x ** 2 - 0.1 * x - 0.7,
            "y+0.2*x^2-0.1*x-0.7"
        )
    },
    2: {
        "first": Function(
            lambda x, y: 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3,
            "0.1 * x ^ 2 + x + 0.2 * y^2 - 0.3"
        ),
        "second": Function(
            lambda x, y: 0.2 * x ** 2 + y - 0.1 * x * y - 0.7,
            "0.2 * x ^ 2 + y - 0.1 * x * y - 0.7"
        )
    },
    # 3: {
    #     "first": Function(
    #         lambda x, y: x**2-x+0.2-y,
    #         "x^2-x+0.2-y"
    #     ),
    #     "second": Function(
    #         lambda x, y: x**2-0.2*x-y,
    #         "x^2-0.2*x-y"
    #     )
    # }
}
