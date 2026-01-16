integer_var=10
print("integer:",integer_var,"|type:",type(integer_var))
float_var=3.14
print("float:",float_var,"|type:",type(float_var))
string_var="hello,python"
print("string:",string_var,"|type:",type(string_var))
bool_var=True
print("boolean:",bool_var,"|type:",type(bool_var))
list_var=[1,2,3,"apple"]
print("list:",list_var,"|type:",type(list_var))
tuple_var=(1,2,3)
print("tuple:",tuple_var,"|type:",type(tuple_var))
set_var={1,2,3}
print("set:",set_var,"|type:",type(set_var))
dict_var={"name":"alice","age":25}
print("dictionary:",dict_var,"|type:",type(dict_var))
none_var=None
print("None:",none_var,"|type:",type(none_var))
print("-"*40)
sum_result=integer_var+float_var
diff_result=integer_var-float_var
prod_result=integer_var*float_var
div_result=integer_var/float_var
print("sum:",sum_result)
print("difference:",diff_result)
print("product:",prod_result)
print("division:",div_result)
try:
    num1=input("enter an integer value:")
    num2=input("enter a float value:")
    int_num=int(num1)
    float_num=float(num2)
    print("converted integer:",int_num,"|type:",type(int_num))
    print("converted float:",float_num,"|type:",type(float_num))
except:
 print("invalid input!pleasenenter numbers only.")
 message=string_var+"number is"+str(int_var)
 print("concatenated string:",message)
 dynamic_var=100
 print("dynamic_var:",dynamic_var,"|type:",type(dynamic_var))
 dynamic_var="now i am a string"
 print("dynamic_var:",dynamic_var,"|type:",type(dynamic_var))
 dynamic_var=3.14
 print("dynamic_var:",dynamic_var,"|type:",type(dynamic_var))
 