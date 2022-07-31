# django_todo_list

1. Install Python <https://www.python.org/>
2. Open ****cmd****
    ```
    # download repo
    > git clone https://github.com/AdamHsu2501/django_todo_list.git
    > cd django_todo_list
    
    # install pipenv
    > pip install pipenv
    
    # Install packages
    > pipenv install
    
    # Start virtual envirment
    > pipenv shell
    > cd config
    
    # Start server
    > python manage.py runserver
    ````
3. Open broswer with http://127.0.0.1:8000/ and login with Username ```admin``` Password ```admin``` 
    * Implement authentication login and registration, and redirect from ```/login``` and ```/register``` while logged in
        
    * List tasks that only the owner can view, and Search filed can filter tasks

    * Create / Update / Delete tasks
![](https://i.imgur.com/LdSSWuo.png)