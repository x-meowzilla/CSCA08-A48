from stacks import StackA
from queues import QueueA


def convert_to_binary_stk(decimal_number):
    '''(int) -> str
    Return a string representing demical_number in binary
    '''
    # This stack will hold the remainders of the divisions,
    # which will eventually become the binary string
    remainder_stack = StackA()

    # if decimal number is 0, then directly push to stack
    if decimal_number == 0:
        remainder_stack.push(decimal_number)

    # while decimal_number is greater than zero, keep dividing it by 2 (using
    # integer division) and pushing the remainder onto the stack. This will
    # result in the stack becoming a binary representation (read top to bottom)
    # of the original decimal_number
    while(decimal_number > 0):
        remainder = decimal_number % 2
        remainder_stack.push(remainder)
        decimal_number = decimal_number // 2

    # the stack, read from top to bottom is now the binary number we want to
    # return. So we simply pop each item and add it (as a string) to the
    # return value
    binary_string = ""

    while(not (remainder_stack.is_empty())):
        binary_string += str(remainder_stack.pop())

    return binary_string


def convert_to_binary_q(decimal_number):
    '''(int) -> str
    Return a string representing demical_number in binary
    '''
    remainder_queue = QueueA()

    if decimal_number == 0:
        remainder_queue.enqueue(decimal_number)

    while(decimal_number > 0):
        remainder = decimal_number % 2
        remainder_queue.enqueue(remainder)
        decimal_number = decimal_number // 2

    binary_string = ""

    # only different from about is here, stack is FILO, but queue is FIFO
    while(not (remainder_queue.is_empty())):
        binary_string = str(remainder_queue.dequeue()) + binary_string

    return binary_string


if (__name__ == "__main__"):
    print(convert_to_binary_stk(0))
    print(convert_to_binary_stk(1))
    print(convert_to_binary_stk(10))
    print(convert_to_binary_stk(42))
    print(convert_to_binary_stk(13452))

    print(convert_to_binary_q(0))
    print(convert_to_binary_q(1))
    print(convert_to_binary_q(10))
    print(convert_to_binary_q(42))
    print(convert_to_binary_q(13452))
