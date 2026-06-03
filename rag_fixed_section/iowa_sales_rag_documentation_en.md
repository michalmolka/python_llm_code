# Database Schema

## Fact Table

### iowa_sales

Table type: Fact table

Columns:
- ID (BIGINT)
- InvoiceItemNumber (STRING)
- DateID (INT)
- StoreID (INT)
- CategoryID (INT)
- VendorID (INT)
- ItemID (INT)
- Pack (INT)
- BottleVolumeMl (INT)
- StateBottleCost (DOUBLE)
- StateBottleRetail (DOUBLE)
- BottlesSold (INT)
- SaleDollars (DOUBLE)
- VolumeSoldLiters (DOUBLE)
- VolumeSoldGallons (DOUBLE)
- PartitionKeyYear (INT)
- Inserted (TIMESTAMP)

## Dimension Tables

### iowa_category

Table type: Dimension table

Columns:
- CategoryID (BIGINT)
- CategoryName (STRING)

### iowa_date

Table type: Dimension table

Columns:
- DateID (INT)
- CalendarDate (DATE)
- CalendarYear (INT)
- CalendarMonth (STRING)
- MonthOfYear (INT)

### iowa_item

Table type: Dimension table

Columns:
- ItemID (BIGINT)
- ItemName (STRING)
- Inserted (TIMESTAMP)

### iowa_store

Table type: Dimension table

Columns:
- StoreID (BIGINT)
- StoreName (STRING)
- City (STRING)
- County (STRING)

### iowa_vendor

Table type: Dimension table

Columns:
- VendorID (BIGINT)
- VendorName (STRING)

# Relationship Rules

## Fact Table Rules

- iowa_sales is the only fact table.
- All joins must start from iowa_sales.
- Do not join dimension tables directly to each other.

## Valid Relationships

### iowa_category

Join condition:
iowa_sales.CategoryID = iowa_category.CategoryID

### iowa_date

Join condition:
iowa_sales.DateID = iowa_date.DateID

### iowa_item

Join condition:
iowa_sales.ItemID = iowa_item.ItemID

### iowa_store

Join condition:
iowa_sales.StoreID = iowa_store.StoreID

### iowa_vendor

Join condition:
iowa_sales.VendorID = iowa_vendor.VendorID

## Available Tables

- iowa_sales
- iowa_category
- iowa_date
- iowa_item
- iowa_store
- iowa_vendor


# Tables Description

## iowa_sales
**PL:** Główna tabela faktów ze sprzedażą. Każdy wiersz reprezentuje pojedynczą pozycję sprzedaży produktu w konkretnym sklepie i dniu, razem z ilościami, wartościami i wolumenem.

**EN:** Main fact table containing sales transactions. Each row represents a sold item in a specific store and date, including quantities, values, and volumes.

## iowa_category
**PL:** Tabela kategorii, grupuje produkty według typu lub przeznaczenia.

**EN:** Category dimension table grouping products by type or purpose.

## iowa_date
**PL:** Tabela wymiaru daty, zawiera różne reprezentacje i atrybuty kalendarzowe i fiskalne dla każdej daty.

**EN:** Date dimension table containing calendar and fiscal attributes for each date.

## iowa_item
**PL:** Tabela produktów, przechowuje listę wszystkich artykułów dostępnych w sprzedaży.

**EN:** Item dimension table storing the list of all products available for sale.

## iowa_store
**PL:** Tabela sklepów, opisuje lokalizacje, nazwy i dane adresowe punktów sprzedaży.

**EN:** Store dimension table describing store locations, names, and address details.

## iowa_vendor
**PL:** Tabela dostawców, przechowuje informacje o firmach dostarczających produkty.

**EN:** Vendor dimension table storing information about product suppliers.

# Columns Description

## Table: iowa_sales

### ID
- Data type: bigint
- PL: Unikalny identyfikator rekordu sprzedaży, techniczny klucz wiersza.
- EN: Unique identifier of the sales record, technical row key.

### InvoiceItemNumber
- Data type: string
- PL: Numer pozycji na fakturze, wskazuje konkretną linię dokumentu sprzedaży.
- EN: Invoice line item number identifying a specific sales line.

### DateID
- Data type: int
- PL: Klucz do tabeli dat, określa dzień sprzedaży.
- EN: Foreign key to date table, indicates the sales date.

### StoreID
- Data type: int
- PL: Klucz sklepu, mówi gdzie dokonano sprzedaży.
- EN: Store foreign key, indicates where the sale happened.

### CategoryID
- Data type: int
- PL: Klucz kategorii produktu, określa typ towaru.
- EN: Product category foreign key, identifies product type.

### VendorID
- Data type: int
- PL: Klucz dostawcy, wskazuje firmę dostarczającą produkt.
- EN: Vendor foreign key, identifies the supplier.

### ItemID
- Data type: int
- PL: Klucz produktu, identyfikuje konkretny artykuł.
- EN: Item foreign key, identifies the specific product.

### Pack
- Data type: int
- PL: Wielkość opakowania, liczba sztuk w paczce.
- EN: Pack size, number of units in a package.

### BottleVolumeMl
- Data type: int
- PL: Pojemność butelki w mililitrach.
- EN: Bottle volume in milliliters.

### StateBottleCost
- Data type: double
- PL: Koszt zakupu jednej butelki dla sklepu (cena hurtowa).
- EN: Wholesale cost of a single bottle.

### StateBottleRetail
- Data type: double
- PL: Cena detaliczna jednej butelki.
- EN: Retail price of a single bottle.

### BottlesSold
- Data type: int
- PL: Liczba sprzedanych butelek w tej pozycji sprzedaży.
- EN: Number of bottles sold in this transaction line.

### SaleDollars
- Data type: double
- PL: Wartość sprzedaży w dolarach.
- EN: Sales value in dollars.

### VolumeSoldLiters
- Data type: double
- PL: Łączna sprzedana objętość w litrach.
- EN: Total sold volume in liters.

### VolumeSoldGallons
- Data type: double
- PL: Łączna sprzedana objętość w galonach.
- EN: Total sold volume in gallons.

### PartitionKeyYear
- Data type: int
- PL: Rok używany do partycjonowania danych w magazynie.
- EN: Year used for data partitioning in storage.

### Inserted
- Data type: timestamp
- PL: Data i czas wstawienia rekordu do systemu.
- EN: Timestamp when the record was inserted into the system.

## Table: iowa_category

### CategoryID
- Data type: bigint
- PL: Unikalny identyfikator kategorii.
- EN: Unique category identifier.

### CategoryName
- Data type: string
- PL: Nazwa kategorii.
- EN: Category name.

## Table: iowa_date

### DateID
- Data type: int
- PL: Unikalny identyfikator daty, klucz do łączenia z faktami.
- EN: Unique date identifier, join key to fact tables.

### CalendarDate
- Data type: date
- PL: Pełna data kalendarzowa.
- EN: Full calendar date.

### CalendarYear
- Data type: int
- PL: Rok kalendarzowy.
- EN: Calendar year.

### CalendarMonth
- Data type: string
- PL: Nazwa miesiąca.
- EN: Month name.

### MonthOfYear
- Data type: int
- PL: Numer miesiąca w roku (1–12).
- EN: Month number in year (1–12).

## Table: iowa_item

### ItemID
- Data type: bigint
- PL: Unikalny identyfikator produktu.
- EN: Unique product identifier.

### ItemName
- Data type: string
- PL: Nazwa produktu.
- EN: Product name.

### Inserted
- Data type: timestamp
- PL: Data dodania produktu do systemu.
- EN: Timestamp when the product was added to the system.

## Table: iowa_store

### StoreID
- Data type: bigint
- PL: Unikalny identyfikator sklepu.
- EN: Unique store identifier.

### StoreName
- Data type: string
- PL: Nazwa sklepu.
- EN: Store name.

### City
- Data type: string
- PL: Miasto, w którym znajduje się sklep.
- EN: City where the store is located.

### County
- Data type: string
- PL: Region / hrabstwo administracyjne.
- EN: Administrative county or region.

## Table: iowa_vendor

### VendorID
- Data type: bigint
- PL: Unikalny identyfikator dostawcy.
- EN: Unique vendor identifier.

### VendorName
- Data type: string
- PL: Nazwa dostawcy.
- EN: Vendor name.


# Iowa Sales Data Documentation for RAG

## Document purpose

This document describes the `Iowa Sales` data model in a format designed for RAG, embeddings, and chunking. The text is intentionally split into short, self-contained sections. Each section includes the table name, business meaning, columns, relationships, and common user questions.

The dataset describes alcoholic beverage sales in the state of Iowa. The central fact table is `iowa_sales`. The dimension tables are `iowa_category`, `iowa_date`, `iowa_item`, `iowa_store`, and `iowa_vendor`.

This model can be used to test semantic retrieval, schema question answering, SQL generation, business-to-technical term mapping, and evaluation of how well a RAG system retrieves the right context.

## General model description

The `Iowa Sales` model follows a star schema. The `iowa_sales` table stores sales facts, meaning records about products sold in specific stores on specific dates. The dimensions describe the sales context: date, store, product category, product item, and vendor.

When a user asks about sales, revenue, bottles sold, volume, transaction value, or financial measures, the most important table is `iowa_sales`. When a user asks about category name, item name, store name, city, county, month, year, or vendor name, the query should join the relevant dimension table.

The relationships start from `iowa_sales`. The column `iowa_sales.CategoryID` joins sales to `iowa_category`. The column `iowa_sales.DateID` joins sales to `iowa_date`. The column `iowa_sales.ItemID` joins sales to `iowa_item`. The column `iowa_sales.StoreID` joins sales to `iowa_store`. The column `iowa_sales.VendorID` joins sales to `iowa_vendor`.

## Fact table iowa_sales

The `iowa_sales` table is the main fact table. One row represents a single sales line, usually an invoice line or transaction item. The table contains financial measures, quantity measures, volume measures, and foreign keys to dimension tables.

Use `iowa_sales` when the question is about sales, revenue, sales value, bottles sold, volume in liters, volume in gallons, retail price, bottle cost, transactions, invoices, or sales trends.

The technical record key is `ID` with type `BIGINT`. The `ID` column identifies a single sales record and can be used for deduplication or row counting.

The `InvoiceItemNumber` column has type `STRING` and stores the invoice line number. It is a source-system identifier useful for transaction-level analysis, auditing, or joining to invoice-level data.

The `DateID` column has type `INT` and is a foreign key to `iowa_date`. Use it to connect a sales record with calendar date, year, month, and month number.

The `StoreID` column has type `INT` and is a foreign key to `iowa_store`. Use it to connect a sales record with store name, city, and county.

The `CategoryID` column has type `INT` and is a foreign key to `iowa_category`. Use it to connect a sales record with product category name.

The `VendorID` column has type `INT` and is a foreign key to `iowa_vendor`. Use it to connect a sales record with vendor or producer name.

The `ItemID` column has type `INT` and is a foreign key to `iowa_item`. Use it to connect a sales record with item name or product name.

The `Pack` column has type `INT` and describes the number of units in a case or package. It can be used for package format analysis and product comparison.

The `BottleVolumeMl` column has type `INT` and describes the volume of one bottle in milliliters. It is useful when comparing products with different bottle sizes and when analyzing volume.

The `StateBottleCost` column has type `DOUBLE` and describes the unit cost of one bottle. It is a unit financial measure. It should not be summed directly. Weighted averages based on `BottlesSold` are usually more meaningful.

The `StateBottleRetail` column has type `DOUBLE` and describes the unit retail price of one bottle. It is a unit price. It should not be summed directly. Weighted averages based on `BottlesSold` are usually more meaningful.

The `BottlesSold` column has type `INT` and describes the number of bottles sold. It is an additive quantity measure. The typical aggregation is `SUM(BottlesSold)`.

The `SaleDollars` column has type `DOUBLE` and describes the sales value in dollars for the sales line. It is the primary revenue measure. The typical aggregation is `SUM(SaleDollars)`.

The `VolumeSoldLiters` column has type `DOUBLE` and describes total product volume sold in liters. It is an additive volume measure. The typical aggregation is `SUM(VolumeSoldLiters)`.

The `VolumeSoldGallons` column has type `DOUBLE` and describes total product volume sold in gallons. It is an additive volume measure. The typical aggregation is `SUM(VolumeSoldGallons)`.

The `PartitionKeyYear` column has type `INT` and is a technical partitioning column by year. For business time analysis, prefer `iowa_date.CalendarYear`, because `PartitionKeyYear` primarily describes data organization.

The `Inserted` column has type `TIMESTAMP` and describes when the record was loaded into the analytical system. It is not the sale date. The sale date should be retrieved through the relationship `iowa_sales.DateID = iowa_date.DateID`.

The source specification lists `PartitionKeyYear` twice. This documentation treats it as one logical column. If the physical schema contains a duplicate column, validate it before building production queries.

## Dimension table iowa_category

The `iowa_category` table is the product category dimension. It describes product groups that sold items belong to. Use this table when the user asks about category, alcohol type, product segment, category ranking, or comparison of sales between categories.

The primary key of `iowa_category` is `CategoryID` with type `BIGINT`. The `CategoryID` column joins to `iowa_sales.CategoryID`. Semantically, it is the category identifier, even if the fact table stores the matching column as `INT`.

The `CategoryName` column has type `STRING` and stores the product category name. Use it when the user wants to view, filter, or group by category name, such as whiskey, vodka, rum, gin, brandy, or other product groups.

Common questions for `iowa_category` include: which category has the highest sales, what is the sales value for vodka, what volume belongs to a category, which categories are growing over time, and how revenue compares between categories.

## Dimension table iowa_date

The `iowa_date` table is the date dimension. It describes calendar date, year, month, and month number. Use this table when the user asks about daily analysis, monthly analysis, yearly analysis, trends, seasonality, or chronological sorting.

The primary key of `iowa_date` is `DateID` with type `INT`. The `DateID` column joins to `iowa_sales.DateID`.

The `CalendarDate` column has type `DATE` and stores the full calendar date. Use it for filtering by a specific day or date range.

The `CalendarYear` column has type `INT` and stores the calendar year. Use it for yearly reports and year filters. For sales year questions, prefer `iowa_date.CalendarYear` rather than the technical column `iowa_sales.PartitionKeyYear`.

The `CalendarMonth` column has type `STRING` and stores the month name. Use it for presenting monthly results. Because it is text, it should not be the only column used for month sorting.

The `MonthOfYear` column has type `INT` and stores the month number from 1 to 12. Use it to correctly sort months in reports.

Common questions for `iowa_date` include: what were sales in 2023, which month had the highest revenue, what is the month-over-month trend, what were sales on a specific day, and how to calculate yearly volume.

## Dimension table iowa_item

The `iowa_item` table is the product item dimension. It describes specific products or assortment items sold in stores. Use this table when the user asks about product, item, SKU, product name, product ranking, or sales for a specific item.

The primary key of `iowa_item` is `ItemID` with type `BIGINT`. The `ItemID` column joins to `iowa_sales.ItemID`. Semantically, it is the product identifier, even if the fact table stores the matching column as `INT`.

The `ItemName` column has type `STRING` and stores the product name. Use it to search products by name and to present analytical results at product level.

The `Inserted` column has type `TIMESTAMP` and describes when the product record was added or loaded into the system. It does not represent the sale date of the product.

Common questions for `iowa_item` include: which products have the highest sales, how much of a specific product was sold, which product has the largest volume in liters, and which products generate the highest revenue.

## Dimension table iowa_store

The `iowa_store` table is the store dimension. It describes sales locations and basic geographic information. Use this table when the user asks about store, sales outlet, city, county, location, store ranking, or regional sales.

The primary key of `iowa_store` is `StoreID` with type `BIGINT`. The `StoreID` column joins to `iowa_sales.StoreID`. Semantically, it is the store identifier, even if the fact table stores the matching column as `INT`.

The `StoreName` column has type `STRING` and stores the store name or outlet name. Use it for store-level reporting and for presenting results to the user.

The `City` column has type `STRING` and stores the city where the store is located. Use it to filter and aggregate sales by city.

The `County` column has type `STRING` and stores the county where the store is located. Use it for regional analysis at county level.

Common questions for `iowa_store` include: which stores have the highest sales, what were sales in a given city, which counties generate the largest volume, and how to compare stores by revenue.

## Dimension table iowa_vendor

The `iowa_vendor` table is the vendor dimension. It describes vendors, producers, or companies associated with sold products. Use this table when the user asks about vendor, producer, supplier, vendor ranking, or vendor share of sales.

The primary key of `iowa_vendor` is `VendorID` with type `BIGINT`. The `VendorID` column joins to `iowa_sales.VendorID`. Semantically, it is the vendor identifier, even if the fact table stores the matching column as `INT`.

The `VendorName` column has type `STRING` and stores the vendor or producer name. Use it for filtering, grouping, and presenting results by vendor.

Common questions for `iowa_vendor` include: which vendor generated the highest sales, what volume belongs to a vendor, how vendor sales changed over time, and which vendors dominate a selected category.

## Relationships and joins

The relationship between `iowa_sales` and `iowa_category` uses the condition `iowa_sales.CategoryID = iowa_category.CategoryID`. Use this relationship when the result needs category name or when the question filters sales by category.

The relationship between `iowa_sales` and `iowa_date` uses the condition `iowa_sales.DateID = iowa_date.DateID`. Use this relationship when the result needs date, year, month, month number, or time trend.

The relationship between `iowa_sales` and `iowa_item` uses the condition `iowa_sales.ItemID = iowa_item.ItemID`. Use this relationship when the result needs item name or when the question is about a specific product.

The relationship between `iowa_sales` and `iowa_store` uses the condition `iowa_sales.StoreID = iowa_store.StoreID`. Use this relationship when the result needs store name, city, county, or store ranking.

The relationship between `iowa_sales` and `iowa_vendor` uses the condition `iowa_sales.VendorID = iowa_vendor.VendorID`. Use this relationship when the result needs vendor name or when the question is about a vendor.

## Sales measures

The main revenue measure is `iowa_sales.SaleDollars`. When the user asks about sales, revenue, turnover, or sales value, the query usually needs `SUM(SaleDollars)`.

The main quantity measure is `iowa_sales.BottlesSold`. When the user asks about number of bottles, sold units, quantity, or count of sold bottles, the query usually needs `SUM(BottlesSold)`.

The main volume measure in liters is `iowa_sales.VolumeSoldLiters`. When the user asks about volume in liters, the query should use `SUM(VolumeSoldLiters)`.

The main volume measure in gallons is `iowa_sales.VolumeSoldGallons`. When the user asks about gallons or volume in gallons, the query should use `SUM(VolumeSoldGallons)`.

The `StateBottleCost` column describes unit bottle cost. The `StateBottleRetail` column describes unit bottle retail price. These columns are not typical additive measures and should not be summed without careful reasoning.

## Mapping user concepts to the schema

If the user asks about sales, revenue, turnover, or sales value, the most important column is `iowa_sales.SaleDollars`.

If the user asks about number of bottles, sold units, quantity, or quantity sold, the most important column is `iowa_sales.BottlesSold`.

If the user asks about volume in liters, the most important column is `iowa_sales.VolumeSoldLiters`.

If the user asks about volume in gallons, the most important column is `iowa_sales.VolumeSoldGallons`.

If the user asks about category, product type, or segment, use `iowa_category.CategoryName` and join it to `iowa_sales` through `CategoryID`.

If the user asks about product, item, SKU, or product name, use `iowa_item.ItemName` and join it to `iowa_sales` through `ItemID`.

If the user asks about store, sales outlet, or store name, use `iowa_store.StoreName` and join it to `iowa_sales` through `StoreID`.

If the user asks about city, use `iowa_store.City`. If the user asks about county, use `iowa_store.County`.

If the user asks about vendor, supplier, or producer, use `iowa_vendor.VendorName` and join it to `iowa_sales` through `VendorID`.

If the user asks about date, day, month, year, or trend, use the `iowa_date` table and join it to `iowa_sales` through `DateID`.

## Example analytical intents

The intent "sales by category" requires `iowa_sales` and `iowa_category`. Join them by `CategoryID`, group by `CategoryName`, and aggregate `SUM(SaleDollars)`.

The intent "sales by month" requires `iowa_sales` and `iowa_date`. Join them by `DateID`, group by `CalendarYear`, `MonthOfYear`, and `CalendarMonth`, and sort the result by year and month number.

The intent "store ranking" requires `iowa_sales` and `iowa_store`. Join them by `StoreID`, group by `StoreName`, optionally `City` and `County`, and sort by `SUM(SaleDollars)` descending.

The intent "sales by vendor" requires `iowa_sales` and `iowa_vendor`. Join them by `VendorID`, group by `VendorName`, and aggregate `SaleDollars`, `BottlesSold`, or `VolumeSoldLiters`.

The intent "product sales over time" requires `iowa_sales`, `iowa_item`, and `iowa_date`. Join sales to item by `ItemID`, join sales to date by `DateID`, filter or group by `ItemName`, and analyze time through `CalendarDate`, `CalendarMonth`, or `CalendarYear`.

The intent "category sales in a city" requires `iowa_sales`, `iowa_category`, and `iowa_store`. Join sales to category by `CategoryID`, join sales to store by `StoreID`, and filter or group by `City` and `CategoryName`.

## Example SQL queries

Example query for sales by category:

```sql
SELECT
    c.CategoryName,
    SUM(s.SaleDollars) AS TotalSalesDollars
FROM iowa_sales s
JOIN iowa_category c
    ON s.CategoryID = c.CategoryID
GROUP BY c.CategoryName
ORDER BY TotalSalesDollars DESC;
```

Example query for sales by month:

```sql
SELECT
    d.CalendarYear,
    d.MonthOfYear,
    d.CalendarMonth,
    SUM(s.SaleDollars) AS TotalSalesDollars
FROM iowa_sales s
JOIN iowa_date d
    ON s.DateID = d.DateID
GROUP BY
    d.CalendarYear,
    d.MonthOfYear,
    d.CalendarMonth
ORDER BY
    d.CalendarYear,
    d.MonthOfYear;
```

Example query for store ranking:

```sql
SELECT
    st.StoreName,
    st.City,
    st.County,
    SUM(s.SaleDollars) AS TotalSalesDollars,
    SUM(s.BottlesSold) AS TotalBottlesSold
FROM iowa_sales s
JOIN iowa_store st
    ON s.StoreID = st.StoreID
GROUP BY
    st.StoreName,
    st.City,
    st.County
ORDER BY TotalSalesDollars DESC;
```

## Test questions for RAG

Which table contains sales value in dollars? The answer should point to `iowa_sales.SaleDollars`.

How do I join sales to category name? The answer should point to the join `iowa_sales.CategoryID = iowa_category.CategoryID`.

Which columns should be used for a monthly report? The answer should point to `iowa_date.CalendarYear`, `iowa_date.MonthOfYear`, `iowa_date.CalendarMonth`, and measures from `iowa_sales`.

What is the difference between `CalendarYear` and `PartitionKeyYear`? The answer should explain that `CalendarYear` is a business date attribute, while `PartitionKeyYear` is a technical partitioning column.

Does `Inserted` represent the sale date? The answer should say no. `Inserted` represents record load time, while the sale date comes from `iowa_date.CalendarDate`.

How do I find sales by vendor? The answer should point to `iowa_sales` and `iowa_vendor`, the relationship through `VendorID`, and the aggregation `SUM(SaleDollars)`.

## Notes for RAG systems

This document is designed so that sections can be chunked independently. A good default is chunking by second-level or third-level headings. Table sections include the table name in the heading and repeat the business context, so a single chunk should be understandable without reading the whole document.

For embeddings, both technical names and business synonyms matter. That is why the descriptions include column names such as `SaleDollars` and user concepts such as sales, revenue, turnover, and sales value.

For SQL generation, the system should prefer dimension tables for textual descriptions and `iowa_sales` for measures. The `iowa_sales` table is the center of the model. All main joins start from `iowa_sales`.

