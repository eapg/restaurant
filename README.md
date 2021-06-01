# Restaurant EA Italian Food

This is a project to manage the complete operation of a restaurant.

## project structure:

 ## - product structure:

   This structure is made up of the basic of a product like the product name, the product id and
   the product description.

## - Inventory structure:

   This structure manages a list of products to know the products that the restaurant have in stock  

## - Inventory product structure:

   This structure relates a product with an inventory also its contain the product quantity

## - Menu structure:

   This structure has the menu of the restaurant. its show the product that the restaurant sell,
   also its show the product description and its price.

## - order structure:

   This structure manages the client orders, its will have products, price, taxes, status and
   other orders details.

## - order amount structure:

   This structure calculates the total amount of the product that the client order.

## - order detail structure:

   This structure have all the order details

## - order status structure:

   This structure has a list of possible status for the order

##  - Generic Repository structure:

   This structure manages the abstraction of the repositories, it works like an interface

## - Product Repository

   This structure manages the implementation of the product repository

## Inventory Repository

   This structure manages the implementation of the inventory repository

## Inventory Product Repository

   This structure manages the implementation of the inventory product repository

## Menu Repository

   This structure manages the implementation of the menu repository

## Order Repository

   This structure manages the implementation of the order repository

## UML Class Diagram

![UML](https://github.com/eapg/restaurant/blob/feature/order_repository/UML_Diagram.png?raw=true)

