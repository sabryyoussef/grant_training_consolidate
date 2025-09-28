# GitHub Actions Deployment Setup

This guide explains how to set up automatic deployment from GitHub to your production server.

## Option 1: Password-based Deployment (Quick Setup)

The `deploy.yml` workflow uses your server password. This is simpler but less secure.

### Steps:
1. The workflow file `deploy.yml` is ready to use
2. Push your code to GitHub
3. GitHub Actions will automatically deploy when you push to `master` or `elearning-system-completed` branches

## Option 2: SSH Key-based Deployment (Recommended)

The `deploy-secure.yml` workflow uses SSH keys for better security.

### Setup Steps:

#### 1. Generate SSH Key Pair (on your local machine)
```bash
ssh-keygen -t rsa -b 4096 -C "github-actions-deploy" -f ~/.ssh/github_deploy_key
```

#### 2. Copy Public Key to Server
```bash
ssh-copy-id -i ~/.ssh/github_deploy_key.pub edafa@216.70.76.85
```

#### 3. Add Private Key to GitHub Secrets
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `SERVER_SSH_KEY`
5. Value: Copy the content of `~/.ssh/github_deploy_key` (private key)
6. Click **Add secret**

#### 4. Rename Workflow File
```bash
# Remove the password-based workflow
rm .github/workflows/deploy.yml

# Rename the secure workflow
mv .github/workflows/deploy-secure.yml .github/workflows/deploy.yml
```

## Deployment Behavior

### Branch-based Deployment:
- **`master` branch**: Deploys both `grants_training_suite_v1` and `grants_training_suite_v2`
- **`elearning-system-completed` branch**: Deploys only `grants_training_suite_v2` (complete system)

### What Happens During Deployment:
1. ✅ Creates backup of current modules
2. ✅ Clones latest code from GitHub
3. ✅ Copies appropriate modules to server
4. ✅ Sets proper permissions
5. ✅ Shows deployment status
6. ⚠️ **Optional**: Restarts Odoo services (uncomment in workflow if needed)

## Server Directory Structure

Your server will have:
```
~/odoo-dev/custom-addons/
├── grants_training_suite_v1/     # (from master branch)
├── grants_training_suite_v2/     # (from both branches)
├── grants_training_backup_YYYYMMDD_HHMMSS/  # (automatic backups)
└── corses_project/               # (existing)
```

## Monitoring Deployments

1. Go to your GitHub repository
2. Click **Actions** tab
3. View deployment logs and status

## Troubleshooting

### Common Issues:
1. **Permission denied**: Check SSH key setup
2. **Module not found**: Verify Odoo addons path configuration
3. **Deployment fails**: Check server disk space and permissions

### Manual Deployment (if needed):
```bash
# SSH to your server
ssh edafa@216.70.76.85

# Navigate to custom-addons
cd ~/odoo-dev/custom-addons

# Clone manually
git clone https://github.com/sabryyoussef/grants-training-suite-main.git temp
cp -r temp/custom_addons/grants_training_suite_v2 ./
rm -rf temp
```

## Security Notes

- ⚠️ **Password-based**: Less secure, password visible in logs
- ✅ **SSH Key-based**: More secure, no passwords in logs
- 🔒 **Recommendation**: Use SSH keys for production environments
