
### Terminal commands

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.


