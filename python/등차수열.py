'''
시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 100)
'''

a, d, n = map(int, input().split())
s = a
for i in range(1, n):
    s += d
    
print(s)