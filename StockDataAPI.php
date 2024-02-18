<?php

class StockDataAPI {

    private static $dataDir = 'Stock_Data'; // Adjust based on your actual directory

    public static function getHistoricalPrice($symbol, $date) {
        // Use `getCsvData` to access and parse relevant date's data
        $data = self::getCsvData($symbol, $date);
        if ($data !== false && isset($data['Adj Close'])) {
            return floatval($data['Adj Close']); // Assuming 'Adj Close' column for adjusted price
        } else {
            return false;
        }
    }

    public static function getDailyPrices($date) {
        // Get data for all symbols on the specified date
        $prices = [];
        foreach (glob(self::$dataDir . '/*.csv') as $file) {
            $symbol = pathinfo($file, PATHINFO_FILENAME);
            $data = self::getCsvData($symbol, $date);
            if ($data !== false && isset($data['Adj Close'])) {
                $prices[$symbol] = floatval($data['Adj Close']);
            }
        }
        return $prices;
    }

    private static function getCsvData($symbol, $date) {
        // Handle CSV file access and data parsing
        $filePath = self::$dataDir . '/' . $symbol . '.csv';
        if (!file_exists($filePath)) {
            return false; // Handle missing file gracefully
        }
        $data = [];
        if (($handle = fopen($filePath, 'r')) !== false) {
            while (($row = fgetcsv($handle, 1000, ',')) !== false) {
                if ($row[0] === $date) {
                    $data = array_combine(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], $row);
                    break;
                }
            }
            fclose($handle);
        }
        return $data;
    }
}
