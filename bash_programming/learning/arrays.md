# NOTE: Important symbol

- **_#_** : no. of symbol
- **_`<array-name>`_** : represent the first element of the array
- **_${array-syntax}_** : without the curly bracket it is treated as string literals.
- **_`!<arry-name[@]>`_** : return the array of indices of the array-specified.

### Example

```bash

#!/bin/bash

var='hello'
arr=("hello, world")

echo $var
echo $arr[0]

: '

Output
hello
hello, world[0]

'

```

# Bash Arrays: Complete Guide

## Array Declaration and Initialization

### Basic Array Declaration

```bash
# Method 1: Declare and initialize separately
declare -a my_array    # Declare indexed array
my_array=(1 2 3 4 5)   # Initialize

# Method 2: Direct initialization
fruits=("apple" "banana" "orange")

# Method 3: Associative array (key-value pairs)
declare -A user_info
user_info=([name]="John" [age]=25)
```

## Accessing Array Elements

### Basic Access Operations

```bash
# Access single element
echo ${fruits}     # First element
echo ${fruits[-1]}    # Last element

# Print all elements
echo ${fruits[@]}     # All elements
echo ${fruits[*]}     # Alternative syntax

# Print array length
echo ${#fruits[@]}    # Number of elements

# Print element length
echo ${#fruits}    # Length of first element
```

## Array Operations

### Adding Elements

```bash
# Append to array
fruits+=("grape")

# Add at specific index
fruits="mango"
```

### Removing Elements

```bash
# Remove single element
unset fruits

# Remove entire array
unset fruits
```

## Array Slicing

### Slice Syntax

```bash
# Slice array (offset/length)
echo ${fruits[@]:1:2}    # Elements from index 1, length 2

# From index to end
echo ${fruits[@]:2}      # Elements from index 2 to end
```

## Array Iteration

### Different Ways to Iterate

```bash
# Method 1: Using index
for i in "${!fruits[@]}"; do
    echo "Index $i: ${fruits[$i]}"
done

# Method 2: Direct elements
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done
```

## Array Manipulation

### Common Operations

```bash
# Copy array
new_fruits=("${fruits[@]}")

# Merge arrays
combined=("${fruits[@]}" "${vegetables[@]}")

# Find index of element
for i in "${!fruits[@]}"; do
    if [[ "${fruits[$i]}" == "apple" ]]; then
        echo "Found at index $i"
    fi
done
```

## Associative Array Operations

### Working with Key-Value Pairs

```bash
# Declare associative array
declare -A user_data

# Add/update elements
user_data[name]="John"
user_data[age]=30

# Access elements
echo ${user_data[name]}

# List all keys
echo ${!user_data[@]}

# Iterate over key-value pairs
for key in "${!user_data[@]}"; do
    echo "Key: $key, Value: ${user_data[$key]}"
done
```

## Important Notes

1. Arrays in Bash are zero-based
2. Always quote array expansions to handle spaces
3. Use `[@]` instead of `[*]` to preserve whitespace in elements
4. Associative arrays require Bash 4.0 or later

## Common Use Cases

1. **Processing Multiple Files:**

```bash
files=( *.txt )
for file in "${files[@]}"; do
    echo "Processing $file"
done
```

2. **Storing Command Output:**

```bash
# Store command output in array
lines=( $(cat file.txt) )
```

3. **Building Command Arguments:**

```bash
opts=(-v -H "Content-Type: text/plain")
curl "${opts[@]}" http://example.com
```
