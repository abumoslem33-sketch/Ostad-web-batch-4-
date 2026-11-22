print("I Have a Plan! this is a Family Card")

expenses=[]
#[{"itme": "XYZ","amount":123,"category":"abc"}]

#FR-03
def get_category_wise_data(data):
   res={}
   for expense in data:
      category=expense["category"]
      amount=expense["amount"]
      res[category]=amount.get(category,0)+amount



#FR-4
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








# item=input("Item:")
# amount=int(input("Amount:"))
# category=input("Category")


# print(item,amount,category)


while True:
    #FR-01
    item=input("item(or 'done' to finish):")


    if item =="done":
        break


amount=int(input("Amount:"))
category=input("Category:")
print(item,amount,category)
#FR-02
    if category=="":
       category="other






















print(expenses)
print(get_category_wise_data(expenses))
print("Done!Thanks for using this app!")











