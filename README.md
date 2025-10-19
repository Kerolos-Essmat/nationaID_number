## User Guide
**For reqesting the token**
curl -X POST http://127.0.0.1:8000/national_id/token/  -H "Content-Type: application/json"  -d "{\"username\": \"admin\", \"password\": \"pass\"}"

**The token generated for the admin user**
for example
Generated token <token> for user admin

**To request the api**
curl -v -X GET "http://127.0.0.1:8000/national_id/national_id_info/<national_id>/"   -H "Accept: application/json"  -H "Authorization: Token <token>"


