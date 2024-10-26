# Job-Portal CRUD Application API

## Table of Contents
- [Project Overview](#project-overview)
- [Team Collaboration](#team-collaboration)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Usage](#usage)

## Project Overview
The Job Portal CRUD Application API is a comprehensive solution designed to facilitate job search and recruitment processes. The application provides a streamlined API that enables users to Create, Read, Update, and Delete job listings efficiently. Its user-friendly interface and responsive design make it accessible across devices, enhancing the experience for job seekers and employers alike.

Key Features:
- **User-Friendly Interface**: Intuitive design allows easy navigation for users to post and browse job listings.
- **CRUD Operations**: Supports creating, reading, updating, and deleting job postings.
- **Dynamic Data Handling**: Ensures up-to-date information with real-time listing management.
- **Responsive Design**: Optimized for mobile and desktop, ensuring seamless access across devices.

This application aims to connect job seekers and employers, simplifying the recruitment process and enhancing user experience.

---

## Team Collaboration
- **Touseef Hanif** (API Development): Developed and implemented core CRUD endpoints for managing job listings, focusing on data efficiency and integrity. Ensured that the API effectively handles user requests and maintains robust performance under load.

- **Muhammad Abdullah Malik** (Documentation): Created comprehensive documentation for the API, including detailed endpoint descriptions and usage examples. This documentation ensures that users can easily understand and utilize the API's features.

- **Syed Danayal Raza** (Testing): Conducted extensive testing of all API endpoints to verify functionality and performance. Identified and resolved issues to ensure a smooth user experience and maintain high-quality standards throughout the application.
---



## API Endpoints
### 1. Create Job Listing
- **Endpoint**: `/jobs`
- **Method**: `POST`
- **Description**: Allows users to create a new job listing by providing job title, description, and other relevant details.
## Installation Process

To set up the Job Portal CRUD Application API on your local machine, follow these steps:
1. **Clone the Repository**
   ```bash
   https://github.com/TouseefH/job-portal.git
2. **Navigate to the Project Directory**
   ```bash
   cd job-portal
3. **Create a Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
5. **Activate the Virtual Environment**
   ```bash
   venv\Scripts\activate
6. **Install Dependencies**
    ```bash
   pip install -r requirements.txt

## Usage
1. **Run the application**
    ```bash
   python manage.py run server

2. **Run the application through docker**
2.1 **Build the Docker Image**
    ```bash
    docker build -t mydjangoapp
2.2 **Run the Application**
    ```bash
    
    docker run -p 8000:8000 mydjangoapp
    
2.3 **Access the application (open your web browser)** 
    ```bash
    
    http://localhost:8000/
