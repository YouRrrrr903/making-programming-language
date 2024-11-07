#파이선 코드로 바꿔주는(?)함수
def transpile(lines):    #lines는 새로운 언어 코드가 들어있는 리스트(코드 한 줄=리스트 값 하나)
    python_lines = []   #파이선으로 바뀐 코드를 저장할 리스트
    for line in lines:     #위에 lines(새로운언어 코드 리스트)의 한 줄식 순회(반복)함
        stripped_line = line.strip()  #strip은 앞뒤 공백을 제거해주는거

        if stripped_line.startswith('#'):   #만약 코드가 #으로 시작하면 
            continue                        #무시하고 지나가 ㄱㄱ

        elif stripped_line.startswith('set '):   #만약 코드가 set으로 시작되면
            python_line = stripped_line[4:]      #5번째 글자부터 파이선 코드로 저장(set 빼고)
            python_lines.append(python_line)

        elif stripped_line.startswith('print '):  #만약 코드가 print로 시작하면
            expression = stripped_line[6:]        #print+공백 뒤 7번째 글자부터 expression에 저장
            python_line = f"print({expression})"  #파이선 코드 리스트에 print(expression)형태로 저장
            python_lines.append(python_line)      

        else:     
            continue
    return '\n'.join(python_lines)


def execute_python_code(python_code):    #파이선 코드로 실행-->결과
    exec(python_code)

#대충 이런 언어가 있다고 쳐보자
code_lines = [
        "# 변수에 값 할당",
        "set x = 10",
        "set y = 20",
        "",
        "# x와 y의 합을 출력",
        "print x + y" ]
        
        
python_code = transpile(code_lines)   #위에서 만든 transpile함수로 코드 처리
print("파이썬 코드:")
print(python_code)    
print("실행 결과:")
execute_python_code(python_code)      #파이선 코드로 실행한 결과
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
준수쿤의 1번째

lines = []
print("코드를 입력하세요 (종료하려면 빈 줄을 입력하세요):")
while True:
    line = input()
    if line == "":  # 빈 줄 입력 시 종료
        break
    lines.append(line)

transpiled_code = transpile(lines)  # 변환된 코드를 얻기
execute_python_code(transpiled_code)  # 변환된 코드를 실행하기
--------------------------------------------------------------------------------------------------------
준수쿤의 2번째

def get_user_input():
    lines = []
    print("코드를 입력하세요 (종료하려면 빈 줄을 입력하세요):")
    while True:
        line = input()
        if line == "":  # 빈 줄 입력 시 종료
            break
        lines.append(line)
    return lines

def transpile(lines):
    # 여기에 변환 로직을 작성하세요.
    # 예시로 입력된 코드를 그대로 반환합니다.
    return "\n".join(lines)

def execute_python_code(code):
    # exec를 사용하여 변환된 코드를 실행합니다.
    try:
        exec(code)
    except Exception as e:
        print(f"코드 실행 중 오류 발생: {e}")

def main():
    lines = get_user_input()

    try:
        transpiled_code = transpile(lines)  # 변환된 코드를 얻기
        print("\n변환된 코드:")
        print(transpiled_code)  # 변환된 코드 출력
        
        print("\n실행 결과:")
        execute_python_code(transpiled_code)  # 변환된 코드를 실행하기
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
