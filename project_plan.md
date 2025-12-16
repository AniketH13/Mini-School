Project Plan – Mini School Management Application Suite

MVP Scope Document

MVP Feature List (Must-Have)
The following features are selected based on MoSCoW prioritization and represent the Minimum Viable Product:

Authentication & Access
- Role-based login (Admin/Principal, Teacher, Parent)
- School-level (multi-tenant) separation

Attendance Management
- Teacher can mark daily attendance
- Parent can view child attendance
- Principal can view school-wide attendance summary

Grading Module
- Teacher can enter and update grades
- Parent can view grades
- Principal can view academic summaries

Parent Communication
- School announcements
- Teacher-to-parent messages (basic)

Dashboards
- Role-specific dashboards with key information


Out-of-Scope Items (Explicitly Excluded)
The following items are intentionally excluded from the MVP:

- Online exams or assessments
- Fee/payment management
- Mobile application
- SMS/Email gateway integration
- Advanced analytics and reports
- Student self-service features

High-Level Timeline (3 Weeks)

Week 1 – Planning & Foundation
- Finalize requirements and MVP scope
- Database schema design
- Low-fidelity wireframes
- Backend project setup

Milestone: Requirements & Architecture Locked

Week 2 – Core Feature Development
- Authentication & RBAC
- Attendance module
- Grading module

Milestone: Core Academic Features Complete

Week 3 – Communication, Testing & Deployment Prep
- Parent communication module
- Dashboards
- Manual testing
- Documentation
- Deployment plan

Milestone: MVP Ready for Demo


Simple Gantt Chart (Conceptual)

| Task / Week                | Week 1 | Week 2 | Week 3 |
|----------------------------|--------|--------|--------|
| Requirements & Design      | ████   |        |        |
| Auth & RBAC                | ████   | ████   |        |
| Attendance Module          |        | ████   |        |
| Grading Module             |        | ████   |        |
| Communication Module       |        |        | ████   |
| Dashboards & Testing       |        |        | ████   |
| Documentation & Deployment |        |        | ████   |

Notes
- Gantt chart mirrors a simple Google Sheets / draw.io representation.
- This plan is designed for a small team or solo developer.
- Timeline assumes part-time development with focused scope control.