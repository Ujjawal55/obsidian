### PTR

- single quote and double quote are treated differently
  - if want to print the value of a variable use double quote. **_ special note: "$variable_name" this will return the value of the variable _**.
- excute the command and grab the value in the variable has different syntax

```bash
#!bin/bash

hello_message='hello, world'
readonly var='it value does not change during the program'
command_variable=$(pwd)

echo '$hello_message $var $command_variable'
echo "$hello_message $var $command_variable"

```
