<?php

// Include necessary libraries
require_once 'StockDataAPI.php'; // Class for historical data access
require_once 'Portfolio.php'; // Class for managing your portfolio

// Initialize variables and session
session_start();
if (!isset($_SESSION['portfolio'])) {
    $_SESSION['portfolio'] = new Portfolio();
}
$portfolio = $_SESSION['portfolio'];
$error = '';
$start_date = isset($_GET['date']) ? $_GET['date'] : '2024-02-05';

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate user input
    $symbol = filter_input(INPUT_POST, 'symbol');
    $quantity = filter_input(INPUT_POST, 'quantity', FILTER_VALIDATE_INT);

    if (!$symbol || !$quantity) {
        $error = 'Please enter a valid symbol and quantity.';
    } else {
        // Attempt to fetch historical price using StockDataAPI
        $price = StockDataAPI::getHistoricalPrice($symbol, $start_date);

        // Handle potential errors in price retrieval
        if ($price === false) {
            $error = 'Invalid symbol or data unavailable for the specified date.';
        } else {
            // If successful, buy the stock and update session data
            $portfolio->buyStock($symbol, $quantity, $price);
            $_SESSION['portfolio'] = $portfolio;
            echo $price; // Provide feedback to user
        }
    }
}

// Display current date
echo $start_date;

// Advance day (replace with logic to fetch actual historical data)
$newPrices = StockDataAPI::getDailyPrices($start_date);

if ($newPrices !== false) {
    $portfolio->updatePrices($newPrices);
    $_SESSION['portfolio'] = $portfolio;
    echo 'prices updated', $start_date;
} else {
    $error = 'Unable to retrieve data for the next day.';
}

// Handle potential errors during price update
if ($error) {
    echo $error; // Display error message to user
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Historical Stock Simulator</title>
</head>
<body>
    <h1>Historical Stock Simulator</h1>
    <h2><?php echo $start_date; ?></h2>

    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
        <label for="symbol">Symbol:</label>
        <input type="text" name="symbol" id="symbol">
        <label for="quantity">Quantity:</label>
        <input type="number" name="quantity" id="quantity">
        <button type="submit">Buy</button>
    </form>

    <?php if ($portfolio->getHoldings()): ?>
        <h2>Portfolio</h2>
        <table>
            <thead>
                <tr>
                    <th>Symbol</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Value</th>
                    <th>Change</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($portfolio->getHoldings() as $symbol => $holding): ?>
                    <tr>
                        <td><?php echo $symbol; ?></td>
                        <td><?php echo $holding['quantity']; ?></td>
                        <td><?php echo number_format($holding['price'], 2); ?></td>
                        <td><?php echo ($holding['price'] * $holding['quantity']); ?></td>
                        <td><?php echo number_format($holding['change'] * 100, 2) . '%'; ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php else: ?>
        <p>No holdings yet.</p>
    <?php endif; ?>

    <p>Click the button below to advance the day and update prices.</p>
    <button onclick="advanceDay()">Advance Day</button>

    <script>
        function advanceDay() {
            // Update date and reload page
            var date = new Date('<?php echo $start_date; ?>');
            date.setDate(date.getDate() + 1);
            var newDate = date.toISOString().split('T')[0];
            window.location.href = 'index.php?date=' + newDate;
        }
    </script>
