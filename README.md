foodgrades
============

Dylan coded up the API. Check it out [here](https://github.com/dylanportelance/foodgrades)

local:

```bash
$ python flask_project/app.py
$ curl http://localhost:5000/api/v1.0/restaurants/id/4/violations/id/1
```

not local:

```bash
$ curl http://104.236.242.57/api/v1.0/restaurants/id/1
```

Usage:

Get all restaurants at "[host]/api/v1.0/restaurants”

Get restaurants with name at "[host]/api/v1.0/restaurants/name/[name]”

Get restaurants with zip at "[host]/api/v1.0/restaurants/zip/[zip]”

Get restaurants with unique id at "[host]/api/v1.0/restaurants/id/[id]”

Get a restaurants violations with unique restaurant id at "[host]/api/v1.0/restaurants/id/[id]/violations”

Get violation with a unique restaurant id and a unique violation id at "[host]/api/v1.0/restaurants/id/[restaurant_id]/violations/id/[violation_id]”





