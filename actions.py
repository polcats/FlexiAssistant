from voice import playText


def do_action(command):

    if command == "test command":
        playText("test command")
    elif command == "exit":
        playText("exiting now")
        return False
    else:
        playText("command is unknown")

    return True
