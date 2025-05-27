def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

def convert():
    a=input("Enter input: ").strip().upper()

    if a.endswith("C"):
        celsius=float(a[:-1])
        fahrenheit=celsius_to_fahrenheit(celsius)
        print(f"{celsius} C is {fahrenheit:.2f} F")


    elif a.endswith("F"):
        fahrenheit=float(a[:-1])
        celsius=fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} F is {celsius:.2f} C")
        
    else:
        print("Specify the unit as 'C' or 'F'")
convert()



    