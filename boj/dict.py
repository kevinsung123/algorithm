# Function calling 
def dictionairy():
    # Declare hash function
    key_value = {}

    # Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:\n sort the keys aplhabetically using key_value.iterkeys() function\n")
    print("Keys are")

    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(key_value.keys()):
        print(i, end=" ")
    print("\n\n")

    print("Task 2: \nKeys and Values sorted in",
          "alphabetical order by the key  ")
    print()
    # sorted(key_value) returns an iterator over the
    # Dictionary’s value sorted in keys.
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")
    print("\n\n")
    print("Task 3:\nKeys and Values sorted",
          "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=
    lambda kv: (kv[1], kv[0])))

    print("\n\n")

    count_dict={}
    # 숫 =등장회수 key-value
    #count_dict[5]=5
    count_dict[4]=5
    count_dict[1]=5
    count_dict[2]=5
    count_dict[5]=4
    count_dict[3]=9
    count_dict[8]=2
    # 수, 등장회수 순서로 넣는다 (기준 : 회수 오름차순, 수 오름차순)
    # 8,2,5,4,1,5,3,9

    print("원래수 : ", end=" ")
    print(count_dict)
    # 맨 안쪽 정렬을 수의 등장횟수 기준으로 정렬하고, 다시 수가 커지는 오름차순으로 정렬
    print("key 기준 정렬 수: ")
    for key in sorted(count_dict.keys()):
        print(key, count_dict[key])

    print("value 기준 정렬 수: ")
    for key in sorted(count_dict.keys(), key=lambda x: count_dict[x]):
        print(key, count_dict[key])

    print("value,key 기준 정렬 수: ")
    for key in sorted(sorted(count_dict.keys(), key=lambda x: count_dict[x])):
        print(key, count_dict[key])

def main():
    # function calling 
    dictionairy()


# Main function calling
if __name__ == "__main__":
    main() 