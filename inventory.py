import json
import argparse
from pathlib import Path

DATA_FILE = Path('inventory.json')

def load_data():
    if DATA_FILE.exists():
        with DATA_FILE.open('r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with DATA_FILE.open('w') as f:
        json.dump(data, f, indent=2)

def list_items(data):
    for barcode, item in data.items():
        status = 'Out of stock' if item['quantity'] <= 0 else 'In stock'
        total_value = item['quantity'] * item['price']
        print(f"{item['name']} | Barcode: {barcode} | Qty: {item['quantity']} | Price: ${item['price']:.2f} | Total: ${total_value:.2f} | {status}")

def out_of_stock(data):
    for barcode, item in data.items():
        if item['quantity'] <= 0:
            print(f"{item['name']} (Barcode: {barcode}) is OUT OF STOCK")

def total_value(data):
    total = sum(item['quantity'] * item['price'] for item in data.values())
    print(f"Total inventory value: ${total:.2f}")

def scan_item(data, barcode, mode):
    if barcode not in data:
        print('Item not found in inventory.')
        return
    if mode == 'add':
        data[barcode]['quantity'] += 1
        print(f"Added one {data[barcode]['name']}. New qty: {data[barcode]['quantity']}")
    elif mode == 'order':
        if data[barcode]['quantity'] > 0:
            data[barcode]['quantity'] -= 1
            print(f"Ordered one {data[barcode]['name']}. New qty: {data[barcode]['quantity']}")
        else:
            print(f"{data[barcode]['name']} is out of stock!")
    save_data(data)

def init_data():
    if not DATA_FILE.exists():
        sample = {
            "123456789012": {"name": "Widget", "quantity": 10, "price": 2.5},
            "987654321098": {"name": "Gadget", "quantity": 0, "price": 5.0}
        }
        save_data(sample)
        print('Initialized inventory with sample data.')

def main():
    parser = argparse.ArgumentParser(description='Inventory Tracking App')
    sub = parser.add_subparsers(dest='command')

    sub.add_parser('list')
    sub.add_parser('outofstock')
    sub.add_parser('total')

    scan = sub.add_parser('scan')
    scan.add_argument('barcode')
    scan.add_argument('--mode', choices=['add', 'order'], required=True)

    parser.add_argument('--init', action='store_true', help='initialize inventory with sample data')

    args = parser.parse_args()

    if args.init:
        init_data()

    data = load_data()

    if args.command == 'list':
        list_items(data)
    elif args.command == 'outofstock':
        out_of_stock(data)
    elif args.command == 'total':
        total_value(data)
    elif args.command == 'scan':
        scan_item(data, args.barcode, args.mode)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
