# Training Dashboard

A standalone analytics dashboard module for Odoo 19 that provides comprehensive KPIs and analytics for training programs.

## Features

- **KPI Metrics**
  - Total students, enrolled students, completed students
  - Completion rate and average completion time
  - Active courses and total enrollments
  - eLearning adoption rate

- **Progress Analytics**
  - Progress distribution (0-25%, 25-50%, 50-75%, 75-100%)
  - Monthly enrollment trends
  - Completion trends over time

- **Student Analytics**
  - Top performers (students with >80% progress)
  - Struggling students (students with <25% progress)
  - Engagement metrics (active vs highly engaged)

- **Course Analytics**
  - Course performance metrics
  - Popular courses ranking
  - Enrollment and completion rates per course

- **Integration Analytics**
  - Integration status summary
  - eLearning adoption rate

- **Auto-Refresh**
  - Automatic dashboard refresh every 15 minutes (configurable)
  - Manual refresh button
  - Last update timestamp

## Installation

1. Copy the module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "Training Dashboard" module

## Dependencies

- **Core:** `base`
- **Optional:** `grants_training_suite_v19` (for full analytics with student/course data)

## Usage

### Creating a Dashboard

1. Go to **Training Dashboard > All Dashboards**
2. Click **Create**
3. Set date range (From Date / To Date)
4. Configure auto-refresh settings
5. Click **Refresh Dashboard** to compute metrics

### Viewing Analytics

The dashboard has 5 tabs:
- **KPI Metrics:** Key performance indicators
- **Progress Analytics:** Progress distribution and trends
- **Student Analytics:** Top performers and struggling students
- **Course Analytics:** Course performance and popularity
- **Integration Analytics:** eLearning adoption and status

### Auto-Refresh

- Enable **Auto Refresh** toggle in the dashboard header
- Set **Refresh Interval** (default: 15 minutes)
- Dashboard will automatically refresh via cron job

## Model

**Model Name:** `training.dashboard`

**Key Fields:**
- `name` - Dashboard name
- `date_from` / `date_to` - Date range for analytics
- `total_students` - Total students in date range
- `completion_rate` - Completion percentage
- `auto_refresh` - Enable/disable auto-refresh
- `last_update` - Last refresh timestamp

## Security

- **Users:** Can read, write, and create dashboards
- **Administrators:** Full access (read, write, create, delete)

## Cron Jobs

**Dashboard Auto Refresh** - Runs every 15 minutes
- Refreshes all dashboards with `auto_refresh = True`
- Updates all computed metrics

## Integration with grants_training_suite_v19

If `grants_training_suite_v19` is installed:
- Full analytics with student, course, and progress tracker data
- All KPI metrics computed from actual data
- Complete analytics functionality

If `grants_training_suite_v19` is not installed:
- Module works standalone
- Metrics will show 0 (no data source)
- Dashboard structure remains available for future integration

## API

### Get Dashboard Data

```python
dashboard_data = self.env['training.dashboard'].get_dashboard_data(dashboard_id)
```

Returns dictionary with:
- `kpi_metrics`
- `progress_analytics`
- `student_analytics`
- `course_analytics`
- `integration_analytics`
- `last_update`

## Future Enhancements

- Chart visualizations (charts.js integration)
- Export to PDF/Excel
- Scheduled reports via email
- Custom widget configuration
- Real-time updates via WebSockets
- Multi-dashboard support
- Dashboard templates
- Role-based dashboard views

## Author

Edafa  
Website: https://www.edafa.sa

## License

OEEL-1

