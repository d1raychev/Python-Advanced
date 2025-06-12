from collections import deque
clients = input()
customer_list = deque()
while clients != "End":
    if clients == "Paid":
        while customer_list:
            print(customer_list.popleft())
    else:
        customer_list.append(clients)

    clients = input()


print(f"{len(customer_list)} people remaining.")