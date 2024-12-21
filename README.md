# xny
Learn X in Y minutes for the CLI

## To-Do

### 1. **Maintain Cache**  
- [ ] Require user to run `--update` on install.  
- [ ] On `--update`, clone the repository to a specified location.  
- [ ] Remove all files except markdown files.  
- [ ] Parse the Markdown files to retain only the important content.  

### 2. **Search**  
- [ ] Allow searching with `xny <term>`.  
- [ ] Implement fuzzy search for `<term>`.  
- [ ] Display content from the relevant file for `<term>`.  
- [ ] Use the default pager (e.g., `less`) to show the content.  

### 3. **Fzf Integration**  
- [ ] Run without any arguments to start `fzf` (requires `fzf` installed).  
- [ ] Add support for `xny --fzf` to enable fuzzy finder mode.  

