# Write a program that manages a list of countries and their capital cities. It should
# prompt the user to enter the name of a country. If the program already "knows"
# the name of the capital city, it should display it. Otherwise it should ask the user to
# enter it. This should carry on until the user terminates the program (how this
# happens is up to you).
# Note: A good solution to this task will be able to cope with the country being entered
# variously as, for example, "Wales", "wales", "WALES" and so on.

country_capitals = {'India':'Delhi','Nepal': 'Ktm','China':'Beijing'}

def add_country():
    country = input("Enter the name of a country: ").capitalize()
    if country in country_capitals:
        print(f"The capital city of {country} is {country_capitals[country]}")
    else:
        capital = input(f"Enter the capital city of {country}: ").capitalize()
        country_capitals[country] = capital
        print(f"{country} and its capital {capital} added to the list.")

def main():
    while True:
        option = input("Enter '1' to add a country or 'q' to quit: ")
        
        if option.lower() == 'q':
            break
        elif option == '1':
            add_country()
        else:
            print("Invalid option. Please enter '1' to add a country or 'q' to quit.")

if __name__ == "__main__":
    main()
print(country_capitals)
