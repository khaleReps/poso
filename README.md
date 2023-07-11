# Mangolo

Poso is an Email client, a web application designed to provide similar functionality and features like your normara. It is built using the MEVN stack (MongoDB, Express.js, Vue.js, Node.js) and Docker for easy deployment. Poso allows users to manage their emails, calendars, and contacts in a user-friendly and intuitive interface.


## Features

- **Email Management:** Send, receive, and organize emails with features like composing, replying, forwarding, and archiving.
- **Calendar:** Manage your schedule, create events, set reminders, and view your calendar in different time views (day, week, month).
- **Contacts:** Store and manage your contacts with features like adding, editing, and deleting contacts, and organizing them into groups.
- **Folders:** Organize your emails into folders such as Inbox, Sent, Drafts, and more.
- **Search:** Search functionality to find specific emails, contacts, or events quickly.
- **User Authentication:** Secure user authentication and authorization system to protect user data and ensure privacy.
- **Responsive Design:** The application is responsive and optimized for various screen sizes and devices.


## Technologies Used

- **MongoDB:** A NoSQL database used to store and retrieve note data.
- **Express.js:** A backend framework for building RESTful APIs and handling server-side logic.
- **Vue.js:** A JavaScript framework for building user interfaces and managing the frontend of the application.
- **Node.js:** A JavaScript runtime environment that executes server-side code and powers the backend of the application.
- **HTML/CSS:** The project uses HTML for markup and CSS for styling and layout.
- **Bootstrap:** Bootstrap is used for responsive design and pre-built UI components to enhance the application's aesthetics.
- **JavaScript:** The primary programming language used for frontend and backend development.
- **Git:** Git is used for version control, allowing easy collaboration and tracking of changes throughout the development process.
- **Docker:** Docker is used to containerize the project for easy deployment and reproducibility.


## Getting Started

To run the poso project locally, follow these steps:

1. **Clone the repository**: Start by cloning this repository to your local machine using the following command:

'git clone <repository-url>'

2. **Build the Docker image**: Navigate to the project directory and build the Docker image using the following command:

`docker build -t poso-app .`

This command builds the Docker image with the tag "portfolio" based on the Dockerfile.

3. **Run the Docker container**: After the Docker image is built, run a container based on the image with the following command:

`docker run -p 3013:3013 poso-app`

This command maps port 3013 on your local machine to port 80 inside the Docker container, allowing you to access the poso project in your browser at `http://localhost:3013`.

4. **Access the website**: Open a web browser and visit `http://localhost:3013` to view the poso project.


## Contributing

Contributions to the project are welcome! If you find any bugs, have suggestions, or would like to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md).