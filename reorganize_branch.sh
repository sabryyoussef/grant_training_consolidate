#!/bin/bash

# =============================================================================
# Branch Reorganization Script
# =============================================================================
# This script helps reorganize a branch's files into a subfolder
# Useful when multiple branches have conflicting top-level files
# =============================================================================

set -e

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

print_step() {
    echo -e "${BLUE}▶ $1${NC}"
}

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    print_error "Not in a git repository!"
    exit 1
fi

# Get the current branch name
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ "$CURRENT_BRANCH" == "main" ] || [ "$CURRENT_BRANCH" == "master" ]; then
    print_error "You're on the $CURRENT_BRANCH branch!"
    print_info "This script should be run on a feature branch, not main/master."
    read -p "Do you want to continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
fi

echo ""
print_info "Current branch: $CURRENT_BRANCH"
echo ""

# Ask for the subfolder name (default to current branch name)
read -p "Enter subfolder name [default: $CURRENT_BRANCH]: " SUBFOLDER_NAME
SUBFOLDER_NAME=${SUBFOLDER_NAME:-$CURRENT_BRANCH}

echo ""
print_info "Files will be moved to: $SUBFOLDER_NAME/"
echo ""
read -p "Do you want to continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_info "Exiting..."
    exit 0
fi

echo ""

# Check if subfolder already exists
if [ -d "$SUBFOLDER_NAME" ]; then
    print_error "Directory '$SUBFOLDER_NAME' already exists!"
    print_info "Please choose a different name or remove the existing directory."
    exit 1
fi

# Create the subfolder
print_step "Creating subfolder: $SUBFOLDER_NAME/"
mkdir "$SUBFOLDER_NAME"
print_success "Subfolder created"

# Move all files (except .git and the new subfolder)
print_step "Moving files to subfolder..."

# First, move regular files
MOVED_COUNT=0
for item in *; do
    if [ "$item" != "$SUBFOLDER_NAME" ] && [ "$item" != ".git" ]; then
        git mv "$item" "$SUBFOLDER_NAME/" 2>/dev/null && MOVED_COUNT=$((MOVED_COUNT + 1)) || true
    fi
done

# Then, move hidden files (except .git and .gitignore which we'll handle separately)
shopt -s dotglob nullglob
for item in .[!.]*; do
    if [ "$item" != ".git" ] && [ -e "$item" ]; then
        git mv "$item" "$SUBFOLDER_NAME/" 2>/dev/null && MOVED_COUNT=$((MOVED_COUNT + 1)) || true
    fi
done
shopt -u dotglob nullglob

print_success "Moved $MOVED_COUNT items to $SUBFOLDER_NAME/"

# Check if there are any changes to commit
if git diff --cached --quiet; then
    print_info "No files were moved (they might already be in the correct location)"
    rmdir "$SUBFOLDER_NAME" 2>/dev/null || true
    exit 0
fi

# Show what will be committed
echo ""
print_info "Changes to be committed:"
git diff --cached --name-status | head -20
TOTAL_CHANGES=$(git diff --cached --name-status | wc -l)
if [ "$TOTAL_CHANGES" -gt 20 ]; then
    print_info "... and $((TOTAL_CHANGES - 20)) more files"
fi

echo ""
read -p "Do you want to commit these changes? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_info "Changes staged but not committed."
    print_info "You can commit manually with: git commit -m 'Reorganize into subfolder'"
    exit 0
fi

# Commit the reorganization
print_step "Committing reorganization..."
git commit -m "Reorganize $CURRENT_BRANCH files into $SUBFOLDER_NAME/ subfolder"
print_success "Changes committed"

# Ask if user wants to push
echo ""
read -p "Do you want to push to origin? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_step "Pushing to origin..."
    git push origin "$CURRENT_BRANCH"
    print_success "Changes pushed"
fi

echo ""
print_success "Reorganization complete! 🎉"
print_info "All files from $CURRENT_BRANCH are now in $SUBFOLDER_NAME/"

