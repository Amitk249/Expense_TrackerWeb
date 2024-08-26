
# **Expense Tracking Application**

## **Overview**

This project is a full-stack expense tracking application designed to help users manage their finances by recording, categorizing, and generating reports of their expenses. The application provides essential features such as user authentication, expense management, category management, and report generation. The backend is developed using Django, while the front end integrates with Django templates.

## **Features**

### **1. User Authentication**

- **Registration:**
  - Users can create an account by providing a username, and password.
  - Upon successful registration, users are automatically logged in.
  
- **Login:**
  - Users can log in using their Username and password.
  
- **Logout:**
  - Users can log out of their session securely.

### **2. Expense Management**

- **Create Expense:**
  - Users can add a new expense by providing details such as description, amount, category, and date.
  - Expenses are associated with the logged-in user and stored in the database.
  
- **View Expenses:**
  - Users can view a list of their recorded expenses, with filtering options by date and category.
  
- **Edit Expense:**
  - Users can update their existing expenses.
  - Only the owner of the expense can edit it, ensuring data integrity.
  
- **Delete Expense:**
  - Users can delete their expenses, with a confirmation step to prevent accidental deletion.

### **3. Category Management**

- **Create Category:**
  - Categories can be created, allowing users to categorize their expenses effectively.
  
- **View Categories:**
  - Users can view a list of available categories.

- **Note:** Categories are currently global and not user-specific. Future updates will include user-specific category management.

### **4. Reports and Summaries**

- **Summary Report:**
  - Users can generate a summary report that includes:
    - Total expenditure
    - Average expenditure
    - Expenditure breakdown by category

- **Expenses by Date Range:**
  - Users can filter and view their expenses within a specific date range.

- **Expenses by Category:**
  - Users can view their expenses grouped by category, providing insights into their spending habits.

### **5. Frontend Integration**

- **Basic UI Implementation:**
  - The frontend is integrated with Django templates, allowing users to interact with the application through forms and views.

- **Templates:**
  - Basic HTML templates are in place for registration, login, expense management, category management, and reports.

### **6. Database Integration**

- **Data Models:**
  - The data models for `User`, `Expense`, and `Category` have been implemented and integrated with the database.

- **Data Storage:**
  - All CRUD operations for expenses and categories are functioning and integrated with the database.

### **7. Security and Performance**

- **Basic Security:**
  - User authentication is in place, and forms are validated.
  - User-specific filtering ensures that users can only access their data.

## **Technology Stack**

- **Backend:** Django
- **Frontend:** Django Templates, HTML, CSS
- **Database:** SQLite (can be upgraded to PostgreSQL or MySQL)
- **Authentication:** Django's built-in authentication system (JWT implementation pending)

## **Installation and Setup**

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd expense-tracker
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```
6. Access the application at `http://127.0.0.1:8000/`.

## **Conclusion**

This expense tracking application is **85%** complete, with core functionalities implemented. The project serves as a robust foundation for personal finance management, with further enhancements planned to optimize security, performance, and user experience.

---

This README provides a comprehensive overview of what has been accomplished so far and what remains to be done. It should give your recruiter a clear picture of your progress and the scope of the project.
