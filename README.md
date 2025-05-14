# 🏰 Castle Apartments

<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/herdisheida/castle_apartments">
    <img src="static/images/app_logo.png" alt="Castle Apartments Logo" width="120" height="120">
  </a>
  <h1>Castle Apartments</h1>
  <p>
    <strong>Revolutionizing real estate with modern technology</strong>
  </p>
  <p>
    A robust web application built with Django, Python, and PostgreSQL to empower Castle Apartments' real estate operations.
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#extra-requirements">Extra requirements</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>


<!-- INFO -->
## About the Project
Castle Apartments is an innovative real estate company looking to disrupt the market with cutting-edge technology. This web application provides:

- Property listing management
- Offer negotiation system
- Interactive property showcases 
- Seller dashboard

### Key Features
- **Seller Portal**:
  - Create property listings
  - Receive and evaluate purchase offers
  - Negotiate with buyers through contingent comments
  - Accept or reject offers with one click

- **Buyer Experience**:
  - Browse available properties
  - Submit competitive offers
  - Receive real-time updates on offer status

### Extra requirements:
- You can become a seller
- You can accept or reject an offer as a seller
- You can create a property as a seller and put it up for listing
- You can add a contingent comment to a offer when you find the offer unsatisfactory


## Getting Started
- Python 3.9+
- PostgreSQL 12+
- pip

### Prerequisites
Install dependencies listed in requirements.txt
   ```sh
   pip install -r requirements.txt
   ```

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/herdisheida/castle_apartments.git
   cd castle_apartments
   ```
2. Set up the virtual environment
   ```sh
   python -m venv venv
   source venv/bin/activate # On mac
   ```
3. Install the dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Running the application
   a) Apply the migrations
   ```sh
   python manage.py migrate
   ```
   b) Run the development server:
   ```sh
   python manage.py runserver
   ```
   c) Access the application at:
   ```sh
   http://localhost:8000
   ```