print("Hello Welcome!")

expenses=[]



#FR-03
#[{"item":"XYZ","amount":123,"category":"abc"}]
def get_category_wise_data(data):
    res={}
    for expense in data:
        category=expense["category"]
        amount=expense["amount"]
        res[category]=res.get(category,0)+amount
    return res 

#FR-04
#[{"item":"XYZ","amount":123,"category":"abc"}]
def get_total_amount(data):
    total=0
    for expense in data :
        total=total+expense["amount"]
    return total



#FR-05
#{"abc":123,"XYZ":567}
def get_max_cost(data):
    top_name="" 
    top_amount=0,
    
    for category,amount in data.items():
        if top_amount > tpo_amount:
           top_amount=category
           top_amount=amount
           
    return top_amount,top_amount 




while True:
    #FR01
    item=input("Item(or 'done'to finish):")


    item== "done"
    break

    
    item=input("Item:")
    amount=int(input("Amount:"))
         
    category=input("Category:")

    expenses.append(
        {
    
             "item":item,
             "amount":amount,
             "category":category
        }     
    # )   


# #FR-7
if len(expenses)==0:
    print("No expenses entered.")


else:
    print(expense)
    category_wise_data=get_category_wise_data(expense)
    print(category_wise_data)
    total_amount=get_total_amount(expense)
    print("total Amount:", total_amount)
    res=get_max_cost(category_wise_data)
    print(f"top category:{res[0]} -Amount: {res[1]}")
    print("Done! Thanks for using this app!")



#FR-6
for category,amount in category_wise_data.items():
    print(f"Category:{category}")
    print(f"Amount:{amount}")
    print(f"Share:{(amount/total_amount)*100}%")
    
print("Done! Thanks for using this app!")

    # print(item,amount,category)
# print("Hi! welcome!")

