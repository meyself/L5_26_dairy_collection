| Issue | Tool / Code | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|---|
| SQL injection | Bandit B608 (Medium) | Security | 11 | INSERT query built with `.format()` | Parameterised query with `?` placeholders |
| Weak MD5 hash | Bandit B324 (High) | Security | 16 | `hashlib.md5` is insecure for security use | Switched to `hashlib.sha256` |
| Shell command injection | Bandit B605 (High) | Security | 31 | `os.system("echo ..." + farmer)` runs a shell command built from input | Replaced with `print()` |
| Unused imports | Flake8 F401 / Pylint W0611 | Style | 2, 3 | `json` and `os` imported but never used | Removed both imports |
| Line too long | Flake8 E501 | Style | 7, 11, 20, 25 | Lines exceed 79 characters | Wrapped across multiple lines |
| Ambiguous variable name | Flake8 E741 | Style | 26 | Variable `l` looks like `1` | Renamed to `top` |
| Comparison to None | Flake8 E711 / Pylint C0121 | Bug | 36 | `fat == None` used for None check | Changed to `fat is None` |
| camelCase function names | Pylint C0103 | Style | 10, 15, 19, 24, 30, 34 | Function names not in snake_case | Renamed to snake_case |
| Redefined outer name `conn` | Pylint W0621 | Design | 10, 19, 24, 34 | Global `conn` shadowed by function parameters | Moved creation into `create_connection()` and `main()` |
| Missing docstrings | Pylint C0114 / C0116 | Style | Module and all functions | No module or function documentation | Added docstrings |
| `max()` on empty table | Robustness | Bug | 26 | Would raise an error when there are no rows | Added `default=None` |
