WITH CTE AS
	(
SELECT 
	  A.sales_id
	, A.customer_id AS Customer
	, B.age
	, C.order_id
	, C.item_id
	, C.quantity
	, D.item_name as item
FROM
	Sales AS A
JOIN
	(
	SELECT 
		* 
	FROM
		Customer 
	WHERE 
		Age BETWEEN 18 AND 35
	) AS B
ON 
	A.customer_id = B.customer_id
JOIN
	(
	SELECT 
		*
	FROM
		Orders
	WHERE
		quantity IS NOT NULL
	) AS C
ON
	A.sales_id = C.sales_id
JOIN
	Items AS D
ON
	C.item_id = D.item_id
	)
	
SELECT
	Customer_ID AS Customer
	, Age
	, Item
	, SUM(Quantity) AS Quantity
FROM
	CTE
GROUP BY
	Customer_ID
	, Age
	, Item