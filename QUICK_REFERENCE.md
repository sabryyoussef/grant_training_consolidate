# 📚 Quick Reference Guide - Grant Suite Consolidation

## 🎯 One-Command Setup

```bash
# 1. Create repo on GitHub: grant_training_consolidate
# 2. Clone and consolidate:
git clone git@github.com:sabryyoussef/grant_training_consolidate.git
cd grant_training_consolidate
./consolidate_repos.sh
```

---

## 🔧 Common Operations

### View All Branches
```bash
git branch -a
```

### Switch to a Branch
```bash
git checkout grant_training_v2
```

### View Branch History
```bash
git log --oneline --graph --decorate
```

### Compare Branches
```bash
git diff grant_training_v2..grant_training
```

---

## 📁 Reorganize Branch Files

### Automatic (Recommended)
```bash
git checkout grant_training_v2
./reorganize_branch.sh
# Follow the prompts
```

### Manual
```bash
git checkout grant_training_v2
mkdir grant_training_v2
git mv * grant_training_v2/ 2>/dev/null
git commit -m "Reorganize into subfolder"
git push origin grant_training_v2
```

---

## 🔄 Update a Branch from Source

If the original repository gets new commits:

```bash
# Add the remote temporarily
git remote add temp_remote git@github.com:sabryyoussef/grant_training_v2.git

# Fetch and merge
git fetch temp_remote
git checkout grant_training_v2
git merge temp_remote/main

# Push and cleanup
git push origin grant_training_v2
git remote remove temp_remote
```

---

## 🌳 Create Unified Main Branch

To merge all branches into a single working tree:

```bash
git checkout main

# For each branch:
git subtree add --prefix=grant_training_v2 grant_training_v2 HEAD --squash
git subtree add --prefix=grant_training grant_training HEAD --squash
# ... repeat for all branches
```

---

## 🧹 Cleanup Operations

### Delete a Branch Locally
```bash
git branch -D branch_name
```

### Delete a Branch Remotely
```bash
git push origin --delete branch_name
```

### Remove Unused Remotes
```bash
git remote prune origin
```

---

## 🔍 Inspection Commands

### List All Files in a Branch
```bash
git ls-tree -r --name-only grant_training_v2
```

### View File from Another Branch
```bash
git show grant_training_v2:path/to/file.py
```

### Count Commits in a Branch
```bash
git rev-list --count grant_training_v2
```

### Show Branch Contributors
```bash
git shortlog -sn grant_training_v2
```

---

## 🚨 Troubleshooting

### Reset Branch to Remote State
```bash
git checkout grant_training_v2
git reset --hard origin/grant_training_v2
```

### Discard Local Changes
```bash
git checkout -- .
git clean -fd
```

### View What Changed
```bash
git status
git diff
git diff --cached  # For staged changes
```

---

## 📊 Repository Statistics

### Disk Usage per Branch
```bash
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  sed -n 's/^blob //p' | \
  sort -k2 | \
  cut -d' ' -f1,3- | \
  numfmt --to=iec --field=1
```

### Total Commits Across All Branches
```bash
git rev-list --all --count
```

### Latest Commit Date for Each Branch
```bash
for branch in $(git branch -r | grep -v HEAD); do
  echo -e "$branch\t$(git log -1 --format=%cd --date=short $branch)"
done
```

---

## 🎨 Git Aliases (Add to ~/.gitconfig)

```ini
[alias]
    branches = branch -a
    contributors = shortlog -sn
    last = log -1 HEAD
    tree = log --oneline --graph --decorate --all
    unstage = reset HEAD --
    undo = reset --soft HEAD~1
```

Usage:
```bash
git tree
git contributors
```

---

## 📋 Branch Checklist

After consolidation, verify each branch:

- [ ] `grant_t_v2_separate`
  - [ ] All commits present
  - [ ] Files intact
  - [ ] Can checkout and build/run
  
- [ ] `grant_training_v2`
  - [ ] All commits present
  - [ ] Files intact
  - [ ] Can checkout and build/run

- [ ] `grant_training`
  - [ ] All commits present
  - [ ] Files intact
  - [ ] Can checkout and build/run

- [ ] `grants_training_suite_main`
  - [ ] All commits present
  - [ ] Files intact
  - [ ] Can checkout and build/run

- [ ] `grant_training_suit`
  - [ ] All commits present
  - [ ] Files intact
  - [ ] Can checkout and build/run

---

## 🔐 SSH Key Setup (If Needed)

```bash
# Generate new SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Start ssh-agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Copy public key (add to GitHub Settings → SSH Keys)
cat ~/.ssh/id_ed25519.pub
```

---

## 📝 Commit Message Conventions

When working in consolidated repo:

- `feat(branch): Add new feature` - New features
- `fix(branch): Fix bug` - Bug fixes
- `refactor(branch): Reorganize code` - Code restructuring
- `docs(branch): Update documentation` - Documentation
- `merge: Consolidate branch_name` - Branch consolidations

---

## 🎯 Next Steps After Consolidation

1. ✅ Verify all branches are present
2. ✅ Test checkout of each branch
3. ✅ Document branch purposes in README
4. ✅ Set up CI/CD if needed
5. ✅ Archive or delete old repositories
6. ✅ Update team documentation
7. ✅ Notify team members of new structure

---

**Last Updated**: 2025-11-18  
**For**: Grant Suite Consolidation Project

