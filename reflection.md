1. Which issues were the easiest to fix, and which were the hardest?
The easiest issues to fix were the stylistic ones such as unused imports, naming conventions, and string formatting. The hardest issue was identifying the correct exception types for the bare `except:` block because it required understanding what kind of errors the code could realistically raise.

2. Did the static analysis tools report any false positives?
Yes, one minor false positive was reported by Flake8 for missing blank lines, which didn’t affect the program’s behavior. While technically valid for style, it wasn’t a functional issue.

3. How would you integrate static analysis tools into your actual software development workflow?
I would integrate Bandit, Flake8, and Pylint into a Continuous Integration (CI) pipeline, so that every commit is automatically scanned. Locally, I would run these tools before pushing code to ensure consistent code quality and security.

4. What tangible improvements did you observe after applying the fixes?
The code is now cleaner, safer, and easier to understand. It handles errors more gracefully, avoids potential data leaks or crashes, and conforms to Python’s best practices. Using static analysis tools improved both reliability and maintainability of the program.
