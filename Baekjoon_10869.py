# 백준 10869번 문제:사칙연산
# A+B,A-B,A*B,A/B(몫),A%B(나머지)출력

# 내 답안, 답은 맞음
my_list = ["7", "3"]
a, b = map(int, my_list)

print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a // b)  # 몫
print(a % b)  # 나머지

##옳은 답안
##input.split 사용해야함
# int 정수변환,map 괄호에 두개의 인자입력
# split 공백기준으로 나누기
# input 문자열입력
a, b = map(int, input().split())

print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a // b)  # 몫
print(a % b)  # 나머지
