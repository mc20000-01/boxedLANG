def to_py(code_json):
    py = "import time\n\n"

    for stmt in code_json:
        cmd = stmt.get('cmd')
        args = stmt.get('args', [])

        if cmd == "say":
            if not args:
                py += "print()\n"
                continue

            text = args[0]

            if isinstance(text, (int, float)):
                py += f"print({text})\n"
            elif isinstance(text, str):
                escaped = text.replace('\\', '\\\\').replace('"', '\\"')
                py += f'print("{escaped}")\n'
            else:
                py += f"print({repr(text)})\n"
            if len(args) > 1:
                delay = args[1]
                try:
                    delay = float(delay)
                    py += f"time.sleep({delay})\n"
                except:
                    pass

        elif cmd == "ask":
            prompt = '""'
            if args and isinstance(args[0], str):
                escaped = args[0].replace('\\', '\\\\').replace('"', '\\"')
                prompt = f'"{escaped}"'
            py += f"input({prompt})\n"

    py += '\ninput("\\nPress Enter to close this window...")\n'

    return py