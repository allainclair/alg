"""https://leetcode.com/problems/masking-personal-information/"""


def mask_email(email):
    name, domain = email.split('@')
    first_letter = name[0].lower()
    last_letter = name[-1].lower()
    return f'{first_letter}*****{last_letter}@{"".join(domain).lower()}'


def mask_tel(tel):
    filtered_tel = ''.join(char for char in tel if char not in {'+()- '})
    print(filtered_tel)


def mask_pii(s):
    return mask_email(s)


def main():
    input1 = 'LeetCode@LeetCode.com'
    assert mask_pii(input1) == 'l*****e@leetcode.com'

    input2 = "AB@qq.com"
    assert mask_pii(input2) == 'a*****b@qq.com'

    input3 = '1(234)567-890'
    input4 = '86-(10)12345678'


if __name__ == '__main__':
    main()
