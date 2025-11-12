# Git Workshop

Welcome to the Git Workshop! This hands-on workshop will teach you essential Git skills through practical exercises.

## Prerequisites

- Git installed on your system
- A GitHub account
- Basic command line knowledge

## Workshop Exercises

### Exercise 1: Basic Git Operations

**Objective**: Learn fundamental Git commands

1. Check your Git installation:
   ```bash
   git --version
   ```

2. Configure your Git identity:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

3. Check your repository status:
   ```bash
   git status
   ```

4. View commit history:
   ```bash
   git log
   git log --oneline
   ```

### Exercise 2: Making Changes and Committing

**Objective**: Practice the Git workflow

1. Make a change to `app.py` (add a new function or modify existing code)

2. Check what changed:
   ```bash
   git diff
   ```

3. Stage your changes:
   ```bash
   git add app.py
   ```

4. Commit your changes:
   ```bash
   git commit -m "Your descriptive commit message"
   ```

5. View your commit in the history:
   ```bash
   git log -1
   ```

### Exercise 3: Branching

**Objective**: Learn to work with branches

1. View all branches:
   ```bash
   git branch
   ```

2. Create a new branch:
   ```bash
   git branch feature/new-feature
   ```

3. Switch to your new branch:
   ```bash
   git checkout feature/new-feature
   # or use the shorthand:
   # git checkout -b feature/new-feature
   ```

4. Make changes and commit them on this branch

5. Switch back to main:
   ```bash
   git checkout main
   ```

6. Notice your changes aren't on main (check the files)

### Exercise 4: Merging Branches

**Objective**: Combine changes from different branches

1. Ensure you're on the main branch:
   ```bash
   git checkout main
   ```

2. Merge your feature branch:
   ```bash
   git merge feature/new-feature
   ```

3. View the updated history:
   ```bash
   git log --oneline --graph
   ```

4. Delete the feature branch (cleanup):
   ```bash
   git branch -d feature/new-feature
   ```

### Exercise 5: Handling Merge Conflicts

**Objective**: Learn to resolve conflicts

1. Create two branches:
   ```bash
   git checkout -b branch-a
   # Make a change to app.py line 10
   git commit -am "Change from branch A"

   git checkout main
   git checkout -b branch-b
   # Make a DIFFERENT change to app.py line 10
   git commit -am "Change from branch B"
   ```

2. Merge branch-a into main:
   ```bash
   git checkout main
   git merge branch-a
   ```

3. Try to merge branch-b (this will create a conflict):
   ```bash
   git merge branch-b
   ```

4. Resolve the conflict:
   - Open the conflicted file
   - Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
   - Edit to keep the desired changes
   - Remove conflict markers

5. Complete the merge:
   ```bash
   git add app.py
   git commit -m "Resolve merge conflict"
   ```

### Exercise 6: Undoing Changes

**Objective**: Learn different ways to undo work

1. **Unstage a file**:
   ```bash
   git add app.py
   git reset app.py
   ```

2. **Discard working directory changes**:
   ```bash
   # Be careful - this discards changes!
   git checkout -- app.py
   ```

3. **Amend the last commit**:
   ```bash
   git commit --amend -m "Updated commit message"
   ```

4. **Revert a commit** (creates a new commit):
   ```bash
   git revert HEAD
   ```

5. **Reset to a previous commit**:
   ```bash
   # Soft reset (keeps changes staged)
   git reset --soft HEAD~1

   # Mixed reset (keeps changes unstaged)
   git reset HEAD~1

   # Hard reset (discards changes - BE CAREFUL!)
   git reset --hard HEAD~1
   ```

### Exercise 7: Working with Remote Repositories

**Objective**: Learn to sync with GitHub

1. View remote repositories:
   ```bash
   git remote -v
   ```

2. Add a remote (if not already added):
   ```bash
   git remote add origin https://github.com/yourusername/repo-name.git
   ```

3. Push your changes:
   ```bash
   git push origin main
   ```

4. Create and push a new branch:
   ```bash
   git checkout -b feature/remote-test
   # Make some changes
   git push -u origin feature/remote-test
   ```

5. Fetch remote changes:
   ```bash
   git fetch origin
   ```

6. Pull remote changes:
   ```bash
   git pull origin main
   ```

### Exercise 8: Git Tags

**Objective**: Learn to create and manage tags

1. Create a lightweight tag:
   ```bash
   git tag v1.0.0
   ```

2. Create an annotated tag:
   ```bash
   git tag -a v1.1.0 -m "Version 1.1.0 release"
   ```

3. List all tags:
   ```bash
   git tag
   ```

4. Push tags to remote:
   ```bash
   git push origin v1.0.0
   # or push all tags:
   git push origin --tags
   ```

5. Checkout a specific tag:
   ```bash
   git checkout v1.0.0
   ```

### Exercise 9: GitHub Actions Workflow

**Objective**: Create a CI/CD pipeline using GitHub Actions

GitHub Actions allows you to automate workflows like testing, building, and deploying your code.

1. Create a workflow directory:
   ```bash
   mkdir -p .github/workflows
   ```

2. Create a workflow file `.github/workflows/python-app.yml`:
   ```yaml
   name: Python Application CI

   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]

   jobs:
     test:
       runs-on: ubuntu-latest

       steps:
       - uses: actions/checkout@v3

       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.9'

       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt

       - name: Run tests
         run: |
           python -m pytest test_app.py -v
   ```

3. Commit and push the workflow:
   ```bash
   git add .github/workflows/python-app.yml
   git commit -m "Add GitHub Actions CI workflow"
   git push origin main
   ```

4. Check the Actions tab on GitHub to see your workflow run

5. **Exercise**: Modify the workflow to:
   - Run on multiple Python versions (3.8, 3.9, 3.10)
   - Add a linting step using `flake8`
   - Add a code coverage step
   - Only run on pull requests to main

6. **Bonus**: Create a second workflow that:
   - Runs on tags (releases)
   - Builds a Docker image
   - Publishes the package to PyPI (test PyPI)

### Exercise 10: Advanced Git History

**Objective**: Master Git history navigation and manipulation

1. View detailed commit history:
   ```bash
   git log --graph --oneline --all --decorate
   ```

2. Search commit history:
   ```bash
   git log --grep="keyword"
   git log --author="Your Name"
   ```

3. View changes in a specific commit:
   ```bash
   git show <commit-hash>
   ```

4. Interactive rebase (rewrite history):
   ```bash
   git rebase -i HEAD~3
   ```

5. Cherry-pick a commit from another branch:
   ```bash
   git cherry-pick <commit-hash>
   ```

## Project Files

- `app.py` - Main application file
- `test_app.py` - Unit tests
- `version.py` - Version information
- `requirements.txt` - Python dependencies
- `broken_feature.py` - File with intentional issues for practice
- `bugfix.md` - Notes about bugs

## Tips and Best Practices

1. **Commit Often**: Make small, logical commits
2. **Write Good Commit Messages**: Be descriptive and clear
3. **Use Branches**: Keep main branch clean, work on feature branches
4. **Pull Before Push**: Always sync with remote before pushing
5. **Review Before Committing**: Use `git diff` and `git status`
6. **Don't Commit Sensitive Data**: Use `.gitignore` for secrets
7. **Test Before Merging**: Ensure code works before merging to main

## Common Git Commands Reference

```bash
# Status and Info
git status                  # Check current status
git log                     # View commit history
git diff                    # See changes

# Basic Operations
git add <file>              # Stage changes
git commit -m "message"     # Commit changes
git push                    # Push to remote
git pull                    # Pull from remote

# Branching
git branch                  # List branches
git branch <name>           # Create branch
git checkout <branch>       # Switch branch
git merge <branch>          # Merge branch

# Undoing
git reset <file>            # Unstage file
git checkout -- <file>      # Discard changes
git revert <commit>         # Revert commit
git reset --hard <commit>   # Reset to commit (dangerous!)

# Remote
git remote -v               # View remotes
git fetch                   # Fetch changes
git pull                    # Fetch and merge
git push                    # Push changes
```

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Oh My Git! (Interactive Game)](https://ohmygit.org/)

## Getting Help

If you're stuck:
1. Check `git --help` or `git <command> --help`
2. Review the exercises above
3. Ask your instructor
4. Search online (Stack Overflow, Git documentation)

Happy Git-ing!
