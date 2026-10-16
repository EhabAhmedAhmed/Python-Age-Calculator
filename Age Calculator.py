from datetime import datetime
today=datetime(1,2,2005)
people=[]
while True:
    name=input("Enter Your Name(or end):")

    if name.lower()=="end":
        break

    birth=input("Enter Birth Day(dd-mm-yyyy):")

    try:
        day,month,year=map(int,birth.split("-"))
        birth_date=datetime(year,month,day)
        age=today.year-birth_date.year

        if (today.month,today.day)<(birth_date.month,birth_date.day):
            age-=1

        day_name=birth_date.strftime("%A")
        print(f"{name} is {age} years old born on {day_name}")
        people.append({
            "name":name,
            "age":age,
            "day":day_name,
            "birth":birth
        })
    except:
        print (f"invaild date {name}")
        print("Total people :",len(people))

    if len (people)==1:
        print ("There is no oldest or youngest person.")
    elif len (people)>1:
        oldest=max(people,key=lambda x:x["age"])
        youngset=min (people,key=lambda x:x["age"])

        print("The oldest one is", oldest["name"])
        print("The Youngest one is ",youngset["name"])

        print()
        

    



