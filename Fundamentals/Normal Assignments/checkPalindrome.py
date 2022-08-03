def checkPalindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False


num = input()
isPalindrome = checkPalindrome(num)

if isPalindrome:
    print('true')
else:
    print('false')