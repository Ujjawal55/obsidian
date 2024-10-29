# Grep

**Defination** : it stand for **'Global Regular Expression print'**.

**Structure** : grep `<what to search for>` `<where to search for>`.

- **global** : it search through the entire file.
- **regular expression** : it searches the `<string>`.
- **print** : it prints the line containing the patterns.

### Flags:

- **-i** : ignore casing.
- **-v** : Invert the matching ("print the character which does not match").
- -r : Recussively search directories for files containing the pattern.
- **-n** : show the line number along with the line.
- **-c** : count of the number of lines instead of the lines itself.
- **-l** : list only the name of files.
- **-h** : supress the prefix name of the files in output.
- **-w** : match the whole pattern.

# cat/head/tail/more/less

**Defination** : this command help to view the content of the file.

**Structure** :

> **cat** `<filename>` : list the content of the file in terminal.

> **head** `<filename>` : list the first 10 lines from the file.
>
> - -n `<number>` `<filename>` : list that `<number>` of line form the `<file>`.

> **tail** `<filename>` : list the last 10 lines from the file.
>
> - -n `<number>` `<filename>` : list that `<number>` of line form the `<file>`.

> **more** `<filename>`: list the one page content at a time and more if we **press**`<space>`.

# Pipe

**Defination** : it pipe the output of the previously executed command to the input of the next command.

**Structure** : `<command1>`|`</command2`

# pushd and popd

**Defination** : pushd and popd works similar to the push and pop of stack data structure.

> **pushd** : push the directory to the stack and.

> **popd** : remove the directory from the stack.

> you will be in the directory that is at the top of the stack.

> to view the stack we can use the we can view `<dirs -v>`.

**Structure** : pushd `<directory-name>` , popd

# Redirection operator

**Defination** : help to redirect either the stdout/stdin/stderror

**Structure** : `<content>` `<redirection-operator` `<location>`

#### Functionality

> `>` : overwrite the `<location>` with the `<content>` — **content should be stdout**

> `>>` : append the `<content>` to the `<location>` — **content should be stdout**

> `2>` : redirect the `<error>` to the `<location>`

##### Example

```bash
ls -a > output.txt 2>&1 #this append the stdout and error(if any) to the output.txt file.
```

# ls

**Defination**: list all the content in the present directory.

### Flags/Additional

- **-a** : list all the files including the hidden.
- **`<char>*`** : list all the files that have the `<char>` in the name.
- **`*.<extension>`** : list all the files that end the this `<extension>`.
- **`[[<char><char>]]*`** : list all the files that has either of the character in them.
- **`[[:upper:]]*`** : list all the files that starts with the uppercase.
- **`[[:lower:]]*`** : list all the files that starts with the lowercase.

# find

**Defination**: find a pattern in the specified directory and all of its sub-directories

**Structure** : find `[path]` -name `[pattern]`

### Additional

- **-iname** : list all the files regardless of the case sensitivity.
- **-type <d/f>** : filter the directory for d and files for f in the path specified.

#### Example

```bash
find . -type d #this will list all the directory in the current directory
```

# Permission and Owner
