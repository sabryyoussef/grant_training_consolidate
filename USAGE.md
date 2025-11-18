# 🎯 Usage Guide - Grant Suite Consolidation

## 📦 What You Have

This directory contains a complete enterprise-grade solution for consolidating your grant repositories.

### Files Included

1. **consolidate_repos.sh** - Main automation script
2. **verify_consolidation.sh** - Verification script
3. **reorganize_branch.sh** - Branch file reorganization helper
4. **README.md** - Complete documentation
5. **QUICK_REFERENCE.md** - Command cheat sheet
6. **USAGE.md** - This file

---

## 🚀 Quick Start (3 Steps)

### Step 1: Create Repository on GitHub

Go to GitHub and create a new repository named **grant_training_consolidate**

```
https://github.com/new

Repository name: grant_training_consolidate
Description: Consolidated grant repositories
Public or Private: Your choice
✗ Do NOT initialize with README
```

### Step 2: Clone and Setup

```bash
# Clone the new repository
git clone git@github.com:sabryyoussef/grant_training_consolidate.git
cd grant_training_consolidate

# Copy these consolidation scripts
cp ~/grant_training_consolidate/*.sh .
cp ~/grant_training_consolidate/.gitignore .
```

### Step 3: Run Consolidation

```bash
# Execute the consolidation script
./consolidate_repos.sh

# Verify everything worked
./verify_consolidation.sh
```

**That's it!** All 5 repositories are now consolidated as branches.

---

## 📚 Complete Workflow

### Phase 1: Initial Setup (5 minutes)

```bash
# 1. Create repo on GitHub (manual)
# 2. Clone locally
git clone git@github.com:sabryyoussef/grant_training_consolidate.git
cd grant_training_consolidate

# 3. Copy scripts
cp ~/grant_training_consolidate/*.sh .
cp ~/grant_training_consolidate/.gitignore .

# 4. Make scripts executable (if not already)
chmod +x *.sh
```

### Phase 2: Consolidation (10-15 minutes)

```bash
# Run the main consolidation script
./consolidate_repos.sh

# It will:
# - Fetch all 5 repositories
# - Create branches with full history
# - Push everything to origin
# - Clean up temporary remotes
```

**What happens:**
- `grant_t_v2_separate` → branch `grant_t_v2_separate`
- `grant_training_v2` → branch `grant_training_v2`
- `grant_training` → branch `grant_training`
- `grants-training-suite-main` → branch `grants_training_suite_main`
- `grant-training-suit` → branch `grant_training_suit`

### Phase 3: Verification (2 minutes)

```bash
# Run verification
./verify_consolidation.sh

# Should show:
# ✓ All repositories successfully consolidated!
# ✓ All branches are accessible
# ✓ Commit history preserved
```

### Phase 4: Optional Reorganization

If branches have conflicting files, reorganize each:

```bash
# For each branch
git checkout grant_training_v2
./reorganize_branch.sh
# Follow prompts

# Repeat for other branches as needed
git checkout grants_training_suite_main
./reorganize_branch.sh
```

---

## 🎮 Daily Operations

### Working with Branches

```bash
# List all branches
git branch -a

# Switch to a branch
git checkout grant_training_v2

# View branch files
ls -la

# View commit history
git log --oneline --graph

# Compare two branches
git diff grant_training_v2..grant_training
```

### Keeping Branches Updated

If source repositories get new commits:

```bash
# Add source as temporary remote
git remote add temp git@github.com:sabryyoussef/grant_training_v2.git

# Fetch and merge
git fetch temp
git checkout grant_training_v2
git merge temp/main

# Push and cleanup
git push origin grant_training_v2
git remote remove temp
```

---

## 🔧 Troubleshooting

### Problem: "Permission denied (publickey)"

**Solution**: Setup SSH keys

```bash
# Generate key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH and GPG keys → New SSH key
```

### Problem: "Branch already exists"

**Solution**: Delete and recreate

```bash
git branch -D branch_name
git push origin --delete branch_name
# Then re-run consolidation
```

### Problem: Script fails on fetch

**Solution**: Check repository access

```bash
# Test SSH connection
ssh -T git@github.com

# Verify repository exists
# Go to: https://github.com/sabryyoussef/[repo-name]

# Check if repository is private (you need access)
```

### Problem: "No main or master branch found"

**Solution**: Some repos use different default branches

Check the repository on GitHub to see the default branch name, then edit the consolidation script to use that branch name.

---

## 📊 Understanding the Structure

### Before Consolidation

```
/workspace/
  ├── grant_t_v2_separate/      (separate repo)
  ├── grant_training_v2/         (separate repo)
  ├── grant_training/            (separate repo)
  ├── grants-training-suite-main/(separate repo)
  └── grant-training-suit/       (separate repo)
```

### After Consolidation

```
/workspace/
  └── grant_training_consolidate/
       ├── main (branch)
       ├── grant_t_v2_separate (branch)
       ├── grant_training_v2 (branch)
       ├── grant_training (branch)
       ├── grants_training_suite_main (branch)
       └── grant_training_suit (branch)
```

### Each Branch Contains

- ✅ Full commit history from source repository
- ✅ All files and directories
- ✅ All git metadata
- ✅ Independent from other branches

---

## 🎯 Success Checklist

After running the consolidation, verify:

- [ ] Created `grant_training_consolidate` repository on GitHub
- [ ] Cloned repository locally
- [ ] Ran `consolidate_repos.sh` successfully
- [ ] All 5 branches exist (check with `git branch -a`)
- [ ] All branches pushed to origin
- [ ] Ran `verify_consolidation.sh` with no errors
- [ ] Can checkout each branch
- [ ] Each branch has commit history
- [ ] Can push/pull from origin

---

## 💡 Pro Tips

### Tip 1: Use Git Aliases

Add to `~/.gitconfig`:

```ini
[alias]
    br = branch -a
    co = checkout
    tree = log --oneline --graph --decorate --all
    ls = ls-tree -r --name-only
```

Usage:
```bash
git br    # List all branches
git co grant_training_v2  # Checkout branch
git tree  # Visual commit history
```

### Tip 2: Quick Branch Inspection

```bash
# See all branches with last commit
for branch in $(git branch | sed 's/^..//'); do
    echo "$branch: $(git log -1 --format=%s $branch)"
done
```

### Tip 3: Backup Before Major Changes

```bash
# Create a backup branch
git checkout grant_training_v2
git checkout -b grant_training_v2_backup
git push origin grant_training_v2_backup
```

---

## 📚 Additional Resources

- **README.md** - Complete documentation
- **QUICK_REFERENCE.md** - Command cheat sheet
- **Git Documentation** - https://git-scm.com/doc
- **GitHub Guides** - https://guides.github.com

---

## 🎉 Next Steps

After successful consolidation:

1. ✅ Archive old repositories on GitHub
2. ✅ Update project documentation
3. ✅ Notify team of new structure
4. ✅ Set up CI/CD if needed
5. ✅ Configure branch protection rules
6. ✅ Update bookmarks/shortcuts
7. ✅ Celebrate! 🎊

---

## 📞 Need Help?

If you encounter issues:

1. Check this documentation
2. Run `./verify_consolidation.sh` for diagnostics
3. Review script output for error messages
4. Check Git status: `git status`
5. Verify SSH access: `ssh -T git@github.com`

---

**Remember**: All original repositories remain untouched on GitHub. This consolidation creates a new unified structure without affecting the sources.

**Happy Coding! 🚀**

