def copy_line(source_file, destination_file, line_number):
    try:
        with open(source_file, 'r') as f_source:
            lines = f_source.readlines()
            if 1 <= line_number <= len(lines):
                line_to_copy = lines[line_number - 1]
                with open(destination_file, 'a') as f_dest:
                    f_dest.write(line_to_copy)
                print("Строка успешно скопирована.")
            else:
                print("Указанный номер строки выходит за пределы файла.")
    except FileNotFoundError:
        print("Один из файлов не найден.")


source_file_name = input("Введите имя исходного файла: ")
destination_file_name = input("Введите имя файла, в который нужно скопировать строку: ")
line_number = int(input("Введите номер строки, которую нужно скопировать: "))

copy_line(source_file_name, destination_file_name, line_number)
