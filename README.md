# Inventory Tracking App

This app is a simple command line tool to manage stock using a JSON file.

## Features
* List all items with quantity, price and stock status
* Show items that are out of stock
* Display total dollar value of items in stock
* Scan items to add or order products by barcode

## Usage
```
python inventory.py --init      # initialize sample inventory (only first time)
python inventory.py list        # list all inventory items
python inventory.py outofstock  # show out of stock items
python inventory.py total       # show total value
python inventory.py scan <barcode> --mode add   # add one to quantity
python inventory.py scan <barcode> --mode order # deduct one when ordering
```

Inventory data is stored in `inventory.json`.
