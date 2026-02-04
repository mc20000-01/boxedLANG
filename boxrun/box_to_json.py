def pull_cmd_from(box_line, ln=0):
    data = box_line.split(" ")
    cmd = data[0] #gets command from box standard
    lenth = len(data)
    args = data[lenth - 1].split("|") #splits args from box standerd
    json = {"cmd": cmd,"args": args, "ln": ln} #makes the json to be run / decoeded further
    return json

def make_code_from(code):
    made_code = [{'cmd': 'null', 'args': ['start'], 'ln': 0},]
    code = code.splitlines()
    for l in code:
        cur_line = l
        cur_line_json  = pull_cmd_from(cur_line, ln=code.index(l))
        made_code = made_code  + [cur_line_json]
    return made_code

def mk(code):
    return make_code_from(code)

def undo_mk(boxed_code):
    code = ""
    for l in boxed_code:
        cmd = l['cmd']
        args = l['args']
        line = cmd + " "
        for a in args:
            line = line + a + "|"
        line = line[:-1] + "\n"
        code = code + line
    return code
