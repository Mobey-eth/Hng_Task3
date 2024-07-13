# Messaging System with Flask, Celery, RabbitMQ, and Nginx

This project demonstrates how to set up a messaging system using Flask, Celery, RabbitMQ, and Nginx. The system includes asynchronous email sending and logging functionalities.

## Table of Contents

- [Messaging System with Flask, Celery, RabbitMQ, and Nginx](#messaging-system-with-flask-celery-rabbitmq-and-nginx)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Endpoints](#endpoints)
  - [Logging](#logging)
  - [Video Walkthrough](#video-walkthrough)
  - [Live Demo](#live-demo)
  - [License](#license)

## Overview

The messaging system is designed to handle email sending asynchronously using Celery and RabbitMQ. It also logs specific requests to a file for later review.

## Features

- Asynchronous email sending
- Request logging
- Integration with RabbitMQ for task management
- Exposed endpoints for triggering email sending and logging
- Downloadable log files

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Mobey-eth/Hng_Task3.git
    cd messaging-system
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up RabbitMQ:**

    Ensure RabbitMQ is installed and running on your machine. You can find installation instructions [here](https://www.rabbitmq.com/download.html).

5. **Set up environment variables:**

    Create a `.env` file in the project root and add your email credentials:

    ```env
    EMAIL_USERNAME=your-email@gmail.com
    EMAIL_PASSWORD=your-app-specific-password
    ```

## Usage

1. **Start the Flask application:**

    ```sh
    python app.py
    ```

2. **Start the Celery worker:**

    ```sh
    celery -A app.celery worker --loglevel=info
    ```

3. **Expose your local server using ngrok:**

    ```sh
    ngrok http 80
    ```

## Endpoints

- **`/`**: Main endpoint for sending emails and logging requests.
    - **`?sendmail=email@example.com`**: Queues an email to be sent to the specified address.
    - **`?talktome`**: Logs the current time and request to the log file.
- **`/log`**: Endpoint to download the log file.

## Logging

Logs are stored in `/var/log/messaging_system.log`. The log file includes timestamps and request details.

## Video Walkthrough

For a detailed explanation of the setup and functionalities, watch the video walkthrough [here](https://www.loom.com/share/cc6a8e7ebdd148a582d6043f18e60402?sid=3ac8486b-9e6e-4446-af2a-a57d4dc1bb8f).

## Live Demo

Access the live demo [here](https://b1f4-197-210-78-161.ngrok-free.app).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
