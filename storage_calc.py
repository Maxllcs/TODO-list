try:
    bytes_input = int(input("Введите количество байт: "))
    
    if bytes_input < 0:
        print("Ошибка: количество байт не может быть отрицательным.")
    else:
        kilobytes = bytes_input / 1024
        megabytes = bytes_input / (1024 ** 2)
        dec_value = str(bytes_input)
        hex_value = hex(bytes_input)[2:].upper()  
        bin_value = bin(bytes_input)[2:]        
        print(f"\n{bytes_input} байт = {kilobytes:.2f} КБ")
        print(f"{bytes_input} байт = {megabytes:.4f} МБ")
        print(f"\nDEC (десятичная): {dec_value}")
        print(f"HEX (шестнадцатеричная): 0x{hex_value}")
        print(f"BIN (двоичная): 0b{bin_value}")
        if len(bin_value) > 32:
            print(f"BIN (первые 32 бита): 0b...{bin_value[-32:]}")

except ValueError:
    print("Ошибка: пожалуйста, введите целое число.")
except Exception as e:
    print(f"Произошла ошибка: {e}")