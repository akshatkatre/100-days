from bid_secret_09.art import logo

bid_details = {}
print(logo)
another_bid_flag = "yes"
while another_bid_flag == 'yes':
    name = input('Bidder name: ')
    amount = int(input('Bid amount :$'))
    bid_details[name] = amount
    another_bid_flag = input('Another user to bid [yes/no] : ').lower()


def find_highest_bidder():
    hightest_bid = -1
    message : str
    for key in bid_details:
      if bid_details[key] > hightest_bid:
        highest_bid = bid_details[key]
        message = f'winner is {key} with a bid of {bid_details[key]}'

    print(message)

find_highest_bidder()