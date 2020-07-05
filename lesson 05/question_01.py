input_string='1,2 , 5,4'
input_list=input_string.split(',')
print(input_list)
for i,st in enumerate(input_list):
    input_list[i] = st.strip()
    print(st)
print(input_list)
max_number = int(input_list[0])
for num_s in input_list:
    num = int(num_s)
    if num > max_number:
        max_number = num
print('Максимальное число: ', max_number)
