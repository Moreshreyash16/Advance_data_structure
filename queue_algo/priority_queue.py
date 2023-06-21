'''
@Author: Shreyash More

@Date: 2023-06-20 21:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 21:34:30

@Title : Write a program to simulate a bank teller system
        where customers arrive in a queue and are served based on priority.

'''
import queue

class Customer:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"Name: {self.name}, Priority: {self.priority}"


def simulate_bank_teller(num_customers,priority):
    """
    Description:
        It calculate the queue based on priority
    Parameter:
        num_customers : Take no of customer input
        priority :  Take list of priority
    Return:
        None
    """
    customer_queue = queue.PriorityQueue()

    # Generate random customers and add them to the queue
    for i in range(num_customers):
        name = f"Customer-{i+1}"
        customer = Customer(name, priority[i])
        customer_queue.put((customer.priority, customer))

    # Serve customers based on priority
    while not customer_queue.empty():
        priority, customer = customer_queue.get()
        print(f"Serving customer: {customer}")

    print("All customers served.")


def main():
    priority=[]
    num_customers = int(input("Enter number of customer "))
    for i in range(1,num_customers+1):
        user_priority=int(input(f"Enter priority for customer :{i} "))
        priority.append(user_priority)
    simulate_bank_teller(num_customers,priority)


if __name__ == "__main__":
    main()

