year=int(input("ENTER THE YEAR:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("THE YEAR IS A LEAP YEAR")
        else:
            print("THE YEAR IS NOT A LEAP YEAR")
    else:
        print("THE YEAR IS A LEAP YEAR")
else:
    print("THE YEAR IS NOT A LEAP YEAR")