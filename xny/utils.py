from subprocess import Popen, PIPE
from pathlib import Path
from display import display

def fzf(matches):    
    path_map = {Path(path).stem: path for path, _ in matches}
    display_names = '\n'.join(path_map.keys())
    
    try:
        fzf_process = Popen(['fzf'], stdin=PIPE, stdout=PIPE, text=True)
        output, _ = fzf_process.communicate(input=display_names)
        selected_name = output.strip()
        
        if selected_name:
            selected_path = path_map[selected_name]
            display(selected_path)
            
    except FileNotFoundError:
        print("|--> fzf command not found. Please install fzf.")
        return None
    