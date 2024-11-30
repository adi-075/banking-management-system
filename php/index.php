<!<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
  header("Location: login.php");
  exit;
}
?>

  <!DOCTYPE html>
  <html lang="en">

  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./styles/styles.css">
    <title>Chase Bank</title>
  </head>

  <body>
    <nav class="navbar">
      <!-- Chase Brand -->
      <a href="index.php" class="navbar-brand" style="margin-left: 20px">
        <img src="assets/chase.svg" width="100" alt="Chase logo" />
      </a>
      <!-- Links -->
      <ul class="nav-links">
        <li class="nav-item">
          <a href="accounts.php">Accounts</a>
        </li>
        <li class="nav-item">
          <a href="services.php" class="">Services</a>
        </li>
        <li class="nav-item">
          <a href="" class="">Transfer Funds</a>
        </li>
        <li class="nav-item">
          <a href="logout.php">Logout</a>
        </li>
      </ul>
    </nav>

    <div class="content">
      <div class="container">
        <h2 style="color: white;padding-top: 100px; font-size: 2rem;text-align: center">
          New Chase<br> customers
        </h2>
        <br>
        <div class="vertical-center">
          <a href="accounts.php">
            <button class="acc-btn">
              Open an Account
            </button>
          </a>
        </div>
      </div>
    </div>

    <!-- <footer class="footer">
      <div class="footer-container">
        <div class="footer-links">
          <div class="footer-column">
            <h4>Banking</h4>
            <ul>
              <li><a href="#">Checking Accounts</a></li>
              <li><a href="#">Savings Accounts</a></li>
              <li><a href="#">Credit Cards</a></li>
              <li><a href="#">Loans</a></li>
            </ul>
          </div>
          <div class="footer-column">
            <h4>Resources</h4>
            <ul>
              <li><a href="#">Customer Service</a></li>
              <li><a href="#">Security Center</a></li>
              <li><a href="#">Privacy Notice</a></li>
              <li><a href="#">Site Map</a></li>
            </ul>
          </div>
          <div class="footer-column">
            <h4>About Us</h4>
            <ul>
              <li><a href="#">Our Company</a></li>
              <li><a href="#">Careers</a></li>
              <li><a href="#">Investor Relations</a></li>
              <li><a href="#">Media Center</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2024 Chase Bank. All rights reserved.</p>
          <p><a href="#">Terms of Use</a> | <a href="#">Privacy Policy</a></p>
        </div>
      </div>
    </footer> -->

  </body>

  </html>