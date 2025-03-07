# Bismillah Motors - Vehicle Management System

## Deployment Instructions

This repository contains deployment packages for different operating systems. Choose the appropriate package for your system:

### Windows Deployment
1. Download `BismillahMotors_Windows.zip`
2. Extract the zip file to a folder of your choice
3. Double-click `install.bat` to start the installation
4. Follow the on-screen instructions
5. Once installed, run `BismillahMotors.exe` to start the application
6. Access the application at http://localhost:5000

*or just run the exe prebuild in /dist/app.exe*

### Linux Deployment
1. Download `BismillahMotors_Linux.zip`
2. Extract the zip file:
   ```bash
   unzip BismillahMotors_Linux.zip
   ```
3. Make the installation script executable:
   ```bash
   chmod +x install.sh
   ```
4. Run the installation script:
   ```bash
   ./install.sh
   ```
5. Access the application at http://localhost:5000

### macOS Deployment
1. Download `BismillahMotors_macOS.zip`
2. Extract the zip file:
   ```bash
   unzip BismillahMotors_macOS.zip
   ```
3. Make the installation script executable:
   ```bash
   chmod +x install.sh
   ```
4. Run the installation script:
   ```bash
   ./install.sh
   ```
5. Access the application at http://localhost:5000

## System Requirements

### Windows
- Windows 10 or later
- No additional software required

### Linux
- Linux (Ubuntu 20.04 LTS or later recommended)
- Python 3.11 or later
- pip (Python package manager)

### macOS
- macOS 10.15 (Catalina) or later
- Python 3.11 or later
- pip (Python package manager)

# Vehicle Management System

A modern Flask web application for managing vehicle sales and purchases. This application helps you keep track of all vehicle-related information including vehicle details, buyer and seller information, and deal details.

## Features

- Modern, responsive design that works on both desktop and mobile devices
- Search vehicles by registration number, make, model, buyer, or seller
- Add new vehicle deals with comprehensive information
- View detailed information about each vehicle
- Organized sections for vehicle, buyer, seller, and deal information
- User-friendly interface with intuitive navigation

## Requirements

- Python 3.8 or higher
- Flask and other dependencies listed in requirements.txt

## Installation

1. Clone this repository or download the source code
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your web browser and navigate to `http://localhost:5000`

## Database

The application uses SQLite as the database, which will be automatically created when you first run the application. The database file will be named `vehicles.db` and will be created in the project directory.

## Usage

1. **Home Page**: The home page features a search box where you can search for vehicles using various parameters.
2. **Add New Deal**: Click the "Add New Deal" button to add a new vehicle transaction.
3. **Search Results**: View search results in a clean, organized table format.
4. **Vehicle Details**: Click the eye icon in search results to view detailed information about a specific vehicle.

## Data Fields

### Vehicle Details
- Registration Number
- Make
- Model
- Copy
- Engine Number
- Chasis Number
- Registered To
- Token

### Buyer Details
- Name
- CNIC
- Address
- Father's Name
- Contact
- Purchase Date

### Seller Details
- Name
- CNIC
- Address
- Father's Name
- Contact
- Witness

### Deal Details
- Deal Date
- Deal Price
- Advance Amount
- Balance Amount

## Contributing

Feel free to submit issues and enhancement requests! 
