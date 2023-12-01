def main():
    input_file = open("input.txt", "r")
    input = input_file.readlines()
    sum = 0
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(len(input)):
        values = [] # store elements as (index, digit)
        
        for d in digits:
            # haha this is disgusting
            if d in input[i]:
                letters = (input[i].index(d), digits.index(d) + 1)
                values.append(letters)
                letters = (input[i].rfind(d), digits.index(d) + 1)
                values.append(letters)
            if str(digits.index(d)+1) in input[i]:
                dig = (input[i].index(str(digits.index(d) + 1)), digits.index(d) + 1)
                values.append(dig)
                dig = (input[i].rfind(str(digits.index(d) + 1)), digits.index(d) + 1)
                values.append(dig)
        
        values.sort()
        calibration = str(values[0][1]) + str(values[len(values)-1][1])
        sum += int(calibration)
    
    print(sum)

main()