Design Choices

### Framework:

I chose to build this in Django because how its built-in authentication and authorization feature makes add security to the app a breeze. Also being that the test is time bound added to the face that I'm relatively comfortable with the framework I decide to go with it.

### Database:

I chose SQLite be cause it was easy to setup and can fully offer the benefits(indexes, constraints etc) of mainstream relational DBMS. Another really important reason I went with it was its support for JSON fields which I used at some point in the project.
Do note that this is only for local development. A configuratable environment variable has been added to change that to PostgreSQL on other environments as it more production grade and has got better scaling features.

### Serializer and Validation:

I used Django Rest Framework because the vaious toolkit it provides in quickly bootstraping an API-based website using Django. Although its serialization and deserialization speed isnt comparable to the likes of Pydantic, it shines more in other features like API Viewsets, Routers and Browserable API views.

### Project Structure

The projects was structured in a way that separates concerns and provides high cohesion and minimal bloat.
A request comes in through a view(view.py), then gets validated in the seriaizer(seriaizer.py), then the core operations happens in the service(service.py) file and its returned values gets sent back to the view which returns it to the client.
The process makes use of various custom classes and utility methods to logically control the flow of requests with decent error handling especially those coming from 3rd party apis.
