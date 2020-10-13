import traceback 
import logging 
from common_utils.os_functions import enter_exit
import datetime 

#装饰器 可以放多个在一个函数上面

def catch_and_print(func):
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except Exception as e :
			logging.error(traceback.format_exc())
			enter_exit(f'Error: Calling function: {func.__name__}')

	return wrapper

def df_row_num_decorator(func):
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        if type(func_result) != tuple:
        	df_num = func_result.shape[0]
        else:
        	df_num = func_result[0].shape[0]

        print(f'当前数据行数:{df_num}')
        #必须要返回func_result的原始结果，否则原始函数的结果会变成wrapper的结果
        return func_result
    return wrapper

def get_run_time(func):
    t_start = datetime.datetime.now()
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        t_stop = datetime.datetime.now()
        print('用时:', round((t_stop - t_start).total_seconds(),1),'秒')
        return result

    return wrapper
