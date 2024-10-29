### Syntax

**Structure**

```bash
if test-expression; then
    # do something here
    command1
    command2
else
    # do something else
    command3
    command4
fi
```

### Test Expression

**Structure** : `[ expression inside ]`

## NOTE

> $(something) will take the value of the that thing without $ it is treated a string literal.

> ((...)) -> this is called the arithmetic expansion that perform arithmetic evaluation inside and return the answer
> variable inside can be used without $.
