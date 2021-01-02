#Class and Names
print("\n")
print("\t","Class: 02")
print("\t","1. P1815360 - Tay Hock Leong Clarence")
print("\t","2. P1815414 - Audrey Lim Wan Yi")
print("-"*100)
print("\t","Portfolio Application Main Menu")
print("-"*100)
print("1. Display Stock")
print("2. Add Stock")
print("3. Update Stock")
print("4. Remove Stock")
print("5. Portfolio Statement")
print("6. Proposed Function 1")
print("7. Proposed Function 2")
print("8. Proposed Function 3")
print("E. Exit Main Menu")
print("-"*100)

def displaystock():
    import pandas as pd
    df= pd.read_csv('portfolioStock.csv')
    print(df)
    
def addstock():
    companyname=input("Enter your company name:")
    marketcap=input("Enter market capitalisation of company: Mega, Large or Mid:")
    stockbought=input("Enter Number of Stock Bought:")
    pricebought=input("Enter Price of Stock Bought:")
    marketprice=input("Enter Market Price of Stock:")
    from csv import writer
    addstock=[companyname,marketcap,stockbought,pricebought,marketprice]
    with open('portfolioStock.csv','a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(addstock)
        f_object.close()
userinput=input("Select an option between 1-8 or enter 'E' to exit")

def updatestock():
    
print("No - Company")
print("-"*50)
print("0 - Microsoft")
print("1 - Amazon")
print("2 - PayPal")
print("3 - Apple")
print("4 - Fastly")
print("5 - Square")
print("-"*50)
userInput=input("Enter 0 to 5 for your selection or E to exit: ")
while userInput<0 and userInput>5 or userInput!="E":
    userInput=input("Enter 0 to 5 for your selection or E to exit: ")
def deletestock():
    print("audrey wheres ur part2")
while userinput!="E":
    if userinput == "1":
        displaystock()
    elif userinput == "2":
        addstock()
    elif userinput == "3":
        updatestock()
    elif userinput == "4":
        deletestock()
    else: 
        print("Please enter 1-8 or 'E' to exit")

    userinput=input("Select an option between 1-8 or enter 'E' to exit")