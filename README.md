# Wilder Watch API
This is the API intended for use in production with the [WilderWatch Client](https://github.com/ryanmphill/wilder-watch-client) built with Python and Django. 

_**Note**: If you are interested in pulling the wilder-watch-api down to run **locally**, you will need to use the [demo version](https://github.com/ryanmphill/wilder-watch-demo-server) that uses a generic `SECRET_KEY` for development purposes_

[Click here for WilderWatch demo server](https://github.com/ryanmphill/wilder-watch-demo-server)

## Endpoints

### Authentication
#### `POST` `/login`

Body:
```JSON
{
    "username": "string",
    "password": "string"
}
```

Response `200`:

```JSON
{
    "valid": "boolean",
    "token": "string"
}
```

#### `POST` `/register`

Body:
```JSON
{
    "username": "string",
    "password": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string"
}
```

Response `200`:

```JSON
{
    "valid": "boolean",
    "token": "string"
}
```

### Regions

#### `GET` `/regions`

Response `200`:

```JSON
[
    {
    "id": "integer",
    "label": "string"
    },
    {
    "id": "integer",
    "label": "string"
    },
]
```

#### `GET` `/regions/{pk}`

```JSON
{
    "id": "integer",
    "label": "string"
}
```

### Study Types

#### `GET` `/study_types`

Response `200`:

```JSON
[
    {
    "id": "integer",
    "label": "string"
    },
    {
    "id": "integer",
    "label": "string"
    },
]
```

#### `GET` `/study_types/{pk}`

```JSON
{
    "id": "integer",
    "label": "string"
}
```

### Studies

#### `GET` `/studies`

Response `200`:

```JSON
[
    {
        "id": "integer",
        "title": "string",
        "author": {
            "id": "integer",
            "user": {
                "id": "integer",
                "username": "string",
                "first_name": "string",
                "last_name": "string",
                "is_staff": "boolean"
            },
            "bio": "string",
            "flair": "string",
            "image_url": "string",
            "is_researcher": "boolean",
            "full_name": "string"
        },
        "subject": "string",
        "summary": "string",
        "details": "string",
        "start_date": "date",
        "end_date": "date",
        "is_complete": "boolean",
        "study_type": {
            "id": "integer",
            "label": "string"
        },
        "region": {
            "id": "integer",
            "label": "string"
        },
        "image_url": "string",
        "observations": [
            {
                "id": "integer",
                "participant": "integer",
                "study": "integer",
                "latitude": "float",
                "longitude": "float",
                "description": "string",
                "image": "string",
                "date": "date",
                "participant_name": "string",
                "study_title": "string"
            }
        ],
        "average_longitude": "float",
        "average_latitude": "float",
        "furthest_longitude": "float",
        "furthest_latitude": "float"
    },
]
```

#### `GET` `/studies/{pk}`

Response `200`:

```JSON
{
        "id": "integer",
        "title": "string",
        "author": {
            "id": "integer",
            "user": {
                "id": "integer",
                "username": "string",
                "first_name": "string",
                "last_name": "string",
                "is_staff": "boolean"
            },
            "bio": "string",
            "flair": "string",
            "image_url": "string",
            "is_researcher": "boolean",
            "full_name": "string"
        },
        "subject": "string",
        "summary": "string",
        "details": "string",
        "start_date": "date",
        "end_date": "date",
        "is_complete": "boolean",
        "study_type": {
            "id": "integer",
            "label": "string"
        },
        "region": {
            "id": "integer",
            "label": "string"
        },
        "image_url": "string",
        "observations": [
            {
                "id": "integer",
                "participant": "integer",
                "study": "integer",
                "latitude": "float",
                "longitude": "float",
                "description": "string",
                "image": "string",
                "date": "date",
                "participant_name": "string",
                "study_title": "string"
            }
        ],
        "average_longitude": "float",
        "average_latitude": "float",
        "furthest_longitude": "float",
        "furthest_latitude": "float"
    }
```

#### `POST` `/studies`

Headers:

```
"Authorization": "Token <Auth token goes here>"
```

Body:

```JSON
{
        "title": "string",
        "subject": "string",
        "summary": "string",
        "details": "string",
        "startDate": "date",
        "endDate": "date",
        "studyTypeId": "integer",
        "regionId": "integer",
        "imageUrl": "string"
}
```

Response `201 Created`:

```JSON
{
        "id": "integer",
        "title": "string",
        "author": {
            "id": "integer",
            "user": {
                "id": "integer",
                "username": "string",
                "first_name": "string",
                "last_name": "string",
                "is_staff": "boolean"
            },
            "bio": "string",
            "flair": "string",
            "image_url": "string",
            "is_researcher": "boolean",
            "full_name": "string"
        },
        "subject": "string",
        "summary": "string",
        "details": "string",
        "start_date": "date",
        "end_date": "date",
        "is_complete": "boolean",
        "study_type": {
            "id": "integer",
            "label": "string"
        },
        "region": {
            "id": "integer",
            "label": "string"
        },
        "image_url": "string",
        "observations": [
            {
                "id": "integer",
                "participant": "integer",
                "study": "integer",
                "latitude": "float",
                "longitude": "float",
                "description": "string",
                "image": "string",
                "date": "date",
                "participant_name": "string",
                "study_title": "string"
            }
        ],
        "average_longitude": "float",
        "average_latitude": "float",
        "furthest_longitude": "float",
        "furthest_latitude": "float"
    }
```

#### `PUT` `/studies/{pk}`

Headers:

```
"Authorization": "Token <Auth token goes here>"
```

Body:

```JSON
{
        "title": "string",
        "subject": "string",
        "summary": "string",
        "details": "string",
        "startDate": "date",
        "endDate": "date",
        "studyTypeId": "integer",
        "regionId": "integer",
        "imageUrl": "string"
}
```

Response: `204 No Content`

#### `DELETE` `/studies/{pk}`

Headers:

```
"Authorization": "Token <Auth token goes here>"
```



Response: `204 No Content`

#### `POST` `/studies/{pk}/add_observation`

Headers:

```
"Authorization": "Token <Auth token goes here>"
```

Body:

```JSON
{
    "latitude": "float",
    "longitude": "float",
    "description": "string",
    "image": "string",
    "date": "date"
}
```

Response `201 Created`:

```JSON
{
    "id": "integer",
    "participant": "integer",
    "study": "integer",
    "latitude": "float",
    "longitude": "float",
    "description": "string",
    "image": "string",
    "date": "date",
    "participant_name": "string",
    "study_title": "string"
}
```

### Users

#### `GET` `/users`

Response `200`:

```JSON
[
    {
        "id": "integer",
        "user": {
            "id": "integer",
            "username": "string",
            "first_name": "string",
            "last_name": "string",
            "is_staff": "boolean"
        },
        "bio": "string",
        "flair": "string",
        "image_url": "string",
        "is_researcher": "boolean",
        "full_name": "string"
    },
]
```

#### `GET` `/users/{pk}`

Response `200`:

```JSON
{
        "id": "integer",
        "user": {
            "id": "integer",
            "username": "string",
            "first_name": "string",
            "last_name": "string",
            "is_staff": "boolean"
        },
        "bio": "string",
        "flair": "string",
        "image_url": "string",
        "is_researcher": "boolean",
        "full_name": "string"
}
```

#### `GET` `/users/{pk}/participated_studies`

Response `200`:

```JSON
[
    {
        "id": "integer",
        "title": "string",
        "author": {
            "id": "integer",
            "user": {
                "id": "integer",
                "username": "string",
                "first_name": "string",
                "last_name": "string",
                "is_staff": "boolean"
            },
            "bio": "string",
            "flair": "string",
            "image_url": "string",
            "is_researcher": "boolean",
            "full_name": "string"
        },
        "subject": "string",
        "summary": "string",
        "details": "string",
        "start_date": "date",
        "end_date": "date",
        "is_complete": "boolean",
        "study_type": {
            "id": "integer",
            "label": "string"
        },
        "region": {
            "id": "integer",
            "label": "string"
        },
        "image_url": "string",
        "observations": [
            {
                "id": "integer",
                "participant": "integer",
                "study": "integer",
                "latitude": "float",
                "longitude": "float",
                "description": "string",
                "image": "string",
                "date": "date",
                "participant_name": "string",
                "study_title": "string"
            }
        ],
        "average_longitude": "float",
        "average_latitude": "float",
        "furthest_longitude": "float",
        "furthest_latitude": "float"
    },
]
```

#### `GET` `/users/{pk}/authored_studies`

Response `200`:

```JSON
[
    {
        "id": "integer",
        "title": "string",
        "author": {
            "id": "integer",
            "user": {
                "id": "integer",
                "username": "string",
                "first_name": "string",
                "last_name": "string",
                "is_staff": "boolean"
            },
            "bio": "string",
            "flair": "string",
            "image_url": "string",
            "is_researcher": "boolean",
            "full_name": "string"
        },
        "subject": "string",
        "summary": "string",
        "details": "string",
        "start_date": "date",
        "end_date": "date",
        "is_complete": "boolean",
        "study_type": {
            "id": "integer",
            "label": "string"
        },
        "region": {
            "id": "integer",
            "label": "string"
        },
        "image_url": "string",
        "observations": [
            {
                "id": "integer",
                "participant": "integer",
                "study": "integer",
                "latitude": "float",
                "longitude": "float",
                "description": "string",
                "image": "string",
                "date": "date",
                "participant_name": "string",
                "study_title": "string"
            }
        ],
        "average_longitude": "float",
        "average_latitude": "float",
        "furthest_longitude": "float",
        "furthest_latitude": "float"
    },
]
```