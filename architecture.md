# System Architecture  
系统架构  

## Main Components / 主要组成部分  
- **Frontend (前端)**: Provides user interface for reminders and statistics visualization.  
- **Backend (后端)**: Handles user data, reminder scheduling, and notification logic.  
- **Database (数据库)**: Stores user information, reminder settings, and activity logs.  

## Architecture Diagram / 架构图  

```plaintext
[User Interface] 
       ↓
[Frontend App (HTML/CSS/JS)] 
       ↓
[Flask API Server (Python)] 
       ↓
[SQLite Database]
