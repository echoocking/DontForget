# coding: utf-8

from functools import wraps
import inspect

class BaseParamsCheker(object):
    """参数检测装饰器
    通过校验传入的args index列表和 kwarg的参数名称列表
    对被装饰函数进行参数的非空校验
    arg 传index太麻烦啦。。。
    """

    def __init__(self, params_check_list):
        self.params_check_list = params_check_list

    def check(self, func):
        # def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            # arg_names 所有参数的变量名数组
            arg_names, varargs, keywords, defaults = inspect.getargspec(func)
            # 根据关键字进行赋值的参数字典
            params_dict = dict(zip(reversed(arg_names), reversed(defaults)))
            # 根据位置做匹配的参数字典
            arg_params = dict(zip(arg_names[:len(args)], args))
            # 整合函数的所有参数
            params_dict.update(arg_params)
            params_dict.update(kwargs)

            # 判断传入的检查参数列表名称是否在 arg_names中
            for param_name in self.params_check_list:
                if param_name not in arg_names:
                    raise ValueError, 'param {} is not in func params'.format(param_name)

            # 执行控制检查逻辑
            self._checker_func(self.params_check_list, params_dict)

            return func(*args, **kwargs)

        return wrapper

    def _checker_func(self, params_check_list, params_dict):
        raise NotImplementedError


class ParamsALLValid(BaseParamsCheker):
    """ 传入的参数名称list中，有任何一个值非true 则raise ValueError"""
    def __init__(self, params_check_list):
        super(ParamsALLValid, self).__init__(params_check_list)

    def _checker_func(self, params_check_list, params_dict):
        if params_check_list:
            for param_name in params_check_list:
                if not params_dict[param_name]:
                    raise ValueError, 'params {} is not valid'.format(param_name)


class NotAllParamsNotValid(BaseParamsCheker):
    """ 传入的参数名称list中，所有值非true 则raise ValueError"""
    def __init__(self, params_check_list):
        super(NotAllParamsNotValid, self).__init__(params_check_list)

    def _checker_func(self, params_check_list, params_dict):
        if params_check_list:
            if all(not params_dict[param_name] for param_name in params_check_list):
                    raise ValueError, 'all params {} is not valid'.format(self.params_check_list)


def not_all_params_is_not_valid(params_check_list):
    return NotAllParamsNotValid(params_check_list).check


def params_all_valid(params_check_list):
    return ParamsALLValid(params_check_list).check


@not_all_params_is_not_valid(['a', 'c', 'f'])
def test_empty_params_wapper(a, b, f, c=0, d=20):
    print 'ok'


test_empty_params_wapper(1, 2, 3)