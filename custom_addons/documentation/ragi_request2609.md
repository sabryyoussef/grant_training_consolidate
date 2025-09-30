# System Enhancement & Bug Fix Tasks

## Intake Batches
- [ ] Support upload of Excel/CSV files (`.xls`, `.xlsx`, `.csv`).
- [ ] Add **column mapping popup** between Excel columns and system fields.
- [ ] Make **Save/Upload/Validate** actions update stages automatically (no manual refresh).
- [ ] Provide a **downloadable Excel template** with required columns + examples.
- [ ] Link **Intake Batches → Students**:
  - Show mapping popup on upload.
  - Import selected fields (Arabic Name, English Name, Email, Phone, Birth Date, Gender, Nationality, Native Language, English Level, Has Certificate, Assigned Agent).
  - Support flexible mapping + selective import.

## Students
- [ ] Add two required name fields:
  - Student Name (Arabic)
  - Student Name (English)
- [ ] Fix **Auto Enroll eLearning** bug (“No eligible courses found…”).
- [ ] Fix **Manual Enroll** error (ensure student/course selection works).
- [ ] Fix **Assign Agent** button error (must work on new/old/edited records).
- [ ] Add **Course selection field** (dropdown) for Enroll (supports Manual, Import, Auto).

## Document Requests
- [ ] Enable **direct stage transitions** (via Actions or clicking stage) without needing page refresh.

## Course Sessions
- [ ] Allow **multiple students in one session** (instead of creating 1 session per student).
  - Keep option for single assign, but add group assign.

## Homework Attempts
- [ ] Fix **stage transition & auto-save** (no manual refresh).
- [ ] Fix **Grade % calculation** – should update automatically when Grade is entered.

## Training Programs
- [ ] Improve **Enroll Eligible Students** button:
  - Add option to select specific students (popup/checklist).
  - Add **Invite option** (instead of direct Enroll).
  - Keep mass Enroll option.
  - Add logging for actions.

## Course Integrations
- [ ] Same **Enroll Eligible Students** fix as Training Programs.
- [ ] Fix **eLearning Integration**: ensure invited students appear in Course Integrations with correct enrollment status.

## Certificates
- [ ] Add **dynamic certificate template**:
  - Student Name, Course Name, Completion Date (+ optional fields like signature/logo).
  - Auto-generate PDF after verification.
  - Allow student to download or receive via email.

## Certificate Automation Dashboard
- [ ] Fix **Completed vs Enrolled bug**:
  - Certificates should generate for students in “Completed” state.
  - Ensure system checks `Completed + success criteria` instead of only `Enrolled`.