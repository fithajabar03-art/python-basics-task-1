import logging
logging.basicConfig(
   filename="errors.log",
   level=logging.ERROR,
format="%(asctime)s-%(levelname)s-%(message)s"
)
class CustomError(Exception):
    pass
try:
    result=10/0
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")
    logging.error("ZeroDvisionError occured",exc_info=True)
except TypeError:
   print("invalid datat type")
   logging.error("TypeError occured",exc_info=True)
except CustomError as e:
   print(e)
   logging.error(e,exc_info=True)
else:
   print("result:",result)
finally:
   print("execution completed")
try:
    raise CustomError("this is a custom error message")
except CustomError as e:
   print(e)
   logging.error(e,exc_info=True)


      

    