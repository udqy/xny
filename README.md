# xny
Learn X in Y minutes for the CLI

Quick setup for testing:
```bash
git clone https://github.com/udqy/xny.git
cd xny
python -m venv .venv
source venv/bin/activate    # for windows: use venv\Scripts\activate
pip install -r requirements.txt
python xny/cli.py --update
```

Example Usage:
```bash
python xny/cli.py javascript
```

As of now:
- Uses the default pager to display content
- Uses fzf to choose between choices
- Works on Linux (and WSL)
- Requires installing [fzf](https://github.com/junegunn/fzf)
- Requires running with '--update' option on first use  


To Implement:
- [ ] Implement a custom Pager using Textual
- [ ] Implement searching in the pager
- [ ] Implement a custom fzf window 
- [ ] Make cross platform
