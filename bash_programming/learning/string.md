# cut

**Structure** : cut -d'delimiter' -field

- **_delimiter_** : is character around the string will be cut
- **field** : each cut is consider as field starting form 1
  **_Example_**

  ```bash
  var='hello-new-world'
  echo "$var" | cut'-' -f1-
  : '
    '-' : this is used as a point to split the string
      output:
      field f1: hello
      field f2: new
      field f3: world
    'f' : this stand for field
    'f1' : this stand for the first field
    'f1-' : - stand for 1 to all the way to the end

    OUTPUT:
      hellonewworld

  '
  ```
