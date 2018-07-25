import disk
import core


def main():
    # inventory_raw_info = disk.open_file('inventory.txt')
    # inventory_dictionary = core.create_inventory_dictionary(inventory_raw_info)
    inventory = {
        '1': {
            'name': 'Hammer',
            'stock': 17,
            'rental cost': 24,
            'replacement cost': 34
        },
        '2': {
            'name': 'Drill',
            'stock': 10,
            'rental cost': 55,
            'replacement cost': 100
        },
        '3': {
            'name': 'Saw',
            'stock': 18,
            'rental cost': 20,
            'replacement cost': 25
        },
        '4': {
            'name': 'Screwdriver',
            'stock': 18,
            'rental cost': 20,
            'replacement cost': 25
        }
    }

    print("Welcome to Daniel's Tool Rental!")

    name = input("What is the name for this rental? ")
    who_are_you = input("Are you a Employee or a Customer? ").strip().title()
    while True:
        if who_are_you == 'Employee':
            print('Checking the inventory!')
        elif who_are_you == 'Customer':
            help = input(
                "Would you like to rent a Tool , see our inventory, or quit? "
            ).strip()
            if help in ['Quit', 'quit']:
                exit()

        if help in [
                'See our inventory', 'see our inventory', 'see inventory',
                'Inventory', 'inventory'
        ]:
            print(
                'Choose of tools:',
                inventory['1']['name'],
                inventory['2']['name'],
                inventory['3']['name'],
                inventory['4']['name'],
            )
        if help in ['rent', 'rent a tool', 'rent a Tool', 'rent']:
            print(
                'Choose of tools:',
                inventory['1']['name'],
                inventory['2']['name'],
                inventory['3']['name'],
                inventory['4']['name'],
            )

            tool = input('OK, what tool would you like to rent? ').strip()
            if tool in ['Hammer', 'hammer']:
                inventory['1']['stock'] -= 1
                print('Rental Cost for', tool, 'is $ 24.0')

            elif tool in ['Drill', 'drill']:
                inventory['2']['stock'] -= 1
                print('Rental Cost for', tool, 'is $ 55.0')

            elif tool in ['Saw', 'saw']:
                inventory['3']['stock'] -= 1
                print('Rental Cost for', tool, 'is $ 15.0')

            elif tool in ['Screwdriver', 'screwdriver']:
                inventory['4']['stock'] -= 1
                print('Rental Cost for', tool, 'is $ 20.0')

    # renting_tool = inventory[tool]
    # renting_tool['In-stock'] -= 1


if __name__ == '__main__':
    main()
