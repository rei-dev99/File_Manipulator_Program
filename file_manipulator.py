commands = input("実行したいコマンドと引数を空白で空けて入力してください。").split()
action = commands[0]
input_path = commands[1]
option = commands[2]
convert = commands[3] if len(commands) > 3 else None

def reverse(input_path, output_path):
    with open(input_path, "r") as f_input:
        contents = f_input.read()
        
    with open(output_path, "w") as f_output:
        f_output.write(contents[::-1])
        
def copy(input_path, output_path):
    with open(input_path, "r") as f_input:
        contents = f_input.read()
        
    with open(output_path, "w") as f_output:
        f_output.write(contents)
        
def duplicate_contents(input_path, n):
    with open(input_path, 'r') as f_input:
        contents = f_input.read()

    with open(input_path, 'a') as f_input:
        for _ in range(int(n)):
            f_input.write(contents)
            
def replace_string(input_path, needle, newstring):
    with open(input_path, 'r') as f_input:
        contents = f_input.read()
        
    replace_contents = contents.replace(needle, newstring)

    with open(input_path, 'w') as f_input:
        f_input.write(replace_contents)

if action == "reverse":
    reverse(input_path, option)
    print("反転出力が完了しました。")
elif action == "copy":
    copy(input_path, option)
    print("コピーが完了しました。")
elif action == "duplicate-contents":
    duplicate_contents(input_path, option)
    print("入力された回数の複製が完了しました。")
elif action == "replace-string":
    replace_string(input_path, option, convert)
    print("needleをnewstringへの置き換えが完了しました。")
else:
    print("メソッドが見つかりません。")