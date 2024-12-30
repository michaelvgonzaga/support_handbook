# Git Error Handling

## Purpose
Identify and resolve common Git errors.

### Common Errors
1. **Detached HEAD**:
   - **Cause**: Checked out a commit instead of a branch.
   - **Solution**:
     ```bash
     git checkout <branch-name>
     ```

2. **Merge Conflicts**:
   - **Cause**: Conflicts between branches.
   - **Solution**:
     1. Open conflicting files.
     2. Resolve conflicts manually.
     3. Stage the changes:
        ```bash
        git add <file>
        ```
     4. Commit the merge:
        ```bash
        git commit
        ```

3. **Authentication Issues**:
   - **Cause**: Incorrect credentials.
   - **Solution**:
     - Update credentials:
       ```bash
       git config --global credential.helper cache
       ```

