def palindrome(s):
    n = len(s)
    for i in range(0, (n-1)//2+1):
        if s[i] != s[n-i-1]:
            print("Not a palindrome")
            return
    print(s+" is a Palindrome")

def countfrequency(s):
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

def anagram(s1,s2):
    d1 = countfrequency(s1)
    d2 = countfrequency(s2)

    for i in d1:
        if i not in d2 and d1[i]!=d2[i]:
            return False
        else:
            d2.pop(i)

    if len(d2.keys()) == 0:
        return True
    else:
        return False

s1 = input("Enter a String: ")
s2 = input("Enter another String: ")
print(anagram(s1,s2))
