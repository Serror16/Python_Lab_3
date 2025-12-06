import ast
from src.fibo_recursive import fibo_recursive as fibo_rec
from src.fibo import fibo as fibo_iter
from src.bubble_sort import bubble_sort
from src.factorial import factorial as factorial_iter
from src.factorial_recursive import factorial_recursive as factorial_rec
from src.quick_sort import quick_sort_main as quick_sort
from src.heap_sort import heap_sort
from src.bucket_sort import bucket_sort
from src.counting_sort import counting_sort
from src.radix_sort import radix_sort
from src.stack import Stack
stack = Stack()


commands = {
    'fibo-rec': fibo_rec,
    'fibonacci-rec': fibo_rec,
    'fibo-iter': fibo_iter,
    'fibonacci-iter': fibo_iter,

    'factorial-rec': factorial_rec,
    'factorial-iter': factorial_iter,
    
    'heap-sort': heap_sort,
    'quick-sort': quick_sort,
    'bubble-sort': bubble_sort,
    'bucket-sort': bucket_sort,
    'counting-sort': counting_sort,
    'radix-sort': radix_sort,
}

def parse_args(args_str: str) -> list:
    """
    Парсит аргументы: либо число, либо список.
    """
    if not args_str:
        return []
    
    args_str = args_str.strip()
    
    if args_str.startswith('['):
        return [ast.literal_eval(args_str)]

    return [int(args_str)]

def stack_command(args_str: str):
    """
    Обрабатывает команды для стека:

        stack push <значение>
        stack pop
        stack peek
        stack size
        stack is_empty
    """
    global stack
    
    if not args_str:
        print("Доступные операции: push, pop, peek, size, is_empty")
        return None
    
    parts = args_str.strip().split(maxsplit=1)
    operation = parts[0].lower()
    
    try:
        if operation == 'push':
            if len(parts) < 2:
                print("Ошибка: для push нужно указать значение")
                return None
            value = parse_args(parts[1])[0]
            stack.push(value)
            print(f"Добавлено: {value}")
            return value
        
        elif operation == 'pop':
            value = stack.pop()
            print(f"Извлечено: {value}")
            return value
        
        elif operation == 'peek':
            value = stack.peek()
            print(f"Верхний элемент: {value}")
            return value
        
        elif operation == 'size':
            size = stack.__len__()
            print(f"Размер: {size}")
            return size
        
        elif operation == 'is_empty':
            is_empty = stack.is_empty()
            status = "пуст" if is_empty else "не пуст"
            print(f"Стек {status}")
            return is_empty
        
        else:
            print(f"Неизвестная операция: {operation}")
            print("Доступные: push <value>, pop, peek, size, is_empty")
            return None
            
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    


def main():

    """Основная функция, которая вызывает команды"""
    
    while True:
        try:
            inp = input("> ").strip()
            if inp.lower() in ('exit'):
                print("Выход из программы.")
                break
            
            if not inp:
                continue

            parts = inp.split(maxsplit=1)
            command_name = parts[0]
            if len(parts) > 1:
                arguments_str = parts[1]
            else:
                arguments_str = ""
            
            if command_name == 'stack':
                result = stack_command(arguments_str)
                if result is not None:
                    print(f"Результат: {result}")
                print()
                continue
            
            if command_name not in commands:
                print(f"Ошибка: неизвестная команда '{command_name}'")
                print(f"Доступные команды: {', '.join(sorted(commands.keys()))}")
                continue
            
            try:
                arguments = parse_args(arguments_str)

            except (ValueError, SyntaxError):
                print(f"Ошибка: неверный формат аргументов '{arguments_str}'")
                continue
            
            try:
                func = commands[command_name]
                result = func(*arguments)
                if result is not None:
                    print(f"Результат: {result}")
                else:
                    print("Команда выполнена")
                    
            except TypeError as e:
                print("Ошибка: неверное количество или тип аргументов")
                print(f"Подробности: {e}")
            except Exception as e:
                print(f"Ошибка при выполнении команды: {e}")

            
        except KeyboardInterrupt:
            print("\nВыход по Ctrl+C")
            break
        except EOFError:
            print("\nВыход")
            break

if __name__ == "__main__":
    main()