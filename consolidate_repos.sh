#!/bin/bash

# =============================================================================
# Repository Consolidation Script
# =============================================================================
# This script consolidates multiple grant repositories into a single repo
# with each old repo preserved as its own branch with full commit history.
# =============================================================================

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
GITHUB_USER="sabryyoussef"
NEW_REPO_NAME="grant_training_consolidate"
NEW_REPO_URL="git@github.com:${GITHUB_USER}/${NEW_REPO_NAME}.git"

# Array of repositories to consolidate
# Format: "remote_name|repo_name|branch_name"
declare -a REPOS=(
    "grant_t_v2_separate|grant_t_v2_separate|grant_t_v2_separate"
    "grant_training_v2|grant_training_v2|grant_training_v2"
    "grant_training|grant_training|grant_training"
    "grants_training_suite|grants-training-suite-main|grants_training_suite_main"
    "grant_training_suit|grant-training-suit|grant_training_suit"
)

# =============================================================================
# Helper Functions
# =============================================================================

print_header() {
    echo -e "${BLUE}=============================================================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}=============================================================================${NC}"
}

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

# =============================================================================
# Main Script
# =============================================================================

print_header "Grant Repository Consolidation Script"

# Check if we're already in a git repository
if [ -d ".git" ]; then
    print_info "Already in a git repository. Checking if it's the consolidated repo..."
    CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null || echo "")
    
    if [[ "$CURRENT_REMOTE" == *"$NEW_REPO_NAME"* ]]; then
        print_success "You're in the consolidated repository. Proceeding..."
    else
        print_error "This appears to be a different repository."
        print_info "Current remote: $CURRENT_REMOTE"
        read -p "Do you want to continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_info "Exiting..."
            exit 1
        fi
    fi
else
    print_error "Not in a git repository!"
    print_info "Please run this script from the root of your consolidated repository."
    print_info "First, create the repository on GitHub, then:"
    echo ""
    echo "  git clone ${NEW_REPO_URL}"
    echo "  cd ${NEW_REPO_NAME}"
    echo "  bash /path/to/this/script.sh"
    echo ""
    exit 1
fi

echo ""
print_info "This script will import ${#REPOS[@]} repositories as branches."
print_info "Each repository's full commit history will be preserved."
echo ""
read -p "Do you want to continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_info "Exiting..."
    exit 0
fi

echo ""

# =============================================================================
# Process Each Repository
# =============================================================================

COUNTER=1
TOTAL=${#REPOS[@]}

for REPO_INFO in "${REPOS[@]}"; do
    IFS='|' read -r REMOTE_NAME REPO_NAME BRANCH_NAME <<< "$REPO_INFO"
    
    print_header "[$COUNTER/$TOTAL] Processing: $REPO_NAME"
    
    REPO_URL="git@github.com:${GITHUB_USER}/${REPO_NAME}.git"
    
    # Step 1: Add remote
    print_step "Adding remote '$REMOTE_NAME'..."
    if git remote add "$REMOTE_NAME" "$REPO_URL" 2>/dev/null; then
        print_success "Remote added"
    else
        print_info "Remote already exists, removing and re-adding..."
        git remote remove "$REMOTE_NAME" 2>/dev/null || true
        git remote add "$REMOTE_NAME" "$REPO_URL"
        print_success "Remote re-added"
    fi
    
    # Step 2: Fetch
    print_step "Fetching from $REPO_NAME..."
    if git fetch "$REMOTE_NAME" --quiet; then
        print_success "Fetch complete"
    else
        print_error "Failed to fetch from $REPO_NAME"
        print_info "Skipping this repository..."
        git remote remove "$REMOTE_NAME" 2>/dev/null || true
        echo ""
        COUNTER=$((COUNTER + 1))
        continue
    fi
    
    # Step 3: Create branch
    print_step "Creating branch '$BRANCH_NAME'..."
    
    # Check if branch already exists locally
    if git show-ref --verify --quiet "refs/heads/$BRANCH_NAME"; then
        print_info "Branch '$BRANCH_NAME' already exists locally"
        read -p "Do you want to recreate it? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git branch -D "$BRANCH_NAME"
            print_success "Deleted existing branch"
        else
            print_info "Skipping branch creation"
            git remote remove "$REMOTE_NAME"
            echo ""
            COUNTER=$((COUNTER + 1))
            continue
        fi
    fi
    
    # Try to checkout from remote main, fall back to master
    if git checkout -b "$BRANCH_NAME" "${REMOTE_NAME}/main" 2>/dev/null; then
        print_success "Branch created from main"
    elif git checkout -b "$BRANCH_NAME" "${REMOTE_NAME}/master" 2>/dev/null; then
        print_success "Branch created from master"
    else
        print_error "Failed to create branch (no main or master branch found)"
        git remote remove "$REMOTE_NAME"
        echo ""
        COUNTER=$((COUNTER + 1))
        continue
    fi
    
    # Step 4: Push to origin
    print_step "Pushing branch to origin..."
    if git push origin "$BRANCH_NAME" --quiet; then
        print_success "Branch pushed to origin"
    else
        print_error "Failed to push branch"
        print_info "You may need to push manually later"
    fi
    
    # Step 5: Remove remote
    print_step "Cleaning up remote..."
    git remote remove "$REMOTE_NAME"
    print_success "Remote removed"
    
    echo ""
    COUNTER=$((COUNTER + 1))
done

# Return to main branch
print_step "Returning to main branch..."
if git checkout main 2>/dev/null || git checkout master 2>/dev/null; then
    print_success "Switched to main branch"
else
    print_info "No main/master branch found, creating one..."
    git checkout -b main
    echo "# Grant Suite Consolidated Repository" > README.md
    git add README.md
    git commit -m "Initial commit"
    git push origin main
    print_success "Main branch created and pushed"
fi

# =============================================================================
# Summary
# =============================================================================

echo ""
print_header "Consolidation Complete!"

echo ""
print_info "Available branches:"
git branch -a | grep -v "HEAD"

echo ""
print_success "All repositories have been consolidated into branches."
print_info "Each branch contains the full commit history of its source repository."
echo ""
print_info "Next steps:"
echo "  1. Review each branch: git checkout <branch_name>"
echo "  2. Optional: Reorganize files into subfolders within branches"
echo "  3. Optional: Create a unified main branch by merging branches"
echo ""
print_success "Done! 🎉"

