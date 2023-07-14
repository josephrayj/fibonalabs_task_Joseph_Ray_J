# Fibonalabs Task 
Joseph Ray J

## Project Goal

To make a Coding platform where participants can solve questions for the problems provided, and the admin can add, edit or delete the questions.

### Basic Requirements:

· Role-based authentication system for admin and participants.

· Create a signup() feature :

· Input: name, email, password, role

· Encrypt passwords using any package supporting hash functions.

· Store users in any database .

· Create a JWT-based access token (1-day expiry).

· Output : email , accesstoken

· Create a login() feature :

· Input: email, password

· Verify email & password from DB and return appropriate response if mismatch.

· Output : email , accesstoken

· Create a middleware to differentiate admins from participants.

· A set of APIs for the admin to add, edit or delete the question. Create a Questions table in the DB.

· A set of APIs for the admin to add test cases to a question.

· An API that takes the solution from the user for a particular question. The functionality of that API should be

· Show the response (error/wrong/success) of the solution

· No need to save the solution in DB.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Question Endpoints](#question-endpoints)
  - [Test Case Endpoints](#test-case-endpoints)
  - [Solution Submission Endpoint](#solution-submission-endpoint)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/josephrayj/fibonalabs_task_Joseph_Ray_J.git
   ```

2. Navigate to the project directory:

   ```shell
   cd project
   ```

3. Create a virtual environment:

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

7. Run the development server:

   ```shell
   python manage.py runserver
   ```

8. Access the application in your web browser at `http://localhost:8000`.

## Usage

### Authentication

To access the protected endpoints, you need to authenticate using JSON Web Tokens (JWT). Follow these steps to authenticate:

1. Signup a new user:

   - Send a POST request to `/api/signup` with the following JSON body:

     ```json
     {
       "name": "John Doe",
       "email": "johndoe@example.com",
       "password": "password123",
       "role": "admin"
     }
     ```

   - On success, you will receive a response with the user's email and access token.

2. Login with the created user:

   - Send a POST request to `/api/login` with the following JSON body:

     ```json
     {
       "email": "johndoe@example.com",
       "password": "password123"
     }
     ```

   - On success, you will receive a response with the user's email and access token.

3. For subsequent requests, add an `Authorization` header to the request with the value `Bearer <access_token>`. Replace `<access_token>` with the access token received during authentication.

### Question Endpoints

- **List Questions**: Retrieve a list of questions.

  - Send a GET request to `/api/questions`.

- **Create Question**: Create a new question.

  - Send a POST request to `/api/questions` with the following JSON body:

    ```json
    {
      "title": "Question Title",
    }
    ```

- **Retrieve Question**: Retrieve a specific question.

  - Send a GET request to `/api/questions/{question_id}` where `{question_id}` is the ID of the question.

- **Update Question**: Update a specific question.

  - Send a PUT request to `/api/questions/{question_id}` where `{question_id}` is the ID of the question, with the following JSON body:

    ```json
    {
      "title": "Updated Question Title",
    }
    ```

- **Delete Question**: Delete a specific question.

  - Send a DELETE request to `/api/questions/{question_id}` where `{question_id}` is the ID of the question.

### Test Case Endpoints

- **Create Test Case**: Add a test case to a question.

  - Send a POST request to `/api/questions/{question_id}/testcases` where `{question_id}` is the ID of the question, with the following JSON body:

    ```json
    {
      "input": "Test Input",
      "output": "Expected Output"
    }
    ```

- **Retrieve, Update, Delete Test Case**: Retrieve, update, or delete a specific test case.

  - Send a GET request to `/api/testcase/{testcase_id}` where `{testcase_id}` is the ID of the test case.

  - Send a PUT request to `/api/testcase/{testcase_id}` where `{testcase_id}` is the ID of the test case, with the following JSON body:

    ```json
    {
      "input": "Updated Test Input",
      "output": "Updated Expected Output"
    }
    ```

  - Send a DELETE request to `/api/testcase/{testcase_id}` where `{testcase_id}` is the ID of the test case.

### Solution Submission Endpoint

- **Submit Solution**: Submit a solution for a specific question and evaluate the response.

  - Send a POST request to `/api/questions/{question_id}/submit` where `{question_id}` is the ID of the question, with the following JSON body:

    ```json
    {
      "solution": "my solution"
    }
    ```
