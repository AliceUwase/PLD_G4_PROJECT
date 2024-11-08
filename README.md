# Freelance Job Manager

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

## Overview
A comprehensive Python-based application designed to streamline freelance business operations through client management, job tracking, and financial monitoring capabilities. Built with a focus on simplicity and efficiency, this system helps freelancers manage their business operations effectively.

## 🚀 Features

### 🔐 Authentication System
- Secure user registration and login
- Password reset functionality
- Session management
- Role-based access control

### 👥 Client Management
- Add and store client information
- Search and filter client database
- Update client details
- View client history

### 📋 Job Tracking
- Create and manage job entries
- Real-time status updates
- Deadline monitoring
- Project milestone tracking
- Search and filter jobs

### 💰 Financial Management
- Track earnings and expenses
- Monitor pending payments
- Generate financial reports
- Export financial summaries

## 🏗️ System Architecture

```
├── README.md
├── main.py
├── auth/
│   └── authentication.py
├── client/
│   └── client_management.py
├── jobs/
│   └── job_management.py
└── finance/
    └── financial_management.py
```

## 🛠️ Technical Implementation

### Core Functions
- `create_account()`, `login()`: User authentication
- `display_menu()`: Navigation interface
- `add_client()`, `view_clients()`, `search_clients()`: Client management
- `add_job()`, `view_jobs()`, `mark_job_complete()`: Job tracking
- `view_financial_summary()`: Financial reporting

### Data Storage
- Python dictionaries and lists for in-memory data management
- File-based persistence for data storage between sessions

## 👥 Team & Contributions

| Member | Role | Contributions | GitHub Commits |
|--------|------|---------------|----------------|
| Alice Uwase | - | - | - |
| Ariane Hirwa | - | - | - |
| Gentil Iradukunda Tonny Christian | Developer | - | @irachrist1 |
| Igor Noel Ishimwe | - | - | - |
| James Mukunzi | - | - | - |
| Larissa Iriza | - | - | - |

## 📊 Project Progress

### Completed
- ✅ Basic menu-driven interface
- ✅ Client management system foundation
- ✅ Job tracking structure
- ✅ Financial summary calculations
- ✅ System architecture design

### In Progress
- 🔄 Authentication system implementation
- 🔄 Data persistence
- 🔄 Input validation

### Upcoming
- ⏳ User testing
- ⏳ Documentation
- ⏳ Final integration
- ⏳ Deployment

## 🚧 Known Challenges & Solutions

### Integration
- **Challenge**: Module integration and data flow
- **Solution**: Implementing unified data structures and session management

### Testing
- **Challenge**: Data persistence across sessions
- **Solution**: File-based storage system implementation

### Collaboration
- **Challenge**: Code synchronization
- **Solution**: Established Git workflow and regular team check-ins

## 🔧 Development Guide

### Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Git Workflow
1. Create feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make changes and commit:
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```
3. Push changes:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Create pull request for review

## 📝 License
[Specify your license here]

## 📞 Contact
[Add team contact information]