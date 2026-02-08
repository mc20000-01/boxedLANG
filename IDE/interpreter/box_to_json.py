def pull_cmd_from(box_line, ln=0):
    data = box_line.split(" ")
    cmd = data[0]  # gets command from box standard
    if cmd.startswith("[=") and cmd.endswith("=]"):
        return {"cmd": "null", "args": ["comment"], "ln": ln, "marks": {}}

    if cmd == "premark":
        marks = {data[1]: ln + 1}
    else:
        marks = {}

    args = data[-1].split("|")
    return {"cmd": cmd, "args": args, "ln": ln, "marks": marks}


def make_code_from(code):
    made_code = [{'cmd': 'null', 'args': ['start'], 'ln': 0, 'marks': {}}]
    for ln, l in enumerate(code.splitlines()):
        cur_line = l.strip()
        if not cur_line:
            continue
        cur_line_json = pull_cmd_from(cur_line, ln=ln)
        made_code.append(cur_line_json)
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
            line += a + "|"
        line = line[:-1] + "\n"
        code += line
    return code

