# 🚀 Grant Suite Repository Consolidation

A complete solution for consolidating multiple grant-related repositories into a single master repository with each old repo preserved as its own branch.

## 📋 Overview

This consolidation preserves **full commit history** from each source repository while organizing them into a clean, maintainable structure.

### Source Repositories

The following repositories will be consolidated:

1. `grant_t_v2_separate` → branch: `grant_t_v2_separate`
2. `grant_training_v2` → branch: `grant_training_v2`
3. `grant_training` → branch: `grant_training`
4. `grants-training-suite-main` → branch: `grants_training_suite_main`
5. `grant-training-suit` → branch: `grant_training_suit`

### Target Architecture

```
grant_training_consolidate/
 ├─ main
 ├─ grant_t_v2_separate
 ├─ grant_training_v2
 ├─ grant_training
 ├─ grants_training_suite_main
 └─ grant_training_suit
```

## 🎯 Quick Start

### Step 1: Create the Consolidated Repository on GitHub

1. Go to GitHub and create a new repository named `grant_training_consolidate`
2. Choose public or private as needed
3. **Do NOT** initialize with README, .gitignore, or license

### Step 2: Clone and Run the Script

```bash
# Clone the new empty repository
git clone git@github.com:sabryyoussef/grant_training_consolidate.git
cd grant_training_consolidate

# Copy the consolidation script into the repo
cp /path/to/consolidate_repos.sh .

# Run the script
./consolidate_repos.sh
```

The script will:
- ✅ Add each old repository as a remote
- ✅ Fetch all commits and history
- ✅ Create a new branch for each repo
- ✅ Push branches to the consolidated repository
- ✅ Clean up temporary remotes
- ✅ Provide detailed progress updates

## 📝 Manual Process (Alternative)

If you prefer to run the consolidation manually:

```bash
# For each repository, repeat this pattern:

# 1. Add the old repo as a remote
git remote add <remote_name> git@github.com:sabryyoussef/<repo_name>.git

# 2. Fetch all commits
git fetch <remote_name>

# 3. Create a new branch from the remote
git checkout -b <branch_name> <remote_name>/main

# 4. Push the branch to origin
git push origin <branch_name>

# 5. Remove the temporary remote
git remote remove <remote_name>
```

### Example for `grant_training_v2`:

```bash
git remote add grant_training_v2 git@github.com:sabryyoussef/grant_training_v2.git
git fetch grant_training_v2
git checkout -b grant_training_v2 grant_training_v2/main
git push origin grant_training_v2
git remote remove grant_training_v2
```

## 🔧 Post-Consolidation Operations

### View All Branches

```bash
git branch -a
```

### Switch Between Branches

```bash
git checkout grant_training_v2
git checkout grants_training_suite_main
```

### Optional: Reorganize Files Into Subfolders

If branches have conflicting top-level files, you can reorganize each branch:

```bash
# Switch to the branch
git checkout grant_training_v2

# Create a subfolder and move all files
mkdir grant_training_v2
git mv * grant_training_v2/ 2>/dev/null || true

# Handle hidden files separately
shopt -s dotglob
for file in .[!.]* ..?*; do
  [ -e "$file" ] && [ "$file" != ".git" ] && git mv "$file" grant_training_v2/
done
shopt -u dotglob

# Commit the reorganization
git commit -m "Reorganize repo into subfolder"
git push origin grant_training_v2
```

### Optional: Create a Unified Main Branch

If you want to merge all branches into a single working tree:

```bash
git checkout main

# Merge each branch using subtree strategy
git merge -s ours --no-commit --allow-unrelated-histories grant_t_v2_separate
git read-tree --prefix=grant_t_v2_separate/ -u grant_t_v2_separate
git commit -m "Merge grant_t_v2_separate as subtree"

# Repeat for other branches...
```

## 🛡️ Features of the Automated Script

- **Error Handling**: Gracefully handles missing branches or fetch failures
- **Progress Tracking**: Clear visual feedback with color-coded output
- **Safety Checks**: Confirms before making changes
- **Branch Detection**: Auto-detects main/master branch names
- **Duplicate Handling**: Prompts before overwriting existing branches
- **Cleanup**: Automatically removes temporary remotes

## 📊 Script Output Example

```
=============================================================================
[1/5] Processing: grant_t_v2_separate
=============================================================================
▶ Adding remote 'grant_t_v2_separate'...
✓ Remote added
▶ Fetching from grant_t_v2_separate...
✓ Fetch complete
▶ Creating branch 'grant_t_v2_separate'...
✓ Branch created from main
▶ Pushing branch to origin...
✓ Branch pushed to origin
▶ Cleaning up remote...
✓ Remote removed
```

## ⚠️ Important Notes

1. **Preserve History**: All commit history is preserved in each branch
2. **No Data Loss**: Original repositories remain unchanged on GitHub
3. **Branch Independence**: Each branch is completely isolated
4. **SSH Keys**: Ensure your SSH keys are set up for GitHub access
5. **Permissions**: You need push access to the consolidated repository

## 🔍 Troubleshooting

### Issue: "Permission denied (publickey)"

**Solution**: Set up SSH keys for GitHub
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub  # Add this to GitHub Settings → SSH Keys
```

### Issue: "Branch already exists"

**Solution**: The script will prompt you to recreate it, or you can manually delete:
```bash
git branch -D <branch_name>
git push origin --delete <branch_name>
```

### Issue: "No main or master branch found"

**Solution**: Some repos might use different default branch names. Update the script or manually specify:
```bash
git checkout -b <branch_name> <remote_name>/<actual_branch_name>
```

## 📚 Additional Resources

- [Git Subtree Merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging#_subtree_merge)
- [Managing Multiple Repositories](https://docs.github.com/en/repositories)
- [Git Remote Documentation](https://git-scm.com/docs/git-remote)

## 🎉 Success Criteria

After running the consolidation:
- ✅ All 5 repositories exist as separate branches
- ✅ Full commit history is accessible in each branch
- ✅ All branches are pushed to origin
- ✅ You can switch between branches freely
- ✅ Original repositories remain untouched

## 📧 Support

If you encounter issues, check:
1. SSH key access to GitHub
2. Repository permissions
3. Network connectivity
4. Git version (2.x+ recommended)

---

**Created**: 2025-11-18  
**Purpose**: Enterprise-grade repository consolidation  
**Status**: Production Ready ✨

