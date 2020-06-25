--SELECT u.id FROM api_user u, api_user_group ug, api_group g where u.id=ug.user_id and ug.group_id=g.id and g.name = "admin" order by u.name
SELECT "api_user"."id", "api_user"."name", "api_user"."email", "api_user"."password", "api_user"."last_login" 
FROM "api_user" WHERE "api_user"."id" 
IN (SELECT u.id FROM api_user u, api_user_group ug, api_group g 
where u.id=ug.user_id and ug.group_id=g.id and g.name = "admin")
ORDER BY "api_user"."name" ASC