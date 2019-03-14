from collections import OrderedDict, namedtuple
from decimal import Decimal
from string import ascii_uppercase

def tabular(table, widths):
    def sandwich(delim, contents):
        return delim + delim.join(contents) + delim
    def cell(value, width):
        return ' ' + str(value).ljust(width - 2)
    def cells(row):
        return sandwich('|', (cell(col, w) for col, w in zip(row, widths))) + '\n'
    horiz_rule = sandwich('+', ('-' * (w - 1) for w in widths)) + '\n'
    return sandwich(horiz_rule, (cells(row) for row in table))

# In Python 3.7, this should be a @dataclass instead:
class Item(namedtuple('Item', 'name price')):
    def __new__(cls, name, price):
        return super().__new__(cls, name, Decimal(price))

def main():
    menu_items = OrderedDict(zip(ascii_uppercase, [
        Item('The "Big Boy" Burger', '16.99'),
        Item('French Fries', '5.99'),
        Item('Currie sauce', '19.99'),
        Item('Napkins with Chokolates', '10.50'),
        Item('Juice Box', '89.01'),
        Item('Takeout', '18.99'),
    ]))

    print(
        tabular([['The Restaurant at the End of the Universe']], [36 + 9]) +
        tabular(
            (('{0} {1.name}'.format(*stuff), '${1.price}'.format(*stuff))
              for stuff in menu_items.items()),
            [36, 9]
        )
    )

    total = Decimal('0.00')
    while True:
        print('Total: ${0}'.format(total))
        selection = input("Select a letter or 'done': ")
        if selection == 'done':
            break
        total += menu_items[selection].price
    print('Final total: ${0}'.format(total))

if __name__ == '__main__':
    main()