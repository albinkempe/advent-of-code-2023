def main():
    input_file = open("input.txt", "r")
    input = input_file.readlines()
    sum = 0
    
    for i in range(len(input)):
        first = -1
        last = -1
        
        for c in input[i]:
            if first == - 1 and c.isdigit():
                first = c
            if c.isdigit():
                last = c

        cv = first + last
        sum += int(cv)
    
    print(sum)

main()