"""https://leetcode.com/problems/friends-of-appropriate-ages/"""


def friend_request(ages):
    # If sorting complexity at least O(n.log(n))
    # If no sorting complexity at least O(n^2)

    friend_request_count = 0
    for i, request_age in enumerate(ages):  # Person A
        for j, receive_age in enumerate(ages):  # Person B
            if i != j:
                # print(request_age, receive_age)
                # friend_request_condition = (
                #     receive_age <= 0.5 * request_age + 7
                #     or receive_age > request_age
                #     or receive_age > 100 and request_age < 100
                # )
                friend_request_condition = (
                    receive_age > 0.5 * request_age + 7
                    and receive_age <= request_age
                    and (receive_age <= 100 or request_age >= 100)
                )

                # print(friend_request_condition)

                # The boolean value is coerced to int (False = 0, True = 1)
                # friend_request_count += not friend_request_condition
                friend_request_count += friend_request_condition
    # print(friend_request_count)
    return friend_request_count


def main():
    input1 = [16, 16]
    assert friend_request(input1) == 2
    print()

    input2 = [16, 17, 18]
    assert friend_request(input2) == 2
    print()

    input3 = [20, 30, 100, 110, 120]
    assert friend_request(input3) == 3


if __name__ == '__main__':
    main()
