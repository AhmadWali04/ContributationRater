# Contributor Rater Project Roadmap

> [!NOTE]
> This document outlines the development roadmap and task list for the Contributor Rater project.
> Tasks are organized by iteration, with each iteration focusing on specific platform integrations.
> Feel free to add or modify tasks as needed.

## Project Overview

Contributor Rater is a tool designed to track and analyze contributor activity across various projects. The application consists of a Discord bot for interaction and a web dashboard for visualization and reporting.

## Iteration 1: Discord Integration

### Core Bot Development

- [ ] Create Discord bot with the following commands:
  - [ ] `/help` - Display all available commands and usage information.
  - [ ] `/setup` - Configure Contribot profile and integrations (Google Sheets, Document Generation).
  - [ ] `/track` - Track contributor activity for a specific project in your project list.
  - [ ] `/info` - Display project and bot information, including version and usage stats.
  - [ ] `/report` - Generate weekly/bi-weekly activity reports, for a specific project or all projects.
  - [ ] `/activity me` - Show personal activity and self-reports, with dashboard link.
  - [ ] `/activity <user>` - Display activity for a specific user, specified by their registered Discord ID.
  - [ ] `/activity <project>` - Show project-wide activity with dashboard link.
  - [ ] `/dashboard` - Provide link to the web dashboard, for any detailed analytics that need to be done.

### API Integrations

- [ ] Discord API integration:
  - [ ] Implement OAuth for user authentication (Discord OAuth, Google OAuth).
  - [ ] Set up webhook event listeners, for activity tracking.
  - [ ] Configure permission management, certain commands should be restricted to admins or project initiators.

- [ ] Google Services Integration:
  - [ ] Google Sheets API with OAuth, for data storage (if sheets is more preferred).
  - [ ] Document Generation API with OAuth, for generating reports.
- [ ] Additional API integrations as needed, such as n8n, Zapier, etc.

### Database Implementation

- [ ] Set up LibSQL/SQLite database:
  - [ ] Design schema for project data.
  - [ ] Design schema for user data.
  - [ ] Design schema for session data.
  - [ ] Implement data migration strategy for schema changes.

### Web Dashboard

- [ ] Configure OAuth for Discord sign-in, or Google OAuth for Google sign-in.
- [ ] Implement data visualization with Chart.js (or similar library).
  - [ ] Bar graphs for activity comparison across users.
  - [ ] Heatmaps for time-based activity analysis.
  - [ ] Pie charts for contribution distribution across projects.
  - [ ] Line graphs for trend analysis over time.
- [ ] Create responsive dashboard layout, in `/client`.
- [ ] Implement user management interface, and project management interface.

## Iteration 2: Slack Integration

**TODO**: This Iteration is not that important right now, but will be later.

## Iteration 3: Microsoft Teams Integration

**TODO**: This Iteration is not that important right now, but will be later.

## Future Enhancements

- [ ] Cross-platform activity aggregation, for users who use multiple platforms.
- [ ] AI generated insights from activity data, and reports generated on a weekly/bi-weekly basis.
- [ ] Machine learning models for predicting future activity.
- [ ] Advanced analytics and reporting, for people who are more interested in the data.
- [ ] Custom notification rules.
- [ ] Integration with project management tools (Jira, Trello, Azure, etc).
- [ ] Plenty of third-party integrations that can be added later and defined by the user.