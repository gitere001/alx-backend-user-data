# Authentication System

This project implements a simple authentication system in Python. The system handles user registration, login validation, session management, and session destruction.

## Features

- **User Registration**: Register a new user with an email and password. The password is securely hashed before storing.
- **Login Validation**: Validate user login by checking the provided password against the stored hashed password.
- **Session Management**:
  - Create a session for a user and generate a unique session ID.
  - Retrieve a user associated with a session ID.
  - Destroy a user's session by removing the session ID.

## Code Overview

- `Auth` Class:
  - **`register_user(email: str, password: str) -> User`**: Registers a new user with the given email and password.
  - **`valid_login(email: str, password: str) -> bool`**: Validates a user's login credentials.
  - **`create_session(email: str) -> Union[str, None]`**: Creates a new session for the user and returns the session ID.
  - **`get_user_from_session_id(session_id: Union[str, None]) -> Union[User, None]`**: Retrieves the user associated with the given session ID.
  - **`destroy_session(user_id: Union[int, None]) -> None`**: Destroys the session associated with the given user ID.

- Helper Functions:
  - **`_hash_password(password: str) -> bytes`**: Hashes the user's password using `bcrypt`.
  - **`_generate_uuid() -> str`**: Generates a unique UUID string for session IDs.

## Type Annotations

The project includes type annotations for all functions and methods, enhancing code clarity and type safety.

## Usage

1. Initialize the `Auth` class.
2. Use the `register_user` method to add a new user.
3. Use `valid_login` to validate login credentials.
4. Create and manage sessions using `create_session`, `get_user_from_session_id`, and `destroy_session`.

## License

This project is open-source and available under the MIT License.
