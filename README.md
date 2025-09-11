# Grants Training Suite - Odoo 18 Module

A comprehensive business intelligence and training management system for educational institutions and training organizations. This module provides end-to-end management of student intake, training sessions, homework assignments, and certification processes.

## 🚀 Features

### 📊 Student Management
- **Intake Batch Processing**: Upload CSV files to bulk import students
- **Eligibility Assessment**: Automated eligibility checking based on age, English level, and certification requirements
- **Student Lifecycle**: Track students from intake through graduation
- **Assignment Management**: Assign students to agents for personalized support

### 📚 Training Management
- **Course Sessions**: Schedule and track individual training sessions
- **Homework System**: Create, assign, and grade homework assignments
- **Progress Tracking**: Monitor student progress through training programs
- **Session Documentation**: Record session details, attendance, and outcomes

### 📄 Document Management
- **Document Requests**: Manage required documents for student enrollment
- **File Upload**: Support for various document types with validation
- **Document Tracking**: Monitor document submission and approval status

### 🏆 Certification System
- **Certificate Generation**: Create completion and achievement certificates
- **Digital Delivery**: Issue and deliver certificates electronically
- **Verification System**: Certificate verification and validation
- **Status Tracking**: Monitor certificate lifecycle from creation to verification

## 🏗️ Module Architecture

### Core Models

#### `gr.intake.batch`
- Manages student intake batches
- CSV file upload and parsing
- Bulk student creation and validation
- Batch processing workflow

#### `gr.student`
- Student profile management
- Eligibility assessment and tracking
- Assignment to agents
- Progress monitoring

#### `gr.assignment`
- Student-agent relationship management
- Contact attempt tracking
- Response time monitoring
- Enrollment progress tracking

#### `gr.document.request`
- Document requirement management
- File upload and validation
- Document status tracking
- Approval workflow

#### `gr.course.session`
- Individual training session management
- Session scheduling and tracking
- Attendance and outcome recording
- Progress documentation

#### `gr.homework.attempt`
- Homework assignment system
- Submission tracking
- Grading and feedback
- Resubmission handling

#### `gr.certificate`
- Certificate generation and management
- Digital delivery system
- Verification and validation
- Status tracking

## 🔧 Installation

### Prerequisites
- Odoo 18.0 or later
- Python 3.8+
- PostgreSQL database

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sabryyoussef/grant-training-suit.git
   ```

2. **Copy to Odoo addons directory**:
   ```bash
   cp -r grant-training-suit /path/to/odoo/addons/
   ```

3. **Update module list**:
   - Go to Odoo Apps menu
   - Click "Update Apps List"
   - Search for "Grants Training Suite"

4. **Install the module**:
   - Click "Install" on the Grants Training Suite module

## 📋 Usage Guide

### 1. Student Intake Process

#### Upload Student Data
1. Navigate to **Grants Training > Intake Management**
2. Create a new intake batch
3. Upload a CSV file with student information
4. Validate the file format and data
5. Process the file to create student records

#### CSV Format Requirements
```csv
name,email,phone,birth_date,gender,nationality,native_language,english_level,has_certificate,certificate_type,certificate_date
John Doe,john@example.com,+1234567890,1990-01-01,Male,American,English,Advanced,true,IELTS,2023-01-01
```

#### Eligibility Criteria
- **Age**: 18-65 years old
- **English Level**: Intermediate or higher
- **Certification**: Must have a valid certificate

### 2. Student Assignment

1. Navigate to **Grants Training > Student Management > Assignments**
2. Create new assignments for eligible students
3. Assign students to agents
4. Track contact attempts and responses

### 3. Training Sessions

1. Navigate to **Grants Training > Training Management > Course Sessions**
2. Create new sessions for assigned students
3. Schedule session dates and times
4. Record session outcomes and progress

### 4. Homework Management

1. Navigate to **Grants Training > Training Management > Homework Attempts**
2. Create homework assignments
3. Students submit homework content or files
4. Grade submissions and provide feedback
5. Handle resubmissions if needed

### 5. Document Management

1. Navigate to **Grants Training > Document Management**
2. Create document requests for students
3. Upload required documents
4. Track document approval status

### 6. Certificate Generation

1. Navigate to **Grants Training > Certification**
2. Create certificates for completed students
3. Issue and deliver certificates
4. Verify certificate authenticity

## 🔐 Security & Permissions

### User Groups

#### `grants_training_suite.group_manager`
- Full access to all module features
- Can manage all students, sessions, and certificates
- Administrative privileges

#### `grants_training_suite.group_agent`
- Limited access to assigned students
- Can manage sessions and homework for assigned students
- Cannot access other agents' students

#### `grants_training_suite.group_student`
- Read-only access to own records
- Can submit homework and view grades
- Limited to personal information

## 📊 Workflow Examples

### Complete Student Journey

1. **Intake**: Student data uploaded via CSV
2. **Eligibility**: System checks eligibility criteria
3. **Assignment**: Eligible student assigned to agent
4. **Training**: Agent conducts training sessions
5. **Homework**: Student submits assignments
6. **Grading**: Agent grades and provides feedback
7. **Certification**: Certificate generated upon completion
8. **Delivery**: Certificate issued and delivered

### Homework Grading Workflow

1. **Creation**: Homework assignment created
2. **Submission**: Student submits content or file
3. **Review**: Agent starts review process
4. **Grading**: Agent enters grade and feedback
5. **Completion**: Homework marked as graded
6. **Return**: Homework returned to student
7. **Resubmission**: Student can resubmit if needed

## 🛠️ Configuration

### Logging Configuration

Add to your `odoo.conf` file:
```ini
# Logging configuration
log_level = info
log_handler = :INFO,grants_training_suite:DEBUG
logfile = /path/to/odoo/logs/odoo.log
```

### Demo Data

The module includes comprehensive demo data for testing:
- Sample student records
- Intake batch examples
- Assignment templates
- Session examples
- Homework samples
- Certificate templates

## 🧪 Testing

### Demo CSV Files

The module includes several demo CSV files for testing:
- `demo_students.csv`: Mixed eligibility students
- `eligible_students.csv`: All eligible students
- `eligible_students_final.csv`: Final test data
- Various test files for debugging

### Testing Workflow

1. Install the module with demo data
2. Test intake batch upload with demo CSV files
3. Verify student eligibility assessment
4. Test assignment creation and management
5. Create and grade homework assignments
6. Generate and verify certificates

## 🔧 Development

### Development Workflow

1. **Development**: Work in `/path/to/grants_training_suite_v2/`
2. **Testing**: Copy to `/path/to/grant-training-suit/`
3. **Deployment**: Commit and push to GitHub
4. **Production**: Deploy from GitHub repository

### Key Development Files

- `models/`: Core business logic
- `views/`: User interface definitions
- `security/`: Access control and permissions
- `data/`: Sequences and default data
- `demo/`: Demo data and test files

## 📈 Performance Considerations

- **Batch Processing**: Intake batches are processed in chunks for large datasets
- **Indexing**: Database indexes on frequently queried fields
- **Caching**: Computed fields are cached for performance
- **Logging**: Comprehensive logging for debugging and monitoring

## 🐛 Troubleshooting

### Common Issues

1. **CSV Upload Errors**: Check file format and required fields
2. **Eligibility Issues**: Verify student data meets criteria
3. **Permission Errors**: Check user group assignments
4. **Validation Errors**: Ensure all required fields are provided

### Debug Mode

Enable debug logging in `odoo.conf`:
```ini
log_level = debug
log_handler = :DEBUG
```

## 📝 License

This module is licensed under the LGPL-3 license.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review the demo data and examples

## 🔄 Version History

### v18.0.1.0.0 (Current)
- Complete homework grading workflow
- Form validation fixes
- Assignment filtering
- Enhanced logging and error handling
- Comprehensive demo data
- Full certificate workflow

### v18.0.0.1.0 (Initial)
- Basic module structure
- Core models and views
- Security implementation
- Initial demo data

---

**Grants Training Suite** - Empowering educational institutions with comprehensive training management solutions.