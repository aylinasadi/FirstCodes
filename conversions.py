while True:
    input_type= int(input("do you want to convert: 1.from decimal or 2.to decimal?"))
    if input_type == 1:
        output_type = int(input("what do you want to convert it to?\n1.Binary\n2.Octal\n3.Hexadecimal\n:"))
        user_input = input("enter your number: ")

        if output_type == 1:
            if user_input == "0":
                print(0)
            else:
                user_input = int(user_input)
                binary = ""
                while user_input > 0:
                    binary = str(user_input % 2) + binary
                    user_input //= 2
                print(binary)
            break
                
        elif output_type == 2:
            if user_input == "0":
                print(0)
            else:
                user_input = int(user_input)
                octal = ""
                while user_input > 0:
                    octal = str(user_input % 8) + octal
                    user_input //= 8
                print(octal)
            break
        elif output_type == 3:
            if user_input == "0":
                print(0)
            else:
                user_input = int(user_input)
                digits = "0123456789ABCDEF"
                hex_num = ""

                while user_input > 0:
                    hex_num = digits[user_input % 16] + hex_num
                    user_input //= 16
                print(hex_num)
            break
    elif input_type == 2:
        output_type = int(input("what is your data type?\n1.Binary\n2.Octal\n3.Hexadecimal\n:"))
        user_input = input("enter your number: ")

        if output_type == 1:
            decimal = 0
            power = len(user_input) - 1
            
            for digit in user_input:
                decimal += int(digit) * (2 ** power)
                power -= 1
            print(decimal)
            break
        
        elif output_type == 2:
            decimal = 0
            power = len(user_input) - 1
            for digit in user_input:
                decimal += int(digit) * (8 ** power)
                power -= 1
            print(decimal)
            break
        
        elif output_type == 3:
            decimal = 0
            power = len(user_input) - 1
            for digit in user_input:
                if digit.isdigit():
                    decimal += int(digit) * (16 ** power)
                else:
                    decimal += (ord(digit.upper()) - 55) * (16 ** power)
                power -= 1
            print(decimal)
            break


    else:
        print("please input 1 or 2")