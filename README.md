# Vendor_management

## Description

The Vendor Management System is a Django-based web application designed to streamline vendor management processes, track purchase orders, and evaluate vendor performance metrics. It provides a user-friendly interface for managing vendor profiles, creating and updating purchase orders, and analyzing vendor performance over time.

## Installation

1. Clone the repository:
git clone https://github.com/naitik-yadav/Vendor_Management.git

2. Navigate to the project directory:
cd vendor-management-system

3. Create and activate a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Run database migrations:
python manage.py migrate

6. Start the development server:
python manage.py runserver

The application will be accessible at `http://localhost:8000`.

## Usage

### Vendor Profile Management

- **Create a new vendor**: Send a POST request to `/api/vendors/` with the vendor details in the request body.
- **List all vendors**: Send a GET request to `/api/vendors/`.
- **Retrieve a specific vendor's details**: Send a GET request to `/api/vendors/{vendor_id}/`.
- **Update a vendor's details**: Send a PUT request to `/api/vendors/{vendor_id}/` with the updated vendor details in the request body.
- **Delete a vendor**: Send a DELETE request to `/api/vendors/{vendor_id}/`.

### Purchase Order Tracking

- **Create a new purchase order**: Send a POST request to `/api/purchase_orders/` with the purchase order details in the request body.
- **List all purchase orders**: Send a GET request to `/api/purchase_orders/`.
- **Retrieve details of a specific purchase order**: Send a GET request to `/api/purchase_orders/{po_id}/`.
- **Update a purchase order**: Send a PUT request to `/api/purchase_orders/{po_id}/` with the updated purchase order details in the request body.
- **Delete a purchase order**: Send a DELETE request to `/api/purchase_orders/{po_id}/`.

### Vendor Performance Evaluation

- **Retrieve a vendor's performance metrics**: Send a GET request to `/api/vendors/{vendor_id}/performance`.

## Testing

To run the test suite, use the following command:
python manage.py test


