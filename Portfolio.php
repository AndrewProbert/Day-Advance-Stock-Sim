<?php

class Portfolio {

    private $holdings = [];

    public function buyStock($symbol, $quantity, $price) {
        if (isset($this->holdings[$symbol])) {
            $this->holdings[$symbol]['quantity'] += $quantity;
        } else {
            $this->holdings[$symbol] = [
                'quantity' => $quantity,
                'price' => $price,
            ];
        }
    }

    public function getHoldings() {
        return $this->holdings;
    }

    public function updatePrices($newPrices) {
        foreach ($this->holdings as $symbol => $holding) {
            if (isset($newPrices[$symbol])) {
                $this->holdings[$symbol]['price'] = $newPrices[$symbol];
                $this->holdings[$symbol]['value'] = $newPrices[$symbol] * $holding['quantity'];
            }
        }
    }

}

?>

