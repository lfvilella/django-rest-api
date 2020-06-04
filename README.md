FORMAT: A1

# Tools API

This is an REST API Tools on the Bossabox challenge. Where I develop an API with the fields "title", "link", "description" and "tags".

I use Python/Django Rest Framework to develop it, I use Postgres as a Database and Docker to automate the stuff.

## To run
```
$ make build
$ make db
$ make up
```

# Group Tools

Resources related to tools in the API.

## Tools collection [ /tools ]

### List all tools [GET]
- Response 200 (application/json)


### Creat a tool [POST]
```
{
    "title": "json-server",
    "link": "https://github.com/typicode/json-server",
    "description": "Fake REST API based on a json schema. Useful for mocking and creating APIs for front-end devs to consume in coding challenges.",
    "tags": [
        "organization",
        "planning",
        "collaboration",
        "writing",
        "calendar"
    ]
}
```
- Response 201 Created (application/json)

## Tools update and delete [ /tools/id/ ]

### Update all tool fields [PUT]
```
{
    "title": "My GitHub",
    "link": "https://github.com/lfvilella",
    "description": "Write the description here",
    "tags": [
        "git",
        "lfvilella",
    ]
}
```
- Response 200 (application/json)


### Update single tool field [PATCH]
```
{
    "title": "lfvilella",
    "description": "Look my profile: Luis Felipe Vilella GitHub"
}
```
- Response 200 (application/json)

### Delete tool [DELETE]
- Response 204 (application/json)

## Search tools by Tag [ /tools?tags=tag-name ]
If you have many tools, you can search on by URL using:

* Simple tag: ``` 'http://localhost:3000/tools/tags=tag-name1' ```

* Or more tags: ``` 'http://localhost:3000/tools/tags=tag-name1&tags=tag-name2' ```


### Get tools by filter [GET]
- Response 200 (application/json)
