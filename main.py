from views import Car

def main():
    print('Hello! You have an access to following functions:\n\tLIST - 1\n\tCREATE - 2\n\tRETRIEVE - 3\n\tUPDATE - 4\n\tDELETE - 5\n\tLIKE - 6\n\tCOMMENT - 7')
    choice=input('Enter your choice: ')
    if choice=='1':
        print(Car.get_data())
        
    elif choice=='2':
        mark=input('Enter mark: ')
        model=input('Enter model: ')
        year_of_manufacture=int(input('Enter mayear of manufacturerk: '))
        engine_capacity=float(input('Enter engine capacity: '))
        color=input('Enter color: ')
        body_type=input('Enter body type: ')
        mileage=input('Enter mileage: ')
        price=float(input('Enter price: '))
        Car(mark, model, year_of_manufacture, engine_capacity, color, body_type, mileage, price)

    elif choice=='3':
        id=int(input('Enter id: '))
        print(Car.retrieve_data(id))

    elif choice=='4':
        id=int(input('Enter id: '))
        key=input('Enter key: ')
        new_value=input('Enter new value: ')
        print(Car.update_data(id,key,new_value))

    elif choice=='5':
        id=int(input('Enter id: '))
        print(Car.delete_data(id))
    
    elif choice=='6':
        id=int(input('Enter id: '))
        print(Car.like(id))

    elif choice=='7':
        id=int(input('Enter id: '))
        com=input('Enter comment: ')
        print(Car.comment(id,com))

    else:
        print('Invalid choice!')
        main()
    
    ask=input('Do you want to continue? (Y/n): ')
    if ask.lower()=='y': main()
    elif ask.lower()=='n': print('Bye-bye!')

main()