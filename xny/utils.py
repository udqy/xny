def fzf(matches):
    from subprocess import Popen, PIPE
    from pathlib import Path
    
    print("|--> Running fzf")
    match_strings = '\n'.join([Path(path).stem for path, _ in matches])

    try:
        fzf_process = Popen(['fzf'], stdin=PIPE, stdout=PIPE, text=True)
        output, _ = fzf_process.communicate(input=match_strings)
        selected = output.strip()
    except FileNotFoundError:
        print("|--> fzf command not found. Please install fzf.")
        return None

    return selected