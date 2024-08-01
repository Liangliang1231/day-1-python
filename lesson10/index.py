import learning

def main():
    p1 = learning.getPerson(name="紀亮亮")
    print(p1.bmi_print())
    print("============")
    p2= learning.Person.getPerson(name="liangliang")
    print(p2.bmi_print())
    print("============")
    p3= learning.Person.getPerson(name="黃泠澤")
    print(p3.bmi_print())
if __name__ == '__main__':
    main()
   