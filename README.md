###### <p align="right">![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/ryanmphill/wilder-watch-server/django-test.yml?label=Tests)
</p> 

# Wilder Watch API

This is the API intended for use in production with the [WilderWatch Client](https://github.com/ryanmphill/wilder-watch-client) built with Python and Django. 

_**Note**: If you are interested in pulling the wilder-watch-api down to run **locally**, you will need to use the [demo version](https://github.com/ryanmphill/wilder-watch-demo-server) that uses a generic `SECRET_KEY` for development purposes_

[Click here for WilderWatch demo server](https://github.com/ryanmphill/wilder-watch-demo-server)

## API Url

`https://wilder-watch-api-iknch.ondigitalocean.app/`

## Endpoints

### Authentication
#### `POST` `/login`

_Authenticates an existing user_

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

_Registers a new user_

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

_Retrieves all regions_

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

_Retrieves single region_

Response `200`:

```JSON
{
    "id": "integer",
    "label": "string"
}
```

### Study Types

#### `GET` `/study_types`

_Retrieves all study types_

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

_Retrieves single study type_

Response `200`:

```JSON
{
    "id": "integer",
    "label": "string"
}
```

### Studies

#### `GET` `/studies`

_Retrieves all studies_

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

_Retrieves single study_

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

_Creates a new study_

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

_Updates an existing study_

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

_Deletes an existing study_

Headers:

```
"Authorization": "Token <Auth token goes here>"
```



Response: `204 No Content`

#### `POST` `/studies/{pk}/add_observation`

_Adds an observation to an existing study_

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

_Retrieves all users_

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

_Retrieves single user_

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

_Retrieves all studies that a user has participated in_

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

_Retrieves all studies that a user has authored_

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