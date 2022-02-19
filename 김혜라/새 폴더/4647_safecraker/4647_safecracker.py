

num, letter = map(str, input().split())
num = int(num)
# print(letter)
# print(ord('Z'))


alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

n = len(letter)
main_list = []
for i in range(1, 1 << n):
    sub_list = []
    #j는 arr_a의 인덱스이므로 0부터 조회해야
    #모든 요소 포함 여부 확인 가능
    for j in range(n):
        if i & (1 << j):
            #print(arr[j], end=' ')
            sub_list.append(letter[j])
    main_list.append(sub_list)
# #
# print(main_list)

# #길이 조건에 맞는 부분집합을 담은 함수 len_list
len_list = []
for i in main_list:
    if len(i) == 5:
        len_list.append(i)

print(len_list)
