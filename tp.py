# coding: utf-8
a=0
b=5
try:
x=b/a
#print(x)
    except  TypeError: print("merci de renseigner un chiffre au denominateur");
    except ZeroDivisionError: print("pas de 0 au doniminateur")
    finally: print("go")


