# ChatApp

A **real-time chat application** built with Django, enabling users to communicate seamlessly in chat rooms with secure, real-time messaging.

## Features

- **Chat Rooms**: Create or join dedicated chat rooms for group or individual discussions.
- **Real-Time Messaging**: Instant message exchange powered by WebSocket and Django Channels.
- **User Authentication**: Secure login and registration system.
- **Responsive Design**: Works across devices.

## Technologies Used

- **Framework**: [Django](https://www.djangoproject.com/)
- **Real-Time Communication**: [Django Channels](https://channels.readthedocs.io/en/stable/)
- **Frontend Styling**: HTML, CSS, JavaScript, Bootstrap/Tailwind
- **Database**: SQLite 
- **Message Broker**: Redis (used as the channel layer backend)

## Prerequisites

To run this project, ensure you have the following installed:

- Python (version 3.8 or higher)
- Redis server or Docker
- Node.js and npm (if additional frontend packages are used)

## Installation and Setup

 1. Clone the Repository

```bash
git clone https://github.com/NikHil12907/ChatApp.git
```

 2. Navigate to Project Folder

  ```bash
  cd ChatApp
  ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
   
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```
6.  Set Up Redis

    ```bash
     sudo apt install redis
    ```
7. Start Redis with the following command:

   ```bash
   redis-server
   ```

   ### Or Open cmd 

   ```bash
   cd <Redis_path>
   redis-server.exe
   ```

8. If You have docker then run following command:

   ```bash
   docker run -d -p 6379:6379 redis
   ```

9. Apply database Migrations:

   ```bash
   python manage.py migrate
   ```

10. Start the Development server:

    ```bash
    python manage.py runserver
    ```

### Both servers need to be running for real-time messaging to work.

### Usage
- **Login/Register**: Users can create an account or log in to access chat rooms.
- **Join or Create Rooms**: Join existing chat rooms or create new ones to start chatting.
- **Real-Time Messaging**: The app supports live message exchange between users in a room.



      



