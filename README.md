# orghub/feed-service
Feed Service for OrgHub app

> Deployed @ https://orghub-feed-service.now.sh

Endpoints
---------
| Endpoint              | Method    |
|:--------------------- |:----------|
| /feed                 | GET       |
| /feed/:org            | GET       |


Commands
--------
- `make dev`: Start development live-reload server
- `make install`: Install dependencies in requirements.txt
- `make test`: Run tests in /tests
- `make build`: Build docker image
- `make run`: Run docker image
- `make inspect`: Inspect docker container
- `make shell`: Open docker container shell
- `make stop`: Stop docker container
- `make clean`: Remove docker container & image
- `make publish`: Publish to now (depends on npm package now)


Author
------
* Olle Lauri Boström (ollebostr@gmail.com)


License
-------
Licensed under the MIT License.
