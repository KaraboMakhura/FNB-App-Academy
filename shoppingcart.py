item_counter = 0
total_cost = 0
exit_condition = False
Food_dict= {}

while (exit_condition == False):
    current_item = input("Enter the food item here: ")
    current_price = float(input("Enter the price:"))
    Food_dict[current_item] = current_price
    total_cost = total_cost + current_price
    item_counter +=1
    cont_add = input("Add another Item? Respond Y/N ").upper()
    if cont_add =='Y':
        exit_condition = False
    elif cont_add == 'N':
        exit_condition = True
        print(Food_dict)
        print("Total items: ", item_counter)
        print("Total cost: R", total_cost)
        print("Thank you for shopping. Come again soon!")