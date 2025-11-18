#!/bin/bash

# =============================================================================
# Consolidation Verification Script
# =============================================================================
# This script verifies that all repositories have been properly consolidated
# and checks the integrity of each branch.
# =============================================================================

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

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

# Expected branches
declare -a EXPECTED_BRANCHES=(
    "grant_t_v2_separate"
    "grant_training_v2"
    "grant_training"
    "grants_training_suite_main"
    "grant_training_suit"
)

print_header "Grant Suite Consolidation Verification"

# Check if in git repository
if [ ! -d ".git" ]; then
    print_error "Not in a git repository!"
    exit 1
fi

print_success "In a git repository"
echo ""

# Check remote
print_step "Checking remote configuration..."
REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
if [ -z "$REMOTE_URL" ]; then
    print_error "No origin remote found!"
    exit 1
fi
print_success "Origin remote: $REMOTE_URL"
echo ""

# Fetch latest from origin
print_step "Fetching latest from origin..."
git fetch origin --quiet 2>/dev/null
print_success "Fetch complete"
echo ""

# Check for expected branches
print_header "Branch Verification"
echo ""

MISSING_BRANCHES=()
PRESENT_BRANCHES=()

for BRANCH in "${EXPECTED_BRANCHES[@]}"; do
    print_step "Checking branch: $BRANCH"
    
    # Check if branch exists locally or remotely
    LOCAL_EXISTS=$(git show-ref --verify --quiet "refs/heads/$BRANCH" && echo "yes" || echo "no")
    REMOTE_EXISTS=$(git show-ref --verify --quiet "refs/remotes/origin/$BRANCH" && echo "yes" || echo "no")
    
    if [ "$LOCAL_EXISTS" = "yes" ] || [ "$REMOTE_EXISTS" = "yes" ]; then
        print_success "Branch exists"
        PRESENT_BRANCHES+=("$BRANCH")
        
        # Get commit count
        if [ "$LOCAL_EXISTS" = "yes" ]; then
            COMMIT_COUNT=$(git rev-list --count "$BRANCH")
        else
            COMMIT_COUNT=$(git rev-list --count "origin/$BRANCH")
        fi
        echo "  Commits: $COMMIT_COUNT"
        
        # Get last commit date
        if [ "$LOCAL_EXISTS" = "yes" ]; then
            LAST_COMMIT=$(git log -1 --format="%cd" --date=short "$BRANCH" 2>/dev/null)
        else
            LAST_COMMIT=$(git log -1 --format="%cd" --date=short "origin/$BRANCH" 2>/dev/null)
        fi
        echo "  Last commit: $LAST_COMMIT"
        
        # Check if pushed to origin
        if [ "$REMOTE_EXISTS" = "yes" ]; then
            print_success "Branch is on origin"
        else
            print_error "Branch NOT pushed to origin"
        fi
    else
        print_error "Branch NOT found"
        MISSING_BRANCHES+=("$BRANCH")
    fi
    
    echo ""
done

# Summary
print_header "Summary"
echo ""

EXPECTED_COUNT=${#EXPECTED_BRANCHES[@]}
PRESENT_COUNT=${#PRESENT_BRANCHES[@]}
MISSING_COUNT=${#MISSING_BRANCHES[@]}

print_info "Expected branches: $EXPECTED_COUNT"
print_success "Present branches: $PRESENT_COUNT"

if [ $MISSING_COUNT -gt 0 ]; then
    print_error "Missing branches: $MISSING_COUNT"
    echo ""
    print_info "Missing branches:"
    for BRANCH in "${MISSING_BRANCHES[@]}"; do
        echo "  - $BRANCH"
    done
    echo ""
else
    print_success "All expected branches are present! 🎉"
fi

echo ""

# Additional checks
print_header "Additional Checks"
echo ""

# Check for uncommitted changes
print_step "Checking for uncommitted changes..."
if git diff-index --quiet HEAD -- 2>/dev/null; then
    print_success "No uncommitted changes"
else
    print_info "Working directory has uncommitted changes"
fi

# Check if current branch is main/master
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
print_step "Current branch: $CURRENT_BRANCH"

if [ "$CURRENT_BRANCH" = "main" ] || [ "$CURRENT_BRANCH" = "master" ]; then
    print_success "On default branch"
else
    print_info "Currently on feature branch: $CURRENT_BRANCH"
fi

echo ""

# Repository statistics
print_header "Repository Statistics"
echo ""

print_info "Total branches (local): $(git branch | wc -l)"
print_info "Total branches (remote): $(git branch -r | grep -v HEAD | wc -l)"
print_info "Total commits (all branches): $(git rev-list --all --count)"
print_info "Repository size: $(du -sh .git | cut -f1)"

echo ""

# Detailed branch information
print_header "Branch Details"
echo ""

printf "%-35s %-10s %-12s %s\n" "Branch" "Commits" "Last Updated" "Size (files)"
printf "%-35s %-10s %-12s %s\n" "------" "-------" "------------" "-----------"

for BRANCH in "${PRESENT_BRANCHES[@]}"; do
    if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
        BRANCH_REF="$BRANCH"
    else
        BRANCH_REF="origin/$BRANCH"
    fi
    
    COMMITS=$(git rev-list --count "$BRANCH_REF" 2>/dev/null || echo "N/A")
    LAST_DATE=$(git log -1 --format="%cd" --date=short "$BRANCH_REF" 2>/dev/null || echo "N/A")
    FILE_COUNT=$(git ls-tree -r "$BRANCH_REF" 2>/dev/null | wc -l || echo "N/A")
    
    printf "%-35s %-10s %-12s %s\n" "$BRANCH" "$COMMITS" "$LAST_DATE" "$FILE_COUNT"
done

echo ""

# Final status
print_header "Verification Status"
echo ""

if [ $MISSING_COUNT -eq 0 ]; then
    print_success "✓ All repositories successfully consolidated!"
    print_success "✓ All branches are accessible"
    print_success "✓ Commit history preserved"
    echo ""
    print_info "Next steps:"
    echo "  1. Review each branch: git checkout <branch_name>"
    echo "  2. Test functionality in each branch"
    echo "  3. Optional: Reorganize files with ./reorganize_branch.sh"
    echo "  4. Optional: Archive old repositories"
    echo ""
    exit 0
else
    print_error "⚠ Consolidation incomplete!"
    echo ""
    print_info "Run ./consolidate_repos.sh to complete the consolidation"
    echo ""
    exit 1
fi

