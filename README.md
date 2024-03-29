# Camera Shop Inventory App :camera_flash:
Solo project from the first module of CodeClan Professional Software Development course, an app which allows the owner of a camera shop to track their inventory.

## The Brief :clipboard:
Shop Inventory
Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

#### MVP
* The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should track manufacturers, including a name and any other appropriate details.
* The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
* This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

#### Inspired by
eBay, Amazon (back end only), Magento

#### Possible Extensions
* Calculate the markup on items in the store, and display it in the inventory
* Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.
* Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.
* Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.

## Built With :building_construction:	
* Python
* Flask
* Postgresql
* HTML
* CSS

## Loading the app :dizzy:		
These instructions should get you a copy of the project up and running on your local machine for development purposes.

Install flask and psycopg:
```
pip3 install Flask
pip3 install psycopg2
```
Create and seed the database:

```
createdb camera_shop_stock
psql -d camera_shop_stock -f camera_shop_stock.sql
```
Run the app:
```
flask run
```
The web applicaiton can then be viewed in the browser by navigating to http://localhost:4999.

Note: The console.py file is available for testing and can be run in the terminal using:
```
python3 console.py
```
