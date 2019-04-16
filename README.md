# todocli
Simple, CLI based TODO list, written in python.<br/>
<br/>
## Usage
Required for running todocli: python3 os, os.path, sys, bash, linux or macOS (wasn't tested on macOS) <br/> <br/>
Download and run (using terminal, in home-dir(~ or $HOME)): 
```
git clone https://github.com/LukyIsHere/todocli
cd todocli
python3 main.py
```
<br/>
Commands:<br/>
 help / h  - shows manual <br/>
 new / n  - adds new TODO line<br/>
 read / r  - prints all TODO lines<br/>
 show / s  - clears screen and prints all TODO lines<br/>
 delete / del  - clears TODO list<br/>
 uncheck / uc  - unchecks TODO line<br/>
 check / cc  - checks TODO line<br/>
<br>

## Configuration

Written in python.<br/><br/>
Things to configure ('config.py'):
```
unfinished = "insert_unchecked_symbol_here"
finished = "insert_checked_symbol_here"
notes_path = "insert_notes_path_here"
hlp_path = "insert_help_path_here"
title = "insert_title_of_TODOlist_here"
```
