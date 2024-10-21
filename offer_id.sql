UPDATE `catalog_items`
SET `offer_id` = 
    CASE 
        WHEN REGEXP_REPLACE(`item_ids`, '[^0-9]', '') = '' THEN 0
        WHEN CAST(REGEXP_REPLACE(`item_ids`, '[^0-9]', '') AS UNSIGNED) > 2147483647 THEN 0
        ELSE CAST(REGEXP_REPLACE(`item_ids`, '[^0-9]', '') AS UNSIGNED)
    END;