import heapq as hp

To_do_list = []

def add():
    hp.heappush(To_do_list,"Sleep quickly before morning ")
    hp.heappush(To_do_list,"practice some python topics")
    hp.heappush(To_do_list,"learn something new")
    hp.heappush(To_do_list,"plan a project ")
    print(To_do_list)

add()

def remove():
    if To_do_list:
        print("remove",hp.heappop(To_do_list))
        print(To_do_list)
    else:
        print("No more To_do_list")



remove()

def peek():
    if To_do_list:
        print("peek",hp.heappop(To_do_list))
        print(To_do_list)
