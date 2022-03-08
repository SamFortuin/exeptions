#99059050, Sam Fortuin, pizzaCalculator
import time

def main():
    #vars
    smallPizzaAmount = int(input("How many small pizza's do you want?\n"))
    mediumPizzaAmount = int(input("How many medium pizza's do you want?\n"))
    largePizzaAmount = int(input("How many large pizza's do you want?\n"))
    #prices in €, based on NYPizza
    pizzaPrices = [11.99, 13.99, 16.99]
    smallPizzaPrice, mediumPizzaPrice, largePizzaPrice = pizzaPrices

    #sum for prices
    smallPizzaTotal = smallPizzaAmount * smallPizzaPrice
    mediumPizzaTotal = mediumPizzaAmount * mediumPizzaPrice
    largePizzaTotal = largePizzaAmount * largePizzaPrice
    totalPrice = smallPizzaTotal + mediumPizzaTotal + largePizzaTotal
    
    #print final calculator line
    print("\n\n--------------------\nYour order:\n--------------------\n\n"+str(smallPizzaAmount),"small pizza's totaling €"+str(round(smallPizzaTotal,2))+"\n"+str(mediumPizzaAmount),"medium pizza's totaling €"+str(round(mediumPizzaTotal,2))+"\n"+str(largePizzaAmount),"large pizza's totaling €"+str(round(largePizzaTotal,2)),"\n\n--------------------\nOrder Total: €"+str(round(totalPrice,2))+"\n--------------------\n")
    
    #asks if another order after 500ms & lowers it
    time.sleep(0.5)
    restart = input("Do you want to buy more pizza's? Y/N ")
    restart = restart.lower()

    #if yes is typed program restarts itself
    if restart == "y" or restart == "yes":
        main()
    #if no is typed exits with ty msg
    elif restart == "n" or restart == "no":
        print("Thank you for using the calculator. program will now exit")
        time.sleep(0.2)
        exit()
    else:
        print("Input not regonized as any form of yes or no. program will now exit")
        time.sleep(0.2)
        exit()

if __name__ == "__main__":
    main()

#add name for the order