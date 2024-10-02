def transpile(lines):
    python_lines = []
    for line in lines:
        stripped_line = line.strip()

        # Skip comment lines
        if stripped_line.startswith('//'):
            continue

        # Convert variable declarations (let)
        elif stripped_line.startswith('let ') and stripped_line.endswith(';'):
            python_line = stripped_line[4:-1].strip()
            python_lines.append(python_line)

        # Convert print statements
        elif stripped_line.startswith('print[') and stripped_line.endswith('];'):
            expression = stripped_line[6:-2].strip()
            python_line = f"print({expression})"
            python_lines.append(python_line)

        # Convert if statements
        elif stripped_line.startswith('if(') and stripped_line.endswith(';'):
            condition, expression = stripped_line[3:-2].split(') ', 1)
            condition = condition.strip()
            expression = expression.strip()
            python_expression = transpile([expression])
            python_line = f"if {condition}:\n    {python_expression}"
            python_lines.append(python_line)

        else:
            continue
        
    return '\n'.join(python_lines)

def execute_python_code(python_code):
    exec(python_code)

code_lines = [
    "// 변수에 값 할당",
    "let x = 10;",
    "let y = 20;",
    "if(x==10) print[x];",
    "",
    "// x와 y의 합을 출력",
    "print[x + y];" ]

python_code = transpile(code_lines)
print("파이썬 코드:")
print(python_code)
print("실행 결과:")
execute_python_code(python_code)
