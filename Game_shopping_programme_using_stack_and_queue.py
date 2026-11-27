def buying_games():
    to_do_list = ["Sony Spiderman 2","gta 5","assassin's creed black flag resynced","Microsoft Flight Simulator"] # To do list to buy games
    print(f"games to buy: {to_do_list}")

    to_do_list.pop()
    print(f"games to buy: {to_do_list} Microsoft Flight Simulator✅")

    to_do_list.pop()
    print(f"games to buy: {to_do_list} assassin's creed black flag resynced✅")

    to_do_list.pop()
    print(f"games to buy: {to_do_list} gta 5✅")

    to_do_list.pop()
    print(f"games to buy: {to_do_list} Sony Spiderman 2✅") # I complete this method using stack data structure

# Complete everything is ready Let's go to Checkout queue

buying_games()

def checkout_queue():
    pay_queue = ["arthur morgan", "bruce aka batman", "Harry Potter", "shanks"] #My friends complete their Shopping I'm the last person in the queue
    print(f"checkout queue: {pay_queue}")

    pay_queue.append("hari")                 #enqueue
    print(f"checkout queue: {pay_queue} hari added queue")

    pay_queue.pop(0)                   #dequeue
    print(f"checkout queue: {pay_queue} arthur morgan Complete Shopping ")

    pay_queue.pop(0)  # dequeue
    print(f"checkout queue: {pay_queue} batman Complete Shopping ")

    pay_queue.pop(0)  # dequeue
    print(f"checkout queue: {pay_queue} harry Complete Shopping ")

    pay_queue.pop(0)  # dequeue
    print(f"checkout queue: {pay_queue} shanks Complete Shopping ")

    pay_queue.pop(0)  # dequeue
    print(f"checkout queue: {pay_queue} queue is Empty it's close the shop") # I complete this method using queue data structure

    # Thanks for watching the repository
checkout_queue()