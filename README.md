# CodePath-Navigator
# 🐍 Python Learning Navigator

A comprehensive command-line application designed to help Python learners organize study resources, track academic performance, and analyze learning progress through an interactive dashboard.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Functionality Overview](#functionality-overview)
- [Data Storage](#data-storage)
- [Requirements](#requirements)
- [Contributing](#contributing)

## ✨ Features

### 📚 Resource Management
- Add and organize learning resources (PDFs, videos, notebooks, links, etc.)
- Categorize resources by subject and topic
- Tag resources for easy filtering
- Search resources by keywords
- Delete resources when no longer needed

### 📈 Performance Tracking
- Log assessments and test scores
- Track multiple assessment types (quizzes, assignments, midterms, finals)
- Calculate percentages automatically
- View assessment history sorted by date
- Delete assessment records

### 📊 Analytics Dashboard
- View overall performance statistics
- Subject-wise performance breakdown with visual bars
- Identify weak areas (topics scoring below 70%)
- Track total resources and assessments
- Calculate average scores across subjects and topics

## 🚀 Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd python-learning-navigator
   ```

2. **Ensure Python 3.6+ is installed**
   ```bash
   python --version
   ```

3. **No external dependencies required** - Uses only Python standard library

## 💻 Usage

### Running the Application

```bash
python academic_navigator.py
```

### Main Menu Options

1. **Dashboard (Analytics)** - View comprehensive performance statistics
2. **Resource Management** - Add, view, search, or delete study resources
3. **Performance Tracking** - Log and manage assessment results
4. **Exit** - Close the application

### Adding a Resource

1. Navigate to Resource Management → Add New Resource
2. Enter resource details:
   - Title (required)
   - Type (PDF, Video, Link, etc.)
   - Subject
   - Topic (optional)
   - URL (optional)
   - Tags (optional, comma-separated)

### Logging an Assessment

1. Navigate to Performance Tracking → Log New Assessment
2. Enter assessment details:
   - Title (required)
   - Type (Quiz, Assignment, etc.)
   - Subject
   - Topic (optional)
   - Score obtained
   - Maximum score
   - Date (optional, defaults to today)

### Viewing Dashboard

The dashboard displays:
- Total resources and assessments
- Overall average performance
- Subject-wise performance with visual bars
- Areas needing attention (topics below 70%)

## 📁 File Structure

```
python-learning-navigator/
│
├── academic_navigator.py    # Main application file
├── resources.json           # Stores learning resources (auto-generated)
├── assessments.json         # Stores assessment records (auto-generated)
└── README.md               # This file
```

## 🔧 Functionality Overview

### Pre-configured Subjects
- Python Basics
- Data Structures
- Object-Oriented Programming
- File Handling
- Libraries & Frameworks
- Web Development
- Data Analysis

### Resource Types
- PDF
- Document
- Link
- Video
- Jupyter Notebook
- Python Script
- Notes
- Tutorial

### Assessment Types
- Quiz
- Assignment
- Midterm
- Final
- Practice Test
- Self-Test

## 💾 Data Storage

The application uses JSON files for persistent storage:

- **resources.json** - Stores all learning resources with metadata
- **assessments.json** - Stores all assessment records with scores

Data files are automatically created on first use and updated with each operation.

### Sample Resource Structure
```json
{
  "id": 1,
  "title": "Python OOP Tutorial",
  "type": "Video",
  "subject": "Object-Oriented Programming",
  "topic": "Classes and Objects",
  "url": "https://example.com/video",
  "tags": ["beginner", "oop", "tutorial"],
  "date_added": "2025-01-15"
}
```

### Sample Assessment Structure
```json
{
  "id": 1,
  "title": "Python Basics Quiz",
  "type": "Quiz",
  "subject": "Python Basics",
  "topic": "Variables and Data Types",
  "score": 18,
  "max_score": 20,
  "percentage": 90.0,
  "date": "2025-01-20"
}
```

## 📦 Requirements

- **Python**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: None (uses only standard library)

### Standard Library Modules Used
- `json` - Data persistence
- `os` - File operations and screen clearing
- `datetime` - Date/time handling
- `typing` - Type hints

## 🎯 Use Cases

- **Students** learning Python programming
- **Self-learners** tracking their progress
- **Bootcamp participants** organizing course materials
- **Anyone** building a structured learning path in Python

## 🤝 Contributing

Contributions are welcome! Here are some ways you can enhance the application:

- Add export functionality (CSV, PDF reports)
- Implement data visualization with charts
- Add study schedule/reminder features
- Create a GUI version
- Add import functionality for bulk resources
- Implement backup and restore features

## 📝 License

This project is available for educational purposes. Feel free to modify and distribute as needed.

## 🐛 Known Issues

- Screen clearing may not work properly in some terminal emulators
- No input validation for date formats (assumes YYYY-MM-DD)
- No data backup mechanism

## 🔮 Future Enhancements

- Web-based interface
- Cloud storage integration
- Study time tracking
- Spaced repetition system
- Goal setting and progress tracking
- Export reports in multiple formats
- Mobile companion app

## 📧 Support

For questions, issues, or suggestions, please open an issue in the repository.

---

**Happy Learning! 🚀**
Remember: Consistent tracking leads to better insights, and better insights lead to improved learning outcomes!
