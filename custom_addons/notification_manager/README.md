# Notification Manager

A standalone, flexible notification system for Odoo 19 that provides multi-channel notifications (Email, SMS, In-App) with automated triggers and status tracking.

## Features

- **Multi-Channel Notifications**
  - Email notifications
  - In-app notifications (mail.activity)
  - SMS notifications (placeholder for future integration)

- **Notification Types**
  - Progress milestones (25%, 50%, 75%, 90%, 100%)
  - Course completion
  - Stalled progress alerts
  - Achievement notifications
  - Reminders and alerts
  - Custom notifications

- **Automated Triggers**
  - Milestone notifications (hourly cron)
  - Stalled progress alerts (daily cron)
  - Completion notifications (6-hourly cron)
  - Automatic cleanup (daily cron)

- **Status Tracking**
  - Draft → Sent → Read → Archived workflow
  - Priority levels (Low, Normal, High, Urgent)
  - Auto-generated vs manual notifications

- **Integration Support**
  - Optional integration with `grants_training_suite_v19`
  - Works standalone without dependencies
  - Generic reference fields for future flexibility

## Installation

1. Copy the module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "Notification Manager" module

## Dependencies

- **Core:** `base`, `mail`
- **Optional:** `grants_training_suite_v19` (for student/tracker integration)

## Usage

### Manual Notification Creation

1. Go to **Notifications > All Notifications**
2. Click **Create**
3. Fill in:
   - Notification Title
   - Message
   - Notification Type
   - Recipient (User, Email, Phone)
   - Priority
4. Click **Send Notification**

### Automated Notifications

Automated notifications are created by cron jobs:
- **Milestone Notifications:** Created hourly when students reach progress milestones
- **Stalled Progress Alerts:** Created daily for students with no progress in 7 days
- **Completion Notifications:** Created every 6 hours for completed courses
- **Cleanup:** Archives notifications older than 30 days

### Views

- **Notification Dashboard:** Kanban view grouped by status
- **All Notifications:** List view with filters and search
- **Form View:** Detailed notification with workflow buttons

## Model

**Model Name:** `notification.manager`

**Key Fields:**
- `name` - Notification title
- `message` - Notification message
- `notification_type` - Type of notification
- `status` - Workflow status (draft/sent/read/archived)
- `priority` - Priority level
- `student_id` - Optional: Link to student (requires grants_training_suite_v19)
- `progress_tracker_id` - Optional: Link to progress tracker (requires grants_training_suite_v19)
- `recipient_email` - Email recipient
- `recipient_user_id` - User recipient
- `auto_generated` - Whether notification was auto-generated

## Security

- **Users:** Can read, write, and create notifications
- **Administrators:** Full access (read, write, create, delete)

## Cron Jobs

1. **Create Milestone Notifications** - Runs every hour
2. **Stalled Progress Alerts** - Runs daily
3. **Completion Notifications** - Runs every 6 hours
4. **Notification Cleanup** - Runs daily

## Integration with grants_training_suite_v19

If `grants_training_suite_v19` is installed:
- `student_id` and `progress_tracker_id` fields become available
- Automated notifications work with progress trackers
- Student email and agent assignment are automatically populated

If `grants_training_suite_v19` is not installed:
- Module works standalone
- Student/tracker fields are hidden
- Generic notifications can still be created manually

## Future Enhancements

- SMS gateway integration
- Push notifications
- Notification templates
- Notification preferences per user
- Rich HTML email templates
- Multi-language support
- Notification analytics dashboard

## Author

Edafa  
Website: https://www.edafa.sa

## License

OEEL-1

