SELECT *
FROM playlist_track as 'A'
ORDER BY A.PlaylistId DESC
LIMIT 5;

SELECT *
FROM tracks as 'B'
ORDER BY B.TrackId
LIMIT 5;

SELECT *
FROM playlist_track INNER JOIN tracks
  ON playlist_track.TrackId = tracks.TrackId
ORDER BY PlaylistId DESC
LIMIT 10;

SELECT A.PlaylistId, B.Name
FROM playlist_track A INNER JOIN tracks B
  ON A.TrackId = B.TrackId
WHERE A.PlaylistId = 10
ORDER BY Name DESC
LIMIT 5;

SELECT * FROM invoices limit 10;
SELECT * FROM invoice_items limit 10;
SELECT * FROM customers limit 10;

SELECT
C.CustomerId, count(*)
FROM invoice_items A
INNER JOIN invoices B
  ON A.InvoiceId = B.InvoiceId
INNER JOIN customers C
  ON B.CustomerId = C.CustomerId
GROUP BY C.CustomerId
ORDER BY C.CustomerId
LIMIT 5;

SELECT
-- C.CustomerId, count(*)
*
FROM invoice_items A
INNER JOIN invoices B
  ON A.InvoiceId = B.InvoiceId
INNER JOIN customers C
  ON B.CustomerId = C.CustomerId
GROUP BY C.CustomerId
ORDER BY C.CustomerId
LIMIT 50;