#99059050, Sam Fortuin, pizzaCalculator
from time import sleep
from sys import stdout

def main():
    #vars
    smallPizzaAmount = input("How many small pizza's do you want?\n")
    try:
        smallPizzaAmount = int(smallPizzaAmount)
    except ValueError:
        print('not a number')
        main()
    # mediumPizzaAmount = int(input("How many medium pizza's do you want?\n"))
    while True:
        mediumPizzaAmount = input("How many medium pizza's do you want?\n")
        try:
            mediumPizzaAmount = int(mediumPizzaAmount)
        except ValueError:
            print('not a number')
            continue
        break
    
    while True:
        largePizzaAmount = input("How many large pizza's do you want?\n")
        try:
            largePizzaAmount = int(largePizzaAmount)
        except ValueError:
            print("not a number")
            continue
        break
    
    #prices in €, based on NYPizza
    pizzaPrices = [11.99, 13.99, 16.99]
    smallPizzaPrice, mediumPizzaPrice, largePizzaPrice = pizzaPrices

    #sum for prices
    smallPizzaTotal = smallPizzaAmount * smallPizzaPrice
    mediumPizzaTotal = mediumPizzaAmount * mediumPizzaPrice
    largePizzaTotal = largePizzaAmount * largePizzaPrice
    totalPrice = smallPizzaTotal + mediumPizzaTotal + largePizzaTotal
    
    #reciept
    stripe = '---------------------'
    smallPizz = f"\n{smallPizzaAmount} small  pizza's totaling €{str(round(smallPizzaTotal,2)).replace('.',',')}" if smallPizzaAmount > 0 else ""
    mediumPizz = f"\n{mediumPizzaAmount} medium  pizza's totaling €{str(round(mediumPizzaTotal,2)).replace('.',',')}" if mediumPizzaAmount > 0 else ""
    largePizz = f"\n{largePizzaAmount} large  pizza's totaling €{str(round(largePizzaTotal,2)).replace('.',',')}" if largePizzaAmount > 0 else ""
    
    print(f"{stripe}\n     Your order:\n{stripe}{smallPizz}{mediumPizz}{largePizz}\
    \n{stripe}\nOrder total:  €{str(round(totalPrice,2)).replace('.',',')}\n{stripe}\n")
    
    # \n{mediumPizzaAmount} medium pizza's totaling €{str(round(mediumPizzaTotal,2)).replace('.',',')}\
    # \n{largePizzaAmount} large  pizza's totaling €{str(round(largePizzaTotal,2)).replace('.',',')}\
    

    restart = input("Do you want to buy more pizza's? Y/N ").lower()[:1].replace('j','y')
    if restart == "y":
        main()
    elif restart == "n":
        print("Thank you for using the calculator. program will now exit")
        exit()
    else:
        print('a')

if __name__ == "__main__":
    main()