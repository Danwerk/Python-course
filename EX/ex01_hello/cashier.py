sum_from_client = int(input("Enter a sum: "))
coins = 0

amount_of_fifty_cents = sum_from_client // 50
coins += amount_of_fifty_cents
sum_from_client2 = sum_from_client % 50

amount_of_twenty_cents = sum_from_client2 // 20
coins += amount_of_twenty_cents
sum_from_client3 = sum_from_client2 % 20

amount_of_ten_cents = sum_from_client3 // 10
coins += amount_of_ten_cents
sum_from_client4 = sum_from_client3 % 10

amount_of_five_cents = sum_from_client4 // 5
coins += amount_of_five_cents
sum_from_client5 = sum_from_client4 % 5

coins += sum_from_client5
print(f"Amount of coins needed: {coins}")
