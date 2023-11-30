
## Overview
Briefly describe your application and its functionality.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - **Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    - **Linux/Mac:**

        ```bash
        source venv/bin/activate
        ```

3. Create a `.env/.py` file in the project root and add your configuration variables [site here](https://unsplash.com/):

    ```env
    UNSPLASH_ACCESS_KEY=your_unsplash_access_key
    ```

    Replace `your_unsplash_access_key` with your Unsplash API access key.

## Running the Application

Run the following command to start the Flask application:

```bash
python main.py
```
Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the application.

## Postman Workspace

Explore the functionality of  application using Postman. [Postman workspace here](https://app.getpostman.com/join-team?invite_code=ee1da645a0b21786df272eee23f4e347&target_code=c501f68879e0a8a0ce38b05a6ba3f3ef). Import the provided Postman collection and document the requests and responses in the collection.

