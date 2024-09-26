#C언어 ---> 파이선 으로 바꾼다고 친다. 
def transpile(lines):
    python_lines = []
    for line in lines:   
        stripped_line = line.strip()

        if stripped_line.startswith('//'):
            continue

        elif stripped_line.startswith('let ') and stripped_line.endswith(';'): 
            python_line = stripped_line[4:-1]  
            python_lines.append(python_line)

        elif stripped_line.startswith('print '):
            expression = stripped_line[6:] 
            python_line = f"print({expression})"
            python_lines.append(python_line)      

        else:     
            continue
    return '\n'.join(python_lines) 
                                   

def execute_python_code(python_code): 
    exec(python_code)


code_lines = [
        "# 변수에 값 할당",
        "let x = 10;",
        "let y = 20;",
        "",
        "# x와 y의 합을 출력",
        "print x + y" ]
        
        
python_code = transpile(code_lines)
print("파이썬 코드:")
print(python_code)    
print("실행 결과:")
execute_python_code(python_code) 