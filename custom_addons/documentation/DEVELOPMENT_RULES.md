# Corses Project Development Rules

## Overview
This document outlines the development rules, guidelines, and best practices for the Corses Project custom addon development in our Odoo 18 environment.

## Project-Specific Rules

### 1. Project Structure Standards
```
corses_project/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── [model_files].py
├── views/
│   └── [view_files].xml
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
├── data/
│   └── [data_files].xml
├── static/
│   ├── description/
│   └── src/
├── wizard/
│   ├── __init__.py
│   └── [wizard_files].py
├── tests/
│   ├── __init__.py
│   └── test_[module].py
├── docs/
│   └── [documentation].md
└── DEVELOPMENT_RULES.md
```

### 2. Odoo 18 Compliance
- **Target Version**: All modules must be compatible with Odoo 18.0
- **Manifest Version**: Use `18.0` in `__manifest__.py`
- **Python Compatibility**: Ensure Python 3.8+ compatibility
- **Dependencies**: Use Odoo 18 compatible dependencies only

### 3. View Development Rules
- **Use List Views**: Replace deprecated `tree` views with `list` views
- **Avoid Deprecated Attributes**: 
  - Do NOT use `attrs` attribute
  - Do NOT use `states` attribute
  - Use `invisible`, `readonly`, `required` directly on fields
- **Modern Field Syntax**: Use Odoo 18 field syntax and attributes

### 4. Code Quality Standards
- **PEP 8 Compliance**: Follow Python PEP 8 standards
- **Docstrings**: Include proper docstrings for all classes and methods
- **Type Hints**: Use type hints where appropriate
- **Error Handling**: Implement proper exception handling
- **Logging**: Use Odoo's logging framework with appropriate log levels

### 5. Security Guidelines
- **Access Rights**: Define proper access rights in `ir.model.access.csv`
- **Record Rules**: Implement record rules for data security
- **SQL Injection Prevention**: Use ORM methods, avoid raw SQL
- **XSS Prevention**: Sanitize user inputs
- **CSRF Protection**: Ensure proper CSRF token handling

### 6. Performance Considerations
- **Database Queries**: Optimize database queries and avoid N+1 problems
- **Lazy Loading**: Use lazy loading for related fields
- **Caching**: Implement appropriate caching strategies
- **Indexing**: Add database indexes where needed
- **Bulk Operations**: Use bulk operations for better performance

### 7. Testing Requirements
- **Unit Tests**: Write unit tests for all business logic
- **Integration Tests**: Test module integrations
- **Coverage**: Maintain good test coverage (minimum 80%)
- **Test Data**: Use proper test data fixtures
- **Mocking**: Use appropriate mocking for external dependencies

### 8. Documentation Standards
- **README**: Include comprehensive README.md for each module
- **API Documentation**: Document all public methods and classes
- **User Guides**: Provide user documentation where applicable
- **Installation Instructions**: Clear setup and installation instructions
- **Changelog**: Maintain a changelog for version tracking

### 9. Development Workflow
- **Planning**: Define requirements and create technical specifications
- **Development**: Follow coding standards and implement incrementally
- **Testing**: Write and run tests during development
- **Code Review**: Perform code reviews before merging
- **Documentation**: Update documentation as you develop

### 10. Version Control Guidelines
- **Git Workflow**: Follow established Git workflow
- **Commit Messages**: Use clear, descriptive commit messages
- **Branching**: Use feature branches for development
- **Tags**: Tag releases appropriately
- **SSH**: Use SSH for GitHub operations (as per user preference)

### 11. Development and Deployment Workflow
- **Development Directory**: Work in `/home/sabry3/odoo-dev/corses_project/grants_training_suite_v2/`
- **Testing Directory**: Push to `/home/sabry3/odoo-dev/grant-training-suit/` for testing and deployment
- **Workflow Process**:
  1. Develop and test in `grants_training_suite_v2/` directory
  2. Copy changes to `grant-training-suit/` repository
  3. Commit and push to GitHub for testing/deployment
  4. Use GitHub repository for production deployment
- **Repository Management**: 
  - `grants_training_suite_v2/` = Development workspace
  - `grant-training-suit/` = GitHub repository for testing and production

## Project-Specific Guidelines

### Module Naming Convention
- Use descriptive, lowercase names with underscores
- Prefix with project identifier if needed (e.g., `corses_`)
- Avoid abbreviations unless they are widely understood

### File Organization
- Group related functionality in appropriate directories
- Keep files focused and maintainable
- Use consistent naming conventions across the project

### Error Handling
- Implement comprehensive error handling
- Provide meaningful error messages to users
- Log errors appropriately for debugging
- Handle edge cases gracefully

### Data Management
- Use proper data validation
- Implement data migration scripts when needed
- Handle data integrity constraints
- Provide data cleanup utilities where necessary

### Integration Guidelines
- Design modules to work well with existing Odoo modules
- Follow Odoo's extension patterns
- Avoid conflicts with standard Odoo functionality
- Test integrations thoroughly

## Development Environment

### IDE Configuration
- **Primary IDE**: PyCharm (as per user preference)
- **Python Interpreter**: Configure for Odoo 18 environment (`~/odoo-dev/.venv/bin/python`)
- **Code Style**: Follow PEP 8 and Odoo conventions
- **Debugging**: Use PyCharm's debugging capabilities

### Odoo Run Configuration
- **Script Path**: `/home/sabry3/odoo-dev/odoo-18/odoo18/odoo-bin`
- **Parameters**: `-c /home/sabry3/odoo-dev/odoo_conf/odoo.conf -d courses2`
- **Working Directory**: `/home/sabry3/odoo-dev`
- **Environment Variables**: `PYTHONUNBUFFERED=1`
- **Database**: Use `courses2` database for development

### Testing Environment
- **Test Database**: Use separate test database
- **Test Data**: Create realistic test data
- **Performance Testing**: Test with realistic data volumes
- **Browser Testing**: Test UI components in different browsers

### Logging Configuration
- **Main Log File**: `/home/sabry3/odoo-dev/logs/odoo.log`
- **Module-Specific Logging**: `grants_training_suite:DEBUG` level in odoo.conf
- **Log Monitoring**: Use `tail -f /home/sabry3/odoo-dev/logs/odoo.log | grep grants_training_suite`
- **Error Tracking**: Separate error files in `/home/sabry3/odoo-dev/corses_project/logs/error_tracking/`

### Error Tracking System
- **Error Directory**: `/home/sabry3/odoo-dev/corses_project/logs/error_tracking/`
- **Error File Format**: `YYYY-MM-DD_module_error_type.log`
- **Error Categories**: 
  - `intake_processing_errors.log`
  - `assignment_errors.log`
  - `document_errors.log`
  - `session_errors.log`
  - `certificate_errors.log`
- **Error Documentation**: Each error file includes:
  - Error description
  - Root cause analysis
  - Solution steps
  - Prevention measures

### Deployment Guidelines
- **Environment Separation**: Maintain dev/staging/prod environments
- **Configuration Management**: Use environment-specific configurations
- **Backup Strategy**: Implement proper backup procedures
- **Monitoring**: Set up monitoring and logging

## Running and Testing

### How to Run Odoo with Grants Training Suite
1. **Start Odoo Server**:
   ```bash
   # Using PyCharm Run Configuration
   Script: /home/sabry3/odoo-dev/odoo-18/odoo18/odoo-bin
   Parameters: -c /home/sabry3/odoo-dev/odoo_conf/odoo.conf -d courses2
   Working Directory: /home/sabry3/odoo-dev
   Environment: PYTHONUNBUFFERED=1
   ```

2. **Install/Update Module**:
   ```bash
   # Install new module (from development directory)
   -c /home/sabry3/odoo-dev/odoo_conf/odoo.conf -d courses2 -i grants_training_suite_v2
   
   # Update existing module (from development directory)
   -c /home/sabry3/odoo-dev/odoo_conf/odoo.conf -d courses2 -u grants_training_suite_v2
   
   # Run tests
   -c /home/sabry3/odoo-dev/odoo_conf/odoo.conf -d courses2 -i grants_training_suite_v2 --test-enable
   
   # For production deployment, use grant-training-suit repository
   # Copy from grants_training_suite_v2/ to grant-training-suit/ then deploy
   ```

3. **Access Application**:
   - URL: `http://localhost:8022`
   - Database: `courses2`
   - Login with admin credentials

### Error Checking and Log Monitoring
1. **Monitor Main Logs**:
   ```bash
   # Real-time monitoring
   tail -f /home/sabry3/odoo-dev/logs/odoo.log
   
   # Filter for module-specific logs
   tail -f /home/sabry3/odoo-dev/logs/odoo.log | grep grants_training_suite
   
   # Filter for errors only
   tail -f /home/sabry3/odoo-dev/logs/odoo.log | grep -i error
   ```

2. **Check Error Tracking Files**:
   ```bash
   # List error files
   ls -la /home/sabry3/odoo-dev/corses_project/logs/error_tracking/
   
   # Monitor specific error types
   tail -f /home/sabry3/odoo-dev/corses_project/logs/error_tracking/intake_processing_errors.log
   tail -f /home/sabry3/odoo-dev/corses_project/logs/error_tracking/assignment_errors.log
   ```

3. **Post-Installation Verification**:
   - [ ] Check main log for installation errors
   - [ ] Verify module appears in Apps list
   - [ ] Test basic CRUD operations
   - [ ] Verify security groups are created
   - [ ] Check demo data loads correctly
   - [ ] Test auto-assignment cron job
   - [ ] Verify email templates are created

## Quality Assurance

### Code Review Checklist
- [ ] Follows Odoo 18 standards and conventions
- [ ] Includes proper error handling
- [ ] Has appropriate test coverage
- [ ] Includes documentation
- [ ] Follows security best practices
- [ ] Performs well under load
- [ ] Integrates properly with existing modules

### Testing Checklist
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] UI tests pass
- [ ] Performance tests pass
- [ ] Security tests pass
- [ ] Cross-browser compatibility verified

## Tools and Resources

### Development Tools
- **IDE**: PyCharm
- **Version Control**: Git with SSH
- **Testing**: Odoo test framework
- **Documentation**: Markdown
- **Code Quality**: PEP 8, pylint

### Useful Resources
- Odoo 18 Official Documentation
- Odoo Community Forum
- GitHub Odoo Repository
- Odoo Development Guidelines
- Python PEP 8 Style Guide

## Maintenance and Updates

### Regular Maintenance
- Keep dependencies updated
- Monitor for security vulnerabilities
- Review and update documentation
- Performance monitoring and optimization

### Version Updates
- Plan migration paths for major updates
- Test thoroughly before deployment
- Maintain backward compatibility where possible
- Document breaking changes

## Contact and Support

### Development Team
- **Project Lead**: [Contact Information]
- **Technical Lead**: [Contact Information]
- **Documentation**: [Documentation Location]
- **Issue Tracking**: [Issue Tracker Location]

### Escalation Procedures
- **Critical Issues**: Immediate escalation to technical lead
- **Feature Requests**: Submit through proper channels
- **Bug Reports**: Use issue tracking system
- **Documentation Issues**: Contact documentation team

## Development to Production Workflow

### Workflow Process
1. **Development Phase**: Work in `/home/sabry3/odoo-dev/corses_project/grants_training_suite_v2/`
2. **Testing Phase**: Copy changes to `/home/sabry3/odoo-dev/grant-training-suit/` and test
3. **Production Phase**: Deploy from GitHub repository `grant-training-suit`
4. **Version Control**: All production-ready code must be in the GitHub repository

### Directory Structure
- **Development**: `/home/sabry3/odoo-dev/corses_project/grants_training_suite_v2/` (working directory)
- **Testing/Production**: `/home/sabry3/odoo-dev/grant-training-suit/` (GitHub repository)
- **GitHub Repository**: https://github.com/sabryyoussef/grant-training-suit

### Deployment Commands
```bash
# Copy from development to testing repository
cp -r /home/sabry3/odoo-dev/corses_project/grants_training_suite_v2/* /home/sabry3/odoo-dev/grant-training-suit/

# Commit and push to GitHub
cd /home/sabry3/odoo-dev/grant-training-suit
git add .
git commit -m "Update module with latest changes"
git push origin main
```

---

*Last Updated: January 2025*
*Version: 1.0*
*Odoo Version: 18.0*
*Project: Corses Project*
