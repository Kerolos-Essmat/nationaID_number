## User Guide
**For reqesting the token**
curl -X POST http://127.0.0.1:8000/national_id/token/  -H "Content-Type: application/json"  -d "{\"username\": \"admin\", \"password\": \"pass\"}"

**The token generated for the admin user**
for example
Generated token <token> for user admin

**To request the api**
curl -v -X GET "http://127.0.0.1:8000/national_id/national_id_info/<national_id>/"   -H "Accept: application/json"  -H "Authorization: Token <token>"


## Summary
the **national_id_api** folder is the project
the **national_id_info** folder is the app
the **lib** is the core logic of the api

the **lib** module we will find that every information has it's own function and there is a one function gets all the data from the input by using all the functions
first we start with the validation then we go with the extracting the data.


