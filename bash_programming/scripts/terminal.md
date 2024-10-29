#### small command to zip all the mp4 files

```bash
# working of the command
# command search for all the file with .mp4 extension (ls "*.mp4" list all the names only)
# then pipe all the files to the zip comamnd ("-" : tell the zip to read from stdin and "@": tell to read the files)
find . -name "*.mp4" -type f | zip file.zip -@
```

```

```
