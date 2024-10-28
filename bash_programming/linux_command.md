# Grep Command

**Defination** : it stand for **'Global Regular Expression print'**.

**Structure** : grep `<what to search for>` `<where to search for>`

- **global** : it search through the entire file
- **regular expression** : it searches the `<string>`
- **print** : it prints the line containing the patterns

### Flags:

- **-i** : ignore casing
- **-v** : Invert the matching ("print the character which does not match")
- -r : Recussively search directories for files containing the pattern
- **-n** : show the line number along with the line
- **-c** : count of the number of lines instead of the lines itself
- **-l** : list only the name of files
- **-h** : supress the prefix name of the files in output.
- **-w** : match the whole pattern

# Pipe Command

**Defination** : it pipe the output of the previously executed command to the input of the next command

**Structure** : `<command1>`|`</command2`
