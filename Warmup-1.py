# SLEEP_IN
def sleep_in(weekday, vacation):
  return True if((weekday == False and vacation == True) or (weekday == False and vacation == False) or (weekday == True and vacation == True)) else False

# MONKEY_TROUBLE
def monkey_trouble(a_smile, b_smile):
  return False if(a_smile == False and b_smile == True) or (a_smile ==True and b_smile == False) else True

# SUM_DOUBLE
def sum_double(a, b):
  return 2*(a+b) if (a == b) else (a+b)

# DIFF21
def diff21(n):
  return 2*abs(n-21) if n>21 else abs(n-21)

# PARROT_TROUBLE
def parrot_trouble(talking, hour):
  return True if ((talking == True) and (hour<7 or hour>20)) else False

# MAKES10
def makes10(a, b):
  return True if((a == 10) or (b == 10) or (a+b == 10)) else False

# NEAR_HUNDRED
def near_hundred(n):
  return True if(abs(n-100)<=10 or abs(n-200)<=10) else False

# POS_NEG
def pos_neg(a, b, negative):
  return True if((negative == True and a<0 and b<0) or(negative == False and ((a>0 and b<0)or(a<0 and b>0)))) else False
  
# NOT_STRING
def not_string(str):
  X = str[:3]
  return str if(X == 'not') else 'not '+str

# MISSING_CHAR
def missing_char(str, n):
  return str[:n] + str[n+1:]

# FRONT_BACK
def front_back(str):
  return str if(len(str) <= 1) else (str[len(str)-1] + str[1:len(str)-1] + str[0])

# FRONT3
def front3(str):
  return 3*str if len(str)<3 else 3*str[:3]