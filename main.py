from scipy import integrate
from sympy import diff
from sympy.abc import x


def get_function(x):
    return 1 / ((x ** 2 + 1)**0.5)


def get_true_integral(func, upper, lower, _integral):
    print(f"{upper}\n\n{func}dx = {_integral[0]}\n\n{lower}")


def use_rectangle_formula(func, lower, upper, _n, _h):
    lower_at_moment = lower + 0.1
    elements_sum = (func.subs(x, lower_at_moment))
    for i in range(_n - 1):
        if lower_at_moment < upper:
            lower_at_moment += _h
            elements_sum += (func.subs(x, lower_at_moment))

    result = elements_sum * _h
    return result


def check_M2(_x, func, lower):
    m2 = abs(diff(func, _x, 2).subs(_x, lower))
    return m2


def check_R(m2, _h, lower, upper):
    r = m2 * (((_h ** 2) * (upper - lower)) / 24)
    return r


def compare_integrals_results(true_result, rect_result):
    comparison_result = abs(true_result - rect_result)
    return comparison_result


def start():
    initial_function = 1 / ((x ** 2 + 1) ** 0.5)
    n = 10
    h = 0.2
    upper_limit = 1.3
    lower_limit = -0.5

    true_integral = integrate.quad(get_function, lower_limit, upper_limit)
    rectangle_integral = use_rectangle_formula(initial_function, lower_limit, upper_limit, n, h)
    m_2 = check_M2(x, initial_function, lower_limit)
    _r = check_R(m_2, h, lower_limit, upper_limit)
    comparison = compare_integrals_results(true_integral[0], rectangle_integral)

    get_true_integral(initial_function, upper_limit, lower_limit, true_integral)
    print(f"Квадратурная формула прямоугольников: {rectangle_integral}")
    print(f"M2 = sup |f''(x)| = |f''({lower_limit})| = ", m_2)
    print(f"R <= M2 * ((h^2 * (b - a)) / 24) = {_r}")
    print(f"Сравнение точного значения интеграла и полученного |{true_integral[0]} - {rectangle_integral}| "
          f"= {comparison}")


start()


