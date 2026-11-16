# Static Code Analysis — Issue Table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk | Security — Medium | 10 | SQL query constructed using string interpolation, which may allow SQL injection. | Use parameterized SQL queries with placeholders and pass values separately. |
| Mutable default argument | Code quality / Bug | 9 | `audit=[]` creates a shared mutable default list across function calls. | Use `audit=None` and initialize a new list inside the function. |
| Shell command execution | Security — Low | 26 | `os.system()` starts a shell process unnecessarily for printing a message. | Replace shell execution with a normal Python operation. |
| Swallowed exception | Code quality / Security — Low | 27–28 | A broad exception is caught and ignored using `pass`, hiding potential errors. | Remove unnecessary exception handling or handle specific expected errors meaningfully. |
| Missing docstrings | Code quality | 1, 9, 15, 24, 31, 37 | The module and functions lack explanatory docstrings. | Add a module docstring and descriptive docstrings to functions. |
| Incorrect naming convention | Code quality | 6, 31 | `disbursed_total` and `bySchemeCount` do not follow the expected naming conventions. | Use an appropriate uppercase constant name or local variable and rename the function to `by_scheme_count`. |
| Incorrect None comparison | Code quality / Style | 32 | Uses `scheme == None` instead of the recommended identity comparison. | Change the condition to `scheme is None`. |
| Long lines | Style | 5, 10, 17, 19, 34 | Several lines exceed the configured Flake8 line-length limit. | Split long statements across multiple lines. |

## Verification

The issues above were identified from the original Pylint, Bandit and Flake8 reports. After fixing the code, rerun all three tools and update this table if the final results differ.