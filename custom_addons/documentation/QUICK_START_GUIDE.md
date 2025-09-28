# Grants Training Suite - Quick Start Guide

## 🚀 Getting Started

This guide will help you quickly set up and test the Grants Training Suite module in phases.

## 📋 Prerequisites

- Odoo 18.0 Enterprise installed
- Python 3.8+ environment
- PostgreSQL database
- PyCharm IDE (recommended)

## ⚡ Quick Setup

### 1. Environment Setup
```bash
# Navigate to project directory
cd /home/sabry3/odoo-dev/corses_project

# Verify module structure
ls -la grants_training_suite/
```

### 2. Odoo Configuration
Your `odoo.conf` is already configured with:
- Module-specific logging: `grants_training_suite:DEBUG`
- Log file: `/home/sabry3/odoo-dev/logs/odoo.log`
- Database: `courses`

### 3. PyCharm Run Configuration
Use these settings in PyCharm:
- **Script**: `/home/sabry3/odoo-dev/odoo-18/odoo18/odoo-bin`
- **Parameters**: `-c /home/sabry3/odoo-dev/odoo_conf/odoo.conf -d courses`
- **Working Directory**: `/home/sabry3/odoo-dev`
- **Environment**: `PYTHONUNBUFFERED=1`

## 🧪 Testing Phases

### Phase 1: Foundation Testing
```bash
# Run Phase 1 tests
cd testing_framework/
python3 checkpoint_testing_script.py --phase 1 --verbose

# Or run from project root
python3 testing_framework/checkpoint_testing_script.py --phase 1 --verbose

# Check results
cat logs/checkpoint_report_*.json
```

### Phase 2: Intake Processing Testing
```bash
# Run Phase 2 tests
cd testing_framework/
python3 checkpoint_testing_script.py --phase 2 --verbose

# Monitor logs
tail -f logs/odoo.log | grep grants_training_suite
```

### All Phases Testing
```bash
# Run all available tests
cd testing_framework/
python3 checkpoint_testing_script.py --all-phases --verbose
```

## 📊 Monitoring & Debugging

### Real-time Log Monitoring
```bash
# Main Odoo logs
tail -f /home/sabry3/odoo-dev/logs/odoo.log

# Module-specific logs
tail -f /home/sabry3/odoo-dev/logs/odoo.log | grep grants_training_suite

# Error tracking logs
tail -f /home/sabry3/odoo-dev/corses_project/logs/error_tracking/*.log
```

### Error Analysis
```bash
# Check error files
ls -la /home/sabry3/odoo-dev/corses_project/logs/error_tracking/

# Search for specific errors
grep -r "ERROR" /home/sabry3/odoo-dev/corses_project/logs/error_tracking/
```

## 🎯 Phase-by-Phase Development

### Current Status
- ✅ **Phase 1**: Foundation & Core Models - COMPLETED
- 🚧 **Phase 2**: Intake Processing & Validation - IN PROGRESS
- ⏳ **Phase 3**: Agent Assignment & Workflow - PENDING

### Next Steps
1. **Complete Phase 2**: File upload and validation
2. **Test Phase 2**: Run checkpoint tests
3. **Start Phase 3**: Agent assignment system
4. **Continue iteratively**: Each phase with testing

## 📋 Milestone Checklists

### Using Milestone Checklists
1. **Copy template**: `cp project_management/MILESTONE_CHECKLIST_TEMPLATE.md project_management/PHASE_X_MILESTONE_CHECKLIST.md`
2. **Fill in details**: Update objectives, deliverables, tests
3. **Run tests**: Use checkpoint testing script
4. **Complete checklist**: Mark all items as done
5. **Sign off**: Get approval for next phase

### Phase 1 Example
- ✅ **Completed**: `PHASE_1_MILESTONE_CHECKLIST.md`
- 📊 **Results**: All tests passed, ready for Phase 2

## 🔧 Troubleshooting

### Common Issues

#### Module Installation Fails
```bash
# Check logs
tail -f /home/sabry3/odoo-dev/logs/odoo.log

# Check dependencies
grep -i "error\|failed" /home/sabry3/odoo-dev/logs/odoo.log
```

#### Permission Errors
```bash
# Check file permissions
ls -la grants_training_suite/

# Fix permissions if needed
chmod -R 755 grants_training_suite/
```

#### Database Connection Issues
```bash
# Check database configuration
grep -i "db_" /home/sabry3/odoo-dev/odoo_conf/odoo.conf

# Test database connection
psql -h localhost -U odoo18 -d courses
```

### Error Tracking
- **Error Files**: Check `/home/sabry3/odoo-dev/corses_project/logs/error_tracking/`
- **Error Categories**: intake_processing, assignment, document, session, certificate, general
- **Error Format**: Timestamp, type, description, context, impact, resolution

## 📚 Documentation

### Key Documents
- **Project Plan**: `project_management/GRANTS_TRAINING_PROJECT_PLAN.md`
- **Development Rules**: `documentation/DEVELOPMENT_RULES.md`
- **Module README**: `grants_training_suite/README.md`
- **Error Tracking**: `logs/error_tracking/README.md`

### Development Workflow
1. **Plan**: Review project plan and current phase
2. **Develop**: Implement phase objectives
3. **Test**: Run checkpoint tests
4. **Review**: Complete milestone checklist
5. **Deploy**: Move to next phase

## 🎯 Success Criteria

### Phase Completion Criteria
- [ ] All phase objectives completed
- [ ] All tests passing
- [ ] No critical errors
- [ ] Documentation updated
- [ ] Performance acceptable
- [ ] Security review complete

### Project Success Criteria
- [ ] All 9 phases completed
- [ ] Production-ready module
- [ ] Comprehensive testing
- [ ] Complete documentation
- [ ] Error-free operation
- [ ] User acceptance

## 📞 Support

### Getting Help
- **Check logs**: Always check error logs first
- **Run tests**: Use checkpoint testing script
- **Review docs**: Check relevant documentation
- **Check milestones**: Use milestone checklists

### Reporting Issues
1. **Check error tracking files**
2. **Run checkpoint tests**
3. **Document the issue**
4. **Include relevant logs**
5. **Follow up on resolution**

---

**Quick Start Guide Version**: 1.0  
**Last Updated**: 2025-01-15  
**Next Review**: After Phase 2 completion  

---

*Happy coding! 🚀*
